---
title: Towards Truly Unsupervised Evaluation of Feature Selection
title_zh: 面向特征选择的真正无监督评估框架
authors:
- Hafiz Saud Arshad
- Muhammad Rajabinasab
- Arthur Zimek
affiliations:
- University of Southern Denmark
arxiv_id: '2608.12057'
url: https://arxiv.org/abs/2608.12057
pdf_url: https://arxiv.org/pdf/2608.12057
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: 无监督特征选择 · 评估框架
tags:
- unsupervised evaluation
- feature selection
- PCA
- optimal transport
- dimensionality reduction
one_liner: 指出现有伪无监督特征选择评估方法缺陷，提出基于PCA与最优传输的纯无监督评估框架
practical_value: '- 可复用该框架对电商推荐/广告场景的特征选择方案做纯无监督评估，无需依赖标签数据，降低冷启动阶段特征筛选成本

  - 可借鉴PCA+最优运输的组合思路，量化特征子集与原特征空间的信息保留度，辅助用户/物品特征工程优化

  - 无标签冷启动场景下，可替代现有依赖下游任务的半监督特征评估方法，减少特征筛选对业务标签的依赖'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有号称无监督的特征选择评估方法普遍存在设计缺陷，本质依赖隐含标签或无监督下游任务的隐式监督，并非真正无监督，无法在完全无标签的业务冷启动等场景下可靠量化特征选择效果。

### 方法关键点
1. 系统性论证传统伪无监督特征选择评估方案的本质缺陷，明确其属于无监督下游任务约束下的监督评估范畴；
2. 提出纯无监督评估框架，先通过无监督PCA提取原全量特征空间的主成分结构，再基于最优运输度量特征选择后生成的子集与原特征空间的分布对齐度，全程无需任何标签信息输入。

### 关键结果
实验验证该框架评估结果与有监督特征选择质量指标的一致性显著优于传统伪无监督评估方法，可完全覆盖无标签场景的特征选择质量评估需求
