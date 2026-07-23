---
title: 'Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared
  Environments'
title_zh: 礼貌预规划：提升持久共享环境下长周期任务规划性能
authors:
- Md Ridwan Hossain Talukder
- Roshan Dhakal
- Elizabeth Phillips
- Gregory J. Stein
arxiv_id: '2607.20289'
url: https://arxiv.org/abs/2607.20289
pdf_url: https://arxiv.org/pdf/2607.20289
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: 多智体 · 共享环境长周期任务规划优化
tags:
- MultiAgent
- TaskPlanning
- Long-Horizon Planning
- Shared Environment
- Cost Estimation
one_liner: 提出基于独立单机器人成本预测器的礼貌预规划方法，降低共享环境多智体长序列任务总开销
practical_value: '- 多Agent协同场景（如电商多运营Agent、履约调度Agent）可借鉴分块估计思路，避免联合推演的组合爆炸问题，降低算力开销

  - 长周期序列决策任务（如用户全生命周期运营、连续广告投放）可参考「即时成本+未来预期总成本」的联合优化目标，避免短视决策

  - 新增Agent仅需训练对应独立预测器的模块化设计，可复用在动态扩缩容的多Agent业务系统中，降低迭代成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有共享环境下的多Agent任务规划多孤立求解单任务，既无未来任务预判，也不考虑其他Agent约束，长任务序列下负外部性累积，总开销持续升高。
### 方法关键点
1. 基于模型的规划器生成候选规划集，避免枚举所有可能动作
2. 每个Agent独立训练成本预测器，预估当前决策对自身未来任务的预期开销，无需联合推演
3. 最终选择同时最小化「即时成本 + 所有Agent未来预期总成本」的最优规划，模块化设计支持灵活新增Agent，仅需训练对应预测器
### 关键结果数字
- 双机器人家庭场景：总开销对比短视规划降低10.43%，对比自私预规划降低4.03%
- 三机器人餐厅场景：总开销对比短视规划降低17.41%，对比自私预规划降低13.24%
