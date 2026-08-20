---
title: 'Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths'
title_zh: 聚合指标的盲区：基准评估如何忽略模型不可替代的独特优势
authors:
- Andrej Tschalzev
- Stefan Lüdtke
- Heiner Stuckenschmidt
- Christian Bartelt
affiliations:
- University of Mannheim
- University of Rostock
- Technical University of Clausthal
arxiv_id: '2608.18919'
url: https://arxiv.org/abs/2608.18919
pdf_url: https://arxiv.org/pdf/2608.18919
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: 机器学习基准评估 · 性能评价体系优化
tags:
- Benchmark
- Model Evaluation
- Tabular ML
- Performance Metric
- Aggregation
one_liner: 提出基于单数据集峰值性能前沿的评估框架，解决传统聚合指标掩盖模型独特优势的问题
practical_value: '- 做推荐/广告模型选型时，不能只看全域平均指标，需拆分不同细分场景（类目、用户群、流量层级）的峰值表现，挖掘单场景最优模型

  - 新模型迭代评估除观测平均指标提升外，需补充评估其是否能扩展特定细分场景的性能上限，避免错过有独特场景优势的模型

  - 离线基准测试体系可新增「场景不可替代性」维度打分，对模型做分级配置：通用模型做兜底，不可替代模型做细分场景定制'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统表格机器学习基准通过跨数据集平均分数、排名、pairwise胜率等聚合指标评估模型，仅适合筛选鲁棒通用模型，会掩盖特定模型在单数据集上的峰值性能优势，无法识别达成单场景最优的必要模型。
### 方法关键点
提出以数据为中心的峰值性能前沿评估框架，基于各数据集上统计显著的最优性能定义前沿线，按模型相对于前沿的位置将其划分为不可替代、足够、冗余、易错四类，补充传统聚合评估的盲区。
### 关键结果
在TabArena基准验证发现，现有聚合指标高度相关，核心衡量模型的一致性与防故障能力，和数据集层面的不可替代性相关性极低；表现平稳但从未在单数据集取得最优的模型在聚合指标上占优，有独特单数据集优势的模型反而被判定为平庸。
