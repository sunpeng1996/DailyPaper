---
title: 'Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models,
  Evaluation, and Open Challenges'
title_zh: 多轮对话AI从文本到多模态交互：数据、模型、评估与开放挑战
authors:
- Syeda Faiza Ahmed
- Zien Sheikh Ali
- Hunzalah Hassan Bhatti
- Firoj Alam
- Shammur Absar Chowdhury
affiliations:
- Qatar Computing Research Institute
arxiv_id: '2608.17605'
url: https://arxiv.org/abs/2608.17605
pdf_url: https://arxiv.org/pdf/2608.17605
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 多模态多轮对话系统技术综述
tags:
- Multi-turn Dialogue
- Multimodal LLM
- Conversational Agent
- Evaluation Benchmark
- AudioLLM
one_liner: 系统性梳理多模态多轮对话的数据集、建模、训练、评估体系，明确核心开放挑战
practical_value: '- 电商多轮导购Agent训练可直接复用论文梳理的策略：SFT阶段优先选用包含指代消解、话题跳转、用户偏好修正的真实会话数据，RLHF优化维度从单轮回复转为会话级整体满意度，大幅提升长对话连贯性

  - 多模态交互场景（如直播语音/视觉导购）可参考论文盘点的技术瓶颈，优先做跨轮模态接地、历史上下文降噪的专项优化，避免语音、视觉信息随对话轮次增加出现衰减失效

  - 多轮对话效果评估可弃用仅看单轮正确率的方案，复用论文提出的会话级评估框架，新增记忆保留、上下文一致性、工具状态跟踪等维度指标，更贴合真实业务的用户体验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前会话式AI已从单轮文本prompt转向多轮、多模态的持续性交互，用户会在对话中澄清需求、修正偏好、切换话题、引入多模态证据，要求系统保留跨轮上下文，但现有系统普遍存在会话级表现远差于单轮、跨轮记忆丢失、模态接地衰减等问题，且此前的综述多孤立研究文本对话、多模态LLM、Agent等方向，缺乏对多轮会话这一核心分析单元的统一梳理。
### 方法关键点
- 从交互深度、模态复杂度、文化语言多样性三个维度，系统性筛选4000余篇文献后纳入200篇核心工作，覆盖文本对话、AudioLLM、全双工语音系统、多模态/全域模态系统、工具增强Agent五大场景；
- 分类整理各场景下的公开数据集、Benchmark、建模范式、训练策略、评估方法，明确不同技术路线的适用场景与局限；
- 识别出领域四大核心差距：能力差距（长上下文窗口不代表会话级能力）、资源差距（主流数据集以英文文本为主）、评估差距（缺乏统一的会话级评估指标）、集成差距（极少Benchmark同时覆盖多模态、长记忆、工具调用、文化适配）。
### 关键结果数字
- 现有公开多轮对话数据集中80%以上为英文文本，仅8个语音、6个视频导向的多轮数据集，多语言、跨文化多轮资源严重不足；
- 现有53个主流Benchmark中32个为纯文本场景，仅少数覆盖会话级记忆、工具状态跟踪等核心能力。
### 核心结论
多模态支持能力的迭代速度远快于会话级交互连贯性的提升，单轮表现优异的系统无法直接迁移至多轮场景，必须针对跨轮记忆、接地、一致性做专项优化
