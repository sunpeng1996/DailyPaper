---
title: Tamed Stochastic Gradient Hamiltonian Monte Carlo
title_zh: 驯服型随机梯度哈密顿蒙特卡洛（tSGHMC）算法
authors:
- Zhuoran Wang
- Ying Zhang
arxiv_id: '2607.14862'
url: https://arxiv.org/abs/2607.14862
pdf_url: https://arxiv.org/pdf/2607.14862
published: '2026-07-16'
collected: '2026-07-19'
category: Training
direction: 随机优化 · 采样训练算法优化
tags:
- SGHMC
- Stochastic Optimization
- Sampling Algorithm
- Convergence Bound
- Excess Risk
one_liner: 提出tSGHMC解决超线性梯度的采样与优化问题，给出理论保障且实测效果优于基准
practical_value: '- 推荐/广告排序模型训练出现梯度爆炸（超线性增长梯度）场景时，可替换普通SGLD采用tSGHMC做优化，降低训练误差

  - 贝叶斯个性化推荐、用户偏好不确定性建模的采样任务中，可引入tSGHMC提升采样效率与收敛速度

  - 电商库存定价、流量投放风险控制类优化问题，可直接用tSGHMC求解CVaR最小化等任务，降低预期超额风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有随机梯度蒙特卡洛算法无法处理梯度超线性增长的优化/采样场景，缺乏非渐近收敛理论保障，在风险控制、运营优化等任务上误差较高。
### 方法关键点
1. 提出tSGHMC算法，针对超线性增长随机梯度的场景设计驯服机制，适配更广泛的优化任务
2. 在平均连续性与强凸条件下，证明Wasserstein-2距离下的非渐近误差界，收敛速率为1/4
3. 推导预期超额风险上界，为算法性能提供严格理论保证
### 关键结果数字
在报童问题、条件风险价值（CVaR）最小化任务上，相比一阶基准tamed unadjusted随机朗之万算法，tSGHMC的RMSE与预期超额风险均更低，数值实验完全匹配理论结论
