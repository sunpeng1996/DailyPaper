---
name: paper_file
description: 把一篇 arXiv 论文加进「论文沉淀」存档。使用场景：用户给一个 arXiv ID / URL（或同时指定主题），希望把这篇论文加入到沉淀里、自动生成详细解读，同步写入 DailyPaper 站点的 archive_papers 并推到 GitHub。触发关键词：「加论文到沉淀」「paper_file」「归入沉淀」。
---

# paper_file

把一篇 arXiv 论文加进 DailyPaper 站点的 `archive_papers` 内容集。

## 资源

- 网站项目：`~/playground/personal/` (GitHub: `sunpeng1996/DailyPaper`)
- 当前已有主题：`gen-rec`（生成式推荐 🎯）/ `gen-search`（生成式搜索 🔎）/ `agentic-rec`（Agent推荐 🧭）/ `user-simulation`（User Simulator 👥）/ `llm-general`（LLM通用 🧠）/ `agent-general`（Agent通用 🤖）/ `agent-auto-research`（Agent Auto-Research 🔬）
- 绑定 LLM：ARK / 豆包（OpenAI 兼容，key 在 `~/playground/api/api_key.txt`）

## 处理流程

用户给一个 arXiv 输入（ID 如 `2510.18821` 或完整 URL）后：

1. **解析主题**。如果用户没指定，从论文摘要里自动推断哪个最贴。无把握就向用户问一次。
2. **运行 `add_paper.py`**，路径见下面 `## 用法`。脚本会：
   - 拉 arXiv 元数据（title / authors / abstract / pdf url / 发表日期）
   - 调 LLM 生成详细解读
   - 写一份 markdown 到 `src/content/archive_papers/{topic}/{slug}.md`
   - 如果传 `--commit`，自动 `git add + commit + push`
3. **告诉用户结果**：site markdown 已写入、是否已推到 GitHub。

## 用法

```bash
# 1) 自动模式：完整一键
python scripts/deep_read.py  # 通过 issue 触发，或本地直接调用

# 2) 本地手动加论文
python skills/paper_file/add_paper.py <arxiv_id_or_url> --topic <topic>
```

## 重要规则

- **永远先把仓库切到干净状态再 commit**。如果有未提交的本地修改，先确认是否一并带上 / stash。
- **若 LLM 调用失败**，脚本会退出非 0；不会留下半成品。
- **避免重复添加**：检查目标主题里是否已有同名 paper，若已存在就跳过并提醒用户。
- **slug**：用 title 做 kebab-case，长度限 70 字符。

## 失败兜底

- arXiv API 拉取失败 → 重试 1 次，仍失败就让用户手动确认是否输错了 ID。
- LLM 调用失败 / 解析失败 → 脚本退出非 0；用户可以重试或换网络。
- git push 冲突 → 不强推，提示用户手工处理。
