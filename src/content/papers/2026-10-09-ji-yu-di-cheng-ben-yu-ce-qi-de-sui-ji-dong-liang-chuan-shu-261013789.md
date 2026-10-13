---
title: Randomized Momentum Transport with Cheap Predictors
title_zh: 基于低成本预测器的随机动量传输优化算法
authors:
- El Mahdi Chayti
- Martin Jaggi
affiliations:
- Machine Learning and Optimization Laboratory (MLO), EPFL
arxiv_id: '2610.13789'
url: https://arxiv.org/abs/2610.13789
pdf_url: https://arxiv.org/pdf/2610.13789
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 深度学习优化 · 动量优化器降本提速
tags:
- Optimizer
- Momentum
- TrainingAcceleration
- StochasticOptimization
- ConvergenceGuarantee
one_liner: 提出概率触发校正+低成本预测器的随机动量传输方法，降低动量优化器计算开销并提升训练效果
practical_value: '- 训练LLM4Rec、搜索推荐排序大模型、Agent微调场景下，可复用概率触发+低成本预测替换的思路，降低二阶动量、HVP等校正步骤的计算开销，无需每迭代执行全量校正

  - 分布式训练推荐大模型时，可直接复用文中重要性加权的无偏估计方案，在减少计算量的同时避免训练偏差

  - 超参数q=0.25（四分之一概率触发校正）的设置可直接落地验证，相同计算成本下可获得更优的收敛效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有STORM、二阶动量等带校正的动量优化器每迭代需1次额外oracle调用（如梯度计算、HVP），计算开销高，亟需降本方案。

### 方法关键点
1. 提出随机动量传输机制，仅以概率q触发校正项计算，其余步用低成本预测值替代，配合重要性加权保证条件期望无偏，仅新增$(q^{-1}-1)$倍预测损失的方差。
2. 理论证明在合理假设下，LMO类更新（含归一化、符号、Muon谱方向）仍保持$O(T^{-1/3})$的平稳性收敛界，在线对角预测器可保证regret到收敛的映射。

### 关键结果数字
相同计算成本下，q=0.25时MNIST1D任务最终训练损失降低18%~43%，CIFAR-10上Hessian-vector传输的测试精度提升1.5个百分点；非归一化STORM在梯度差噪声模超过平滑常数时，q<1可降低梯度预算领先系数最高约10%。
