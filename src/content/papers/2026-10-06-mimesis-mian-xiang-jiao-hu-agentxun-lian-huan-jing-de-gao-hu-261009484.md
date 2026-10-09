---
title: 'MIMESIS: Learning User Simulators as Training Environments for Interactive
  Agents'
title_zh: MIMESIS：面向交互Agent训练环境的高保真用户模拟器学习框架
authors:
- Hoang Phan
- Dat Huynh
- Andrey Zhmoginov
- Qi Zeng
- Wancen Mu
- Yue Cao
- Shengjie Bi
- Yun He
- Changdae Oh
- Deren Lei
affiliations:
- Meta Superintelligence Labs
- New York University
- University of Wisconsin - Madison
arxiv_id: '2610.09484'
url: https://arxiv.org/abs/2610.09484
pdf_url: https://arxiv.org/pdf/2610.09484
published: '2026-10-06'
collected: '2026-10-09'
category: Agent
direction: 交互Agent训练 · 高保真用户模拟器
tags:
- UserSimulator
- InteractiveAgent
- ReinforcementLearning
- MultiTurnDialogue
- Distillation
one_liner: 基于真实对话训练的高保真用户模拟器，配套自蒸馏方法提升交互Agent泛化性能
practical_value: '- 电商导购/客服对话Agent训练可复用该用户模拟器构建思路：基于真实业务对话数据微调，内置13种真实用户行为模式（如需求模糊、临时改诉求、不耐烦等），替代部分真实用户交互降本，同时避免通用LLM模拟用户过于配合导致的Agent泛化差问题

  - CSD自蒸馏方法可直接迁移到多轮交互Agent训练流程：用模拟用户的隐式思考+后续回复生成 coaching 信号，补充稀疏任务奖励的不足，提供稠密token级监督，训练效率更高且部署时无额外输入开销

  - 交互Agent评估时不要直接用通用LLM当模拟用户，其交互难度和真实用户偏差可达20个百分点以上，会导致评估结果失真，建议用经过真实行为校准的专用用户模拟器'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前交互Agent（客服、导购、工具Agent等）的训练与评估高度依赖真实用户多轮交互，但真实交互采集成本高、难规模化；通用LLM角色扮演的用户过于合作、行为同质化，和真实用户偏差极大，会导致训练出的Agent在真实场景表现严重失真，任务成功率偏差可达20个百分点以上。

### 方法关键点
1. 两阶段训练框架：先训高保真用户模拟器，再用冻结的模拟器作为环境训练交互Agent
2. MIMESIS模拟器训练：基于21.2M真实人机对话做用户侧中训练，学习从用户视角生成回复；引入ThoughtTrace标注数据，监督用户回复前的隐式推理轨迹，避免仅模仿表层话术；从真实交互中提炼13种典型用户行为模式（隐藏评估标准、临时改需求、不配合澄清、不耐烦等），用多域RL联合训练让模拟器自然输出符合场景的真实行为
3. Agent训练优化：基于GRPO做多轮强化学习；提出CSD自蒸馏方法，将模拟器生成的隐式思考+下一轮用户回复转换为 coaching 笔记，提供稠密token级监督，补充稀疏任务奖励的不足，部署时Agent无需访问额外信息

### 关键结果
MIMESIS-9B SOUL-Index达65.7，超过Claude-Opus-5（64.9）；RealUserSim上行为保真度94.0，比Claude-Opus-5高13.4个百分点；SimulatorArena上Turing距离38.7，比Claude-Opus-5低3.6个点。用MIMESIS训练的Agent在9个未见过的用户模拟器上平均得分29.54，比用GPT-5.5训练的高3.44分，加CSD后进一步提升到31.09。

### 核心结论
用户模拟器的核心价值不止是表层对话自然，更要还原真实用户的交互难度，才能训练出泛化到真实场景的Agent
