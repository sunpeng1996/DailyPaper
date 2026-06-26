import { CheckCircle2, CircleAlert } from "lucide-react";
import type { SourceStatus } from "@/types";

interface SourceStatusRailProps {
  items: SourceStatus[];
}

export function SourceStatusRail({ items }: SourceStatusRailProps) {
  return (
    <aside className="source-rail" aria-label="数据源状态">
      <p className="source-rail-title">数据源状态</p>
      <div className="source-list">
        {items.map((item) => (
          <div className="source-row" key={item.source}>
            {item.ok ? <CheckCircle2 size={16} /> : <CircleAlert size={16} />}
            <span>{item.source}</span>
            <strong>{item.fetched}</strong>
          </div>
        ))}
      </div>
    </aside>
  );
}
