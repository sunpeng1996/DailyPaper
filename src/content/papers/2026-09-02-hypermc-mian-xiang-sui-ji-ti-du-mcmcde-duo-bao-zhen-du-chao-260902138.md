---
title: 'HyperMC: Multi-Fidelity Hyperparameter Tuning for Stochastic Gradient MCMC'
title_zh: HyperMC：面向随机梯度MCMC的多保真度超参数调优框架
authors:
- Ming Tan
- Xiyun Jiao
affiliations:
- Department of Statistics and Data Science, Southern University of Science and Technology
arxiv_id: '2609.02138'
url: https://arxiv.org/abs/2609.02138
pdf_url: https://arxiv.org/pdf/2609.02138
published: '2026-09-02'
collected: '2026-09-05'
category: Training
direction: 模型训练 · SGMCMC超参数优化
tags:
- SGMCMC
- Hyperparameter Tuning
- Hyperband
- Kernel Stein Discrepancy
- Bayesian Inference
one_liner: 结合Hyperband资源分配与KSD评估，实现无需MH接受率的SGMCMC超参数高效调优
practical_value: '- 可复用Hyperband+successive halving的多保真度调优思路，用于CTR预估、召回排序模型的超参数搜索，大幅降低调优算力开销

  - 当调优目标无明确可直接观测的精度/接受率指标时，可借鉴KSD作为替代评估指标，实现无监督的超参数效果判别

  - Robust HyperMC的全局网格初始化+精英局部优化的策略，可迁移至推荐/广告模型的A/B实验参数选优，降低随机抽样带来的结果波动'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
SGMCMC是可扩展贝叶斯推理的核心方法，但步长、mini-batch size、蛙跳步数等超参数对效果影响极大，且多数SGMCMC无Metropolis-Hastings接受率，传统基于接受率的调优方法无法直接复用，超参数调优效率低、稳定性差。
### 方法关键点
HyperMC多保真度调优框架结合Hyperband风格的资源分配与核Stein偏差（KSD）评估，通过多轮successive halving bracket，在固定算力预算下平衡连续超参数空间的探索与优质配置的精准评估；进一步升级为Robust HyperMC，采用全局网格初始化+精英引导的局部优化，降低随机候选生成与有限预算评估噪声的敏感性。
### 关键结果
在逻辑回归、概率矩阵分解、贝叶斯神经网络任务上，HyperMC相比MAMBA、网格搜索、启发式基线，后验近似或预测校准效果更优，Robust HyperMC调优结果稳定性与可复现性进一步提升。
