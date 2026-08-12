---
title: Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Time Series
  Forecasting
title_zh: 面向保均值概率时序预测的两阶段奇数残差流框架
authors:
- Kiran Madhusudhanan
- Christian Klötergens
- Lars Schmidt-Thieme
- Vijaya Krishna Yalavarthi
affiliations:
- University of Hildesheim
- Institute of Computer Science, University of Hildesheim
arxiv_id: '2608.11114'
url: https://arxiv.org/abs/2608.11114
pdf_url: https://arxiv.org/pdf/2608.11114
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 概率时序预测 · 不确定性量化
tags:
- Time-Series-Forecasting
- Probabilistic-Forecasting
- Normalizing-Flows
- Uncertainty-Quantification
- TORF
one_liner: 提出两阶段奇数残差流TORF框架，解耦时序预测的均值预测与不确定性估计，兼顾精度与分布灵活性
practical_value: '- 电商需求预测、库存规划场景可复用两阶段解耦思路：先训确定性模型拿到高精度均值预测，再单独建模残差分布做不确定性估计，避免联合优化损失拉低点预测精度

  - 残差分布建模可参考严格奇函数约束的受限Normalizing Flow设计，无需Monte Carlo采样即可保证均值不变，降低线上推理开销

  - 对需要风险敏感决策的场景（如大促备货、广告预算分配），可直接复用TORF框架同时获取高精度点预测与可靠不确定性区间，平衡决策收益与风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
概率时序预测是风险敏感决策（如电商需求规划、大促备货）的核心能力，现有方法存在分布灵活性与均值预测精度的固有权衡：传统参数方法（如MVE）联合优化NLL损失时会拉低点预测精度，而Normalizing Flows、扩散模型等生成式方法依赖高成本蒙特卡洛采样，均值估计效果不佳。

### 方法关键点
提出两阶段奇数残差流（TORF）框架，完全解耦均值预测与不确定性估计：第一阶段用预训练的确定性模型输出高精度均值预测；第二阶段采用仅含严格奇函数的受限Normalizing Flow学习点预测周围的灵活残差分布，无需采样即可保证第一阶段的均值完全保留。

### 关键结果
在长短时序预测任务上，TORF的确定性预测精度（NMAE）达到SOTA，同时密度估计性能（CRPS）表现优异。
