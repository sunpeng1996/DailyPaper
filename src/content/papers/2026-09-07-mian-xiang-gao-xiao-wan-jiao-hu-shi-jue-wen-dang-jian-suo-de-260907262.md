---
title: Query-Aware Token Budgeting for Efficient Late-Interaction Visual Document
  Retrieval
title_zh: 面向高效晚交互视觉文档检索的查询感知Token预算分配方法
authors:
- PS Rishi
- Rajeev Ranjan Dwivedi
- Vinod K Kurmi
affiliations:
- Indian Institute of Science Education and Research Bhopal (IISER Bhopal)
arxiv_id: '2609.07262'
url: https://arxiv.org/abs/2609.07262
pdf_url: https://arxiv.org/pdf/2609.07262
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: 晚交互视觉检索 · 效率优化
tags:
- Late-Interaction
- Visual-Document-Retrieval
- Token-Selection
- Submodular-Optimization
- Efficient-Retrieval
one_liner: 提出查询感知Token预算分配策略，8倍压缩预算下恢复98.39%的晚交互视觉文档全Token检索精度
practical_value: '- 晚交互多模态检索场景可替换静态Pooling为两阶段架构：轻量召回生成候选集+查询感知Token选择重排，兼顾存储成本与检索精度

  - 预算受限的Token选择场景优先采用贪心边际增益策略，8倍压缩下仅损失1.6%精度，效果远优于静态Pooling方案

  - 低延迟交互检索场景可采用Token Top-K策略，延迟更低的同时仍能恢复93.9%的全Token检索精度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
晚交互视觉文档检索需存储单页大量Token embedding，存储与查询计算成本高，静态Pooling方案因预索引时未知查询，无法灵活保留关键证据，精度损失严重。
### 方法关键点
采用两阶段检索架构：1）高压缩热路径索引快速生成候选集；2）将短列表页的Token选择建模为带预算的MaxSim覆盖问题，证明裁剪后的问题为单调子模问题，对比覆盖优先、聚类引导、Token Top-K、边际增益四类选择策略。
### 关键结果
10个ViDoRe任务测试显示：32倍静态Pooling使NDCG@5从无压缩的0.6309降至0.4738；同等候选生成条件下，8倍等价重排预算时，Token Top-K恢复93.93%全Token精度，贪心边际增益策略恢复98.39%；延迟分析验证Token Top-K适合低延迟交互检索，贪心策略为精度上限。
