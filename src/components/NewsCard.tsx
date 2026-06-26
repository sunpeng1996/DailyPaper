import { ExternalLink } from "lucide-react";
import type { NewsItem } from "@/types";
import { TagList } from "@/components/TagList";
import { formatDateTime } from "@/lib/format";

interface NewsCardProps {
  item: NewsItem;
}

export function NewsCard({ item }: NewsCardProps) {
  return (
    <article className="news-card">
      <div className="card-meta">
        <span>{item.source}</span>
        {item.publishedAt ? <span>{formatDateTime(item.publishedAt)}</span> : null}
        <span>score {item.score}</span>
      </div>
      <h3>{item.title}</h3>
      <p>{item.summary}</p>
      <TagList tags={item.tags} />
      <a className="text-link" href={item.url} target="_blank" rel="noreferrer">
        原文 <ExternalLink size={14} />
      </a>
    </article>
  );
}
