---
title: 'Small Is Not Dead: Distance-Aware Cluster Revival for e-means'
title_zh: 面向e-means的距离感知死簇复活优化算法
authors:
- Eyal Weiss
affiliations:
- Robotics Institute, Carnegie Mellon University
arxiv_id: '2611.18238'
url: https://arxiv.org/abs/2611.18238
pdf_url: https://arxiv.org/pdf/2611.18238
published: '2026-11-13'
collected: '2026-11-16'
category: RecSys
direction: 向量检索 · 嵌入聚类优化
tags:
- e-means
- FAISS
- Clustering
- Embedding Retrieval
- Mini-batch K-means
one_liner: 为FAISS库中的e-means聚类新增距离判别条件，保留稀有小簇，无额外耗时且聚类误差显著降低
practical_value: '- 可直接替换FAISS中原生e-means的死簇复活逻辑，针对有大量长尾小众用户/商品嵌入的场景，聚类误差最高可降80%，无额外计算耗时

  - 聚类去冗余时不要仅依赖簇大小判定，新增簇中心距离与全局MSE比值的判别条件，可有效保留长尾小众样本对应的簇，避免召回漏覆盖

  - 微批量聚类的迭代优化逻辑可复用在推荐系统实时用户/商品embedding聚类更新模块，平衡更新速度与聚类精度'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
FAISS 内置的 e-means 微批量k-means算法速度比Lloyd算法快一个数量级，但其死簇复活机制仅依据簇大小判定，会误删覆盖稀有孤立样本的小簇，导致聚类误差升高。

### 方法关键点
新增距离判别条件，仅当小簇中心与其他簇中心的平方距离小于全局MSE的动态估计值时才判定为死簇；每5个微批次仅对小簇做1次最近中心搜索，无额外可测量耗时。

### 关键结果数字
在e-means原有基准数据集上效果与FAISS原生版本完全一致；含稀有孤立组的数据集上，2个epoch后测试误差相对原计数式复活机制降低10%~80%，同时保留k-means++初始化的优势；其余数据集误差与最优版本差值小于1%。
