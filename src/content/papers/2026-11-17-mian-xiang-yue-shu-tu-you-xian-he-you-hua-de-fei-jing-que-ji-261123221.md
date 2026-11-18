---
title: An inexact stochastic variance-reduced gradient method for constrained convex
  finite-sum optimization
title_zh: 面向约束凸有限和优化的非精确随机方差缩减梯度方法
authors:
- Zhaosong Lu
- Yifeng Xiao
arxiv_id: '2611.23221'
url: https://arxiv.org/abs/2611.23221
pdf_url: https://arxiv.org/pdf/2611.23221
published: '2026-11-17'
collected: '2026-11-18'
category: Other
direction: 约束凸优化 · 随机方差缩减梯度
tags:
- SVRG
- convex_optimization
- finite-sum_optimization
- variance_reduction
- constrained_optimization
one_liner: 提出约束凸有限和优化的非精确SVRG方法，大幅降低ε-SFSO解的一阶oracle复杂度
practical_value: '- 推荐系统带硬约束的排序/召回优化（如ROI、库存约束下的CTR/CVR预估损失优化）可尝试引入该非精确SVRG方法，降低梯度计算开销，提升训练速度

  - 当优化场景下约束梯度计算、凸锥投影的成本远低于目标函数梯度评估成本时，可替换现有凸优化求解器，获得更优的求解效率

  - 多目标带硬约束的LLM微调、RLHF优化场景可复用ε-SFSO解的求解思路，保证约束条件确定性满足，避免概率性约束违反带来的业务风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
带硬约束的凸有限和优化是工业级优化问题的常见形式，现有方法求解**ε-SFSO解**（约束违反确定性≤ε、期望最优间隙≤ε）的一阶oracle复杂度远高于期望可行解的求解复杂度，存在明显优化空间。
### 方法关键点
1. 针对带凸锥约束的有限和优化场景，设计非精确随机方差缩减梯度（SVRG）求解框架
2. 单目标场景下可退化为标准凸锥优化的确定性一阶方法，适配更多基础优化场景
### 关键结果
相比此前业界最优方法，ε-SFSO解的一阶oracle复杂度实现量级优化；单目标场景下目标函数梯度评估复杂度显著优于现有求解器，数值实验验证性能提升
