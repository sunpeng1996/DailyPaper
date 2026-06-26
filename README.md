# AI Daily

参考 `https://slinene.github.io/ai-papers-daily/` 搭建的 GitHub Pages 静态日报站点。站点每天从 arXiv、Hugging Face Daily Papers、Hacker News、Reddit 和主流中文 AI 媒体抓取 AI 行业动态、热门项目与最新论文，并生成可归档的 JSON 数据。

## 本地开发

```bash
npm install
npm run dev
```

## 生成每日数据

```bash
pip install -r requirements.txt
python scripts/fetch_daily.py --public-dir public --config config/sources.json
```

生成结果位于：

- `public/data/site-index.json`
- `public/data/daily/YYYY-MM-DD.json`
- `public/data/papers/*.json`
- `public/data/sources-status.json`

## 数据源与兴趣筛选

数据源和兴趣关键词集中配置在 `config/sources.json`。

当前默认数据源：

- `arxiv`：arXiv Atom API，默认查询 `cs.AI`、`cs.CL`、`cs.CV`、`cs.LG`、`cs.IR`。
- `hugging_face`：Hugging Face Daily Papers 页面。
- `hacker_news`：Hacker News Algolia Search API。
- `reddit`：`LocalLLaMA`、`MachineLearning`、`singularity`、`ArtificialInteligence`。
- `chinese_media`：机器之心、量子位、InfoQ AI、新智元 RSS。

前置筛选只保留以下方向相关内容：

- Agent
- 多模态大模型
- 后训练 / 对齐 / 偏好优化
- 生成式搜推 / 生成式推荐 / 生成式检索

添加更多来源：

- 新增中文媒体 RSS：在 `sources.chinese_media.rss` 增加 `"名称": "RSS_URL"`。
- 新增 Reddit 版块：在 `sources.reddit.subreddits` 追加版块名。
- 调整 HN 查询：修改 `sources.hacker_news.query`。
- 调整 arXiv 范围：修改 `sources.arxiv.query`。
- 关闭某个源：将对应源的 `enabled` 改为 `false`。
- 扩展研究兴趣：在 `interests.keywords` 增加关键词。

## GitHub Pages

项目包含两个 workflow：

- `.github/workflows/pages.yml`：push 后构建并发布静态站点。
- `.github/workflows/daily-digest.yml`：北京时间每天 09:00 定时抓取数据、提交 JSON 并发布站点。

首次使用时，在 GitHub 仓库 Settings -> Pages 中选择 GitHub Actions 作为发布来源。

## 可配置项

当前抓取脚本默认不依赖 LLM API Key，使用规则摘要和标签。后续可以在 `scripts/fetch_daily.py` 中接入 OpenAI/Ark 兼容接口，增强中文摘要与工作参考价值。
