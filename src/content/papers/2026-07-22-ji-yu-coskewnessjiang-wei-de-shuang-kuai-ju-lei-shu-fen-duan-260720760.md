---
title: 'Twoblock clustering trees with coskewness-based dimension reduction: recovering
  piecewise multivariate linear regimes'
title_zh: 基于coskewness降维的双块聚类树：分段多元线性模式恢复
authors:
- Sven Serneels
affiliations:
- Snow Stallion AI, USA
- University of Antwerp, Belgium
arxiv_id: '2607.20760'
url: https://arxiv.org/abs/2607.20760
pdf_url: https://arxiv.org/pdf/2607.20760
published: '2026-07-22'
collected: '2026-07-25'
category: Other
direction: 可解释机器学习 · 回归树建模
tags:
- interpretable ML
- regression tree
- dimension reduction
- coskewness
- clustering
one_liner: 基于coskewness降维的高可解释多响应回归树tbtree，性能比肩随机森林且全链路可解释
practical_value: '- 电商用户分群+转化预估场景，可借鉴双块降维+叶节点局部线性模型的架构，替代传统GBDT单值输出，在性能损失极小的情况下支持分群归因分析

  - 交易/点击等偏斜分布的用户行为数据聚类，可复用coskewness最大化的降维方法，比普通PCA更能捕捉非正态特征模式，提升分群精准度

  - 金融/教育类合规要求高的电商推荐场景，可用tbtree替代黑盒集成模型，性能相当的同时满足监管对模型可解释性的要求'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
工业场景中多数预测任务的响应面呈分段线性特征，单一全局线性模型拟合精度不足，随机森林等黑盒模型可解释性差，无法适配需要可归因、可校验的业务需求。

### 方法关键点
- 双块聚类树（tbtree）为确定性决策树，叶节点采用局部多元线性模型，分裂规则计算与叶节点建模均引入稠密/稀疏双块降维计算不纯度，兼顾计算效率与可解释性
- 基于coskewness最大化设计双块降维空间估计器，可有效识别数据中的非正态聚类，适配偏斜分布的业务数据

### 关键结果
仿真实验可精准恢复分段线性模式；真实数据集上性能与随机森林等黑盒模型持平，且分裂规则、叶节点模型全链路可人工校验解释。
