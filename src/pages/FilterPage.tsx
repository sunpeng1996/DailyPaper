import { useParams } from "react-router-dom";
import { NewsCard } from "@/components/NewsCard";
import { PaperCard } from "@/components/PaperCard";
import { ProjectCard } from "@/components/ProjectCard";
import { SectionHeader } from "@/components/SectionHeader";
import { getDailyDigest } from "@/lib/data";
import { deslugify } from "@/lib/format";
import { useAsync } from "@/hooks/useAsync";

export default function FilterPage() {
  const { tag, source } = useParams();
  const keyword = deslugify(tag ?? source);
  const mode = tag ? "标签" : "来源";
  const { data, error, loading } = useAsync(() => getDailyDigest(), keyword);

  if (loading) {
    return <main className="page-state">正在筛选内容...</main>;
  }

  if (error || !data) {
    return <main className="page-state">筛选失败：{error}</main>;
  }

  const lowerKeyword = keyword.toLowerCase();
  const news = data.news.filter((item) =>
    tag ? item.tags.some((value) => value.toLowerCase() === lowerKeyword) : item.source.toLowerCase() === lowerKeyword,
  );
  const projects = data.projects.filter((item) =>
    tag ? item.tags.some((value) => value.toLowerCase() === lowerKeyword) : item.name.toLowerCase().includes(lowerKeyword),
  );
  const papers = [...data.featuredPapers, ...data.otherPapers].filter((item) =>
    tag ? item.tags.some((value) => value.toLowerCase() === lowerKeyword) : item.source.toLowerCase() === lowerKeyword,
  );

  return (
    <main className="filter-page">
      <section className="archive-hero">
        <p className="kicker">{mode}</p>
        <h1>{keyword}</h1>
        <p>基于最新日报的轻量筛选视图，适合快速回看相关内容。</p>
      </section>

      <SectionHeader kicker="Papers" title="相关论文" />
      <div className="compact-list">
        {papers.map((item) => (
          <PaperCard compact item={item} key={item.id} />
        ))}
      </div>

      <SectionHeader kicker="News" title="相关新闻" />
      <div className="news-grid">
        {news.map((item) => (
          <NewsCard item={item} key={item.id} />
        ))}
      </div>

      <SectionHeader kicker="Projects" title="相关项目" />
      <div className="project-grid">
        {projects.map((item) => (
          <ProjectCard item={item} key={item.id} />
        ))}
      </div>
    </main>
  );
}
