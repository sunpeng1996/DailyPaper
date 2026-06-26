import { Link } from "react-router-dom";
import { CalendarDays } from "lucide-react";
import { getDailyDigest, getSiteIndex } from "@/lib/data";
import { formatDate } from "@/lib/format";
import { useAsync } from "@/hooks/useAsync";

async function loadArchive() {
  const index = await getSiteIndex();
  const digests = await Promise.all(index.dates.map((date) => getDailyDigest(date)));
  return { index, digests };
}

export default function Archive() {
  const { data, error, loading } = useAsync(loadArchive);

  if (loading) {
    return <main className="page-state">正在读取归档...</main>;
  }

  if (error || !data) {
    return <main className="page-state">归档读取失败：{error}</main>;
  }

  return (
    <main className="archive-page">
      <section className="archive-hero">
        <p className="kicker">Archive</p>
        <h1>历史日报与标签索引</h1>
        <p>当前索引收录 {data.index.totalItems} 条内容，后续由 GitHub Actions 每日追加。</p>
      </section>
      <section className="archive-grid">
        <div className="archive-card">
          <h2>日期</h2>
          {data.digests.map((digest) => (
            <Link className="archive-row" key={digest.date} to="/">
              <CalendarDays size={16} />
              <span>{formatDate(digest.date)}</span>
              <strong>{digest.stats.totalItems}</strong>
            </Link>
          ))}
        </div>
        <div className="archive-card">
          <h2>标签</h2>
          <div className="tag-index">
            {Object.entries(data.index.tags).map(([tag, count]) => (
              <Link key={tag} to={`/tag/${encodeURIComponent(tag.toLowerCase())}`}>
                {tag}<span>{count}</span>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
