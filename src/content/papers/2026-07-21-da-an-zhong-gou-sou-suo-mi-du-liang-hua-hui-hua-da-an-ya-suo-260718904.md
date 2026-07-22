---
title: 'Answer-Reconstruction Search Density: Measuring the Query and Source Work
  Compressed by Conversational Answers'
title_zh: 答案重构搜索密度：量化会话答案压缩的查询与源搜索工作量
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso, Tel Aviv, Israel
arxiv_id: '2607.18904'
url: https://arxiv.org/abs/2607.18904
pdf_url: https://arxiv.org/pdf/2607.18904
published: '2026-07-21'
collected: '2026-07-22'
category: Eval
direction: 会话搜索评估 · 信息压缩效率量化
tags:
- conversational search
- evaluation metric
- query compression
- information retrieval
- answer evaluation
one_liner: 提出ARSD指标量化会话生成答案背后对应的最小传统搜索工作量
practical_value: '- 对话Agent/RAG场景可借鉴ARSD指标量化生成回答对应的检索工作量，优化query拆分/生成策略，减少冗余检索请求，降低推理成本

  - 电商导购/客服Agent场景可复用该指标评估答案信息压缩效率，平衡回答信息量与检索耗时，提升用户体验

  - 多轮会话搜索场景可复用文中的答案原子单元覆盖校准方法，优化query改写/召回逻辑，提升检索命中率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有检索指标仅评估排序、用户effort或事实支撑性，无法量化会话系统将多步搜索、结果比对流程压缩为单条合成答案的效率，缺少对会话搜索压缩工作量的量化手段。
### 方法关键点
1. 定义ARSD（Answer-Reconstruction Search Density）：固定重构策略下，覆盖目标比例可检索答案原子单元所需的最少不同查询动作数；
2. 同步定义页面密度指标，拆分查询压缩、源压缩两类贡献；
3. 分两阶段验证：先基于私有183条信息寻求会话语料做结构覆盖诊断，再用6个合成任务、36个固定查询做公开校准。
### 关键结果数字
私有语料中覆盖80%答案单元中位数需要3个词汇facet，每选中1个facet中位数覆盖3.25个单元；多轮对话ARSD差异90%以上由答案单元数量而非对话深度贡献；公开校准场景下，覆盖80%单元的中位数ARSD为1.5次查询、中位数页面密度为2个页面。
