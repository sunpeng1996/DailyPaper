---
title: 'A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale
  RL for Robot Control'
title_zh: 均衡数据策略：解决超大规模机器人控制强化学习的探索瓶颈
authors:
- Octi Zhang
- Mateo Guaman Castro
- Patrick Yin
- Ignacio Dagnino
- Abhishek Gupta
- Rosario Scalise
- Byron Boots
affiliations:
- University of Washington
- NVIDIA
arxiv_id: '2610.12465'
url: https://arxiv.org/abs/2610.12465
pdf_url: https://arxiv.org/pdf/2610.12465
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 强化学习 · 自适应采样优化
tags:
- Reinforcement Learning
- Adaptive Sampling
- Sim-to-Real
- Robot Control
- Large-scale Training
one_liner: 提出成功引导采样SGS，自适应聚焦RL训练的能力边界任务配置，大幅提升超大规模并行RL训练效率
practical_value: '- 自适应采样思路可复用在推荐/广告的负采样优化：避免采样过易（已转化）或过难（完全无兴趣）的负样本，聚焦用户决策边界样本提升训练效率

  - 能力边界采样逻辑可迁移到Agent技能学习流程：优先训练Agent当前能力边缘的任务，避免无效经验浪费，加速多技能Agent迭代

  - 大规模并行训练的样本效率优化思路可复用到LLM4Rec的预训练/微调阶段，降低无效batch占比，提升算力利用率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前超大规模并行模拟RL的均匀采样策略，会把大量训练经验浪费在策略已经掌握或暂时无法完成的任务配置上，导致并行算力的scaling收益不明显，还需大量人工设计逐任务的结构先验（如塑形奖励、演示数据）。
### 方法关键点
提出Success Guided Sampling（SGS）自适应采样器，动态追踪策略的能力边界，优先采样处于当前能力边缘的任务配置，最大化每一批次训练样本的有效学习信号，无需人工设计逐任务的先验信息。
### 关键结果
最高支持$2^{20}$（超100万）并行环境训练，在多地形四足机器人运动、高接触力装配任务上，解决了原有采样方法无法收敛的问题，蒸馏得到的RGB策略可零样本迁移到真实硬件的装配任务。
