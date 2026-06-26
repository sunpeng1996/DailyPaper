import { Link } from "react-router-dom";
import { ArrowRight, ExternalLink } from "lucide-react";
import type { PaperSummary } from "@/types";
import { TagList } from "@/components/TagList";

interface PaperCardProps {
  item: PaperSummary;
  compact?: boolean;
}

export function PaperCard({ item, compact = false }: PaperCardProps) {
  return (
    <article className={compact ? "paper-card paper-card-compact" : "paper-card"}>
      <div className="paper-score">{item.score}/10</div>
      <p className="source-label">{item.source} · {item.categories.join(", ")}</p>
      <h3>{item.titleZh || item.title}</h3>
      {!compact ? <p className="paper-title-en">{item.title}</p> : null}
      <p className="topic-line">{item.topicLine}</p>
      <p>{item.summary}</p>
      {!compact ? (
        <ul className="takeaway-list">
          {item.takeaways.slice(0, 4).map((takeaway) => (
            <li key={takeaway}>{takeaway}</li>
          ))}
        </ul>
      ) : null}
      <TagList tags={item.tags} />
      <div className="card-actions">
        <Link className="text-link" to={`/paper/${item.id}`}>
          深度解读 <ArrowRight size={14} />
        </Link>
        <a className="text-link muted" href={item.url} target="_blank" rel="noreferrer">
          来源 <ExternalLink size={14} />
        </a>
      </div>
    </article>
  );
}
