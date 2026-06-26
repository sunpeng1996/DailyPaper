import { Link } from "react-router-dom";
import { slugify } from "@/lib/format";

interface TagListProps {
  tags: string[];
  limit?: number;
}

export function TagList({ tags, limit = 6 }: TagListProps) {
  return (
    <div className="tag-list" aria-label="标签列表">
      {tags.slice(0, limit).map((tag) => (
        <Link className="tag-pill" key={tag} to={`/tag/${slugify(tag)}`}>
          {tag}
        </Link>
      ))}
    </div>
  );
}
