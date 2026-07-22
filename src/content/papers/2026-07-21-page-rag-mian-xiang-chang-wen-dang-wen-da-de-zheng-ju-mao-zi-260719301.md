---
title: 'PAGE-RAG: Evidence-Grounded Adaptive Graph Retrieval for Long-Document Question
  Answering'
title_zh: PAGE-RAG：面向长文档问答的证据锚定自适应图检索RAG框架
authors:
- Xingyu Chen
- Junxiu An
- Jun Guo
- Li Wang
affiliations:
- 成都信息工程大学
- 北京航空航天大学
arxiv_id: '2607.19301'
url: https://arxiv.org/abs/2607.19301
pdf_url: https://arxiv.org/pdf/2607.19301
published: '2026-07-21'
collected: '2026-07-22'
category: RAG
direction: GraphRAG优化 · 长文档问答
tags:
- GraphRAG
- Long-document QA
- Adaptive Retrieval
- Evidence Grounding
- Knowledge Boundary
one_liner: 将图作为语义骨架而非原文替代，结合自适应路由与证据边界控制，优化长文档GraphRAG的质量效率可靠性
practical_value: '- 搭建业务RAG系统（电商商品知识库、Agent记忆库、客服问答库等）时，不要用GraphRAG完全替代文本检索，保留文本作为证据底座，图仅做语义导航，可在降低幻觉的同时控制检索成本

  - 可复用query自适应路由逻辑：先对用户query打标（局部/关系/全局、是否多跳、是否需要全局合成），动态选择文本检索、图邻域查询、路径推理、社区摘要等算子组合，分配不同证据的token预算，避免全量图遍历浪费算力，适配高并发实时业务场景

  - 电商咨询、客服等对答案准确性要求高的场景，可直接复用显式证据边界校验机制，证据不足时直接触发拒答，避免生成错误信息误导用户，降低客诉率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG将自动构建的知识图谱视为独立知识源，存在三大核心缺陷：一是自动生成的图是原文的有损投影，丢失局部细节易引发幻觉；二是对所有query采用固定检索逻辑，要么算力浪费严重要么召回不足；三是仅靠prompt软约束生成边界，证据不足时仍会编造答案，可靠性无法保证。

### 方法关键点
- 构建混合知识库：同时保留原文文本库（作为不可替代的证据底座，所有答案可溯源到原始片段）和图语义骨架（按文档类型适配实体/关系提取规则，建立图元素到原文片段的绑定映射）
- 实现query自适应路由：对query打标（查询范围、是否需要多跳、是否需要全局合成、边界敏感度），动态选择召回算子组合，分配不同类型证据的token预算，避免不必要的全局图遍历
- 增加显式证据边界控制：生成前先校验召回证据的充分性，证据不足时直接拒答，而非依赖prompt软约束保证接地性

### 关键实验
在两本长篇书籍（《仿象与拟真》《百年孤独》）和UltraDomain-Mix跨域数据集上对比纯文本RAG、LightRAG、微软GraphRAG：①两个书籍数据集上正确拒答率达100%（24道无答案问题全部正确拒答），宽松准确率最高达92.6%，查询latency比LightRAG低68%；②UltraDomain-Mix上效果接近微软GraphRAG，但单query token消耗仅为后者的1.4%，latency低65%；③消融实验显示，移除文本底座后宽松准确率从90.1%降至58.2%，移除证据约束后正确拒答率从100%降至16.7%。

**最值得记住的一句话**：GraphRAG中的图应该是组织导航知识的语义骨架，而非替代原文的独立知识源，平衡质量、效率、可靠性的核心是始终把原文作为证据底座。
