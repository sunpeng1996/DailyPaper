---
title: Autorelevance function and other feature relevance measures for univariate
  time series
title_zh: 单变量时间序列的自相关函数及其他特征相关性度量方法
authors:
- Julian Cardenas
- Jamie Arjona
- Pedro Delicado
affiliations:
- Universitat Politècnica de Catalunya - BarcelonaTech
arxiv_id: '2607.01959'
url: https://arxiv.org/abs/2607.01959
pdf_url: https://arxiv.org/pdf/2607.01959
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 时间序列可解释性 · 特征重要性度量
tags:
- xAI
- Time Series
- Shapley Value
- Feature Importance
- Forecasting
one_liner: 提出模型无关的单变量时间序列预测滞后相关性度量方法及缺失特征替换策略
practical_value: '- 电商销量、流量、库存等单变量时序预测场景，可复用该方法度量不同滞后阶数的特征重要性，精简输入特征降低推理成本

  - 基于Shapley的可解释性框架中遇到缺失特征时，可借鉴用同模型单步预测值替换的trick，提升解释结果可靠性

  - 推荐系统中用户行为时序类召回/排序特征的重要性评估可参考该模型无关框架，无需重新训练即可完成特征贡献量化'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
黑盒时序预测模型可解释性不足，难以量化各滞后阶输入的贡献，传统自相关方法无法适配复杂ML模型的特征重要性评估需求。
### 方法关键点
1. 融合Ghost变量、Shapley值与加性重要性度量框架，推出自相关、偏自相关函数作为滞后重要性度量指标，整体框架模型无关
2. 针对基于coalition的可解释方法中的特征缺失问题，采用同模型单步预测值替换缺失特征的优化策略
### 关键结果
在ARMA、RNN等多类时序预测模型的仿真和真实数据集上验证，所提相关性度量方法在几乎所有场景下可正确还原预期的滞后结构。
