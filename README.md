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

## 论文沉淀主题

主题 ID、名称、图标及页面顺序统一配置在 `config/paper-topics.json`，深读脚本和本地添加脚本共用该配置。主题即使暂未收录论文，也会显示在论文沉淀页。

新增主题时，同时更新 `.github/ISSUE_TEMPLATE/deep-read.yml` 中的下拉选项，格式为 `图标 名称 (主题ID)`。单篇论文通过 Markdown frontmatter 的 `topic` 指定归属，`topic_name` 和 `topic_icon` 保存显示信息。

每日论文的关注方向与打分偏好仍由 `scripts/process.py` 的 `RELEVANCE_SYSTEM` 控制。

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
