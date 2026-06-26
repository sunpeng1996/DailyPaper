#!/usr/bin/env python3
"""paper_file skill — add an arXiv paper to DailyPaper's archive_papers collection.

Workflow:
  1. Resolve arxiv id (accept bare id or arxiv URL)
  2. Fetch arxiv metadata (title, authors, abstract, pdf url, published date)
  3. Use LLM (ARK / DeepSeek compatible) to generate a deep-read markdown
     with the standard 5-section structure
  4. Write src/content/archive_papers/<topic>/<slug>.md
  5. Optionally git commit + push

Usage:
  python skills/paper_file/add_paper.py <arxiv_id_or_url> --topic <id> [--commit]

Env (loaded from .env at project root if present):
  LLM_API_KEY           required (or DEEPSEEK_API_KEY for back-compat)
  LLM_BASE_URL          default https://ark-cn-beijing.bytedance.net/api/v3
  LLM_MODEL             default ep-20260626155131-7psq6
  PAPER_FILE_SITE       override DailyPaper project root
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

import feedparser
import httpx
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError
from slugify import slugify

# ------- Paths & config ------------------------------------------------------

DEFAULT_SITE = Path(__file__).resolve().parents[2]  # personal/


def load_env_from(site: Path) -> None:
    """Best-effort .env load from the project root."""
    env_path = site / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


# ------- Models --------------------------------------------------------------

class DeepReadResult(BaseModel):
    title_zh: str = ""
    idea: str = ""
    tags: list[str] = Field(default_factory=list)
    body_md: str = ""


SYSTEM = """你是论文深度解读专家，读者是 AI 算法工程师。读完整篇论文，产出「可复现细节级」的中文深度解读。
目标不是摘要，而是让工程师读完就能理解到能复现的程度：每个子模块的输入/输出、关键公式（带符号含义）、张量维度、训练目标/loss、关键超参、数据构造。

只输出一个 JSON 对象：
{
  "title_zh": "<中文标题，<=50字>",
  "idea": "<2-3 句卡片摘要，点明核心 idea/范式>",
  "tags": ["<3-5 个英文标签，CamelCase+空格>"],
  "body_md": "<markdown 正文，严格按五大块，用 ## 标题>"
}

body_md 的五大块（标题必须完全一致）：
## 核心思路
一句话讲清解决什么问题、用什么关键 idea。
## 整体实现思路
端到端 pipeline：输入→各阶段→输出（可用代码块画 ASCII 流程）。
## 子模块实现（可复现细节）
逐个子模块用 ### 小标题，写 输入/输出、关键公式（带符号含义）、维度/超参/loss、数据构造。宁可长、带公式。
## 实验设置与结果
数据集/baseline/指标定义/**关键数字用 markdown 表格**/消融结论。
## 思考与可参考价值
批判性看局限 + 对电商/搜索推荐/Agent 方向的可借鉴点。

要求：信息密度高、不要套话；术语保留英文；公式用行内 `...` 或 $$ 块；数字结果用 markdown 表格。"""


def call_llm(paper: dict) -> DeepReadResult:
    api_key = os.environ.get("LLM_API_KEY") or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("LLM_API_KEY missing (looked in env and .env)")
    base_url = (os.environ.get("LLM_BASE_URL")
                or os.environ.get("DEEPSEEK_BASE_URL")
                or "https://ark-cn-beijing.bytedance.net/api/v3")
    model = (os.environ.get("LLM_MODEL")
             or os.environ.get("DEEPSEEK_MODEL")
             or "ep-20260626155131-7psq6")

    client = OpenAI(api_key=api_key, base_url=base_url, timeout=300, max_retries=2)
    authors_str = ", ".join(paper["authors"][:6]) + (" 等" if len(paper["authors"]) > 6 else "")
    user = (
        f"arxiv id: {paper['arxiv_id']}\n"
        f"标题: {paper['title']}\n"
        f"作者: {authors_str}\n"
        f"发表: {paper['published']}\n\n"
        f"摘要:\n{paper['abstract']}\n"
    )

    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
    ]
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=12000,
            )
        except OpenAIError as exc:
            print(f"llm api error attempt={attempt}: {exc}", file=sys.stderr)
            continue
        text = (resp.choices[0].message.content or "").strip()
        try:
            return DeepReadResult.model_validate_json(text)
        except (ValidationError, json.JSONDecodeError) as exc:
            print(f"llm parse failed attempt={attempt}: {exc} | text={text[:200]}",
                  file=sys.stderr)
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user",
                             "content": "返回的不是合法 JSON 或字段不符合 schema。只返回一个 JSON 对象。"})
    raise SystemExit("llm failed after 2 attempts")


# ------- arXiv fetch ---------------------------------------------------------

def resolve_arxiv_id(raw: str) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})", raw or "")
    if not m:
        raise SystemExit(f"无法从输入解析 arxiv id: {raw}")
    return m.group(1)


def fetch_meta(aid: str) -> dict:
    feed = feedparser.parse(f"http://export.arxiv.org/api/query?id_list={aid}")
    if not feed.entries:
        return {"title": aid, "authors": [], "published": "", "summary": "",
                "url": f"https://arxiv.org/abs/{aid}", "arxiv_id": aid}
    e = feed.entries[0]
    authors = [a.name for a in getattr(e, "authors", [])]
    published = getattr(e, "published", "")[:10]  # YYYY-MM-DD
    title = re.sub(r"\s+", " ", e.title).strip()
    summary = re.sub(r"\s+", " ", e.summary).strip()
    url = f"https://arxiv.org/abs/{aid}"
    return {"title": title, "authors": authors, "published": published,
            "abstract": summary, "url": url, "arxiv_id": aid}


# ------- Markdown writer -----------------------------------------------------

TOPIC_NAMES = {
    "gen-rec": ("生成式推荐", "🎯"),
    "gen-search": ("生成式搜索", "🔎"),
    "agentic-rec": ("Agent推荐", "🧭"),
    "user-simulation": ("User Simulator", "👥"),
    "llm-general": ("LLM通用", "🧠"),
    "agent-general": ("Agent通用", "🤖"),
    "agent-auto-research": ("Agent Auto-Research", "🔬"),
}


def make_slug(title: str) -> str:
    s = slugify(title, lowercase=False, max_length=70, word_boundary=True)
    return s or "paper"


def write_markdown(site: Path, topic: str, paper: dict, result: DeepReadResult) -> Path:
    archive_dir = site / "src" / "content" / "archive_papers" / topic
    archive_dir.mkdir(parents=True, exist_ok=True)
    slug = make_slug(paper["title"])
    path = archive_dir / f"{slug}.md"

    tags_line = ", ".join(f'"{t}"' for t in (result.tags or []))
    authors_line = ", ".join(paper["authors"][:8])

    frontmatter = f"""---
title: "{paper['title']}"
title_zh: "{result.title_zh}"
date: {paper['published']}
arxiv_id: "{paper['arxiv_id']}"
url: "{paper['url']}"
authors: "{authors_line}"
tags: [{tags_line}]
topic: "{topic}"
---

{result.body_md}
"""
    path.write_text(frontmatter, encoding="utf-8")
    return path


# ------- Git helpers ---------------------------------------------------------

def git_commit_push(site: Path, slug: str, topic: str) -> None:
    subprocess.run(["git", "add", "src/content/archive_papers"],
                   cwd=site, check=True)
    result = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=site)
    if result.returncode == 0:
        print("[git] no changes")
        return
    subprocess.run(["git", "commit", "-m", f"add paper: {slug} -> {topic}"],
                   cwd=site, check=True)
    subprocess.run(["git", "push"], cwd=site, check=True)


# ------- Main ----------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Add an arXiv paper to DailyPaper archive")
    parser.add_argument("arxiv", help="arxiv id or URL")
    parser.add_argument("--topic", required=True,
                        help="topic id: " + ", ".join(TOPIC_NAMES.keys()))
    parser.add_argument("--site", type=Path, default=None,
                        help=f"path to DailyPaper project (default: {DEFAULT_SITE})")
    parser.add_argument("--commit", action="store_true",
                        help="git add + commit + push")
    args = parser.parse_args()

    site = args.site or DEFAULT_SITE
    load_env_from(site)

    topic = args.topic.strip().lower()
    if topic not in TOPIC_NAMES:
        raise SystemExit(f"unknown topic '{topic}'. valid: {', '.join(TOPIC_NAMES.keys())}")

    aid = resolve_arxiv_id(args.arxiv)
    print(f"[arxiv] fetching metadata for {aid} ...", file=sys.stderr)
    paper = fetch_meta(aid)
    print(f"[arxiv] title: {paper['title'][:80]}", file=sys.stderr)

    print("[llm] generating deep read ...", file=sys.stderr)
    result = call_llm(paper)

    path = write_markdown(site, topic, paper, result)
    print(f"[md]    wrote {path}", file=sys.stderr)

    if args.commit:
        print("[git]   commit + push DailyPaper", file=sys.stderr)
        git_commit_push(site, make_slug(paper["title"]), topic)

    print(json.dumps({
        "slug": make_slug(paper["title"]),
        "topic": topic,
        "path": str(path),
        "ok": True,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
