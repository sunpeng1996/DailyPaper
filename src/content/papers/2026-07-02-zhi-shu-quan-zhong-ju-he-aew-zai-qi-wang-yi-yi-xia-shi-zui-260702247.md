---
title: Aggregation with Exponential Weights is Optimal in Expectation
title_zh: 指数权重聚合(AEW)在期望意义下是最优的
authors:
- Mikael Møller Høgsgaard
- Patrick Rebeschini
- Tobias Wegel
affiliations:
- Department of Statistics, University of Oxford
- Department of Computer Science, ETH Zurich
arxiv_id: '2607.02247'
url: https://arxiv.org/abs/2607.02247
pdf_url: https://arxiv.org/pdf/2607.02247
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 统计学习 · 模型聚合理论
tags:
- AEW
- Model Aggregation
- Minimax Optimality
- Exponential Weights
- Statistical Learning
one_liner: 解决2013年提出的开放问题，证明满足温度条件的AEW无需伯恩斯坦假设即可达到最优期望超额风险
practical_value: '- 多召回源/多排序模型加权融合场景，可参考AEW温度设置逻辑，平方损失下温度≥4b²（b为预测/标签值域上限）可保证期望最优

  - MoE门控的指数加权模块可参考该结论调整温度超参，规避温度过低导致的效果次优问题

  - 核心结论偏理论，暂无法直接支撑端到端业务效果提升，更适合做基础算法模块的超参调优参考'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
指数权重聚合(AEW)是广泛使用的模型选择聚合方法，但随机设计、固定温度场景下AEW是否在期望意义下达到最小最大率最优，是2013年即被提出的长期开放问题。
### 方法关键点
无需引入伯恩斯坦型假设，仅基于损失函数有界、L-Lipschitz连续、µ-强凸的基础假设，推导AEW的期望超额风险上界，明确温度阈值的约束条件。
### 关键结果
- 当温度T满足$(L^2/T)\exp(B/T)\leq \mu/2$时，AEW期望超额风险达到$T\log(M)/(n+1)$，符合最小最大最优率
- 针对平方损失场景，若预测与标签值域为$[0,b]$，$T\geq 4b^2$即可满足最优条件
- AEW存在清晰的温度相变点：低于阈值时效果次优，高于阈值即达到最优
