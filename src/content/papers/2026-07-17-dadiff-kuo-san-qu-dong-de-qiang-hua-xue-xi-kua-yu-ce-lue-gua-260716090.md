---
title: 'DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement
  Learning'
title_zh: DADiff：扩散驱动的强化学习跨域策略适配方法
authors:
- Hanyang Chen
- Anirudh Satheesh
- Longchao Da
- Hua Wei
arxiv_id: '2607.16090'
url: https://arxiv.org/abs/2607.16090
pdf_url: https://arxiv.org/pdf/2607.16090
published: '2026-07-17'
collected: '2026-07-20'
category: Other
direction: 强化学习跨域策略迁移
tags:
- Reinforcement-Learning
- Diffusion-Model
- Domain-Adaptation
- Policy-Transfer
- Sim-to-Real
one_liner: 基于扩散模型生成轨迹偏差估计跨域动态差异，实现少交互下的RL策略跨域迁移
practical_value: '- 做推荐/广告投放的RL策略跨场景迁移时，可借鉴用扩散生成的源/目标域轨迹偏差衡量分布漂移，替代传统分布对齐方法

  - 针对目标域交互成本高的场景（如新电商类目冷启动策略调优），可复用该框架的奖励修正、数据筛选两个适配分支，降低目标域采样需求

  - 做Agent跨环境部署时，可参考该文的理论边界推导，量化策略跨域性能损失上限，提前预判迁移效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
强化学习跨域策略迁移受源域与目标域的动态不匹配限制，而目标域通常受安全、成本约束仅允许少量交互，现有基于域分类器、价值导向数据过滤、表征学习的适配方案效果有限。
### 方法关键点
1. 提出DADiff扩散框架，通过生成下一个状态过程中的源/目标域生成轨迹偏差，量化跨域动态差异
2. 设计奖励修正、数据筛选两类适配分支，实现策略向目标域迁移
3. 理论证明给定策略的跨域性能差受生成轨迹偏差的上界约束
### 关键结果
在多类动态偏移环境的实验中，性能全面优于现有跨域适配方法，有效解决动态不匹配问题。
