---
title: 'Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym'
title_zh: 主动式LLM Agent基础：设计原则、技术层与评估测试床Proactivity-Gym
authors:
- Jio Oh
- Seunghyun Do
- Young-Jun Lee
- Steven Euijong Whang
- Dongyeop Kang
affiliations:
- KAIST
- University of Minnesota
arxiv_id: '2609.37267'
url: https://arxiv.org/abs/2609.37267
pdf_url: https://arxiv.org/pdf/2609.37267
published: '2026-09-28'
collected: '2026-10-06'
category: Agent
direction: 主动式Agent 设计框架与评估
tags:
- Proactive Agent
- LLM Agent
- Agent Evaluation
- Trust Modeling
- User Preference
one_liner: 提出主动式LLM Agent的3T设计原则、5维设计空间与多日长周期评估测试床Proactivity-Gym
practical_value: '- 电商/内容类主动助理Agent可直接复用3T框架，做预判推荐、主动售后干预时，同步权衡任务准确性、执行时机、用户信任，避免过度打扰导致用户流失

  - 复用睡眠计算设计思路，在用户非活跃时段（如深夜）批量预处理潜在需求（加购商品降价预警、凑单方案生成），既不占用活跃时段算力也减少打扰

  - Agent效果评估不要仅看任务准确率，需补充时机匹配度、用户信任维度指标，LLM judge易混淆任务能力和信任感知，可补充小流量真人测试校准结果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent大多为响应式，主动式Agent易出现内容无关、时机不当、过度干预等问题，反而降低用户体验；现有研究多仅关注任务完成能力，忽略时间分配与用户信任的联合优化，也缺少长周期动态场景的评估工具。

### 方法关键点
- 提出3T核心设计原则：Task Capability（预判需求并正确完成）、Temporal Allocation（结合资源空闲度与需求时效性分配算力，区分交互时段/睡眠时段）、Trust（匹配用户偏好的干预深度，避免越权操作）
- 定义5维设计空间：任务范围、预判horizon、触发条件、执行时机、干预深度，指导Agent落地
- 开源PROACTIVITY-GYM评估测试床：包含10个多日长周期场景、每个场景3种用户persona、有状态环境模拟，可同时评估3T指标

### 关键实验
测试9种LLM+3种Agent框架共23种配置，最强的Claude Opus 5的TC得分仅65.1，TA得分仅51.7%，TR-D得分仅52.4%；TC与TA、TR-D的相关系数仅0.31、0.34，LLM judge的信任评分与TC相关系数达0.7，明显混淆任务能力与信任；30人真人测试显示，相较于打扰当前工作的正确主动服务，用户对需修正的睡眠时段服务的接受度从26.7%提升到97.8%，单次干预失准会让用户信任下降1.86分，恢复难度远高于损失速度。

### 核心结论
主动式Agent的核心不是「做得多」，而是在对的时间、用对的方式，做用户需要的事
