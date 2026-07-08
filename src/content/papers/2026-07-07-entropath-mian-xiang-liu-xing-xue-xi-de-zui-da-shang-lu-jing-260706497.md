---
title: 'EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning'
title_zh: EntroPath：面向流形学习的最大熵路径集成嵌入方法
authors:
- Przemysław Rola
affiliations:
- Department of Mathematics, Krakow University of Economics
arxiv_id: '2607.06497'
url: https://arxiv.org/abs/2607.06497
pdf_url: https://arxiv.org/pdf/2607.06497
published: '2026-07-07'
collected: '2026-07-08'
category: Other
direction: 流形学习 · 图嵌入距离度量优化
tags:
- Manifold Learning
- Graph Embedding
- Maximum Entropy Random Walk
- Dimensionality Reduction
- Geodesic Distance
one_liner: 提出基于最大熵随机游走的流形学习方法EntroPath，解决现有图嵌入偏置问题，性能优于主流基线
practical_value: '- 图表征场景可将现有随机游走逻辑替换为最大熵随机游走路径聚合，解决稠密区域偏置、短路边敏感问题，提升用户/物品异构图表征鲁棒性

  - 用户行为路径相似度计算可借鉴k步全量路径聚合思路，替代现有单路径/最短路径计算逻辑，更准确刻画用户行为内在关联

  - 高维特征降维场景可引入EntroPath替代t-SNE/UMAP，在非均匀采样的用户群体上获得更贴合真实分布的低维表征'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于图的流形嵌入方法存在两类核心缺陷：局部归一化随机游走易在稠密采样区域集中扩散，最短路径距离对图中虚假短路边高度敏感，均难以准确还原流形的测地几何结构。
### 方法关键点
1. 基于最大熵随机游走（MERW）构建异质性度量，聚合点对间所有k步路径而非依赖单条轨迹；2. 扩散深度k可平滑插值局部邻域结构与全局流形几何，对称化核支持精确Gram分解，可无缝对接核方法；3. 提供基于地标投影、扩散势伪时间的可扩展工程实现方案。
### 关键结果
在合成流形、单细胞基准测试集上，性能一致匹配或优于基于扩散、最短路径的同类方法，局部结构指标表现与UMAP、t-SNE等邻域保留嵌入相当；在非均匀采样密度、分支轨迹分离的流形上，测地几何保留效果提升最显著
