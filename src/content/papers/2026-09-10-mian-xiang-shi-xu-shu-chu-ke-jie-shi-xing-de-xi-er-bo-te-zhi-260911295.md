---
title: A Hilbert-Valued Functional Decomposition Framework for Explaining Time-Dependent
  Outputs
title_zh: 面向时序输出可解释性的希尔伯特值函数分解框架
authors:
- Sophie Hanna Langbein
- Niklas Koenen
- Marvin N. Wright
- Julia Herbinger
affiliations:
- Leibniz Institute for Prevention Research and Epidemiology – BIPS
- University of Bremen
arxiv_id: '2609.11295'
url: https://arxiv.org/abs/2609.11295
pdf_url: https://arxiv.org/pdf/2609.11295
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 时序模型可解释性 · 函数分解方法
tags:
- XAI
- Time Series
- Model Explanation
- Functional Decomposition
- Demand Forecasting
one_liner: 提出支持时序依赖感知与多粒度解释的时序输出模型可解释统一框架
practical_value: '- 电商需求/流量预测、广告投放转化时序类场景做模型可解释时，可复用其多时间粒度（时间点/时间窗/聚合时段）的解释逻辑，避免逐点解释忽略时序依赖的问题

  - 可借鉴核函数输出表示方法，对推荐系统用户长期行为序列、商品销量时序预测等连续输出场景做特征贡献归因

  - 现有逐点可解释方案可直接作为该框架的特例扩展，无需重构原有解释链路，改造成本低'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有特征归因类可解释方法主要针对标量输出设计，在需求预测、波动率预测等时序输出场景下，传统逐点独立解释的方案会忽略输出间的时序依赖，导致解释结果一致性差、参考价值低。
**方法关键点**：将函数分解推广到希尔伯特值预测函数空间，扩展通用特征可解释框架适配时序输出场景；引入基于核的输出表示，支持时间点级、时间解析级、时间聚合级三个维度的时序依赖感知解释，原有逐点解释方法可作为该框架的特例直接兼容。
**关键结果**：在合成数据集、日内金融市场波动率预测、能源需求预测三类场景完成验证，解释结果对时序依赖的刻画精度显著优于传统逐点独立解释方案。
