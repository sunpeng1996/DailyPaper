---
title: 'Split-RL: Local Conflict Resolution in Reinforcement Learning'
title_zh: Split-RL：强化学习场景下的局部冲突消解算法
authors:
- Benjamin Fuhrer
- Chen Tessler
- Gal Dalal
affiliations:
- NVIDIA
- NVIDIA Research
arxiv_id: '2611.34799'
url: https://arxiv.org/abs/2611.34799
pdf_url: https://arxiv.org/pdf/2611.34799
published: '2026-11-25'
collected: '2026-11-27'
category: Training
direction: 强化学习训练 · 多目标冲突消解
tags:
- Reinforcement Learning
- Gradient Boosting Trees
- Multi-Objective Optimization
- Offline RL
- Constrained RL
one_liner: 基于梯度提升树设计引导标签路由机制，隔离强化学习中时空局部冲突的训练信号
practical_value: '- 多目标推荐排序场景可借鉴信号路由思路，对新老用户、高低客单价等细分场景隔离冲突优化梯度，避免全局目标拉扯导致局部效果下降

  - 基于RL训练推荐Agent时，可引入现有业务规则作为引导标签，在树结构训练中划分状态空间，平衡规则约束与策略优化的效果

  - 大促、异常用户等稀有事件的策略优化，可通过引导标签单独划分状态子空间训练，避免梯度被普通场景信号淹没'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
RL训练常混合时空局部冲突的反馈信号，传统NN参数全局共享导致不同目标的信号互相干扰，标准GBT树拟合流程也会提前聚合冲突梯度，丢失分目标的局部优化信息，无法适配不同状态区域目标优先级不同的场景。
### 方法关键点
提出Split-RL算法，基于GBT天然的状态空间划分归纳偏置，将启发式规则、业务规则、传感器事件生成的引导标签嵌入树构造流程，把不同目标的梯度更新路由到互不重叠的状态空间子区域，从结构上避免冲突信号干扰，同时保留规则结构与策略学习能力。
### 关键结果
在含空间、稀有事件、时间冲突的多类场景中，Split-RL在满足回合成本预算的同时保持竞争力的奖励，效果优于现有基线；离线RL场景下，在不同数据集规模上均接近专家性能，平衡模仿与策略优化的效果超过基线方法。
