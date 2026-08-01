---
title: Scalable Graph Coreset Selection via Greedy Sampling
title_zh: 基于贪婪采样的可扩展图核心集选择方法
authors:
- Zhaiming Shen
- Alexander Cloninger
affiliations:
- Georgia Institute of Technology
- University of California, San Diego
arxiv_id: '2607.27602'
url: https://arxiv.org/abs/2607.27602
pdf_url: https://arxiv.org/pdf/2607.27602
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 大规模图采样 · 核心集选择
tags:
- Graph Sampling
- Coreset Selection
- Greedy Algorithm
- Scalable Graph
- Graph Signal Processing
one_liner: 提出无需全图拉普拉斯与特征分解的贪婪图采样算法，适配超大规模图节点采样场景
practical_value: '- 大规模用户行为图/商品关联图的核心节点采样可复用该方法，无需存储全图拉普拉斯矩阵，大幅降低内存开销

  - 图上用户/商品统计量（如平均偏好、类目热度）估算场景，可直接套用最小内积贪婪采样规则，替代全图遍历降低计算量

  - 分群均衡的图场景（如用户分层、商品类目聚类）下采样结果与群规模成正比，可直接用于分层抽样的下游统计任务'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有大图代表性节点采样方法需加载全图拉普拉斯矩阵、执行特征分解或全图遍历，超大规模图（如亿级用户/商品关联图）场景下内存与计算开销过高，无法落地。

### 方法关键点
提出基于最小内积的列选择贪婪采样规则，每轮迭代仅随机访问小部分拉普拉斯列，无需特征分解、全图遍历，也无需存储全量拉普拉斯矩阵，适配内存无法加载全图的超大规模场景。

### 关键结果
随机块模型理论分析显示，节点度分布均衡时采样比例与簇规模正相关，带限图信号均值估计误差随簇间连通性减弱而衰减；合成与真实数据集实验均验证了方法的采样有效性与扩展性。
