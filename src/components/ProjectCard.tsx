import { ExternalLink, Star } from "lucide-react";
import type { ProjectItem } from "@/types";
import { compactNumber } from "@/lib/format";
import { TagList } from "@/components/TagList";

interface ProjectCardProps {
  item: ProjectItem;
}

export function ProjectCard({ item }: ProjectCardProps) {
  return (
    <article className="project-card">
      <div className="project-topline">
        <div>
          <p className="source-label">{item.language ?? "Project"}</p>
          <h3>{item.name}</h3>
        </div>
        <span className="star-badge">
          <Star size={15} />
          {compactNumber(item.stars)}
        </span>
      </div>
      <p>{item.summary}</p>
      <ul className="takeaway-list">
        {item.takeaways.slice(0, 3).map((takeaway) => (
          <li key={takeaway}>{takeaway}</li>
        ))}
      </ul>
      <TagList tags={item.tags} limit={5} />
      <a className="text-link" href={item.url} target="_blank" rel="noreferrer">
        查看项目 <ExternalLink size={14} />
      </a>
    </article>
  );
}
