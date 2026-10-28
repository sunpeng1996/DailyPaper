---
title: Interpretable Meta-Policies for Neural Decision Making
title_zh: 面向神经决策的可解释元策略框架NEXUS
authors:
- Raban Emunds
- Jannis Blüml
- Quentin Delfosse
- Kristian Kersting
affiliations:
- Technical University Darmstadt, Department of Computer Science
- Hessian Center for Artificial Intelligence (hessian.AI)
- Centre for Cognitive Science, Darmstadt
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2610.37451'
url: https://arxiv.org/abs/2610.37451
pdf_url: https://arxiv.org/pdf/2610.37451
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 可解释Agent · 神经符号分层RL
tags:
- Reinforcement Learning
- Neuro-Symbolic
- Interpretability
- Hierarchical RL
- LLM-assisted Policy
one_liner: 分层RL框架NEXUS结合符号元策略与神经技能，兼顾决策性能、可解释性与鲁棒性
practical_value: '- 分层决策架构可直接复用：上层用可解释规则做粗粒度决策（如推荐场景的召回粗排规则、导购Agent的任务选择），下层用神经模型做细粒度执行（如精排排序、技能落地），同时满足业务可解释性要求与性能指标

  - LLM辅助生成规则与reward的思路可迁移：电商/广告场景可基于业务规则文档，用LLM自动生成召回/粗排规则、分层reward函数，大幅降低人工定义成本，减少规则迭代周期

  - 三种元策略选型建议可直接落地：优先选择纯符号元策略保证可解释性与业务对齐性，歧义多的复杂场景用神经符号混合方案，无需可解释性的场景用纯神经方案

  - 抗reward hacking思路可借鉴：通过分层子目标reward约束神经模型行为，避免推荐/广告场景中模型为了短期点击目标忽略长期用户体验、违规流量套利等捷径行为'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
深度RL策略为黑盒，存在可解释性差、易对齐偏移、reward hacking等问题；直接将神经符号方法应用于低阶动作会出现规则爆炸，现有分层RL方法的技能易纠缠、元策略不透明，无法同时兼顾性能、可解释性与业务对齐性。

### 方法关键点
- 提出分层RL框架NEXUS，参考认知双系统理论设计两层架构：上层符号元策略（对应慢思考）做高维技能选择，下层神经技能（对应快思考）执行低阶动作，通过抽象大幅降低符号规则复杂度
- 提供三种元策略选型：纯神经元策略（性能最优、可解释性弱）、纯符号元策略（完全可解释、需定义规则）、神经符号混合元策略（规则过滤候选技能+Q值选最优，兼顾灵活度与可解释性）
- 支持LLM辅助生成技能定义、元策略规则、各技能专属reward函数，基于对象级表征训练保证技能解耦，元策略与技能支持联合离线训练

### 关键实验结果
在Seaquest、Kangaroo、Crafter三个RL环境测试，对比PQN、PPO、HPQN基线：
1. 可解释性：对比低阶动作层面的符号策略，NEXUS元策略规则数从16条降至2-4条，平均决策路径长度从23.56降至2.5-3，符合人类工作记忆容量
2. 性能：与基线游戏reward持平，任务对齐指标（如Seaquest救援潜水员数、Kangaroo关卡进度）比基线高20%+，有效抑制reward hacking
3. 鲁棒性：环境简化场景下，纯符号/神经符号NEXUS的性能下降比基线低60%以上，部分场景性能不降反升

> 最值得记住的结论：分层抽象是兼顾AI系统性能、可解释性和对齐性的核心路径，将符号推理放在高维决策层、神经执行放在低维动作层是平衡三者的可行方案
