---
title: 'PatientAct: Theory-Grounded Mental Health Client Simulation'
title_zh: PatientAct：基于临床理论支撑的心理健康来访者模拟框架
authors:
- Sahand Sabour
- TszYam NG
- Yaqian Chen
- Guanqun Bi
- Jialu Zhao
- Minlie Huang
affiliations:
- 清华大学计算机系人工智能研究院CoAI组
- 北京师范大学心理学部
- 清华大学心理咨询与发展指导中心
arxiv_id: '2608.12750'
url: https://arxiv.org/abs/2608.12750
pdf_url: https://arxiv.org/pdf/2608.12750
published: '2026-08-13'
collected: '2026-08-16'
category: Agent
direction: 基于领域理论的智能体行为模拟
tags:
- LLM Simulation
- Agent Behavior Modeling
- Dynamic Memory
- Trust Threshold
- Clinical AI
one_liner: 提出融合临床理论与动态信任阈值记忆的来访者模拟Agent框架，解决现有模拟过于配合的缺陷
practical_value: '- 动态记忆+信任阈值的设计可直接复用在电商客服/导购Agent的用户模拟场景，模拟真实用户对隐私/敏感问题的抗拒行为，提升训练数据真实性

  - 先建模情绪反应、行为决策再生成回复的架构，可迁移到虚拟人/客服Agent的回复生成链路，优化回复拟人化程度

  - 基于领域成熟理论构建智能体画像的方法，可用于电商场景的用户/导购Agent画像设计，避免画像同质化、行为不符合真实逻辑'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有基于LLM的心理咨询来访者模拟器普遍存在过于配合、信息披露无门槛、单次会话就解决核心问题的缺陷，根源是用户画像缺乏因果深度、所有记忆内容无访问权限限制。

### 方法关键点
1. 画像层融合临床通用5Ps病例范式，不绑定特定治疗流派，保证画像的因果逻辑深度；
2. 新增动态记忆层，每个记忆项绑定信任阈值，症状类低敏感信息可早披露，成长记忆等高敏感信息需建立足够信任后才开放访问；
3. 每轮回复前先建模情绪反应与行为决策，触及阈值外的敏感内容时，从信息量、内容、风格三个维度生成多样化抗拒反馈，而非默认配合。

### 关键结果
在40个临床场景测试中，生成的画像临床合理性高，抗拒行为质量与行为真实性相比基线实现大幅提升。
