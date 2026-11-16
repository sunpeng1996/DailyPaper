---
title: On numerical issues of divergences between nearly equal distributions
title_zh: 《近似相等分类分布间散度计算的数值稳定性问题研究》
authors:
- Brandon Amos
affiliations:
- Reflection AI
arxiv_id: '2611.18511'
url: https://arxiv.org/abs/2611.18511
pdf_url: https://arxiv.org/pdf/2611.18511
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 训练优化 · 散度计算数值稳定性提升
tags:
- NumericalStability
- KLDivergence
- JSDivergence
- LossOptimization
- KnowledgeDistillation
- ReinforcementLearning
one_liner: 发现KL、JSD等散度在近似相等分布下的数值缺陷，给出稳定重写方案及可复用实现
practical_value: '- 做LLM4Rec、排序模型知识蒸馏时，替换KL散度为论文提供的稳定实现，避免师生分布接近时梯度消失导致蒸馏效果差

  - 推荐场景用RL做序列优化、Agent用PPO等近端算法时，散度约束模块直接复用该稳定实现，减少训练震荡

  - 生成式推荐做分布对齐（如生成item分布与真实分布对齐）用到JSD时，采用该方案解决分布接近时收敛不动的问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Barron等2026年发现softmax、软交叉熵损失存在数值缺陷，现有标准散度实现未覆盖近似相等分布下的异常场景，会导致知识蒸馏、强化学习、近端优化等任务训练异常。
### 方法关键点
1. 验证前向/反向KL散度、广义JSD、蒙特卡洛KL估计、熵计算在分布近似相等时，均会出现舍入、抵消问题，影响前向计算结果与梯度回传准确性
2. 针对每类散度运算给出数值稳定的重写公式，配套可直接落地的代码实现
### 关键结果
所有稳定实现均通过基于属性的测试，在分布相似度极高的场景下，前向计算精度、梯度准确性相比标准实现提升3个数量级以上，无梯度消失或异常梯度问题
