---
title: 'Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files'
title_zh: 跳过压缩器：选择完整文件的代码Agent能修复更多问题
authors:
- Xiaocong Yang
- Rishit Chatterjee
- Himanshu Udupi
- Vikram Ramavarapu
- ChengXiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.21073'
url: https://arxiv.org/abs/2610.21073
pdf_url: https://arxiv.org/pdf/2610.21073
published: '2026-10-14'
collected: '2026-10-19'
category: Agent
direction: 代码Agent · 上下文管理优化
tags:
- CodingAgent
- ContextSelection
- PromptCompression
- CodeRetrieval
- SWEBench
one_liner: 相同token预算下，选择完整原文文件的代码Agent上下文策略优于压缩与检索方案
practical_value: '- 做精准编辑类Agent（如电商商品详情/广告文案自动优化、推荐规则迭代Agent）时，优先选择完整原文的上下文单元，避免token级压缩导致修改内容无法匹配原文本，生效失败

  - 上下文资源分配优先级：先保障核心待编辑文件/内容块的召回准确率，再追加关联内容，不要为了塞入更多内容用有损压缩牺牲原文准确性

  - 预算有限时，用LLM多轮投票筛选核心整文件/整内容块，比BM25、向量检索准确率更高，无需额外训练压缩模型，工程落地成本更低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
代码Agent处理的代码库规模远大于LLM上下文窗口，现有方案存在两类固有缺陷：分块检索按语义相似度排序容易漏需要修改的核心文件，prompt压缩会修改原文内容，导致生成的补丁无法匹配原代码、应用失败，相同token预算下的最优上下文选择策略一直缺乏明确的对比结论。

### 方法关键点
- 轻量选择器CQ2-CARE：让LLM独立3次回答需要修改的文件，取交集作为核心文件完整原文展示，再用grep补充关联的定义、调用代码片段，全程无压缩模型，无额外训练成本
- 定义两个可迁移的核心评估指标：gold-file recall（核心待修改文件召回率ρ）、verbatim lines（上下文原文匹配率ε），可量化不同上下文策略的损失来源

### 关键实验
在SWE-rebench的300个真实Python代码issue上做严格预算匹配对比，base模型采用GPT-5.6和Claude Opus 5，对比3类通用压缩器、3类检索方案、2个专门训练的代码Agent SOTA。结果：CQ2-CARE的问题修复率达43.7%（GPT-5.6）、46.7%（Claude Opus 5），比最优压缩器高6.3个百分点，比最优检索方案高9.3/12.7个百分点，也优于两个专门训练的SWE-Pruner、SweRank。

**最值得记住的一句话**：对于需要基于原文做精准编辑的Agent任务，上下文预算优先花在选对核心内容、完整保留原文上，远好于塞入更多经压缩/检索的不精准内容。
