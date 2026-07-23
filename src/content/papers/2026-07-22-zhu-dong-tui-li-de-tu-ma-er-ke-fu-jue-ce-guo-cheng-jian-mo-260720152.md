---
title: Active Inference as a Convex Markov Decision Process
title_zh: 主动推理的凸马尔可夫决策过程建模与优化方法
authors:
- Nikola Milosevic
- Nicolás Hinrichs
- Nico Scherf
affiliations:
- Max Planck Institute for Human Cognitive and Brain Sciences
arxiv_id: '2607.20152'
url: https://arxiv.org/abs/2607.20152
pdf_url: https://arxiv.org/pdf/2607.20152
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: 主动推理 · Agent决策优化
tags:
- Active Inference
- Convex MDP
- Expected Free Energy
- Mirror Descent
- Reinforcement Learning
one_liner: 将主动推理的期望自由能最小化转化为凸MDP，推导兼容主流RL的镜像下降优化算法
practical_value: '- 做推荐/广告的探索利用平衡决策时，可借鉴将认知探索收益转化为策略依赖奖励的思路，无需单独搭建探索分支即可融合到现有RL排序框架

  - 电商Agent多步决策（如用户旅程引导、会话推荐）可复用凸MDP建模思路，降低长期策略优化的收敛难度

  - 可将提出的局部线性化镜像下降算法应用到现有actor-critic推荐框架，提升端到端策略优化的稳定性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有主动推理（AIF）优化框架与主流强化学习（RL）兼容性差，缺乏工程落地所需的收敛性保障，限制其在工业Agent场景的应用。
### 方法关键点
1. 将AIF核心目标期望自由能（EFE）最小化转化为凸MDP问题，其中务实目标对应隐式MDP的奖励最大化，认知价值引入的非线性项是其与标准RL的核心差异；
2. 推导镜像下降优化算法，对EFE目标围绕当前状态边缘分布做局部线性化，得到的策略依赖奖励完全兼容actor-critic与动态规划方法；
3. 证明AIF耦合世界模型学习与策略优化的结构属于表现性RL，可直接对接现代RL的收敛分析与策略改进理论。
### 关键结果
统一了AIF与主流RL的优化框架，为AIF提供了可落地的工程实现路径与理论收敛保障。
