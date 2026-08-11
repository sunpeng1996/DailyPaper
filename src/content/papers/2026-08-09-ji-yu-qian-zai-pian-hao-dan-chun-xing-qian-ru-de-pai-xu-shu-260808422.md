---
title: Population-Level Generative Modeling for Ranking Data
title_zh: 基于潜在偏好单纯形嵌入的排序数据群体级生成框架
authors:
- Zhaoyang Shi
affiliations:
- Fudan University
arxiv_id: '2608.08422'
url: https://arxiv.org/abs/2608.08422
pdf_url: https://arxiv.org/pdf/2608.08422
published: '2026-08-09'
collected: '2026-08-11'
category: RecSys
direction: 排序数据生成 · 偏好异质性建模
tags:
- Generative Modeling
- Ranking Data
- Plackett-Luce Model
- Flow Matching
- Preference Embedding
one_liner: 提出结合潜在偏好单纯形嵌入与流匹配的排序数据生成框架，兼顾高保真度与偏好异质性可解释性
practical_value: '- 电商隐私合规场景：可基于该框架生成合成用户排序行为数据，规避原始用户数据泄露风险，用于模型训练、A/B测试仿真

  - 推荐算法benchmark构建：自定义生成不同偏好异质性的排序数据集，验证新召回/排序模型在不同用户群体分布下的鲁棒性

  - 用户偏好建模优化：借鉴潜在偏好单纯形嵌入方法，将用户对商品的效用向量拆解为K类偏好类型的加权组合，替代黑盒用户embedding聚类，实现可解释用户分群

  - 大促流量仿真：基于历史排序数据生成虚拟用户的排序偏好，模拟流量峰谷下推荐系统的性能表现，提前完成容量规划'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有排序数据研究多聚焦偏好估计、排序预测等推理任务，缺乏群体级生成能力；合成真实排序数据对隐私合规的数据共享、排序算法benchmark构建、推荐系统仿真、不确定性量化等场景至关重要，但排序是高维组合对象，非欧依赖结构复杂，且用户群体偏好异质性强，直接建模难度极大。

### 方法关键点
- 基于Plackett-Luce排序模型，将用户效用向量拆解为K个潜在偏好类型的加权组合，映射到低维潜在偏好单纯形空间，大幅降低建模维度
- 采用约束极大似然估计+顶点恢复算法，从观测排序数据中估计潜在偏好类型的效用矩阵与用户的偏好权重分布
- 引入流匹配算法学习单纯形空间上的用户偏好权重分布，生成新的偏好权重后通过Plackett-Luce模型解码为合成排序数据

### 关键结果
在合成数据集、Sushi偏好数据集、APA选举数据集上对比GPVAE、GMVAE两个基线：Sushi数据集上∆Pair（pairwise偏好误差）比次优的GMVAE低34%，APA数据集上∆Pair比次优的GPVAE低18.7%，且生成的偏好类型具备明确语义可解释性。

最值得记住的一句话：排序数据生成无需直接在高维组合空间建模，通过低维可解释的偏好嵌入降维可同时兼顾生成精度与业务可解释性
