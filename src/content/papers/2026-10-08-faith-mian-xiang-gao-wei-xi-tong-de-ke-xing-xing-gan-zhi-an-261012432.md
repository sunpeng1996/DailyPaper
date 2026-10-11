---
title: 'FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems'
title_zh: FAITH：面向高维系统的可行性感知安全过滤强化学习框架
authors:
- Songyuan Zhang
- Baljeet Singh
- Sarthak Ranjeet Kaingade
- Chuchu Fan
- Bryan Trinh
affiliations:
- Massachusetts Institute of Technology
- Amazon
arxiv_id: '2610.12432'
url: https://arxiv.org/abs/2610.12432
pdf_url: https://arxiv.org/pdf/2610.12432
published: '2026-10-08'
collected: '2026-10-11'
category: Training
direction: RL安全过滤训练框架 高维系统适配
tags:
- Reinforcement Learning
- Safety Filter
- Model-free
- High-dimensional System
- Constraint Optimization
one_liner: 提出无模型可行性感知安全过滤RL框架FAITH，解耦安全约束与任务目标适配高维系统
practical_value: '- 解耦主任务目标与安全约束的架构思路可直接迁移到广告/推荐系统，将合规性、负向体验控制从主排序目标剥离为独立过滤模块，避免多目标优化的梯度冲突

  - 无模型安全值估计方法可复用在Agent动作生成场景，无需预先枚举所有硬规则即可实现低干预的合规动作修正，大幅降低规则维护成本

  - 无可行安全动作时的最小伤害降级策略，可参考用于大促、流量突增等极端场景的推荐降级方案，优先保障核心合规要求前提下最大化业务收益'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统安全RL将安全约束与任务目标合并优化易产生梯度冲突；经典安全过滤器依赖解析安全函数与动力学模型，最小干预过滤器仅考虑瞬时动作偏差缺乏长视距考量，无安全动作时硬投影方案完全失效。
### 方法关键点
1. 无模型框架，拟合最优状态-动作安全值，用前馈网络实现最小干预过滤的摊销计算；
2. 任务策略基于过滤后的动力学优化收益，更新过程无冲突的安全项约束；
3. 无满足条件的安全动作时，自动选择预测峰值伤害最低的动作。
### 关键结果
Safety Gym环境下可行启动场景无违规同时收益最高，不可行启动场景伤害最低；29自由度人形机器人Walking-Avoid任务安全率99.95%，保留97%未过滤版本收益，Push-Avoid任务安全率达业界最高，已在真实Unitree G1机器人落地验证。
