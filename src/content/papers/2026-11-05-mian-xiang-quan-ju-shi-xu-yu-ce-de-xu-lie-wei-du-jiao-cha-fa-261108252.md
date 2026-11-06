---
title: Series-wise Cross-validation for Global Time Series Forecasting
title_zh: 面向全局时序预测的序列维度交叉验证方法
authors:
- Vitor Cerqueira
- Mariana Oliveira
- Luis Roque
affiliations:
- University of Coimbra, CISUC/LASI, DEI
- Faculty of Engineering, University of Porto
arxiv_id: '2611.08252'
url: https://arxiv.org/abs/2611.08252
pdf_url: https://arxiv.org/pdf/2611.08252
published: '2026-11-05'
collected: '2026-11-06'
category: Eval
direction: 时序预测 · 交叉验证方案优化
tags:
- TimeSeriesForecasting
- CrossValidation
- ModelSelection
- GlobalForecasting
- DistributionShift
one_liner: 提出面向全局时序预测的序列维度交叉验证框架，明确其与时间维度CV的适用场景差异
practical_value: '- 做电商多SKU销量、多用户行为序列的全局时序预测时，用序列维度CV做模型选择，能提升新SKU/新用户场景下的泛化精度

  - 当业务需要准确估计现有序列的未来误差时，优先保留传统时间维度CV做效果评估，兼顾泛化性和误差估计准确性

  - 可将K-fold、bootstrapping等序列CV变体引入推荐系统时序召回/排序模型的离线评估流程，降低分布偏移带来的过拟合风险'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统时序预测交叉验证仅沿时间维度划分，不适用于在多序列上训练的全局深度学习预测模型，无法模拟训练时未见过的新序列场景（如电商新SKU、新用户预测），容易导致模型选择偏差。

### 方法关键点
提出序列维度交叉验证框架，同时沿序列和时间两个维度划分数据，支持K-fold CV、bootstrapping、Monte Carlo CV等多种实现；设计随机隐藏部分序列仅用于测试的评估协议，模拟新序列分布偏移场景，从性能估计、过乐观率、模型选择准确率等5个维度对比不同CV方案。

### 关键结果
在11个数据集、10种神经网络架构上测试，序列维度CV引导选出的模型下游预测精度更优，同时能跨时间和序列泛化；传统时间维度CV在样本外误差估计精度上仅存微弱优势。
