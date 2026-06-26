from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import feedparser
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field


DEFAULT_CONFIG_PATH = Path("config/sources.json")

INTEREST_KEYWORDS = [
    "agent",
    "llm",
    "language model",
    "multimodal",
    "vision-language",
    "rag",
    "retrieval",
    "embedding",
    "inference",
    "alignment",
    "post-training",
    "reasoning",
    "diffusion",
    "qwen",
    "deepseek",
    "openai",
    "anthropic",
    "ai",
    "智能体",
    "多模态",
    "视觉语言",
    "后训练",
    "对齐",
    "奖励模型",
    "生成式推荐",
    "生成式检索",
    "搜推",
]

TAG_RULES = {
    "Agent": ["agent", "tool", "trajectory", "workflow"],
    "Multimodal": ["multimodal", "vision", "video", "image", "vlm"],
    "Training": ["training", "alignment", "post-training", "rlhf", "dpo", "grpo"],
    "Inference": ["inference", "quantization", "decode", "latency", "throughput"],
    "RAG": ["rag", "retrieval", "embedding", "vector"],
    "RecSys": ["recommend", "ranking", "retrieval", "recsys"],
    "Evaluation": ["benchmark", "evaluation", "eval"],
}

CHINESE_RSS = {
    "机器之心": "https://www.jiqizhixin.com/rss",
    "量子位": "https://www.qbitai.com/feed",
    "InfoQ AI": "https://www.infoq.cn/feed/ai",
    "新智元": "https://www.aigc.cn/rss",
}

DEFAULT_SOURCE_CONFIG: dict[str, Any] = {
    "interests": {
        "keywords": INTEREST_KEYWORDS,
    },
    "sources": {
        "arxiv": {
            "enabled": True,
            "query": "cat:cs.AI OR cat:cs.CL OR cat:cs.CV OR cat:cs.LG OR cat:cs.IR",
        },
        "hugging_face": {
            "enabled": True,
            "url": "https://huggingface.co/papers",
        },
        "hacker_news": {
            "enabled": True,
            "query": "agent OR multimodal OR post-training OR recommendation OR retrieval OR search",
        },
        "reddit": {
            "enabled": True,
            "subreddits": ["LocalLLaMA", "MachineLearning", "singularity"],
        },
        "chinese_media": {
            "enabled": True,
            "rss": CHINESE_RSS,
        },
    },
}


class SourceStatus(BaseModel):
    source: str
    ok: bool
    fetched: int
    message: str | None = None
    updatedAt: str


class RawItem(BaseModel):
    kind: str
    title: str
    url: str
    source: str
    summary: str = ""
    publishedAt: str | None = None
    authors: list[str] = Field(default_factory=list)
    categories: list[str] = Field(default_factory=list)
    stars: int | None = None
    language: str | None = None
    score: int = 0


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stable_id(prefix: str, value: str) -> str:
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:48]
    return f"{prefix}-{slug}-{digest}" if slug else f"{prefix}-{digest}"


def clean_text(value: str, limit: int = 420) -> str:
    raw = value or ""
    if "<" in raw and ">" in raw:
        raw = BeautifulSoup(raw, "html.parser").get_text(" ")
    text = re.sub(r"\s+", " ", raw).strip()
    return text if len(text) <= limit else f"{text[:limit].rstrip()}..."


def infer_tags(title: str, summary: str) -> list[str]:
    haystack = f"{title} {summary}".lower()
    tags = [tag for tag, needles in TAG_RULES.items() if any(needle in haystack for needle in needles)]
    return tags[:6] or ["AI"]


def load_source_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return DEFAULT_SOURCE_CONFIG

    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    merged = DEFAULT_SOURCE_CONFIG | config
    merged["sources"] = DEFAULT_SOURCE_CONFIG["sources"] | config.get("sources", {})
    merged["interests"] = DEFAULT_SOURCE_CONFIG["interests"] | config.get("interests", {})
    return merged


def get_interest_keywords(config: dict[str, Any]) -> list[str]:
    values = config.get("interests", {}).get("keywords", INTEREST_KEYWORDS)
    return [str(value).lower() for value in values if str(value).strip()]


def is_interest_related(title: str, summary: str = "", keywords: list[str] | None = None) -> bool:
    haystack = f"{title} {summary}".lower()
    candidates = keywords or INTEREST_KEYWORDS
    return any(keyword.lower() in haystack for keyword in candidates)


async def fetch_arxiv(
    client: httpx.AsyncClient,
    limit: int,
    query: str,
    keywords: list[str],
) -> tuple[list[RawItem], SourceStatus]:
    source = "arXiv"
    url = (
        "https://export.arxiv.org/api/query?"
        f"search_query={quote_plus(query)}&sortBy=submittedDate&sortOrder=descending&max_results={limit * 4}"
    )
    try:
        response = await client.get(url)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        items: list[RawItem] = []
        for entry in feed.entries:
            title = clean_text(entry.get("title", ""), 260)
            summary = clean_text(entry.get("summary", ""))
            if not is_interest_related(title, summary, keywords):
                continue
            items.append(
                RawItem(
                    kind="paper",
                    title=title,
                    url=entry.get("link", ""),
                    source=source,
                    summary=summary,
                    publishedAt=entry.get("published", "")[:10],
                    authors=[author.name for author in entry.get("authors", [])][:8],
                    categories=[tag.get("term", "") for tag in entry.get("tags", [])][:3],
                    score=score_item(title, summary, 35),
                )
            )
            if len(items) >= limit:
                break
        return items, SourceStatus(source=source, ok=True, fetched=len(items), updatedAt=now_iso())
    except Exception as exc:
        return [], SourceStatus(source=source, ok=False, fetched=0, message=str(exc), updatedAt=now_iso())


async def fetch_hn(
    client: httpx.AsyncClient,
    limit: int,
    query: str,
    keywords: list[str],
) -> tuple[list[RawItem], SourceStatus]:
    source = "Hacker News"
    url = f"https://hn.algolia.com/api/v1/search_by_date?query={quote_plus(query)}&tags=story"
    try:
        response = await client.get(url)
        response.raise_for_status()
        hits = response.json().get("hits", [])
        items: list[RawItem] = []
        for hit in hits:
            title = clean_text(hit.get("title") or hit.get("story_title") or "", 220)
            if not title or not is_interest_related(title, "", keywords):
                continue
            link = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
            points = int(hit.get("points") or 0)
            kind = "project" if "github.com" in link.lower() else "news"
            items.append(
                RawItem(
                    kind=kind,
                    title=title,
                    url=link,
                    source=source,
                    summary=(
                        "Hacker News 发现的开源 AI 项目，适合进一步评估复用价值。"
                        if kind == "project"
                        else "Hacker News 社区讨论信号，适合观察海外开发者对 AI 产品、模型与基础设施的反馈。"
                    ),
                    publishedAt=hit.get("created_at"),
                    score=min(95, 45 + points // 8),
                )
            )
            if len(items) >= limit:
                break
        return items, SourceStatus(source=source, ok=True, fetched=len(items), updatedAt=now_iso())
    except Exception as exc:
        return [], SourceStatus(source=source, ok=False, fetched=0, message=str(exc), updatedAt=now_iso())


async def fetch_reddit(
    client: httpx.AsyncClient,
    limit: int,
    subreddits: list[str],
    keywords: list[str],
) -> tuple[list[RawItem], SourceStatus]:
    source = "Reddit"
    items: list[RawItem] = []
    try:
        for subreddit in subreddits:
            response = await client.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=15")
            response.raise_for_status()
            for child in response.json().get("data", {}).get("children", []):
                data = child.get("data", {})
                title = clean_text(data.get("title", ""), 220)
                summary = clean_text(data.get("selftext", ""))
                if not title or not is_interest_related(title, summary, keywords):
                    continue
                outbound_url = data.get("url") or ""
                kind = "project" if "github.com" in outbound_url.lower() else "news"
                items.append(
                    RawItem(
                        kind=kind,
                        title=title,
                        url=outbound_url if kind == "project" else f"https://www.reddit.com{data.get('permalink', '')}",
                        source=f"r/{subreddit}",
                        summary=summary or (
                            "Reddit 发现的 AI 开源项目，适合跟踪模型部署、工具链或应用生态。"
                            if kind == "project"
                            else "Reddit AI 社区热帖，反映模型部署、开源生态与硬件实践的一线讨论。"
                        ),
                        publishedAt=datetime.fromtimestamp(data.get("created_utc", 0), UTC).isoformat(),
                        score=min(94, 40 + int(data.get("score") or 0) // 30),
                    )
                )
                if len(items) >= limit:
                    break
        return items[:limit], SourceStatus(source=source, ok=True, fetched=len(items[:limit]), updatedAt=now_iso())
    except Exception as exc:
        return items[:limit], SourceStatus(source=source, ok=False, fetched=len(items[:limit]), message=str(exc), updatedAt=now_iso())


async def fetch_hugging_face(
    client: httpx.AsyncClient,
    limit: int,
    url: str,
    keywords: list[str],
) -> tuple[list[RawItem], SourceStatus]:
    source = "Hugging Face"
    try:
        response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        items: list[RawItem] = []
        for link in soup.select('a[href^="/papers/"]'):
            title = clean_text(link.get_text(" "), 220)
            href = link.get("href", "")
            summary = "Hugging Face Daily Papers 热门论文，代表社区关注的模型、数据和工程方向。"
            if len(title) < 12 or not href or not is_interest_related(title, summary, keywords):
                continue
            items.append(
                RawItem(
                    kind="paper",
                    title=title,
                    url=f"https://huggingface.co{href}",
                    source=source,
                    summary=summary,
                    publishedAt=datetime.now(UTC).date().isoformat(),
                    score=72,
                )
            )
            if len(items) >= limit:
                break
        return items, SourceStatus(source=source, ok=True, fetched=len(items), updatedAt=now_iso())
    except Exception as exc:
        return [], SourceStatus(source=source, ok=False, fetched=0, message=str(exc), updatedAt=now_iso())


async def fetch_chinese_media(
    client: httpx.AsyncClient,
    limit: int,
    rss_sources: dict[str, str],
    keywords: list[str],
) -> tuple[list[RawItem], SourceStatus]:
    source = "中文媒体"
    items: list[RawItem] = []
    messages: list[str] = []
    for name, url in rss_sources.items():
        try:
            response = await client.get(url)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            for entry in feed.entries[:8]:
                title = clean_text(entry.get("title", ""), 220)
                summary = clean_text(entry.get("summary", ""))
                if not title or not is_interest_related(title, summary, keywords):
                    continue
                items.append(
                    RawItem(
                        kind="news",
                        title=title,
                        url=entry.get("link", ""),
                        source=name,
                        summary=summary or f"{name} AI 行业动态。",
                        publishedAt=entry.get("published", None),
                        score=68,
                    )
                )
                if len(items) >= limit:
                    break
        except Exception as exc:
            messages.append(f"{name}: {exc}")
        if len(items) >= limit:
            break
    return items[:limit], SourceStatus(
        source=source,
        ok=len(items) > 0,
        fetched=len(items[:limit]),
        message="; ".join(messages) if messages else None,
        updatedAt=now_iso(),
    )


def score_item(title: str, summary: str, base: int) -> int:
    text = f"{title} {summary}".lower()
    score = base + sum(5 for keyword in INTEREST_KEYWORDS if keyword in text)
    return max(45, min(96, score))


def dedupe(items: list[RawItem]) -> list[RawItem]:
    seen: set[str] = set()
    unique: list[RawItem] = []
    for item in items:
        key = re.sub(r"https?://(www\.)?", "", item.url).rstrip("/") or item.title.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def make_takeaways(item: RawItem, tags: list[str]) -> list[str]:
    first_tag = tags[0] if tags else "AI"
    return [
        f"该条目与 {first_tag} 方向相关，值得纳入当日技术雷达。",
        "可进一步阅读原文，判断是否需要进入实验复现或产品调研队列。",
        "若后续配置 LLM 摘要 Key，可自动生成更细的工程参考价值。",
    ]


def build_digest(items: list[RawItem], statuses: list[SourceStatus], output_date: str) -> dict[str, Any]:
    unique = sorted(dedupe(items), key=lambda item: item.score, reverse=True)
    papers = [item for item in unique if item.kind == "paper"]
    news = [item for item in unique if item.kind == "news"]
    projects = [item for item in unique if item.kind == "project"]

    def paper_payload(item: RawItem) -> dict[str, Any]:
        tags = infer_tags(item.title, item.summary)
        return {
            "id": stable_id("paper", item.url or item.title),
            "title": item.title,
            "titleZh": "",
            "url": item.url,
            "arxivId": extract_arxiv_id(item.url),
            "source": item.source,
            "authors": item.authors,
            "institutions": [],
            "categories": item.categories,
            "publishedAt": item.publishedAt or output_date,
            "summary": item.summary,
            "topicLine": " · ".join(tags[:3]),
            "tags": tags,
            "score": max(1, min(10, round(item.score / 10))),
            "takeaways": make_takeaways(item, tags),
        }

    def news_payload(item: RawItem) -> dict[str, Any]:
        tags = infer_tags(item.title, item.summary)
        return {
            "id": stable_id("news", item.url or item.title),
            "title": item.title,
            "summary": item.summary,
            "source": item.source,
            "url": item.url,
            "publishedAt": item.publishedAt,
            "tags": tags,
            "score": item.score,
        }

    def project_payload(item: RawItem) -> dict[str, Any]:
        tags = infer_tags(item.title, item.summary)
        return {
            "id": stable_id("project", item.url or item.title),
            "name": item.title,
            "url": item.url,
            "summary": item.summary,
            "language": item.language,
            "stars": item.stars,
            "tags": tags,
            "takeaways": make_takeaways(item, tags),
            "score": item.score,
        }

    featured = [paper_payload(item) for item in papers[:5]]
    other = [paper_payload(item) for item in papers[5:20]]
    news_payloads = [news_payload(item) for item in news[:12]]
    project_payloads = [project_payload(item) for item in projects[:8]]
    return {
        "date": output_date,
        "generatedAt": now_iso(),
        "stats": {
            "papers": len(featured) + len(other),
            "news": len(news_payloads),
            "projects": len(project_payloads),
            "totalItems": len(featured) + len(other) + len(news_payloads) + len(project_payloads),
        },
        "news": news_payloads,
        "projects": project_payloads,
        "featuredPapers": featured,
        "otherPapers": other,
        "sourceStatus": [status.model_dump() for status in statuses],
    }


def extract_arxiv_id(url: str) -> str | None:
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url)
    return match.group(1) if match else None


def write_outputs(digest: dict[str, Any], public_dir: Path) -> None:
    data_dir = public_dir / "data"
    daily_dir = data_dir / "daily"
    paper_dir = data_dir / "papers"
    daily_dir.mkdir(parents=True, exist_ok=True)
    paper_dir.mkdir(parents=True, exist_ok=True)

    date = digest["date"]
    daily_path = daily_dir / f"{date}.json"
    daily_path.write_text(json.dumps(digest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    papers = digest["featuredPapers"] + digest["otherPapers"]
    for paper in papers:
        (paper_dir / f"{paper['id']}.json").write_text(
            json.dumps(paper, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    dates = sorted({path.stem for path in daily_dir.glob("*.json")}, reverse=True)
    all_tags: Counter[str] = Counter()
    all_sources: Counter[str] = Counter()
    total_items = 0
    for path in daily_dir.glob("*.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        total_items += payload["stats"]["totalItems"]
        for collection in ["news", "projects", "featuredPapers", "otherPapers"]:
            for item in payload.get(collection, []):
                all_tags.update(item.get("tags", []))
                all_sources.update([item.get("source", "unknown")])

    index = {
        "latestDate": dates[0],
        "dates": dates,
        "totalItems": total_items,
        "tags": dict(all_tags.most_common()),
        "sources": dict(all_sources.most_common()),
    }
    (data_dir / "site-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (data_dir / "sources-status.json").write_text(
        json.dumps(digest["sourceStatus"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def is_enabled(config: dict[str, Any], source_name: str) -> bool:
    return bool(config.get("sources", {}).get(source_name, {}).get("enabled", True))


async def collect(limit: int, config: dict[str, Any]) -> tuple[list[RawItem], list[SourceStatus]]:
    headers = {"User-Agent": "AI-Daily-Bot/0.1 (+https://github.com/)"}
    timeout = httpx.Timeout(18.0, connect=8.0)
    sources = config.get("sources", {})
    keywords = get_interest_keywords(config)
    tasks = []
    async with httpx.AsyncClient(headers=headers, timeout=timeout, follow_redirects=True) as client:
        if is_enabled(config, "arxiv"):
            arxiv = sources.get("arxiv", {})
            tasks.append(fetch_arxiv(client, limit, str(arxiv.get("query", "")), keywords))
        if is_enabled(config, "hugging_face"):
            hugging_face = sources.get("hugging_face", {})
            tasks.append(fetch_hugging_face(client, max(5, limit // 2), str(hugging_face.get("url", "")), keywords))
        if is_enabled(config, "hacker_news"):
            hacker_news = sources.get("hacker_news", {})
            tasks.append(fetch_hn(client, limit, str(hacker_news.get("query", "")), keywords))
        if is_enabled(config, "reddit"):
            reddit = sources.get("reddit", {})
            subreddits = [str(value) for value in reddit.get("subreddits", [])]
            tasks.append(fetch_reddit(client, limit, subreddits, keywords))
        if is_enabled(config, "chinese_media"):
            chinese_media = sources.get("chinese_media", {})
            rss_sources = {str(key): str(value) for key, value in chinese_media.get("rss", {}).items()}
            tasks.append(fetch_chinese_media(client, limit, rss_sources, keywords))

        if not tasks:
            return [], []

        results = await asyncio_gather_safe(*tasks)
    items: list[RawItem] = []
    statuses: list[SourceStatus] = []
    for source_items, status in results:
        items.extend(source_items)
        statuses.append(status)
    return items, statuses


async def asyncio_gather_safe(*coroutines: Any) -> list[Any]:
    import asyncio

    return await asyncio.gather(*coroutines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch AI daily digest data.")
    parser.add_argument("--public-dir", type=Path, default=Path("public"))
    parser.add_argument("--date", default=datetime.now(UTC).date().isoformat())
    parser.add_argument("--limit", type=int, default=24)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    args = parser.parse_args()

    import asyncio

    config = load_source_config(args.config)
    items, statuses = asyncio.run(collect(args.limit, config))
    digest = build_digest(items, statuses, args.date)
    write_outputs(digest, args.public_dir)
    print(f"generated {digest['stats']['totalItems']} items for {args.date}")


if __name__ == "__main__":
    main()
