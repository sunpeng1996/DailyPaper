import type { DailyDigest, SiteIndex } from "@/types";

const DATA_BASE = `${import.meta.env.BASE_URL}data`.replace(/\/+$/, "");

async function readJson<T>(path: string): Promise<T> {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`读取数据失败: ${path}`);
  }

  return response.json() as Promise<T>;
}

export async function getSiteIndex(): Promise<SiteIndex> {
  return readJson<SiteIndex>(`${DATA_BASE}/site-index.json`);
}

export async function getDailyDigest(date?: string): Promise<DailyDigest> {
  const index = await getSiteIndex();
  const targetDate = date ?? index.latestDate;
  return readJson<DailyDigest>(`${DATA_BASE}/daily/${targetDate}.json`);
}

export async function getPaper(id: string): Promise<DailyDigest["featuredPapers"][number]> {
  try {
    return await readJson<DailyDigest["featuredPapers"][number]>(`${DATA_BASE}/papers/${id}.json`);
  } catch {
    const index = await getSiteIndex();
    const digests = await Promise.all(index.dates.map((date) => getDailyDigest(date)));
    const paper = digests
      .flatMap((digest) => [...digest.featuredPapers, ...digest.otherPapers])
      .find((item) => item.id === id);

    if (!paper) {
      throw new Error(`未找到论文: ${id}`);
    }

    return paper;
  }
}
