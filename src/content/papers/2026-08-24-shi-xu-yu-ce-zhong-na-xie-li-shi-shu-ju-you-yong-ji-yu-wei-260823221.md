---
title: Which Histories Matter for Time Series Forecasting? Learning Predictive Relevance
  with Future Supervision
title_zh: 时序预测中哪些历史数据有用？基于未来监督学习预测相关性
authors:
- Yong-Hoon Choi
- Youngjin Cho
affiliations:
- Kwangwoon University
arxiv_id: '2608.23221'
url: https://arxiv.org/abs/2608.23221
pdf_url: https://arxiv.org/pdf/2608.23221
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: 检索增强时序预测 · 召回重排优化
tags:
- Time-Series Forecasting
- Retrieval Augmentation
- Reranker
- Privileged Supervision
- Future Supervision
one_liner: 用训练阶段真实未来作为特权监督，训练轻量重排器优化时序预测的历史样本检索
practical_value: '- 电商销量预测、流量预测等时序类业务的RAG pipeline可复用该思路，训练阶段引入未来真实值作为特权监督优化历史样本重排，无推理额外成本

  - 检索重排环节可参考最优相关性分解逻辑，拆分候选全局效用与查询侧兼容性做针对性调优，适配不同业务场景特性

  - 可复用论文的Candidate-Prior、Shuffled-Future控制方法诊断业务相关性模式，选择匹配的检索规则，避免盲目套用统一检索策略'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
时序预测的检索增强方案普遍以历史相似性作为样本有用性的代理指标，无法精准识别对当前查询真正具备预测价值的历史片段，相似性高的样本不一定能提升最终预测效果。
### 方法关键点
1. 定义预测相关性为推理时可观测信息条件下的期望未来效用，仅在训练阶段用已观测的真实未来作为特权监督，推理阶段完全不引入未来信息
2. 保留原有相似性召回链路生成粗候选集，新增轻量残差MLP学习列表式未来兼容性目标做重排，架构改动成本极低
3. 设计Candidate-Prior、Shuffled-Future控制策略，可诊断三种相关性机制：候选全局、查询专属、混合模式
### 关键结果
在6个基准数据集上提升模式检索效果，12个验证任务全面优于Pattern检索和SARAF检索规则，消融实验证明性能增益核心来自未来监督而非MLP结构
