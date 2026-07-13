---
title: Graph-Regularized Low-Rank Matrix Completion by Variable Projection
title_zh: 基于变量投影的图正则化低秩矩阵补全方法
authors:
- Benoît Loucheur
- P. -A. Absil
- Michel Journée
affiliations:
- ICTEAM Institute, UCLouvain
- Royal Meteorological Institute of Belgium
arxiv_id: '2607.09546'
url: https://arxiv.org/abs/2607.09546
pdf_url: https://arxiv.org/pdf/2607.09546
published: '2026-07-10'
collected: '2026-07-13'
category: RecSys
direction: 推荐系统 · 稀疏矩阵补全优化
tags:
- Low-Rank Matrix Completion
- Graph Regularization
- Riemannian Optimization
- Sparse Data Imputation
one_liner: 在黎曼信赖域矩阵补全框架中引入行列关联图正则，提升稀疏强关联场景下的矩阵补全效果
practical_value: '- 处理用户-商品交互/评分矩阵的稀疏补全场景时，可引入用户社交关联、商品类目关联作为图正则约束，提升低秩补全准确率

  - 冷启动等极端稀疏场景下，可借鉴基于Grassmann manifold的无约束优化思路，降低大规模矩阵补全的计算开销

  - 针对行列存在强关联的场景（如同画像用户、同品类商品），可直接复用GR-RTRMC框架做缺失值补全，鲁棒性优于原生RTRMC'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统低秩矩阵补全方法在数据稀疏、行列存在强关联的场景（如电商推荐、气象预测）下准确率和鲁棒性不足；现有RTRMC框架仅利用低秩约束，未显式建模行列间固有依赖，无法充分利用关联信息提升补全效果。
### 方法关键点
1. 提出GR-RTRMC框架，在原RTRMC基于Grassmann manifold的无约束优化基础上，加入行列关联的图正则项；
2. 采用变量投影法融合低秩约束与图正则约束，既保留黎曼优化的高效性，又显式引入行列间先验关联信息。
### 关键结果
在行列强关联的稀疏测试集上，相比原生RTRMC，补全MAE平均降低11%；稀疏度高于90%的极端场景下，补全准确率提升18%以上，鲁棒性显著优于无正则的低秩补全方法。
