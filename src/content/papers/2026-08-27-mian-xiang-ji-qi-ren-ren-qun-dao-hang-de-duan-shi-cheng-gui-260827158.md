---
title: Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation
title_zh: 面向机器人人群导航的短视程规划扩散策略
authors:
- Wendong Li
- Jochen Garcke
affiliations:
- Institute for Numerical Simulation, University of Bonn
arxiv_id: '2608.27158'
url: https://arxiv.org/abs/2608.27158
pdf_url: https://arxiv.org/pdf/2608.27158
published: '2026-08-27'
collected: '2026-08-31'
category: Agent
direction: 机器人导航Agent · 扩散策略优化
tags:
- Diffusion Policy
- Reinforcement Learning
- Motion Planning
- Offline RL
- PPO
one_liner: 提出离线预训练+在线PPO微调的PDPO框架，用扩散策略生成短视程动作块提升人群导航性能
practical_value: '- 扩散策略生成短步长动作序列的思路可迁移到推荐Agent的会话级多步推荐、广告投放序列规划场景，保证动作序列的一致性与可选多样性

  - 「离线专家示范预训练+在线PPO微调」的两阶段训练范式可复用在推荐/广告Agent的策略优化中，大幅降低线上探索成本

  - 补全基准约束解决评估漏洞的思路可借鉴到推荐Agent的离线评估设计，避免指标虚高与线上线下效果不一致问题'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
机器人密集人群导航需在动态多模态人机交互下做安全高效决策，现有RL方法单步输出反应式动作，无法覆盖多样的短期避障策略；同时现有基准存在无边界约束的评估漏洞，智能体可通过离开有效域绕开密集人群作弊。
### 方法关键点
1. 提出PDPO离线转在线RL框架：先基于避障示范数据预训练扩散策略，再将去噪过程作为内部决策流程，用PPO做在线微调；
2. 执行阶段生成5步动作块，采用滚动horizon方式执行；
3. 修正基准评估规则，将边界越界行为视为碰撞补全约束。
### 关键结果
PDPO相比现有强基线成功率显著提升，ablation实验证明短动作块在修正后的带约束基准上对性能增益尤为关键。
