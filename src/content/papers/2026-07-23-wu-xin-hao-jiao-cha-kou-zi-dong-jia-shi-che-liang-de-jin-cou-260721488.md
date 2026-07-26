---
title: Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections
title_zh: 无信号交叉口自动驾驶车辆的紧凑隐式协调方法
authors:
- Gil Lifshits
- Igal Bilik
- Gilad Katz
affiliations:
- Ben-Gurion University of the Negev
arxiv_id: '2607.21488'
url: https://arxiv.org/abs/2607.21488
pdf_url: https://arxiv.org/pdf/2607.21488
published: '2026-07-23'
collected: '2026-07-26'
category: MultiAgent
direction: 多智能体分层协作优化
tags:
- MARL
- Hierarchical RL
- Multi-Agent Coordination
- Zero-shot Generalization
- Embedding
one_liner: 提出分层MARL架构MAPS，通过全局proto-plan嵌入实现无信号路口多车高效协调，泛化性优异
practical_value: '- 分层主从Agent的解耦设计（全局策略生成+本地执行）可直接迁移至多Agent广告投放、推荐流量调控场景，避免全局优化的复杂度爆炸

  - 用紧凑连续embedding作为全局协调信号替代显式通信，可大幅降低多Agent系统通信开销，适配搜索推荐等低延迟要求场景

  - 小Agent规模训练、大Agent规模零样本部署的思路，可显著降低高流量多Agent推荐/广告系统的训练成本与迭代周期'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
无信号交叉口多自动驾驶车辆协调是MARL领域核心难点，现有方案普遍存在动作空间组合爆炸、依赖特权信息、Agent设计僵化、跨场景泛化性差等问题。
### 方法关键点
提出分层DRL架构MAPS：中心化Master Agent生成编码全局协调策略的连续紧凑proto-plan嵌入；去中心化Worker Agent融合该嵌入与本地观测输出单车辆控制策略，实现全局战略意图与局部战术执行完全解耦，两个模块可独立优化。
### 关键结果
在HighwayEnv 72种交叉口配置下实现100%无碰撞导航，平均通行时间显著优于SOTA基线；3Agent训练的模型零样本迁移到5Agent场景成功率达94%，泛化能力突出。
