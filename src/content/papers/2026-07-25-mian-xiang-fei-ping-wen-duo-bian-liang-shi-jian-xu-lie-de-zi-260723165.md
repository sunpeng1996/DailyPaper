---
title: Adaptive Multi-Scale Forecasting and Gate-Localized Conformal Prediction for
  Multivariate Nonstationary Time Series
title_zh: 面向非平稳多变量时间序列的自适应多尺度预测与保形校准框架
authors:
- Ziling Ma
- Junshu Jiang
- Ángel López-Oriona
- Ying Sun
- Hernando Ombao
affiliations:
- King Abdullah University of Science and Technology (KAUST), Statistics Department
- King Abdullah University of Science and Technology (KAUST), NeuroAI Laboratory
arxiv_id: '2607.23165'
url: https://arxiv.org/abs/2607.23165
pdf_url: https://arxiv.org/pdf/2607.23165
published: '2026-07-25'
collected: '2026-07-29'
category: Other
direction: 非平稳时序预测 · 不确定性量化
tags:
- Time Series Forecasting
- Conformal Prediction
- Uncertainty Quantification
- Nonstationary Time Series
- Multi-scale Forecasting
one_liner: 模型无关的ABF-T-GLCP框架，同步提升非平稳多变量时序预测精度与不确定性量化效果
practical_value: '- 电商销量、大促流量、广告投放效果预估等非平稳时序预测场景，可复用horizon专属时序专家+门控融合的多尺度预测结构，提升不同预测周期的精度

  - 保形预测落地时，可借鉴GLCP的门控状态+时间近邻筛选局部校准残差的思路，在保证覆盖率的前提下大幅缩窄预测区间，降低不确定性预估冗余

  - 点预测和不确定性量化模块共享状态表示的架构，可直接迁移到库存预警、ROI预估等需要同时输出预测值和风险区间的业务场景'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
非平稳多变量时序（如金融商品价格、电商销量、大促流量）受外部环境波动影响大，传统方法预测精度不足，且不确定性量化输出的预测区间过宽、覆盖率不达标，难以支撑风险决策。
### 方法关键点
1. 模型无关的ABF-T-GLCP框架，预测模块通过学习门控融合不同预测周期的专属时序专家，结合跨序列稀疏迁移优化点预测结果；
2. 不确定性模块GLCP复用门控状态+时间近邻性筛选局部校准残差，将保形预测校准过程与预测模型的时序模式对齐；
3. 点预测与不确定性量化共享状态表示，适配动态变化的时序分布。
### 关键结果
在大规模高频大宗商品预测基准上，点预测精度稳定提升，预测区间大幅缩窄，实际覆盖率接近标称值，可扩展到金融外的通用非平稳时序场景。
