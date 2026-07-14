---
title: Rank-Conditioned Sample Reuse for the Plackett--Luce Best-of-$K$ Objective
title_zh: 面向Plackett-Luce Best-of-K目标的秩条件样本复用方法
authors:
- Melveena Jolly
- Midhun Xavier
affiliations:
- Independent Researcher
arxiv_id: '2607.11146'
url: https://arxiv.org/abs/2607.11146
pdf_url: https://arxiv.org/pdf/2607.11146
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: 训练优化 · 无偏梯度估计
tags:
- Policy Gradient
- Best-of-K
- Unbiased Estimator
- Plackett-Luce
- Sample Reuse
one_liner: 针对Plackett-Luce无放回采样Best-of-K目标，提出无偏样本复用梯度估计器，计算复杂度降至O(nlogn+nKQ)
practical_value: '- 做LLM Best-of-N对齐、生成式推荐多样性采样时，若采用Gumbel-Top-K/Stochastic Beam Search采样，可直接复用该梯度估计方案解决i.i.d.权重的偏差问题，避免重复采样浪费算力

  - 训练时只要设置采样池大小n≥2K，就能保证梯度二阶矩有限、训练稳定，该配置条件可直接落地到业务训练脚本中，规避梯度爆炸风险

  - 涉及无放回采样的排序/推荐任务优化（比如避免推荐重复物品的多目标优化），可复用秩条件Horvitz-Thompson重加权思路，降低样本复用的偏差'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有Best-of-K优化的样本复用梯度估计器均基于i.i.d.有放回采样假设，但Gumbel-Top-K/Stochastic Beam Search等业务常用采样属于无放回Plackett-Luce采样，直接套用i.i.d.权重会引入系统性偏差，三物品实例下偏差可达20%；现有无偏梯度估计方案无样本复用能力，算力消耗高。

### 方法关键点
- 基于秩条件Horvitz-Thompson估计构造无偏估计器，从大小为n> K的Gumbel-Top-n采样池中复用所有C(n,K)个K子集，实现Plackett-Luce Best-of-K目标的无偏估计
- 设计Max目标专属的奖励排序动态规划，将组合数级别的子集求和精确降为一维积分，结合Gauss-Laguerre求积实现O(nlogn +nKQ)计算复杂度（Q为求积节点数）
- 严格证明当采样池大小n≥2K时，估计器及对应代理梯度的二阶矩有限，可保证训练稳定性

### 关键结果
有限模型验证中，估计器值误差、梯度相对L2误差均低于1e-11，与暴力枚举结果的相对误差低于3e-13；n=16、K=8场景下相比暴力枚举提速超650倍，n=50、K=10场景下单步计算仅需3.9ms。

最值得记住的结论：无放回Plackett-Luce采样下的Best-of-K优化，只要采样池大小≥2K，采用秩条件重加权方案即可无偏复用所有样本，大幅降低训练算力消耗。
