---
title: 'Modular Bayesian Foundation Models: Bayesian time series encoders for OOD
  detection, routing and forecasting'
title_zh: 模块化贝叶斯基础模型：面向OOD检测、路由与预测的时序编码器
authors:
- Mame Diarra Toure
- Quang Hung Pham
- Mohamed Ryad Zemouri
- David Stephens
- Luc Vouligny
- Martin Gagnon
affiliations:
- McGill University
- Hydro-Quebec
arxiv_id: '2610.39043'
url: https://arxiv.org/abs/2610.39043
pdf_url: https://arxiv.org/pdf/2610.39043
published: '2026-10-28'
collected: '2026-10-31'
category: Training
direction: 模块化时序基础模型 · 贝叶斯训练与路由
tags:
- Bayesian Neural Network
- Time Series
- Modular Foundation Model
- OOD Detection
- Uncertainty Routing
one_liner: 提出融合SBNN与不确定性路由的模块化时序基础模型，低参数量下实现更优预测可靠性
practical_value: '- 可将不确定性路由机制迁移到MoE架构的推荐/广告排序模型中，无需标签即可实现分布漂移下的最优专家选择，提升跨场景适配性

  - SBNN轻量贝叶斯编码器可复用到时序用户行为建模任务，相比深度集成、MC Dropout最高降92.8%参数量，大幅降低存储推理成本

  - 基于认知不确定性的无标签OOD检测方案，可直接用于电商推荐的异常流量、异常用户识别，无需额外标注投入'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
工业时序数据采样频率、量级、动态模式差异大，单一基础模型无法适配所有分布，全量重训应对模式漂移的算力成本极高，现有模块化专家架构缺乏轻量专家设计与无标签路由机制。
### 方法关键点
1. 采用奇异贝叶斯神经网络（SBNN）训练轻量贝叶斯时序编码器集群，基于认知不确定性实现无标签的专家路由选择
2. 端到端框架支持新增专家扩展能力，无需重训全量模型即可适配新数据分布
### 关键结果
- 编码器集群存储比确定性版本低63.8%；对比MC Dropout、深度集成、全秩贝叶斯模型，参数量分别降63.9%、92.8%、81.9%，MSE与最优基线持平
- 不确定性路由对比距离路由，7个数据集上预测MSE相当，平均ECE从0.086降至0.072，NLL从0.907降至0.836，PICP90从82.28%提升至89.03%
