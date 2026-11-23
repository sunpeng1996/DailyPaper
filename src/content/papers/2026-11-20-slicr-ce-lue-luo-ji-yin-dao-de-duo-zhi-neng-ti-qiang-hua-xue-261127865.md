---
title: 'SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning'
title_zh: SLICR：策略逻辑引导的多智能体强化学习
authors:
- Arshia Rafieioskouie
- Matthew Lucas
- Tzu-Han Hsu
- Borzoo Bonakdarpour
affiliations:
- Michigan State University
arxiv_id: '2611.27865'
url: https://arxiv.org/abs/2611.27865
pdf_url: https://arxiv.org/pdf/2611.27865
published: '2026-11-20'
collected: '2026-11-23'
category: MultiAgent
direction: 多智能体强化学习·对抗场景策略优化
tags:
- MultiAgent
- ReinforcementLearning
- StrategyLogic
- LTL
- AdversarialLearning
one_liner: 融合策略逻辑与LTL的多智能体RL框架SLICR，适配部分可观测对抗场景动态对手响应需求
practical_value: '- 多智能体流量分配、广告竞价博弈场景可引入Strategy Logic+LTL组合，将业务约束、对手响应规则转化为RL塑形奖励，降低人工reward设计复杂度

  - 电商反作弊、大促同行竞价等对抗性场景的Agent设计可参考SLICR思路，放弃固定对手策略假设，适配动态/非理性对手行为

  - 搜推广链路多模块联合优化等多Agent协作任务，可复用其显式量化各Agent策略的逻辑，提升跨模块策略对齐效率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有规范引导的多智能体RL（MARL）默认对手策略稳定，仅学习固定任务的单一策略，无法适配部分可观测对抗场景下动态、非理性的对手行为，落地鲁棒性不足。
### 方法关键点
1. SLICR框架引入Strategy Logic（SL）显式量化各Agent的策略空间，结合线性时序逻辑（LTL）定义Agent的优化目标与行为约束
2. 支持同时推理自身满足规范的行为路径，以及对其他Agent策略、行为的动态响应逻辑，无需预设对手策略的稳定性假设
### 关键结果
在Predator-Prey、Google Research Football、扩展版SMAC-HARD三类基准任务上验证，相比现有SOTA方法具备更优的效果、可扩展性，以及对多样化对抗策略的适配能力
