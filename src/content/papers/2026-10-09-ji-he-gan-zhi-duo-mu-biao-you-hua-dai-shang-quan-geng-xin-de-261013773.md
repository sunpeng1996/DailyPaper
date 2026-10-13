---
title: 'Geometry-Aware Multi-Objective Optimization: Norm-Constrained Oracles with
  Entropic Weight Updates'
title_zh: 几何感知多目标优化：带熵权更新的范数约束预言机方法
authors:
- El Mahdi Chayti
- Alireza Mirrokni
- Martin Jaggi
affiliations:
- EPFL Machine Learning and Optimization Laboratory (MLO)
arxiv_id: '2610.13773'
url: https://arxiv.org/abs/2610.13773
pdf_url: https://arxiv.org/pdf/2610.13773
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 多任务训练 · 多目标优化器设计
tags:
- Multi-Objective Optimization
- Gradient Descent
- Norm Constraints
- Entropic Update
- Multi-Task Training
one_liner: 提出支持任意范数的单循环多目标优化方法，收敛速度领先且首项无任务数显式依赖
practical_value: '- 多目标推荐/广告排序场景，可复用其熵权更新+范数约束梯度组合逻辑，缓解多目标梯度冲突，大幅降低损失权重人工调参成本

  - 多任务LLM4Rec/Agent大模型微调（同时优化点击率、转化率、无害性等多目标），可引入其动量缓冲区设计，收敛速度不受任务数增长拖累

  - 可直接替换现有多目标优化器（如MGDA），在同等算力下获得更稳定的帕累托最优解，提升多任务模型整体表现'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多梯度下降默认基于欧氏几何，无法适配矩阵感知优化器的非欧范数需求，传统多目标优化器收敛速度随任务数增长明显退化，损失权重人工调参成本高。
### 方法关键点
1. 设计单循环多目标优化框架，融合范数约束线性最小化oracle与任务权重熵更新逻辑，支持任意有限维范数对；
2. 引入持久混合梯度动量缓冲区适配随机梯度场景，加入熵正则与权重floor保障迭代内间隙可控。
### 关键结果
- 确定性场景下遍历平稳率达$O(T^{-1/2})$；
- 随机梯度场景下收敛率达$O(T^{-1/4})$，首项无任务数显式依赖；
- 对比现有多任务优化器在不同范数下表现更优。
