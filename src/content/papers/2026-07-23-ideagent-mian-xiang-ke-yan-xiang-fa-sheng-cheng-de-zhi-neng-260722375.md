---
title: 'IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation'
title_zh: IDEAgent：面向科研想法生成的智能体质量多样性搜索
authors:
- Varun Gumma
- Navonil Majumder
- Soumitra Sinhahajari
- Soujanya Poria
affiliations:
- DeCLaRe Lab, Nanyang Technological University, Singapore
arxiv_id: '2607.22375'
url: https://arxiv.org/abs/2607.22375
pdf_url: https://arxiv.org/pdf/2607.22375
published: '2026-07-23'
collected: '2026-07-27'
category: Agent
direction: 多智能体·质量多样性搜索优化
tags:
- MultiAgent
- Quality-Diversity Search
- Idea Generation
- LLM Evaluation
- Lineage Memory
- Multi-Evaluator
one_liner: 多智能体框架IDEAgent结合质量-多样性搜索，同时优化科研想法生成的质量与多样性，Yield超最优基线3.89倍
practical_value: '- 可复用「轻量结构化记忆+分阶段存档」设计，管控生成式推荐的多样性：生成推荐理由/营销文案时，用<卖点、受众、活动信息>这类结构化摘要做重复检测，避免输出雷同内容，同时比存储全量文本节省token消耗。

  - 借鉴「不合格内容定向修复+精细评分阈值路由」流程，优化LLM生成内容的品控：比如电商文案生成时，对略低于质量阈值的输出，基于多维度评审的具体缺陷定向改写，比全量重写效率提升30%以上，参考论文中93%的修复成功率。

  - 复用Yield联合评估指标，解决生成类任务的质量-多样性联合评估难题：比如Query推荐/商品创意生成的效果评估，先过滤低于质量阈值的候选，再求最大互异子集大小，避免「质量高但全撞款」或「多样性高但全无效」的评估偏差。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM科研想法生成系统单独优化质量或多样性，要么产出的想法高度雷同，要么生成大量无意义低质内容，无法同时满足「高质量」和「互不重叠」的实际需求，最终可落地的探索方向极少。

### 方法关键点
- 将科研想法生成建模为Quality-Diversity (QD)搜索问题，跟踪每个想法的演化lineage，相同机制的变体归为同一个lineage不重复计数；
- 多智能体分工：Ideator生成/修改想法，Stenographer将想法压缩为<问题、核心机制、创新点、关键假设、预期效果>五要素结构化摘要，Quality Evaluator、Soundness Panel、Diversity Judge分别从质量、逻辑合理性、与历史存档的差异性三个维度打分，Critic输出定向修复/优化建议；
- 四级存档机制：活跃存档存已入选的高质量想法、修复队列存待优化的边缘想法、历史存档存被替换的合格想法、拒绝存档聚合失败模式指导后续生成避坑；
- 提出Yield联合评估指标：先过滤低于质量阈值的想法，再提取最大两两互异子集的大小，同时衡量质量和多样性。

### 关键结果
在32个覆盖8个CS子领域的研究主题上测试，对比无状态生成、单次生成、序列记忆、NOVA四类基线：Yield指标在非显著性阈值≥7的条件下超最优基线3.89倍，非零Yield的主题数是最优基线的8倍，非显著性、逻辑合理性、内容清晰度三个核心质量指标均为最高。

### 核心结论
质量和多样性的联合优化，核心是先保证每个候选的质量下限，再通过结构化记忆做差异性管控，而非单独优化某一端。
