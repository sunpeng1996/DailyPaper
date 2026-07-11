---
title: 'Dimensionality Reduction Meets Network Science: Sensemaking on UMAP''s kNN
  Graph'
title_zh: 降维与网络科学结合：UMAP内部kNN图的分析价值挖掘
authors:
- Duen Horng Chau
- Donghao Ren
- Fred Hohman
- Dominik Moritz
affiliations:
- Apple
arxiv_id: '2607.08746'
url: https://arxiv.org/abs/2607.08746
pdf_url: https://arxiv.org/pdf/2607.08746
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 高维数据处理 · UMAP kNN图分析
tags:
- UMAP
- kNN Graph
- PageRank
- k-core
- Dimensionality Reduction
one_liner: 挖掘UMAP内部未受重视的kNN图，用经典图算法实现优于/互补专用方法的高维数据分析效果
practical_value: '- 推荐场景用户/物品高维Embedding聚类、核心样本筛选时，可直接复用UMAP内置kNN图，无需额外构建kNN索引降低计算成本

  - 冷启动Item选品、典型用户画像挖掘时，用UMAP kNN图+PageRank选代表性样本，效果与k-medoids相当，实现更简洁

  - 高维Embedding分群时，可组合k-core分解+聚类系数方法，区分核心/边缘样本簇，补全HDBSCAN等聚类方法的结果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
UMAP是当前高维数据可视化与探索的主流工具，但现有应用流程仅使用其输出的低维嵌入结果，完全忽略了生成低维投影前构建的、无投影失真的内部kNN图的信息价值，高维表征挖掘的效率和精度存在优化空间。
### 方法关键点
直接对UMAP内置的高维空间kNN图应用三类成熟经典图算法：1）PageRank筛选代表性数据点；2）k-core分解区分高密度核心区域与稀疏边缘区域；3）聚类系数识别高相似紧密度邻域。
### 关键结果
在MNIST、Fashion MNIST数据集上验证，三类图算法效果与专用方法相当甚至互补：PageRank选代表性样本效果对标k-medoids，k-core+聚类系数的聚类结果可有效补充HDBSCAN等密度聚类方法的输出。
