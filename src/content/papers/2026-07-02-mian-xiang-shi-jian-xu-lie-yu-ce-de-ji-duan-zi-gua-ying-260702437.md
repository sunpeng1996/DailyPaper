---
title: Extreme Adaptive Transformer for Time Series Forecasting
title_zh: 面向时间序列预测的极端自适应Transformer
authors:
- Sanjeev Shrestha
- Hui Liu
- Yifan Zhang
affiliations:
- Department of Computer Science, Missouri State University
arxiv_id: '2607.02437'
url: https://arxiv.org/abs/2607.02437
pdf_url: https://arxiv.org/pdf/2607.02437
published: '2026-07-02'
collected: '2026-07-03'
category: Other
direction: 不平衡时序预测 · 极端感知注意力
tags:
- Transformer
- Time Series Forecasting
- Sparse Attention
- Imbalanced Data
- Extreme Event Modeling
one_liner: 提出含三类稀疏注意力的Exformer框架，提升含稀有极端事件的不平衡时序预测性能
practical_value: '- 电商大促、突发舆情等稀有极端场景的流量、销量、客诉时序预测，可参考三分支稀疏注意力设计，单独建模极端与普通事件的关联

  - 处理不平衡时序数据时，可通过独立的极端事件注意力分支针对性提升稀有高价值样本的预测精度，同时避免全量加权带来的计算开销

  - 推荐系统用户行为时序建模中，可复用该思路单独建模大促下单、大额消费等稀有但高价值的行为特征，提升高ARPU用户的推荐效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Transformer时序预测模型对所有时间点均匀建模，无法有效捕获包含稀有但影响重大的极端事件的不平衡时序特征，在水文、金融、电商等对极端事件敏感的场景下预测精度不足。
### 方法关键点
提出Extreme-Adaptive Transformer（Exformer）预测框架，核心为三类稀疏注意力组成的极端自适应注意力机制：Local分支捕获短期时序依赖，Stride分支捕获周期性时序依赖，Extreme分支选择性建模普通事件与极端事件之间的关联依赖。
### 关键结果
在4个真实世界水文径流数据集上，3天预测效果优于所有SOTA基线，验证了极端感知注意力对含稀有高影响事件的不平衡时序预测的显著提升作用。
