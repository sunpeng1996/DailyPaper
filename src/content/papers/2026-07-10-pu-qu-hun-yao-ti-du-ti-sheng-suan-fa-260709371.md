---
title: Spectrally Deconfounded Gradient Boosting
title_zh: 谱去混淆梯度提升算法
authors:
- Andrea Nava
- Peter Bühlmann
- Fabio Sigrist
arxiv_id: '2607.09371'
url: https://arxiv.org/abs/2607.09371
pdf_url: https://arxiv.org/pdf/2607.09371
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 梯度提升训练 · 隐混淆鲁棒性优化
tags:
- Gradient Boosting
- Spectral Deconfounding
- Causal Inference
- Regularization
- Tabular Prediction
one_liner: 提出适配梯度提升的谱去混淆框架，解决隐混淆导致的模型泛化性差问题
practical_value: '- 电商CTR/CVR、广告出价预估等tabular建模场景存在大量未观测隐混淆（如时令、用户隐性偏好），可将谱损失替换传统平方误差损失接入现有GBDT训练流程，提升分布偏移下的预估稳定性

  - 落地时可复用论文经验贝叶斯调参方案，结合早停正则实现去混淆效果，无需额外增加大量调参成本

  - 该方法扩展性优于现有非线性去混淆基线，可直接对LightGBM、XGBoost等开源框架做少量二次开发即可落地'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
梯度提升是tabular数据预测的SOTA方案，但高灵活性使其易拟合未观测隐混淆带来的伪关联，导致分布偏移场景下泛化性大幅下降；现有谱去混淆方法多针对线性模型，缺乏非线性场景下的高可用方案。

### 方法关键点
1. 设计适配梯度提升的谱去混淆框架，用谱损失替代普通平方误差损失，减慢模型在混淆对齐方向的学习速度；
2. 明确谱去混淆效果依赖谱收缩与正则（尤其是早停）的协同作用，单一谱损失无法实现去混淆；
3. 给出混合模型解释，基于经验贝叶斯自动调优谱损失，还通过拉普拉斯近似、核随机效应扩展到通用似然与非线性混淆场景。

### 关键结果
隐混淆场景下目标函数估计效果显著优于基线，扩展性比现有非线性谱去混淆方法大幅提升，可支撑大规模tabular数据训练。
