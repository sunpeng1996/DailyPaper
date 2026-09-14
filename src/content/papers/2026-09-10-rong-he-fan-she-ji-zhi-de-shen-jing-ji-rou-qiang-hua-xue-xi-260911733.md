---
title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion
title_zh: 融合反射机制的神经肌肉强化学习用于肌肉驱动运动控制
authors:
- Jian Zhou
- Xingyu Zhang
- Rui Ma
- Yu Cao
- Shane Xie
- Zhi-qiang Zhang
affiliations:
- University of Leeds
arxiv_id: '2609.11733'
url: https://arxiv.org/abs/2609.11733
pdf_url: https://arxiv.org/pdf/2609.11733
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 肌肉驱动运动控制 · 强化学习融合反射机制
tags:
- ReinforcementLearning
- NeuromuscularControl
- Physics-basedSimulation
- LocomotionControl
- ResidualLearning
one_liner: 结合固定相位反射控制器与RL残差参数调制，实现生理可信且高鲁棒的肌肉驱动运动控制
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
肌肉驱动运动是物理可信人体运动生成的核心路径，但现有方案难以同时满足生理合理性、对肌肉骨骼能力变化与外部扰动的自适应能力，落地限制较大。

### 方法关键点
提出融合反射机制的神经肌肉强化学习框架：底层采用固定相位依赖的反射控制器作为基础神经肌肉控制机制，上层RL策略仅输出4个具备生物力学意义的残差参数，根据当前状态调制髋摆动、膝支撑、踝推进相关的核心反射增益与阈值，控制逻辑完全符合生理规律。

### 关键结果数字
标称行走场景下运动学精度、动态一致性、双侧对称性、步间一致性均实现显著提升；无需重训练即可在肌肉无力、外部扰动场景下保持鲁棒性，适应能力远超基线方案。
