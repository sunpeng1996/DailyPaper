# DailyPaper

这是一个 AI 每日论文 + 行业动态静态站：arXiv + Hugging Face Daily Papers + 新闻源 + GitHub 热门项目，经 LLM 处理后写入 Astro content collection，生成静态日报站点。

线上地址：

`https://sunpeng1996.github.io/DailyPaper/`

## 功能

- 首页 Daily Digest：今日论文、新闻、热门项目、累计统计。
- 论文详情页：摘要、方向、标签、分数、深度解读。
- 归档页：按日期聚合。
- 分类页：按 category 聚合。
- 标签页：按 tag 聚合。
- 搜索页：前端静态搜索。
- RSS：`/rss.xml`。
- 自动 pipeline：每天北京时间 09:00 抓取、处理、写 Markdown、构建、发布。
- 可选飞书推送：通过 GitHub Secrets 配置。

## 本地开发

```bash
npm install
npm run dev
```

默认本地路径：

`http://localhost:4321/DailyPaper/`

## 本地构建

```bash
npm run build
```

## 运行完整抓取流水线

需要先配置 `.env`：

```bash
cp .env.example .env
```

至少需要：

```bash
DEEPSEEK_API_KEY=你的 key
SITE_URL=https://sunpeng1996.github.io
BASE_PATH=/DailyPaper
```

然后运行：

```bash
pip install -r requirements.txt
python scripts/run_all.py
```

## GitHub Secrets / Variables

Secrets 不会暴露在公开仓库中。

必需 Secret：

- `DEEPSEEK_API_KEY`

可选 Secrets：

- `FEISHU_WEBHOOK`
- `FEISHU_SECRET`
- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`
- `FEISHU_CHAT_ID`

建议 Variables：

- `SITE_URL=https://sunpeng1996.github.io`
- `BASE_PATH=/DailyPaper`
- `DEEPSEEK_BASE_URL=https://api.deepseek.com`
- `DEEPSEEK_MODEL=deepseek-v4-pro`
- `MAX_PAPERS_PER_DAY=30`
- `MIN_SCORE_KEEP=6`
- `MIN_SCORE_DEEP=8`
