---
title: 'SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement
  Learning'
title_zh: SafeDiSTL：面向安全多智能体强化学习的联合约束分解方法
authors:
- Hongrui Zheng
- Aditya Singh
- Rahul Mangharam
affiliations:
- University of Pennsylvania
arxiv_id: '2610.13737'
url: https://arxiv.org/abs/2610.13737
pdf_url: https://arxiv.org/pdf/2610.13737
published: '2026-10-09'
collected: '2026-10-12'
category: MultiAgent
direction: 多智能体强化学习 · 安全约束归因
tags:
- Multi-Agent RL
- Safe RL
- Constraint Decomposition
- STL
- Credit Assignment
one_liner: 基于STL鲁棒性梯度分解共享约束，实现高任务性能的安全多智能体强化学习
practical_value: '- 电商多广告位投放、多渠道流量调控等带全局约束的多智能体决策场景，可复用本文的敏感性加权约束归因思路，替代传统全局统一罚则，避免合规约束下的业务收益过度损失

  - 共享约束的成本拆分可直接借鉴本文的增量成本分配方案，仅给对违规有实际贡献的智能体施加惩罚，减少无效策略更新，提升协同效率

  - 有全局安全/合规要求的多Agent调度系统（如电商仓储机器人调度、广告投放预算管控），可直接复用SafeDiSTL的约束分解+拉格朗日优化框架，快速实现兼顾性能与合规的策略训练'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有约束多智能体强化学习大多假设单智能体具备独立可观测的成本函数，但真实协同场景（如多机器人运输、交通管控、电商多渠道全局预算约束）的约束是全局共享的，违规责任难以归因到单个智能体，全局统一罚则会导致策略死锁或任务性能大幅下降，缺乏合理的共享约束分解机制。
### 方法关键点
- 采用Signal Temporal Logic(STL)鲁棒性指标量化全局约束的违反程度，通过可微动力学反向传播计算每个智能体各时刻动作对最终违规的敏感性权重
- 基于敏感性权重将全局违规增量成本分配到对应智能体，保留总成本不变，避免均分罚则导致的协调失效问题
- 融合归因后的单智能体成本与全局拉格朗日乘子，基于MAPPO实现中心化训练、去中心化执行的策略优化
### 关键实验
在3类协同任务上对比无约束MAPPO、约束基线MACPO、MAPPO-L：载荷运输任务安全成功率达基线的1.6-5.1倍；连通导航任务安全成功率相对提升11.1%；交通管控任务吞吐量比现有约束基线高50%-68%，同时保留无约束MAPPO 71.4%的任务性能。
### 核心结论
共享约束下的差异化责任归因，而非全局统一罚则，是平衡多智能体协同任务性能与安全合规的核心。
