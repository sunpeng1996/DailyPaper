---
title: 'Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential
  Uncertainty Quantification for Nonlinear Dynamics'
title_zh: 神经条件高斯模型：面向非线性动力学的带不确定性量化高效数据同化
authors:
- Chuanqi Chen
- Nan Chen
affiliations:
- University of Chicago
- University of Wisconsin–Madison
arxiv_id: '2611.26463'
url: https://arxiv.org/abs/2611.26463
pdf_url: https://arxiv.org/pdf/2611.26463
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 非线性动力学建模 · 不确定性量化
tags:
- Uncertainty Quantification
- Data Assimilation
- Dynamical System
- Latent Space
- Neural Model
one_liner: 提出数据驱动的神经条件高斯模型，降低非线性系统数据同化在线成本同时保证精度
practical_value: '- 建模用户兴趣演化这类非线性动态序列时，可借鉴隐空间条件高斯结构做隐状态闭式更新，降低在线推理开销

  - 做推荐结果不确定性量化时，可参考将隐层后验统计量直接接入训练损失的思路，避免单独后处理引入的误差

  - 无显式规则的动态预测场景（如大促流量预估、用户序列行为预测），可复用编解码器结合隐空间高斯动力学的轻量架构'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
部分观测非线性系统的数据同化需同步估计隐状态及对应不确定性，传统非线性滤波方法计算开销极高，且强依赖人工定义的显式动力学模型，难以适配无明确控制方程的复杂动态场景。
### 方法关键点
1. 提出Neural CGM数据驱动动力学模型，通过编码器将物理状态映射至隐空间，隐态动力学遵循条件高斯结构，支持隐空间闭式数据同化更新，同时保留非线性编解码器对复杂物理空间动态的拟合能力；
2. 设计高斯解码器融合局部矩传播与可学习非线性校正，将隐空间后验均值、协方差映射回物理空间，后验统计量直接接入训练阶段的高斯负对数似然损失，实现预测结果与不确定性的端到端联合优化；
3. 无需已知显式控制方程即可完成状态预测与仿真。
### 关键结果
在非线性动力学基准测试中，状态估计与预测精度与传统方法持平，在线同化成本较传统非线性数据同化方法大幅降低。
