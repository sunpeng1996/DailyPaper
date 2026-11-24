---
title: 'Habitats: A Framework for Open-Ended Evolution of Agent Objectives'
title_zh: Habitats：面向Agent目标开放式演化的通用框架
authors:
- Nicolas Bolouri
- Gaya Mehenni
- Daniel Toyama
affiliations:
- Google DeepMind
arxiv_id: '2611.31160'
url: https://arxiv.org/abs/2611.31160
pdf_url: https://arxiv.org/pdf/2611.31160
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: Agent 开放式目标演化框架
tags:
- AgentEvolution
- OpenEndedLearning
- LLM4RL
- RewardDesign
- QualityDiversity
one_liner: 解耦群体规划与奖励生成，实现Agent目标开放式演化，兼具高行为多样性与下游复用效率
practical_value: '- 多目标推荐/广告系统可借鉴双阶段解耦设计：上层Planner基于业务目标多样性、流量覆盖度等指标做目标优先级规划，下层Mutator负责生成具体的loss函数/打分规则，避免多目标优化趋同导致的推荐同质化

  - 构建Agent技能库/用户行为策略库时，可复用交叉适配度矩阵设计，通过策略在多目标下的表现衡量功能多样性，而非仅对比单任务指标，大幅提升下游未知场景的复用效率

  - 面向电商导购/客服Agent的目标迭代中，可采用同款幸存者筛选规则：仅保留性能显著超过随机基线、且在对应目标下表现最优的策略，降低无效迭代的算力开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于LLM的奖励生成方法通常为预定义任务优化目标，且将探索方向决策和奖励生成逻辑耦合，容易导致Agent行为收窄，下游未知任务复用性差；同时手工设计奖励成本高、易存在捷径，偏好奖励模型又容易发生过优化，开放式场景下目标设计本身就是核心瓶颈。

### 方法关键点
- 双阶段解耦架构：将群体级规划（Planner）和奖励代码生成（Mutator）分离，Planner基于交叉适配度矩阵、Specialist Quality（SQ）、Behavioral Diversity（BD）等指标选择父本、生成自然语言变异指令，Mutator负责将指令转化为可执行、可验证的奖励函数
- 交叉适配度矩阵：每个策略在群体所有奖励上做评估，对角线衡量自我掌握度，非对角线衡量迁移性，通过列归一化消除奖励数值尺度差异
- 幸存者筛选规则：只有在对应奖励上性能超过所有其他策略、且显著优于随机策略的奖励-策略对才能保留到下一代，保证保留的都是可学习、有价值的目标

### 关键结果
在离散卡片沙箱、Cart-Pole、Hopper、Cheetah4个环境对比Independent Generation、Direct Mutation两个基线，最终BD达到Direct Mutation的1.8倍、Independent Generation的2.5倍；下游10个未知任务上，10000轮适配的冻结Habitats策略库配对胜率达61.7%，超过20000轮从零训练的专属策略，也优于同规模基线的策略库。

最值得记住的结论：将群体级探索规划和具体奖励生成解耦，是平衡目标优化质量和行为多样性、提升Agent技能库下游复用性的有效路径。
