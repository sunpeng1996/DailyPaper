---
title: 'Valid Per-Field Selective Risk Control for Document Extraction: Three Failure
  Modes, a Validity Ladder, and When Conditioning Pays'
title_zh: 文档抽取逐字段选择性风险控制：失效模式、有效性阶梯与条件适用场景
authors:
- Bhaskar Gurram
affiliations:
- Zasti AI
arxiv_id: '2608.14639'
url: https://arxiv.org/abs/2608.14639
pdf_url: https://arxiv.org/pdf/2608.14639
published: '2026-07-27'
collected: '2026-08-19'
category: Other
direction: 文档信息抽取 · 风险控制
tags:
- Document Extraction
- Selective Risk Control
- Calibration
- PAC Certification
- Selective Prediction
one_liner: 诊断文档抽取风控3种失效模式，提出分层有效性阶梯与适配的风险控制方案
practical_value: '- 电商/广告场景的结构化信息抽取（商品属性、发票、订单信息抽取）可直接复用这套逐字段风险阈值校准方法，控制上线错误率

  - 做模型置信度校准时需严格拆分fit/val集，避免score-refit泄漏，尤其小样本标注场景下可防止高估覆盖度、低估实际风险

  - 大模型结构化抽取落地可参考有效性阶梯分层选方案：追求平均吞吐量用fit/val拆分方案，需合规强保障用PAC认证的分组控制方案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文档抽取系统的逐字段置信度阈值风控方案，在真实数据上会静默违反预设的错误率上限（alpha）要求，缺乏可信的风险保障，难以落地到对准确率要求严格的业务场景。

### 方法关键点
1. 诊断出3类核心失效模式：文档聚类导致有效校准样本减半（设计效应1.84-2.45）、score-refit泄漏、tie-mass分数退化导致阈值网格失效；
2. 提出分层有效性阶梯，从低到高分别为fit/val拆分的预期风险控制、Mondrian Learn-then-Test的分组PAC认证，适配不同严格度的业务要求；
3. 明确条件阈值与全局pooled阈值的适用边界：低准确率场景下条件阈值更优，高准确率场景下全局阈值表现更好。

### 关键结果
alpha=0.10时，fit/val拆分方案实现覆盖度0.318、实际风险0.096，仅47.5%的重拆分超过alpha；分组PAC认证的doc-iid方案风险低至0.020，覆盖度0.060；人工审计确认落地版本实际风险1.3%远低于10%的预算。
