---
title: 'e-means: outperforming k-means (in one-tenth the epochs)'
title_zh: e-means：仅用十分之一epoch性能超越k-means的聚类算法
authors:
- Swann Bessa
- Pierre-Emmanuel Mazaré
- Gergely Szilvasy
- Hugo Touvron
- David Picard
- Matthijs Douze
- Hervé Jégou
affiliations:
- FAIR at Meta
- École Nationale des Ponts et Chaussées
arxiv_id: '2611.09501'
url: https://arxiv.org/abs/2611.09501
pdf_url: https://arxiv.org/pdf/2611.09501
published: '2026-11-05'
collected: '2026-11-11'
category: RecSys
direction: 大规模嵌入聚类 · 向量检索量化加速
tags:
- Clustering
- K-Means
- EMA
- Vector Quantization
- Large-scale Retrieval
one_liner: 基于EMA小批量更新的e-means聚类算法，仅用k-means 1/10 epoch，精度更高GPU速度快10~45倍
practical_value: '- 做大规模用户/物品embedding聚类、Semantic ID生成时，可直接替换现有k-means方案，降低10倍以上的聚类算力开销，缩短离线迭代周期

  - 无需调参的超参数公式可直接复用，适配不同规模的嵌入数据集，省去调参成本，适合工业界离线流水线的自动化部署

  - 小批量EMA更新的聚类逻辑可迁移到实时流embedding的动态聚类场景，支撑实时用户分群、实时召回池更新需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统k-means是聚类、向量量化、检索的通用标准方案，但大规模嵌入场景下收敛慢、迭代轮数多、调参成本高，无法适配百亿级嵌入的聚类需求。
### 方法关键点
1. 基于指数移动平均(EMA)实现小批量更新的k-means优化，复用深度学习训练框架的工程能力；
2. 推导得到衰减率、batch size与性能的缩放定律，给出固定超参数的公式化规则，无需超参数搜索。
### 关键结果数字
在多类嵌入数据集上，仅用1.4~2.6 epoch即可超过Lloyd k-means 25 epoch的效果，GPU端到端速度比SOTA k-means实现快10~45倍；对100亿规模的DINO embedding做1600万类聚类，仅需2.5 epoch即可达到比k-means 25 epoch更低的损失
