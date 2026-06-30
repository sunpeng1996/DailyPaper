"""Stage 2: filter relevance + summarize using Doubao (OpenAI-compatible).

Reads .cache/raw_papers.json -> writes .cache/processed_papers.json.

Pipeline per paper (single model, varying input/output size):
  1. Relevance score (0-10) from title+abstract — cheap, short.
  2. If score >= MIN_SCORE_KEEP, write a card from the abstract.
  3. If score >= MIN_SCORE_DEEP, download the PDF, extract text with pypdf,
     and write a deeper card with the extracted full text in context.

Doubao (ARK) API is OpenAI-compatible; we use the openai SDK with base_url
overridden. PDFs are not natively supported — text is extracted locally.
Structured output uses response_format={"type":"json_object"} plus
Pydantic validation (since strict json_schema isn't guaranteed on
non-OpenAI endpoints).
"""
from __future__ import annotations

import io
import json
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Type, TypeVar

import httpx
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError
from pypdf import PdfReader

from common import (
    CACHE_DIR,
    add_usage,
    env_int,
    env_str,
    llm_api_key,
    llm_base_url,
    llm_model,
    log,
    read_json,
    reset_usage,
    write_json,
)

LLM_API_KEY = llm_api_key()
LLM_BASE_URL = llm_base_url()
HAS_LLM = bool(LLM_API_KEY)

# Two-tier model strategy:
#   SCORE_MODEL — wide funnel, every candidate scored; use light/fast model
#   SUMMARY_MODEL — narrow output (~MAX_PAPERS_PER_DAY calls); use pro
LLM_MODEL = llm_model()
LLM_SCORE_MODEL = env_str("LLM_SCORE_MODEL", env_str("DEEPSEEK_SCORE_MODEL", LLM_MODEL))
LLM_SUMMARY_MODEL = env_str("LLM_SUMMARY_MODEL", env_str("DEEPSEEK_SUMMARY_MODEL", LLM_MODEL))

MIN_SCORE_KEEP = env_int("MIN_SCORE_KEEP", 6)
MIN_SCORE_DEEP = env_int("MIN_SCORE_DEEP", 8)
MIN_PAPERS_PER_DAY = env_int("MIN_PAPERS_PER_DAY", 8)   # backfill floor
MAX_PAPERS_PER_DAY = env_int("MAX_PAPERS_PER_DAY", 30)
PDF_TEXT_MAX_CHARS = env_int("PDF_TEXT_MAX_CHARS", 60000)
SCORE_CONCURRENCY = env_int("SCORE_CONCURRENCY", 6)
SUMMARY_CONCURRENCY = env_int("SUMMARY_CONCURRENCY", 6)

client = OpenAI(
    api_key=LLM_API_KEY or "missing",
    base_url=LLM_BASE_URL,
    timeout=httpx.Timeout(200.0, connect=30.0),
    max_retries=3,
)

RELEVANCE_SYSTEM = """你是一位 AI 论文领域专家。读者是一名 **AI 算法从业者**，专注：
**电商 / 广告（计算广告、CTR/CVR 预估、出价竞价）/ 搜索推荐系统**，
核心关注 **Agent 结合搜索推荐系统** 与 **LLM 结合搜索推荐系统** 这两条主线。
他看论文是为了**找能迁移进业务、提升工作效率的方法**，不是学术兴趣。

按对这个读者的实用价值打 0-10 分。

注意：画像用来**排序倾斜**，不是把通用好论文一棍子打死。优质 LLM/Agent/ML
论文即使不直接命中搜推广也值得读，给 7-8。只有真和 AI 无关才给低分。

10 分（直接命中其业务，必读）：
- **LLM 结合搜索推荐系统**：LLM4Rec、生成式推荐 GenRec、Semantic ID / RQ-VAE for items、
  生成式检索 Generative Retrieval、LLM 做排序 / 召回 / query 理解 / 用户兴趣建模
- **Agent 结合搜索推荐系统**：Agentic Recommendation / Agentic Search（推荐/搜索/营销/广告
  场景里的 LLM Agent、planning、tool-use、multi-agent、对话式推荐与搜索）
- **广告 / 计算广告**：CTR/CVR/CTCVR 预估、竞价 bidding、预算分配、创意生成、广告召回与排序、
  归因，尤其结合 LLM/Agent
- **电商场景 AI**（搜推广、用户建模、营销、商品理解、履约）+ LLM/Agent
- 推荐词场景的 LLM/Agent 应用：query / 话题 / 搜索词 / 消息推送词的推荐、生成、改写、扩展
  （query 推荐与改写、话题推荐、push/消息选词与文案、SEO 推词、suggestion / autocomplete）

8-9 分（高质量，方法大概率可借鉴）：
- 通用 Agent / Tool-use / Memory / Planning / Multi-Agent（方法可迁移到搜推广）
- 大语言模型核心：训练 / 对齐 / 推理 / Long-context / MoE / Distill / 量化 / RL
- RAG / Retrieval / Reasoning
- 经典推荐 / 搜索 / 排序 / 召回 / 用户建模有显著创新

6-7 分（值得一看的主流 AI/ML 工作）：
- 其他主流 LLM/ML 方向；评估/效率/可解释；偏工程或增量但扎实
- 视觉/语音/多模态（不结合 LLM 时封顶 7）

3-5 分：沾边、非主流、纯理论且业务无关
0-2 分：与 AI 完全无关 / 纯水文

额外加权（头部大厂出品）：
若能从**标题/摘要**判断出自下列头部工业界团队，在同等相关度下优先，并整体**上浮 1-2 分**
（封顶 10；但与 AI/搜推广完全无关的仍不超过 5，大厂光环不救水文）：
- 国内：字节 ByteDance Seed / Doubao、抖音 Douyin / TikTok 搜推广团队、快手 Kuaishou / 可灵 Kling、
  阿里 通义 Qwen / 淘天 / 蚂蚁 Ant、腾讯 混元 Hunyuan / 微信 WeChat AI、百度 文心 ERNIE、
  美团 Meituan、京东 JD、小红书 RED、DeepSeek、月之暗面 Moonshot / Kimi、智谱 Zhipu GLM、MiniMax、阶跃 StepFun
- 国外：Google / DeepMind、OpenAI、Anthropic、Meta AI (FAIR)、Microsoft Research、NVIDIA、Apple、Amazon、
  Mistral、Cohere；以及搜推广强相关的 Netflix / Pinterest / Spotify / LinkedIn / Snap
判断线索：标题/摘要出现上述机构名，或其代表模型/系统名（Gemini、GPT、Qwen、Hunyuan、ERNIE、Doubao、
Kling、Kimi、GLM、Llama 等）。**摘要无法判断机构时，按内容正常打分，不要臆测机构。**

只输出 JSON：
{"score": <0-10 整数>, "reasoning": "<不超过 120 字，点明对电商/广告/搜索推荐系统业务的价值；若判断出自头部大厂，一并点出机构>"}"""

SUMMARY_SYSTEM = """你是一位 AI 论文解读专家。读者是 **专注电商 / 广告 / 搜索推荐系统，核心关注
Agent 与 LLM 结合搜索推荐系统的 AI 算法从业者**，看论文是为了把有用的东西迁移进业务。为他写一张中文论文卡片。

风格要求：
- 直接、信息密度高，不要套话；术语保留英文（LoRA、RAG、KV cache、MoE、Semantic ID）
- 不重复原标题；不要"本文提出了 / 本研究表明"
- summary_md 用 markdown：动机 → 方法关键点 → 关键结果数字
- practical_value 是重点：站在电商/推荐/Agent 从业者角度，写 2-4 条
  「可以怎么借鉴到工作里」——具体到方法 trick、架构选择、工程实现、能复用的结论；
  没有可迁移价值就直说"主要是学术贡献，业务可借鉴点有限"

只输出 JSON，结构：
{
  "title_zh":       "<论文标题的中文翻译，简洁，<= 50 字>",
  "one_liner":      "<一句话核心贡献，<= 60 字，不带句号>",
  "category":       "<单选: GenRec | RecSys | QueryRec | Agent | MultiAgent | LLM | RAG | Eval | Training | Multimodal | Reasoning | Other>",
  "direction":      "<一句话方向归属，<= 24 字，例如 '生成式推荐 · Semantic ID' 或 'Agent 多智体协作优化'>",
  "tags":           ["<3-6 个英文标签>"],
  "affiliations":   ["<从提供的 PDF 首页文本提取作者所属机构，最多 5 个，去重；实在提取不到才 []>"],
  "practical_value":"<markdown，2-4 条 '- ' 列表，面向电商/Agent/生成式推荐从业者的可借鉴点>",
  "summary_md":     "<markdown 正文：动机/方法/结果>"
}

category 归类提示：
- 论文核心是「给用户推荐/生成 query、话题、搜索词、消息推送词」——query 推荐与改写、
  话题推荐、push/消息选词与文案、SEO 推词、search suggestion / autocomplete → QueryRec
- 普通物品/内容/广告推荐、排序、召回、用户建模 → RecSys
- 生成式物品推荐、Semantic ID、LLM4Rec 直接生成 item → GenRec"""


class Relevance(BaseModel):
    score: int = Field(ge=0, le=10)
    reasoning: str = Field(max_length=200)


class Summary(BaseModel):
    title_zh: str
    one_liner: str = Field(max_length=120)
    category: str
    direction: str = Field(default="", max_length=60)
    tags: list[str] = Field(min_length=1, max_length=8)
    affiliations: list[str] = Field(default_factory=list, max_length=8)
    practical_value: str = Field(default="")
    summary_md: str


T = TypeVar("T", bound=BaseModel)


def _strip_surrogates(s: str) -> str:
    """pypdf can emit lone UTF-16 surrogates (math glyphs like 𝐀 in U+1D400),
    which make json/utf-8 encoding of the API request body raise
    UnicodeEncodeError. Replace any unencodable code points."""
    if not s:
        return s
    return s.encode("utf-8", "replace").decode("utf-8")


def _short_authors(p: dict) -> str:
    a = p.get("authors") or []
    head = ", ".join(a[:5])
    return head + (" 等" if len(a) > 5 else "")


def _heuristic_score(paper: dict) -> Relevance:
    blob = f"{paper.get('title','')} {paper.get('abstract','')}".lower()
    score = 4
    rules = [
        (r"\b(recommend|recommender|ranking|retrieval|search|advertis|ctr|cvr|query)\b", 3),
        (r"\b(agent|agentic|multi-agent|tool use|planning|memory)\b", 2),
        (r"\b(llm|large language model|gpt|rag|reasoning|alignment|post-training|rlhf|grpo)\b", 2),
        (r"\b(multimodal|vision-language|vlm|image|video|speech)\b", 1),
        (r"\b(benchmark|evaluation|dataset)\b", 1),
    ]
    hits: list[str] = []
    for pattern, weight in rules:
        if re.search(pattern, blob):
            score += weight
            hits.append(pattern.split("|")[0].strip(r"\b("))
    if paper.get("source") == "huggingface-daily":
        score += 1
    if int(paper.get("hf_upvotes") or 0) >= 10:
        score += 1
    score = max(0, min(10, score))
    reason = "规则打分"
    if hits:
        reason += "：" + "、".join(hits[:3])
    return Relevance(score=score, reasoning=reason[:120])


def _category_from_text(text: str) -> str:
    t = text.lower()
    if re.search(r"recommend|recommender|ranking|ctr|cvr|advertis", t):
        return "RecSys"
    if re.search(r"query|search suggestion|autocomplete", t):
        return "QueryRec"
    if re.search(r"agent|agentic|tool use|multi-agent", t):
        return "Agent"
    if re.search(r"rag|retrieval", t):
        return "RAG"
    if re.search(r"multimodal|vision-language|vlm|image|video|speech", t):
        return "Multimodal"
    if re.search(r"train|alignment|rlhf|grpo|post-training|distill", t):
        return "Training"
    if re.search(r"reasoning", t):
        return "Reasoning"
    return "LLM"


def _heuristic_summary(paper: dict) -> Summary:
    title = (paper.get("title") or "").strip()
    abstract = re.sub(r"\s+", " ", paper.get("abstract") or "").strip()
    category = _category_from_text(f"{title} {abstract}")
    tags = [category, "LLM" if category != "LLM" else "AI"]
    if "agent" in f"{title} {abstract}".lower() and "Agent" not in tags:
        tags.append("Agent")
    if "recommend" in f"{title} {abstract}".lower() and "RecSys" not in tags:
        tags.append("RecSys")
    one_liner = abstract[:95].rstrip() + ("..." if len(abstract) > 95 else "")
    if not one_liner:
        one_liner = "未配置 LLM API Key，使用标题和摘要生成规则摘要"
    practical = (
        "- 可先根据论文标题和摘要判断是否进入人工精读列表。\n"
        "- 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。"
    )
    summary = (
        "### 摘要\n\n"
        f"{abstract or title}\n\n"
        "> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。"
    )
    return Summary(
        title_zh=title[:50] or "未命名论文",
        one_liner=one_liner[:120],
        category=category,
        direction=category,
        tags=tags[:6],
        affiliations=[],
        practical_value=practical,
        summary_md=summary,
    )


def _call_json(
    system: str,
    user: str,
    schema: Type[T],
    *,
    model: str = "",
    max_tokens: int = 2000,
    label: str = "",
) -> T | None:
    """One round-trip to the LLM that demands a JSON object and validates it
    against the given Pydantic schema. Retries once on parse/validation error
    with an explicit "must be JSON only" reminder."""
    model = model or LLM_SUMMARY_MODEL
    # Single chokepoint for every LLM call (score / abstract / deep) — strip
    # surrogates so the OpenAI SDK can UTF-8 encode the request body.
    messages = [
        {"role": "system", "content": _strip_surrogates(system)},
        {"role": "user", "content": _strip_surrogates(user)},
    ]
    last_error = None
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=max_tokens,
            )
        except OpenAIError as exc:
            log.warning("[%s] api error attempt=%d: %s", label, attempt, exc)
            last_error = exc
            continue
        add_usage(model, getattr(resp, "usage", None))
        text = (resp.choices[0].message.content or "").strip()
        try:
            return schema.model_validate_json(text)
        except (ValidationError, json.JSONDecodeError) as exc:
            log.warning("[%s] parse failed attempt=%d: %s | text=%.200s",
                        label, attempt, exc, text)
            last_error = exc
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user",
                             "content": "上次返回不是有效 JSON 或字段不符合。请只返回一个 JSON 对象，不要加任何前后说明。"})
    log.warning("[%s] all %d attempts failed: %s", label, 2, last_error)
    return None


def score_relevance(paper: dict) -> Relevance | None:
    if not HAS_LLM:
        return _heuristic_score(paper)

    # authors give the model a weak extra signal for the big-lab boost (arXiv
    # has no affiliations, but author names sometimes hint at the team).
    user = (
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"摘要:\n{paper['abstract'][:2500]}"
    )
    # Score path uses the cheaper/faster model (flash). Pro's deep reasoning
    # chain made 19 candidates take ~45 min — overkill for a 0-10 score.
    return _call_json(
        RELEVANCE_SYSTEM, user, Relevance,
        model=LLM_SCORE_MODEL,
        max_tokens=1500,
        label=f"score:{paper['arxiv_id']}",
    )


def _first_page_text(paper: dict) -> str:
    """Cheap affiliation source: arXiv abstracts never include affiliations,
    but PDF page 1 always has the author/affiliation block. Grab ~2.5k chars
    (~page 1) only. Best-effort — empty string on any failure."""
    url = paper.get("pdf_url")
    if not url:
        return ""
    pdf = _fetch_pdf(url)
    if not pdf:
        return ""
    return _extract_pdf_text(pdf, 2500)


def summarize_abstract(paper: dict) -> Summary | None:
    if not HAS_LLM:
        return _heuristic_summary(paper)

    fp = _first_page_text(paper)
    fp_block = (
        f"\n\nPDF 首页文本（含作者单位，用于提取 affiliations）:\n"
        f"-----\n{fp}\n-----\n"
        if fp else "\n\n（无 PDF 首页，affiliations 提取不到则留空）"
    )
    user = (
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"摘要:\n{paper['abstract']}"
        f"{fp_block}\n\n"
        f"请基于以上信息写卡片。summary_md 200-450 字。"
        f"affiliations 请从「PDF 首页文本」里提取作者所属机构。"
    )
    return _call_json(
        SUMMARY_SYSTEM, user, Summary,
        max_tokens=4000, label=f"abs:{paper['arxiv_id']}",
    )


def _fetch_pdf(url: str) -> bytes | None:
    try:
        with httpx.Client(timeout=60.0, follow_redirects=True) as cli:
            r = cli.get(url, headers={"User-Agent": "DailyPaper/0.1"})
            r.raise_for_status()
            return r.content
    except Exception as exc:
        log.warning("pdf fetch failed %s: %s", url, exc)
        return None


def _extract_pdf_text(pdf_bytes: bytes, max_chars: int) -> str:
    """Pull plain text out of an arXiv PDF page by page until max_chars hit.
    Returns empty string if the PDF is unreadable or scanned-only."""
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
    except Exception as exc:
        log.warning("pdf parse failed: %s", exc)
        return ""
    parts: list[str] = []
    used = 0
    for page in reader.pages:
        try:
            t = page.extract_text() or ""
        except Exception:
            continue
        if not t:
            continue
        parts.append(t)
        used += len(t)
        if used >= max_chars:
            break
    text = "\n\n".join(parts)
    return _strip_surrogates(text[:max_chars])


def summarize_with_pdf(paper: dict) -> Summary | None:
    if not HAS_LLM:
        return None

    pdf_url = paper.get("pdf_url")
    if not pdf_url:
        return None
    pdf_bytes = _fetch_pdf(pdf_url)
    if not pdf_bytes:
        return None
    text = _extract_pdf_text(pdf_bytes, PDF_TEXT_MAX_CHARS)
    if not text or len(text) < 500:
        log.info("pdf text too short or empty for %s, skip deep read",
                 paper["arxiv_id"])
        return None
    user = (
        f"以下是 arXiv 论文 {paper['arxiv_id']} 的正文文本（pypdf 抽取）。\n"
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"正文（截断到 {PDF_TEXT_MAX_CHARS} 字符）:\n"
        f"-----\n{text}\n-----\n\n"
        "请基于以上正文输出中文卡片。summary_md 写 400-800 字，要求：\n"
        "1) 一段动机：为什么这个问题值得做\n"
        "2) 方法关键点：模型/算法/数据的具体设计，列要点\n"
        "3) 关键实验：数据集、对比 baseline、最关键的几个数字\n"
        "4) 你认为最值得记住的一句话"
    )
    return _call_json(
        SUMMARY_SYSTEM, user, Summary,
        max_tokens=8000, label=f"deep:{paper['arxiv_id']}",
    )


PROGRESS_FILE = CACHE_DIR / "process_progress.json"


def _progress(msg: str) -> None:
    log.info(msg)
    print(msg, flush=True)


def _load_progress() -> dict:
    data = read_json(PROGRESS_FILE)
    if not isinstance(data, dict):
        return {"scored_papers": [], "processed_papers": []}
    data.setdefault("scored_papers", [])
    data.setdefault("processed_papers", [])
    return data


def _save_progress(scored_papers: list[dict], processed_papers: list[dict]) -> None:
    write_json(PROGRESS_FILE, {
        "scored_papers": scored_papers,
        "processed_papers": processed_papers,
    })


def _clear_progress() -> None:
    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()


def main():
    reset_usage()  # first LLM stage of the pipeline — start the cost tally fresh
    raws = read_json(CACHE_DIR / "raw_papers.json") or []
    if not HAS_LLM:
        log.warning("LLM_API_KEY is not configured; using heuristic paper processing")
    log.info("processing %d raw papers via %s @ %s",
             len(raws), LLM_MODEL, LLM_BASE_URL)

    progress = _load_progress()
    prev_scored = progress["scored_papers"]
    prev_processed = progress["processed_papers"]
    prev_scored_ids = {p["arxiv_id"] for p in prev_scored}
    prev_processed_ids = {p["arxiv_id"] for p in prev_processed}

    if prev_scored:
        log.info("resumed from progress file: %d scored, %d processed already done",
                 len(prev_scored), len(prev_processed))

    # Step 1: relevance scoring. Resume from where we left off.
    all_scored: list[dict] = list(prev_scored)
    remaining_raws = [p for p in raws if p["arxiv_id"] not in prev_scored_ids]
    total_raws = len(raws)

    if remaining_raws:
        _progress(f"=== Step 1: Scoring {len(remaining_raws)} papers (concurrency={SCORE_CONCURRENCY}) ===")
        _score_lock = threading.Lock()
        _done_count = len(all_scored)
        _fail_count = 0

        def _score_one(paper: dict) -> dict | None:
            nonlocal _done_count, _fail_count
            arxiv_id = paper.get("arxiv_id", "")
            try:
                rel = score_relevance(paper)
            except Exception as exc:
                with _score_lock:
                    _fail_count += 1
                log.warning("[scoring FAIL] %s: %s", arxiv_id, exc)
                return None
            if rel is None:
                with _score_lock:
                    _fail_count += 1
                log.warning("[scoring FAIL] %s: returned None", arxiv_id)
                return None
            paper["_score"] = rel.score
            paper["_score_reason"] = rel.reasoning
            with _score_lock:
                _done_count += 1
                _progress(f"[scoring {_done_count}/{total_raws}] {arxiv_id or paper.get('title', '')[:60]} (score={rel.score:.1f})")
                all_scored.append(paper)
                _save_progress(all_scored, prev_processed)
            return paper

        with ThreadPoolExecutor(max_workers=SCORE_CONCURRENCY) as pool:
            futures = [pool.submit(_score_one, p) for p in remaining_raws]
            for f in as_completed(futures):
                try:
                    f.result()
                except Exception as exc:
                    log.warning("score task crashed: %s", exc)
        _progress(f"=== Step 1 done: scored {len(all_scored)} papers, {_fail_count} failed ===")

    all_scored.sort(
        key=lambda x: (x["_score"], x.get("hf_upvotes", 0)),
        reverse=True,
    )
    above = [p for p in all_scored if p["_score"] >= MIN_SCORE_KEEP]
    if len(above) >= MIN_PAPERS_PER_DAY:
        scored = above[:MAX_PAPERS_PER_DAY]
    else:
        # not enough cleared the bar — take the top-ranked anyway so the
        # digest is never paper-empty
        scored = all_scored[:max(MIN_PAPERS_PER_DAY, len(above))][:MAX_PAPERS_PER_DAY]
    log.info("scored %d, %d >= %d; kept %d (min=%d max=%d)",
             len(all_scored), len(above), MIN_SCORE_KEEP, len(scored),
             MIN_PAPERS_PER_DAY, MAX_PAPERS_PER_DAY)

    # Step 2: summarize. Resume from where we left off.
    processed: list[dict] = list(prev_processed)
    remaining_scored = [p for p in scored if p["arxiv_id"] not in prev_processed_ids]
    total_to_process = len(scored)

    if remaining_scored:
        _progress(f"=== Step 2: Summarizing {len(remaining_scored)} papers (concurrency={SUMMARY_CONCURRENCY}) ===")
        _summary_lock = threading.Lock()
        _summary_done = len(processed)
        _summary_fail = 0

        def _summarize_one(paper: dict) -> dict | None:
            nonlocal _summary_done, _summary_fail
            depth = "abstract"
            summary: Summary | None = None
            arxiv_id = paper.get("arxiv_id", "")
            try:
                if paper["_score"] >= MIN_SCORE_DEEP:
                    summary = summarize_with_pdf(paper)
                    if summary is not None:
                        depth = "full_pdf"
                if summary is None:
                    summary = summarize_abstract(paper)
            except Exception as exc:
                with _summary_lock:
                    _summary_fail += 1
                log.warning("[summarize FAIL] %s: %s", arxiv_id, exc)
                return None
            if summary is None:
                with _summary_lock:
                    _summary_fail += 1
                log.warning("[summarize FAIL] %s: returned None", arxiv_id)
                return None

            result = {
                "arxiv_id": paper["arxiv_id"],
                "title": paper["title"],
                "title_zh": summary.title_zh,
                "authors": paper.get("authors", []),
                "affiliations": summary.affiliations or [],
                "url": paper["url"],
                "pdf_url": paper.get("pdf_url"),
                "published": (paper.get("published") or "")[:10],
                "category": summary.category or "Other",
                "direction": summary.direction or "",
                "tags": summary.tags or [],
                "one_liner": summary.one_liner,
                "practical_value": summary.practical_value or "",
                "summary_md": summary.summary_md,
                "score": paper["_score"],
                "source": paper.get("source", ""),
                "depth": depth,
            }
            with _summary_lock:
                _summary_done += 1
                _progress(f"[summarizing {_summary_done}/{total_to_process}] {arxiv_id or paper.get('title', '')[:60]} (score={paper.get('_score', 0):.1f}, depth={depth})")
                processed.append(result)
                _save_progress(all_scored, processed)
            return result

        with ThreadPoolExecutor(max_workers=SUMMARY_CONCURRENCY) as pool:
            futures = [pool.submit(_summarize_one, p) for p in remaining_scored]
            for f in as_completed(futures):
                try:
                    f.result()
                except Exception as exc:
                    log.warning("summary task crashed: %s", exc)
        _progress(f"=== Step 2 done: processed {len(processed)} papers, {_summary_fail} failed ===")

    write_json(CACHE_DIR / "processed_papers.json", processed)
    _clear_progress()
    log.info("processed %d papers (deep=%d). All done — progress cleared.",
             len(processed), sum(1 for x in processed if x["depth"] == "full_pdf"))


if __name__ == "__main__":
    main()
