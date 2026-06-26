export interface DigestStats {
  papers: number;
  news: number;
  projects: number;
  totalItems: number;
}

export interface SourceStatus {
  source: string;
  ok: boolean;
  fetched: number;
  message?: string;
  updatedAt: string;
}

export interface NewsItem {
  id: string;
  title: string;
  summary: string;
  source: string;
  url: string;
  publishedAt?: string;
  tags: string[];
  score: number;
}

export interface ProjectItem {
  id: string;
  name: string;
  url: string;
  summary: string;
  language?: string;
  stars?: number;
  tags: string[];
  takeaways: string[];
  score: number;
}

export interface PaperSummary {
  id: string;
  title: string;
  titleZh?: string;
  url: string;
  arxivId?: string;
  source: string;
  authors: string[];
  institutions: string[];
  categories: string[];
  publishedAt: string;
  summary: string;
  topicLine: string;
  tags: string[];
  score: number;
  takeaways: string[];
}

export interface DailyDigest {
  date: string;
  generatedAt: string;
  stats: DigestStats;
  news: NewsItem[];
  projects: ProjectItem[];
  featuredPapers: PaperSummary[];
  otherPapers: PaperSummary[];
  sourceStatus: SourceStatus[];
}

export interface SiteIndex {
  latestDate: string;
  dates: string[];
  totalItems: number;
  tags: Record<string, number>;
  sources: Record<string, number>;
}
