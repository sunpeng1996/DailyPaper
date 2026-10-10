---
title: A Unified Bellman Operator for Safety-Critical Reinforcement Learning
title_zh: 面向安全关键场景强化学习的统一贝尔曼算子
authors:
- Nishanth Arun Rao
- Royina Karegoudra Jayanth
- Benjamin Eysenbach
- Jaime Fernández Fisac
affiliations:
- Princeton University
arxiv_id: '2610.12420'
url: https://arxiv.org/abs/2610.12420
pdf_url: https://arxiv.org/pdf/2610.12420
published: '2026-10-08'
collected: '2026-10-10'
category: Agent
direction: 智能体训练 · 安全强化学习
tags:
- Safe-RL
- Bellman-Operator
- Temporal-Difference
- Constrained-Optimization
- Policy-Training
one_liner: 提出融合性能与安全目标的统一贝尔曼算子，双时间尺度TD学习收敛到近零违规最优策略
practical_value: '- 电商RL排序、动态调价等安全敏感场景可借鉴联合价值函数设计，将合规、低质内容过滤等安全约束与收益目标融合进贝尔曼更新，避免事后过滤的性能损耗

  - 双时间尺度更新框架可直接复用：安全约束项用快迭代步更新保证约束实时生效，核心业务目标用慢迭代步更新保证收敛稳定性，适配多目标RL落地

  - 智能客服话术生成、广告自动投放调参等Agent决策场景可参考该算子的严格安全保证特性，降低上线阶段违规输出风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
安全关键场景强化学习需同时最大化任务性能与严格满足安全约束，现有方案存在明显权衡：要么依赖先验知识做安全过滤，要么仅能满足平均安全约束，无法兼顾最优性与全时序安全。
### 方法关键点
1. 设计统一Bellman算子，将性能、安全目标融合为单个联合价值函数，无需额外独立安全模块
2. 基于双时间尺度随机近似框架实现TD学习：快时间尺度估计当前策略的安全价值，慢时间尺度更新联合价值
3. 理论上通过占位平均微分包含证明收敛性，可渐近收敛到满足安全约束的最优价值函数集合
### 关键结果
理论上收敛后最优策略可在全时序保证安全的同时最大化任务收益，连续控制任务仿真中实现稳定收敛，测试阶段安全违规率接近0。
