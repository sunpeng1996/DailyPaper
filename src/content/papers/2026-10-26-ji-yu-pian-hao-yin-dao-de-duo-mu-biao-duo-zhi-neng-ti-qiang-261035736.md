---
title: Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement
  Learning
title_zh: 基于偏好引导的多目标多智能体强化学习协作框架
authors:
- Qiyue Xia
- J. Michael Herrmann
affiliations:
- University of Edinburgh
arxiv_id: '2610.35736'
url: https://arxiv.org/abs/2610.35736
pdf_url: https://arxiv.org/pdf/2610.35736
published: '2026-10-26'
collected: '2026-10-27'
category: MultiAgent
direction: 多智能体协作 · 多目标强化学习
tags:
- MultiAgent
- MARL
- MORL
- MetaGradient
- CreditAssignment
one_liner: 提出利用多目标结构引导协作的MIRL算法（含静态/动态变体），显著提升多智能体任务的Pareto前沿质量
practical_value: '- 多目标多智能体场景可借鉴分层偏好设计：上层固定业务全局目标权重，下层给单个Agent留出可学习的目标偏好空间，避免人工分配权重的偏差

  - 信贷分配环节可复用按目标维度拆分的反事实优势计算方法：分别统计每个Agent对GMV、转化率、客单价等不同业务目标的贡献，提供更精准的学习信号

  - 复杂协作任务（如多Agent协同做用户运营、内容分发链路协同）可引入元梯度动态调整单个Agent的目标偏好，适配不同业务场景的协作需求

  - 多目标优化场景的效果评估可直接复用Hypervolume、Expected Utility、Sparsity三个指标，全面衡量Pareto前沿的质量、覆盖度和均匀性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有的多目标多智能体强化学习（MOMARL）普遍将多目标优化和多智能体协作当做两个独立模块处理，复杂度极高，且未利用多目标本身的结构特征来降低协作难度，难以适配复杂动态的协作场景。

### 方法关键点
- 设计分层偏好机制：上层是固定的团队全局目标权重，下层是每个Agent可学习的个体目标偏好，在对齐全局目标的前提下给个体Agent留出灵活调整贡献方向的空间
- 提出分目标维度的反事实信贷分配：中央Critic输出每个目标维度的向量值Q函数，通过反事实基线计算每个Agent对不同目标的单独贡献，避免直接标量融合丢失目标维度信息
- 引入元梯度偏好更新机制：将个体偏好作为元参数，通过后续全局目标的表现回传梯度更新偏好，分别实现静态（全训练周期固定单个Agent偏好）和动态（每步根据当前状态生成偏好）两个算法变体MIRL-S、MIRL-D

### 关键实验
在多智能体粒子环境（MPE）的4个协作任务上对比DTDE-PPO、CTDE-PPO、MO-COMA、MO-MIX等5个基线，MIRL-D在4个任务的Hypervolume指标上分别提升0.8%~12.5%，Expected Utility提升0.2%~10.3%，动态变体在需要灵活协作的任务上优势更明显。

### 核心结论
多目标结构本身可以作为引导多智能体协作的信号，而非仅仅是额外的优化负担。
