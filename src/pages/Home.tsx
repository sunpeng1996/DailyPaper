import { Link } from "react-router-dom";
import { Activity, Archive, BookOpen, Github, Radio } from "lucide-react";
import { NewsCard } from "@/components/NewsCard";
import { PaperCard } from "@/components/PaperCard";
import { ProjectCard } from "@/components/ProjectCard";
import { SectionHeader } from "@/components/SectionHeader";
import { SourceStatusRail } from "@/components/SourceStatusRail";
import { getDailyDigest } from "@/lib/data";
import { formatDate, formatDateTime } from "@/lib/format";
import { useAsync } from "@/hooks/useAsync";

export default function Home() {
  const { data, error, loading } = useAsync(() => getDailyDigest());

  if (loading) {
    return <main className="page-state">正在读取今日日报...</main>;
  }

  if (error || !data) {
    return <main className="page-state">数据读取失败：{error}</main>;
  }

  return (
    <main className="daily-layout">
      <section className="hero-panel">
        <p className="kicker">今日播报 · Daily Digest</p>
        <h1>{formatDate(data.date)}</h1>
        <p className="hero-copy">
          自动聚合 arXiv、Hugging Face Daily Papers、Hacker News、Reddit 与中文 AI 媒体，
          为研究和工程决策保留高信号密度的每日快照。
        </p>
        <div className="stats-grid">
          <div>
            <strong>{data.stats.papers}</strong>
            <span>论文</span>
          </div>
          <div>
            <strong>{data.stats.news}</strong>
            <span>新闻</span>
          </div>
          <div>
            <strong>{data.stats.projects}</strong>
            <span>项目</span>
          </div>
          <div>
            <strong>{data.stats.totalItems}</strong>
            <span>累计条目</span>
          </div>
        </div>
        <div className="hero-actions">
          <Link className="primary-action" to="/archive">
            <Archive size={16} />
            查看归档
          </Link>
          <a className="secondary-action" href="https://github.com/" target="_blank" rel="noreferrer">
            <Github size={16} />
            GitHub Pages
          </a>
        </div>
        <SourceStatusRail items={data.sourceStatus} />
        <p className="updated-at">生成时间：{formatDateTime(data.generatedAt)}</p>
      </section>

      <section className="content-flow">
        <SectionHeader
          kicker="Industry"
          title="今日行业动态"
          description="优先保留会影响模型、平台、硬件和应用趋势的信号。"
        />
        <div className="news-grid">
          {data.news.map((item) => (
            <NewsCard item={item} key={item.id} />
          ))}
        </div>

        <SectionHeader
          kicker="Projects"
          title="今日热门 AI 项目"
          description="从社区讨论和开源项目中抽取可复用的工程线索。"
          action={<Radio size={18} />}
        />
        <div className="project-grid">
          {data.projects.map((item) => (
            <ProjectCard item={item} key={item.id} />
          ))}
        </div>

        <SectionHeader
          kicker="Papers"
          title="今日精选论文"
          description="按研究价值、工程迁移性和讨论热度排序。"
          action={<BookOpen size={18} />}
        />
        <div className="paper-stack">
          {data.featuredPapers.map((item) => (
            <PaperCard item={item} key={item.id} />
          ))}
        </div>

        <SectionHeader
          kicker="More"
          title="今日其他"
          description="保留更多值得回看的论文与社区信号。"
          action={<Activity size={18} />}
        />
        <div className="compact-list">
          {data.otherPapers.map((item) => (
            <PaperCard compact item={item} key={item.id} />
          ))}
        </div>
      </section>
    </main>
  );
}
