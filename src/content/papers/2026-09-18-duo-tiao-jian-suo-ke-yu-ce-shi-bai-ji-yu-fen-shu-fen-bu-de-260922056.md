---
title: 'Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence
  Scoring and Abstention'
title_zh: 多跳检索可预测失败：基于分数分布的置信度打分与弃权机制
authors:
- Andre Bacellar
arxiv_id: '2609.22056'
url: https://arxiv.org/abs/2609.22056
pdf_url: https://arxiv.org/pdf/2609.22056
published: '2026-09-18'
collected: '2026-09-21'
category: RAG
direction: RAG多跳检索置信度与弃权优化
tags:
- Multi-Hop Retrieval
- Confidence Scoring
- Abstention
- RAG
- ANN Score
- CWAR
one_liner: 基于检索分数分布轻量特征构建无额外LLM调用的置信度评分，实现多跳检索校准弃权，降低高置信错误率
practical_value: '- 多跳RAG/Agent检索场景可复用本文的9个轻量ANN分数特征（hop1/hop2分数分布、query长度等）计算检索置信度，完全不需要额外LLM调用，延迟可忽略，适合高并发场景

  - 电商搜索/多轮导购的多步检索场景可引入本文的弃权机制，对置信度低于阈值的query触发人工兜底/更重的检索pipeline，减少高置信错误带来的用户体验损失

  - 不同检索场景的主导特征存在差异，无需盲目叠加特征，可通过留一法 ablation 快速筛选适配自身业务的核心特征（比如长query场景优先选query长度特征，密集检索场景优先选topN分数均值特征）

  - 跨数据集迁移效果优异，可先在通用多跳数据集上预训练置信度模型，再用少量业务数据微调即可落地，降低冷启动成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RAG多跳检索pipeline默认对所有query返回结果，高置信错误（Confident-Wrong-Answer）分布不均但没有显性信号，下游组件无法识别证据不全的检索结果，在对准确率要求高的场景（比如电商智能客服、事实问答）会带来严重体验问题，且现有置信度方案大多需要额外LLM调用，成本高延迟大。

### 方法关键点
- 理论证明：只有当检索特征与检索成功存在互信息时，才能降低高置信错误率（CWAR），且没有单一ANN特征能适配所有失败场景，需多特征聚合
- 提出REGIMEABSTAIN框架，仅用检索后天然存在的9个轻量特征（hop1的最大分数、top3均值、熵、lift，hop2的最大分数、margin、熵，query长度），通过逻辑回归训练Retrieval Confidence Score（RCS），无任何额外LLM调用，耗时<1ms
- 支持基于CWAR目标动态调整阈值，实现校准的弃权策略，也可对接query路由逻辑触发fallback pipeline

### 关键结果
在MuSiQue、2WikiMultiHopQA、HoVer三个多跳基准数据集，LLM-judge和dense-only两种检索架构的5个失败场景（基础CWAR 14.5%~62.1%）上测试，RCS在所有场景均取得最优或并列最优AUC-AC；在MuSiQue LLM-judge场景下，50%覆盖率时CWAR从39.5%降至20.6%，相对下降47.8%，ECE仅0.035校准效果优异；跨数据集迁移仅损失0.5pp AUC，泛化性强。

> 最值得记住的一句话：多跳检索的失败是结构可预测的，仅靠检索阶段天然存在的轻量分数特征，就可以在几乎无额外成本的前提下大幅降低高置信错误率。
