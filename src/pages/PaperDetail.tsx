import { Link, useParams } from "react-router-dom";
import { ArrowLeft, ExternalLink } from "lucide-react";
import { TagList } from "@/components/TagList";
import { getPaper } from "@/lib/data";
import { formatDate } from "@/lib/format";
import { useAsync } from "@/hooks/useAsync";

export default function PaperDetail() {
  const { id } = useParams();
  const { data, error, loading } = useAsync(() => getPaper(id ?? ""), id ?? "");

  if (loading) {
    return <main className="page-state">正在读取论文详情...</main>;
  }

  if (error || !data) {
    return <main className="page-state">论文读取失败：{error}</main>;
  }

  return (
    <main className="detail-page">
      <Link className="text-link" to="/">
        <ArrowLeft size={15} />
        返回今日
      </Link>
      <article className="paper-detail">
        <p className="kicker">{data.source} · {formatDate(data.publishedAt)}</p>
        <h1>{data.titleZh || data.title}</h1>
        <p className="paper-title-en">{data.title}</p>
        <div className="detail-meta">
          <span>评分 {data.score}/10</span>
          <span>{data.categories.join(", ")}</span>
          {data.arxivId ? <span>arXiv {data.arxivId}</span> : null}
        </div>
        <TagList tags={data.tags} limit={12} />
        <p className="detail-summary">{data.summary}</p>
        <section>
          <h2>工作参考价值</h2>
          <ul className="takeaway-list detail-takeaways">
            {data.takeaways.map((takeaway) => (
              <li key={takeaway}>{takeaway}</li>
            ))}
          </ul>
        </section>
        <section>
          <h2>作者与机构</h2>
          <p>{data.authors.join(", ") || "待补充"}</p>
          <p>{data.institutions.join(", ") || "待补充"}</p>
        </section>
        <a className="primary-action inline-action" href={data.url} target="_blank" rel="noreferrer">
          打开来源 <ExternalLink size={15} />
        </a>
      </article>
    </main>
  );
}
