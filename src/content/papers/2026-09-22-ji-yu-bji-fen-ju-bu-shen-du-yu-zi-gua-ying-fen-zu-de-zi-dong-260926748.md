---
title: Automatic depth-based local center clustering via $β$-integrated local depth
  and adaptive grouping
title_zh: 基于β积分局部深度与自适应分组的自动深度型局部中心聚类
authors:
- Siyi Wang
- Alexandre Leblanc
- Paul D. McNicholas
arxiv_id: '2609.26748'
url: https://arxiv.org/abs/2609.26748
pdf_url: https://arxiv.org/pdf/2609.26748
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 无监督聚类 · 无参数自动聚类
tags:
- Clustering
- Unsupervised Learning
- Parameter-free
- Depth-based Clustering
- Adaptive Grouping
one_liner: 提出无参数全自动聚类算法A-DLCC，自动确定聚类数输出可解释结果
practical_value: '- 电商用户分群、物品聚类场景可复用A-DLCC无参数设计思路，避免人工调聚类数、邻域大小的繁琐工作，提升聚类迭代效率

  - 做用户/物品语义表征聚类时，可借鉴β积分局部深度筛选稳定簇中心的思路，提升簇的可解释性

  - 层级聚类合并逻辑可借鉴图论瓶颈路径+自适应合并判据的设计，减少不合理簇合并'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有聚类算法大多需要人工指定聚类数、邻域大小等参数，依赖先验知识且调参成本高，不适配无先验的大规模异构数据聚类场景。

### 方法关键点
1. 提出β积分局部深度指标，筛选跨多个局部层级均稳定的点作为局部中心，按代表性排序；
2. 设计非参数组级局部相似度度量，每个局部中心初始对应一个独立簇；
3. 引入图论瓶颈路径思想构建自适应合并规则，仅当接触强度高于配置模型零假设时执行合并，自动判断聚类终止条件，无需提前指定聚类数。

### 关键结果
在合成与真实数据集上验证，无需任何参数调优即可输出可解释的聚类结果，效果匹配需人工调参的主流聚类算法。
