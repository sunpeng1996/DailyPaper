---
title: 'Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical
  Multi-Objective Optimization'
title_zh: 非等权重目标优化：面向分层多目标的优先级约束下降方法
authors:
- Dara Varam
- Mohamed I. Alhajri
affiliations:
- American University of Sharjah
- Massachusetts Institute of Technology
arxiv_id: '2606.29521'
url: https://arxiv.org/abs/2606.29521
pdf_url: https://arxiv.org/pdf/2606.29521
published: '2026-06-28'
collected: '2026-06-30'
category: Training
direction: 深度学习训练 · 分层多目标优化
tags:
- Multi-Objective Optimization
- Gradient Descent
- Model Compression
- Pareto Optimality
- Training Framework
one_liner: 单参数调控的优先级约束下降框架，解决分层多目标优化的对称性偏差问题
practical_value: '- 推荐多目标训练（主目标CTR/CVR、次目标延迟/稀疏性/鲁棒性）场景，可直接替换现有多目标优化器，用τ参数灵活调控主次目标tradeoff，无需手动调整多目标权重

  - 做LLM/推荐模型轻量化时，主目标保效果、次目标提稀疏/低秩度，可复用PCD的闭形式解快速得到Pareto最优解，大幅降低调参成本

  - 多Agent协作任务有明确主次目标（如主目标转化率、次目标用户满意度）时，可复用PCD的优先级约束逻辑做梯度层面的目标对齐'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有多目标优化方法默认目标权重对称，忽略深度学习任务中普遍存在的主次目标分层结构，无法保证主目标性能不衰减的前提下优化次目标，且目标量纲差异易导致训练不稳定。
### 方法关键点
优先级约束下降（PCD）梯度优化框架核心逻辑为：保留主目标下降方向的基础上，仅做最小程度的梯度扭曲保证次目标迭代进展，仅用单参数τ∈[0,1]控制扭曲强度，不受目标量纲缩放影响，2/3个目标的场景可直接用闭形式解计算，无额外推理开销。
### 关键结果
在合成实验、网络压缩（非结构化稀疏、低秩分解）等任务上，相比基线方法实现Pareto占优，相同主目标性能下，次目标表现平均提升8%以上，τ调控的tradeoff曲线平滑可解释。
