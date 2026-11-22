---
title: Bayesian optimization on amortized search space
title_zh: 基于摊销搜索空间的贝叶斯优化方法
authors:
- Tristan Fauvel
- Federico Pavone
- Titouan Guillou
- Pau Redon Muñoz
- Chloé Geoffroy
affiliations:
- Theremia, Paris, France
arxiv_id: '2611.26459'
url: https://arxiv.org/abs/2611.26459
pdf_url: https://arxiv.org/pdf/2611.26459
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 黑盒优化 · 贝叶斯优化降维
tags:
- BayesianOptimization
- BlackBoxOptimization
- AmortizedInference
- GaussianProcess
- DimensionalityReduction
one_liner: 利用模拟器摊销逆映射压缩贝叶斯优化搜索空间，适配原问题几何结构提升黑盒优化效率
practical_value: '- 推荐/广告链路超参数调优场景，可先基于历史数据训练离线超参-效果映射的摊销模型，将贝叶斯优化的高维搜索空间压缩到低维表征空间，大幅减少调优迭代次数

  - 个性化配置类场景（如用户权益发放阈值、广告出价策略），可复用「离线预训练映射+在线低维空间搜索」架构，在保证效果的前提下降低在线计算开销

  - 高维黑盒优化时，可引入先验模拟器的几何信息调整Gaussian Process核函数，降低近似偏差，提升优化结果鲁棒性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
工业界大量高维黑盒优化问题（如超参调优、策略配置）采样成本极高，传统Bayesian Optimization在高维空间下效率低、收敛慢，而已有先验模拟器的价值未被充分利用。
### 方法关键点
1. 预训练离线神经网络学习模拟器的摊销逆映射，将高维原始搜索空间映射到低维内在表征空间，缩小搜索范围；
2. 设计适配原问题几何结构的Gaussian Process核函数，降低空间映射带来的近似偏差；
3. 在线Bayesian Optimization直接在低维表征空间搜索，再映射回原始空间执行。
### 关键结果
在帕金森病个性化用药dosing任务中采样效率显著优于原生Bayesian Optimization，在模拟器存在偏差的场景下仍保持鲁棒性，理论上可导出依赖内在维度的regret收敛速率。
