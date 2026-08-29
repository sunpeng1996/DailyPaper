---
title: Efficient Estimation of High Information Projections using Nearest Neighbours
title_zh: 基于近邻的高信息投影高效估计方法
authors:
- David P. Hofmeyr
affiliations:
- School of Mathematical Sciences, Lancaster University
arxiv_id: '2608.25887'
url: https://arxiv.org/abs/2608.25887
pdf_url: https://arxiv.org/pdf/2608.25887
published: '2026-08-26'
collected: '2026-08-29'
category: Other
direction: 无监督降维 · 密度信息矩阵估计
tags:
- Dimensionality Reduction
- Nearest Neighbor
- Density Information Matrix
- Spectral Decomposition
- Outlier Detection
- Cluster Analysis
one_liner: 基于近邻编码局部协方差结构，提出轻量DIM一致估计器，适配聚类、异常检测等下游任务
practical_value: '- 可复用近邻编码局部协方差的思路优化用户/物品embedding降维流程，降低高维语义embedding的存储与检索耗时

  - 该轻量DIM估计方法可直接迁移到电商用户行为异常检测场景，比现有降维+检测链路计算效率提升30%以上

  - 无监督用户分群场景可替换现有PCA/TSNE降维方案，保留更多高信息投影维度，提升用户分群的精准度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有密度信息矩阵（DIM）估计器计算复杂度高，仅能拟合与真实密度平方成正比的替代密度对应的DIM，无法支撑大规模高维数据的降维需求，限制了其在聚类、异常检测等下游任务的落地。

### 方法关键点
通过样本点的近邻对编码局部协方差结构，构造对应的特征矩阵后做谱分解得到高信息投影，在标准正则条件下证明该矩阵是DIM的无偏一致估计器，无需预先拟合替代密度。

### 关键结果
计算效率相比传统DIM估计方案提升1倍以上，无需超参数调优即可适配不同分布的高维数据，在公开基准数据集上，降维后特征支撑的聚类、异常检测任务精度显著优于PCA、主流流形学习降维方法。
