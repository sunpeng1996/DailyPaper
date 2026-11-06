---
title: 'ShapleyOG: Fast Adaptive Shapley Value Estimation with Odd Gaussian Processes'
title_zh: ShapleyOG：基于奇高斯过程的快速自适应Shapley值估计方法
authors:
- David Rundel
- R. Teal Witter
- Santo M. A. R. Thies
- Matthias Feurer
- Fabian Fumagalli
- Bernd Bischl
affiliations:
- LMU Munich
- MCML
- Claremont McKenna College
- TU Dortmund University
- Lamarr Institute for Machine Learning and Artificial Intelligence
arxiv_id: '2611.07173'
url: https://arxiv.org/abs/2611.07173
pdf_url: https://arxiv.org/pdf/2611.07173
published: '2026-11-04'
collected: '2026-11-06'
category: Other
direction: 机器学习归因 · Shapley值高效估计
tags:
- Shapley Value
- Model Attribution
- Gaussian Process
- Efficient Inference
- Interpretability
one_liner: 基于奇高斯过程的自适应Shapley值估计方法，精度持平下计算开销降3个数量级
practical_value: '- 电商/推荐场景的特征归因、模型可解释性分析可直接替换原Shapley估计器，相同精度下减少99.9%计算开销，相同预算下获得更高估计精度

  - 仅对Shapley值依赖的奇分量建模拟合的思路可迁移到其他归因方法的加速优化中，裁剪不必要的计算冗余

  - 稀疏调度重拟合代理模型+间隔更新选择准则的工程优化方案，可复用在所有需要迭代拟合代理模型的算法落地场景'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
Shapley值是机器学习归因的核心工具，精确计算复杂度为指数级，现有自适应估计方案ShaplEIG需每轮重拟合高斯过程代理模型，计算开销极高，仅适用于低评估预算的高成本博弈场景。

### 方法关键点
1. 利用Shapley值仅依赖博弈奇分量的特性，配对采样下仅对奇分量拟合高斯过程，观测数减半即可获得相同的Shapley值后验与联盟选择准则；
2. 采用稀疏调度重拟合代理模型，间隔期高效更新选择准则；
3. 扩展积分计算方案到Shapley值先验协方差，支持精确或低成本近似计算。

### 关键结果
多类博弈实验中，精度与ShaplEIG持平，计算开销最高降低3个数量级；单轮评估仅需0.1s、数千次评估预算的场景下，同等总计算时间性能优于SOTA非自适应估计器，大幅拓宽自适应方法适用范围。
