---
title: Gradient TD($λ$) for Non-Linear Function Approximation
title_zh: 面向非线性函数逼近的梯度TD(λ)算法
authors:
- Sujeet Lahane
arxiv_id: '2611.34826'
url: https://arxiv.org/abs/2611.34826
pdf_url: https://arxiv.org/pdf/2611.34826
published: '2026-11-25'
collected: '2026-11-27'
category: Training
direction: 强化学习时序差分训练算法优化
tags:
- TD Learning
- Gradient TD
- Non-linear Function Approximation
- Off-policy RL
- Convergence
one_liner: 将梯度TD(λ)算法从线性函数逼近扩展到非线性场景，保留离策略收敛性保证
practical_value: '- 电商/广告推荐中基于RL的动态排序、用户LTV预估场景，可替换原有半梯度TD训练方法，降低离线策略训练发散风险

  - 采用DNN、LoRA微调等非线性拟合方案的RL推荐Agent，可直接复用该算法框架获得收敛性保证

  - 长序列用户行为价值回溯建模场景，λ-return的非线性适配可提升长期收益预估稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
半梯度TD算法存在易发散问题，基于均方Bellman/TD误差目标的算法分析难度极高；现有具备收敛保证的梯度TD(λ)仅支持线性函数逼近，无法适配DNN、Transformer等主流非线性拟合场景，限制了其在高维复杂业务任务中的应用。

### 方法关键点
以经典投影Bellman误差为核心优化目标，无需引入广义投影Bellman误差的额外假设，将梯度TD(λ)的适用范围从线性函数逼近扩展到非线性场景，完整保留原算法的离策略学习能力与收敛性保证。

### 关键结果
理论证明非线性场景下的梯度TD(λ)收敛性与线性版本完全一致，可直接对接各类现代非线性函数逼近器使用，无额外适配成本。
