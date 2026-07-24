---
title: Adaptive deep nonparametric regression from dependent data under covariate
  shift
title_zh: 协变量偏移下依赖数据的自适应深度非参数回归方法
authors:
- William Kengne
- Ehud Mossa Ockegna
affiliations:
- Université Jean Monnet
- ICJ UMR5208
- CNRS
- Ecole Centrale de Lyon
- INSA Lyon
arxiv_id: '2607.20309'
url: https://arxiv.org/abs/2607.20309
pdf_url: https://arxiv.org/pdf/2607.20309
published: '2026-07-22'
collected: '2026-07-24'
category: Training
direction: 协变量偏移优化 · 非参数回归
tags:
- Covariate Shift
- Deep Neural Network
- Nonparametric Regression
- Sparse Regularization
- Convergence Rate
one_liner: 提出稀疏惩罚DNN估计器，解决协变量偏移下依赖数据的非参数回归问题，达近最小最大最优收敛率
practical_value: '- 推荐/广告场景存在训练测试分布偏移时，可复用「密度比估计+重加权训练」的两阶段预训练流程，缓解covariate shift带来的效果掉点

  - 稀疏惩罚DNN的设计思路可迁移到排序/召回模型的特征选择环节，降低模型对源域分布的过拟合风险

  - 针对时序依赖的用户行为数据建模，其泛化误差界结论可用于指导模型正则系数、训练轮次等超参数调优'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现实场景中训练（源）与测试（目标）数据常存在covariate shift，标准训练范式下模型泛化表现差，现有DNN回归估计的理论保障大多假设独立同分布，未覆盖依赖数据（如时序用户行为）场景。

### 方法关键点
1. 稀疏惩罚深度神经网络（SPDNN）估计器适配分位数、Huber回归两类任务，显式建模源域与目标域的分布差异
2. 协变量的源-目标密度比未知时，采用两阶段预训练：先训练最小二乘SPDNN估计密度比，再用密度比重加权训练回归任务SPDNN
3. 推导满足i.i.d、φ混合、强混合等多种数据模式的广义Bernstein型不等式作为理论支撑

### 关键结果
SPDNN估计器的非渐近误差界在Hölder光滑函数类上得到证明，在i.i.d和经典时序模型下均可自适应达到（仅差对数因子）最小最大最优收敛率
