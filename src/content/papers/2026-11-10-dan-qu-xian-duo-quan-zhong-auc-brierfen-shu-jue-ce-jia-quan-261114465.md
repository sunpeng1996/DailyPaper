---
title: 'One Curve, Different Weights: AUC, the Brier Score, Decision-Weighted AUC,
  and the Policy Youden Index'
title_zh: 单曲线多权重：AUC、Brier分数、决策加权AUC与策略约登指数
authors:
- Yegor Baranovski
arxiv_id: '2611.14465'
url: https://arxiv.org/abs/2611.14465
pdf_url: https://arxiv.org/pdf/2611.14465
published: '2026-11-10'
collected: '2026-11-12'
category: Eval
direction: 二分类模型评估 · 决策适配度量
tags:
- Model Evaluation
- AUC
- Brier Score
- Binary Classification
- Decision Metric
one_liner: 统一AUC、Brier分数等二分类度量底层逻辑，提出适配决策场景的决策加权AUC与策略约登指数
practical_value: '- 电商风控、广告点击率预估等二分类任务，可根据业务决策规则（如投放阈值、拦截阈值）构造AUC_π，替代传统AUC做更贴合业务的模型排序，解决传统AUC与业务效果不一致的问题

  - 策略约登指数可直接作为固定决策流下的模型效果度量，避免传统AUC不同模型对阈值权重不一致导致的排序偏差

  - 做离线在线效果对齐时，可基于Youden曲线的加权逻辑，把离线指标和线上实际决策的收益直接挂钩，缩小离在线差异'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统二分类风险评分的标准评估指标AUC与Brier分数常出现模型排序结果不一致的问题，且指标与实际业务决策场景适配性弱，离线评估难对齐线上收益。
### 方法关键点
1. AUC、Brier分数、决策加权AUC_π本质都是Youden曲线J(t)=TPR(t)-FPR(t)在不同阈值权重下的加权平均，权重分别对应全量得分分布、真实条件概率$	{E}[Y|S]$、决策者的行动概率
2. 采用$|\pi(s)-\pi(s')|$对样本对加权是唯一可让成对加权AUC对任意得分分布都等价于Youden曲线平均的预定义权重
3. 策略约登指数为AUC_π的分子，用固定决策政策评估所有模型
### 关键结果
归一化后的AUC_π等价于将权重偏移到决策者关注阈值的理想预测Brier技能分数；策略约登指数可统一不同模型的评估基准，避免传统AUC的排序偏差问题
