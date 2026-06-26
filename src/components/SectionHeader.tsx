import type { ReactNode } from "react";

interface SectionHeaderProps {
  kicker: string;
  title: string;
  description?: string;
  action?: ReactNode;
}

export function SectionHeader({ kicker, title, description, action }: SectionHeaderProps) {
  return (
    <div className="section-header">
      <div>
        <p className="kicker">{kicker}</p>
        <h2>{title}</h2>
        {description ? <p className="section-description">{description}</p> : null}
      </div>
      {action ? <div className="section-action">{action}</div> : null}
    </div>
  );
}
