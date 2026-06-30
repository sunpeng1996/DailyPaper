"""Stage 2b: filter + cluster + summarize today's news items via Doubao.

Reads .cache/raw_news.json -> writes .cache/processed_news.json with shape:
{
  "date": "2026-05-14",
  "topics": [
    {"title": "...", "summary": "...", "tags": [...],
     "source_indices": [0, 3, 5]},   // indices into the filtered items list
    ...
  ],
  "items": [{title, url, source, points}, ...]   // the filtered set
}

Pipeline:
  1) Local keyword pre-filter — drop items that don't mention any AI/LLM term.
     Cheap, high-precision noise removal before paying for LLM tokens.
  2) Doubao single call clusters the survivors into 4-6 topics, writes a
     2-3 sentence Chinese summary per topic, picks tags, and references items
     by index. Uses response_format=json_object + Pydantic validation.
"""
from __future__ import annotations

import json
import os
import re

from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError

from common import (
    CACHE_DIR,
    add_usage,
    env_int,
    env_str,
    llm_api_key,
    llm_base_url,
    llm_model,
    log,
    now_iso_date,
    read_json,
    write_json,
)

LLM_API_KEY = llm_api_key()
LLM_BASE_URL = llm_base_url()
LLM_MODEL = llm_model()
HAS_LLM = bool(LLM_API_KEY)

MAX_NEWS_ITEMS = env_int("MAX_NEWS_ITEMS", 50)
MAX_NEWS_TOPICS = env_int("MAX_NEWS_TOPICS", 10)
MIN_NEWS_TOPICS = env_int("MIN_NEWS_TOPICS", 7)

# Keep an item if its title or snippet matches any of these (case-insensitive).
# Broad on purpose — the LLM will do the precise filtering downstream.
KEYWORD_RE = re.compile(
    r"(?i)\b("
    r"llm|gpt|chatgpt|claude|anthropic|openai|gemini|deepmind|"
    r"llama|meta\s*ai|deepseek|mistral|qwen|grok|copilot|"
    r"agent|agentic|rag|retrieval|reasoning|"
    r"fine[-\s]?tun|moe|distill|alignment|"
    r"transformer|inference|gpu|training|"
    r"hugging\s*face|nvidia|cuda|"
    r"ai\b|artificial intelligence|machine learning"
    r")\b"
)

# Chinese keyword filter — for general-tech Chinese feeds (e.g., 36kr) that
# include lots of non-AI content. AI-focused Chinese sources bypass this.
CN_KEYWORD_RE = re.compile(
    r"(LLM|GPT|大模型|大语言模型|智能体|Agent|RAG|"
    r"微调|fine[-\s]?tun|推理|强化学习|多模态|生成式|"
    r"OpenAI|Anthropic|Claude|Gemini|DeepSeek|Qwen|Kimi|Llama|"
    r"文心|混元|通义|盘古|豆包|"
    r"字节|阿里|腾讯|百度|智谱|月之暗面|MiniMax|百川|零一万物|"
    r"人工智能|AGI|AI\s|开源模型|大厂|算力)",
    re.IGNORECASE,
)

client = OpenAI(
    api_key=LLM_API_KEY or "missing",
    base_url=LLM_BASE_URL,
    timeout=300,
    max_retries=3,
)


SYSTEM = """你是一位 AI 行业观察分析师，要把今天从 Hacker News 和 Reddit 收集到的若干条 AI 动态聚成几个新闻主题。

任务约束：
- **目标产出 7-10 个主题**。颗粒度要细，不要过度合并
- 一个主题 = **一个公司的一个具体动作 / 一个产品发布 / 一个事件**
- 即使只有 1 个 source 也可以独立成 topic，只要事件本身值得关注（产品发布、并购、争议、开源、benchmark 等）
- 强反模式（不要这样做）：把"阿里悟空放量""蚂蚁灵波开源""国产 GPU 联盟""田渊栋创业""淘天金码奖"聚成一个"中国 AI 多领域加速突破"——这是 5 个独立 topic
- 强反模式 2：把"Anthropic 发布 Claude for Business""Anthropic 调整订阅政策"放在同一个 topic（虽然同一家公司，但是不同事件不同时间）
- 正例：每家公司的每个具体动作都独立成 topic
- 每个主题 summary 写 2-3 句中文，要有信息密度，给出"发生了什么 / 为什么值得关注"
- 不要复述 title；从 source 中提炼事实
- 每个主题给 2-4 个 tag（英文为主，如 LLM、OpenAI、Agent、Open Source；公司名也可作 tag）
- source_indices 必须是输入 items 列表里的下标（从 0 开始）
- 信号不强 / 重复明显的条目可以丢弃，不算进任何主题
- 西方公司（OpenAI/Anthropic/Google/Meta/DeepMind）+ 中国大厂（字节/阿里/腾讯/百度/蚂蚁/DeepSeek/Moonshot/Zhipu）的动作都要均衡覆盖

只输出 JSON：
{
  "topics": [
    {
      "title": "<主题标题，简洁，<= 30 字中文>",
      "summary": "<2-3 句中文概述>",
      "tags": ["<2-4 个英文标签>"],
      "source_indices": [<整数下标>]
    }
  ]
}"""


class Topic(BaseModel):
    title: str = Field(max_length=80)
    summary: str = Field(max_length=400)
    tags: list[str] = Field(default_factory=list, max_length=6)
    source_indices: list[int] = Field(default_factory=list)


class ClusterOutput(BaseModel):
    topics: list[Topic]


def heuristic_cluster(items: list[dict]) -> ClusterOutput:
    """Fallback when no LLM key is configured."""
    topics: list[Topic] = []
    for idx, it in enumerate(items[:MAX_NEWS_TOPICS]):
        title = re.sub(r"\s+", " ", it.get("title") or "").strip()
        snippet = re.sub(r"\s+", " ", it.get("snippet") or "").strip()
        source = it.get("source", "")
        tags = ["AI"]
        if source.startswith("cn:"):
            tags.append("China AI")
        elif source.startswith("blog:"):
            tags.append("Company Blog")
        elif source.startswith("reddit:"):
            tags.append("Reddit")
        elif source == "hn":
            tags.append("Hacker News")
        summary = snippet or title
        topics.append(Topic(
            title=title[:30] or "AI 动态",
            summary=(summary[:220] or "未配置 LLM API Key，使用规则聚合生成摘要。"),
            tags=tags[:4],
            source_indices=[idx],
        ))
    return ClusterOutput(topics=topics)


def prefilter(raws: list[dict]) -> list[dict]:
    """Keep items that mention an AI/LLM keyword (EN or CN), or come from a
    domain-curated AI source (where the source itself is the trust signal)."""
    out: list[dict] = []
    for it in raws:
        # Source-level allowlist: items from AI-focused Chinese media skip the
        # keyword gate because the editorial filter already happened upstream.
        if it.get("ai_focused"):
            out.append(it)
            continue
        blob = (it.get("title") or "") + " " + (it.get("snippet") or "")
        src = it.get("source", "")
        if src.startswith("cn:"):
            # Chinese general feeds (36kr etc.) — apply Chinese keyword regex
            if CN_KEYWORD_RE.search(blob):
                out.append(it)
        else:
            # HN / Reddit / etc. — English keyword regex
            if KEYWORD_RE.search(blob):
                out.append(it)
    return out


def cluster_and_summarize(items: list[dict]) -> ClusterOutput | None:
    """Single LLM call: cluster + summarize. Retries on API error and bad JSON."""
    if not HAS_LLM:
        log.warning("LLM_API_KEY is not configured; using heuristic news clustering")
        return heuristic_cluster(items)

    lines: list[str] = []
    for idx, it in enumerate(items):
        meta = f"[{it.get('source','?')}"
        if it.get("points"):
            meta += f" · {it['points']}pts"
        meta += "]"
        title = it.get("title", "").replace("\n", " ")
        snippet = (it.get("snippet") or "").replace("\n", " ")[:200]
        line = f"{idx}. {meta} {title}"
        if snippet:
            line += f" — {snippet}"
        lines.append(line)
    user = (
        f"今天收集到 {len(items)} 条候选新闻条目，已按 source 标注（hn / reddit:<sub>）:\n\n"
        + "\n".join(lines)
        + "\n\n请按要求聚成 3-6 个主题输出 JSON。"
    )

    # defensive: drop lone surrogates so the SDK can UTF-8 encode the body
    safe_user = user.encode("utf-8", "replace").decode("utf-8")
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": safe_user},
    ]
    last_error = None
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3,
                # 16000: V4-Pro reasoning_tokens 大头吃了 ~4-6k，加上 35 items
                # 输入解析 + 10 个主题 JSON 输出，6000 会截断。给充裕空间。
                max_tokens=16000,
            )
        except OpenAIError as exc:
            log.warning("news cluster api error attempt=%d: %s", attempt, exc)
            last_error = exc
            continue
        add_usage(LLM_MODEL, getattr(resp, "usage", None))
        text = (resp.choices[0].message.content or "").strip()
        try:
            return ClusterOutput.model_validate_json(text)
        except (ValidationError, json.JSONDecodeError) as exc:
            log.warning("news cluster parse attempt=%d failed: %s | text=%.300s",
                        attempt, exc, text)
            last_error = exc
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user",
                             "content": "返回的不是合法 JSON 或字段不符合 schema。只返回一个 JSON 对象。"})
    log.warning("news cluster failed after 2 attempts: %s — falling back to heuristic", last_error)
    return heuristic_cluster(items)


def main():
    raws = read_json(CACHE_DIR / "raw_news.json") or []
    log.info("raw news count: %d", len(raws))

    filtered = prefilter(raws)
    log.info("after keyword prefilter: %d", len(filtered))

    if not filtered:
        log.info("no news survived prefilter, skipping LLM call")
        write_json(CACHE_DIR / "processed_news.json", {
            "date": now_iso_date(),
            "topics": [],
            "items": [],
        })
        return

    # Stratified selection. RSS sources (cn:* and blog:*) carry no points, so a
    # plain points sort would bulldoze them under HN/Reddit. Give each a quota,
    # then fill the rest with the highest-points HN/Reddit items.
    CN_QUOTA = env_int("NEWS_CN_QUOTA", 14)
    BLOG_QUOTA = env_int("NEWS_BLOG_QUOTA", 12)

    def _is(prefix: str, x: dict) -> bool:
        return (x.get("source") or "").startswith(prefix)

    chinese = [x for x in filtered if _is("cn:", x)][:CN_QUOTA]
    blog = [x for x in filtered if _is("blog:", x)][:BLOG_QUOTA]
    rest = [x for x in filtered if not _is("cn:", x) and not _is("blog:", x)]
    rest.sort(key=lambda x: int(x.get("points") or 0), reverse=True)
    rest = rest[: max(0, MAX_NEWS_ITEMS - len(chinese) - len(blog))]
    filtered = chinese + blog + rest
    log.info("post-stratify: %d cn + %d blog + %d hn/reddit = %d total",
             len(chinese), len(blog), len(rest), len(filtered))

    cluster = cluster_and_summarize(filtered)
    if cluster is None or not cluster.topics:
        log.warning("clustering failed; writing empty news file")
        write_json(CACHE_DIR / "processed_news.json", {
            "date": now_iso_date(),
            "topics": [],
            "items": [],
        })
        return

    # Trim to MAX_NEWS_TOPICS and resolve indices to source dicts
    topics_out: list[dict] = []
    for t in cluster.topics[:MAX_NEWS_TOPICS]:
        srcs: list[dict] = []
        for i in t.source_indices:
            if 0 <= i < len(filtered):
                it = filtered[i]
                srcs.append({
                    "title": it.get("title", ""),
                    "url": it.get("url", ""),
                    "source": it.get("source", ""),
                    "points": int(it.get("points") or 0),
                })
        if not srcs:
            continue
        topics_out.append({
            "title": t.title,
            "summary": t.summary,
            "tags": t.tags or [],
            "sources": srcs,
        })

    write_json(CACHE_DIR / "processed_news.json", {
        "date": now_iso_date(),
        "topics": topics_out,
        "items": filtered,
    })
    log.info("clustered into %d topics covering %d items",
             len(topics_out),
             sum(len(t["sources"]) for t in topics_out))


if __name__ == "__main__":
    main()
