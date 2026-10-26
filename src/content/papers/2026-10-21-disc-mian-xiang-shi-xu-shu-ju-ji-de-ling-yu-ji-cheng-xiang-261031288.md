---
title: 'DISC: Domain-Integrated Similarity Cost for Time-Series Dataset'
title_zh: DISC：面向时序数据集的领域集成相似性代价度量方法
authors:
- Yen-Ku Liu
- Hongjie Chen
- Franck Dernoncourt
- Ryan Rossi
affiliations:
- National Yang Ming Chiao Tung University
- Dolby Laboratories
- Adobe Research
arxiv_id: '2610.31288'
url: https://arxiv.org/abs/2610.31288
pdf_url: https://arxiv.org/pdf/2610.31288
published: '2026-10-21'
collected: '2026-10-26'
category: Training
direction: 时序迁移学习 · 相似性度量聚合
tags:
- time-series
- transfer-learning
- similarity-measure
- metric-learning
- domain-adaptation
one_liner: 可学习的时序数据集相似性度量聚合框架DISC，提升迁移场景下源目标域相似度与下游效用的对齐度
practical_value: '- 电商跨域推荐/广告迁移场景中，可复用DISC多度量加权聚合思路，替代人工选择单一相似度指标评估源/目标域适配性，减少预训练模型迁移试错成本

  - 时序类推荐任务（用户行为序列建模、销量预测跨域迁移）可复用「少量校准样本学习度量权重」方案，快速适配不同下游任务的相似度评估需求

  - 小样本跨域推荐场景，可基于DISC框架快速筛选最优源域预训练权重，降低全量微调的算力开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
时序大模型跨域迁移普及后，传统单一数据集相似度指标与下游任务效用对齐度差，无法在迁移前快速评估源目标域适配性，全量试错算力与时间成本极高。

### 方法关键点
DISC为可学习聚合框架，仅依赖少量校准迁移观测样本，自动选择、加权组合多类时序相似度指标，针对不同下游任务定制化适配相似度评估逻辑，精准捕捉对下游表现有影响的源-目标数据集差异。

### 关键结果
在分布外、迁移学习两类时序预测场景下，校准后的DISC仅需输入源目标对的多维度相似度值，即可实现比单一参考度量更高的下游效用对齐度，验证了时序相似度的任务依赖特性，学习式度量集成比人工选择单一度量的迁移表征能力更强。
