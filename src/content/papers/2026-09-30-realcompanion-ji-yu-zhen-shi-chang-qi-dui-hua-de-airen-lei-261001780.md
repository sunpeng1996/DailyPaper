---
title: 'RealCompanion: Benchmarking Human Understanding from Reasoning over Longitudinal
  Real-World Conversations'
title_zh: RealCompanion：基于真实长期对话的AI人类理解能力评测基准
authors:
- Arman Behnam
- Sunglyoung Kim
- Liangwei Yang
affiliations:
- Quis Lab, USA
- Independent Researcher, USA
arxiv_id: '2610.01780'
url: https://arxiv.org/abs/2610.01780
pdf_url: https://arxiv.org/pdf/2610.01780
published: '2026-09-30'
collected: '2026-10-06'
category: Agent
direction: Agent 个人理解能力评测
tags:
- Long-term Memory
- AI Companion
- Benchmark
- Conversational Agent
- Personalization
one_liner: 发布10组真实用户与AI伴侣的长期对话数据集及评测基准，填补真实场景个人理解评测缺口
practical_value: '- 做长期交互型Agent（如电商导购AI、会员陪伴Agent）时不要过度设计记忆召回：真实场景仅3.4%的用户消息需要回溯历史，高频召回反而带来29%+的误触发率，降低用户体验

  - 记忆召回模块可优先用轻量的最近消息滑窗：全量测试中最近消息滑窗的召回准确率达95.9%，仅在<2%的需要回溯数千条历史的场景才需要BM25或向量检索

  - 给Agent的记忆片段做提示词设计时，避免使用「记忆」这类引导性标签：相同历史消息标为「记忆」比标为「历史对话」会让模型多10~14个百分点的不必要历史引用

  - 可复用本基准的分层评测逻辑：区分用户画像重建、对话回复、问答三个评测轨道，分别测试记忆准确性、召回时机、应用合理性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI伴侣、长期交互Agent的评测基准多使用合成对话、预定义Persona，默认几乎所有对话都需要调用历史记忆，完全不符合真实用户交互规律，无法准确衡量模型对真实用户的理解能力，也无法验证记忆模块的实际业务效果。
### 方法关键点
- 数据集来自10位真实用户与AI伴侣的36~120天交互数据，共27218条消息，全部经用户授权匿名化处理
- 为每个用户配套5类可溯源标注：原始对话、Profile（用户明确表述的事实信息，对应原始证据消息）、Persona（推理得到的用户性格/决策偏好，对应原始证据消息）、对话评测集、问答评测集
- 设计三类评测轨道：重建轨道（测试用户Profile/Persona提取能力）、对话轨道（测试回复的记忆调用合理性）、问答轨道（测试用户相关问题的回答准确性）
### 关键结果
- 真实场景仅3.4%的用户消息需要调用当前会话外的历史记忆，需调用的历史消息中位数距当前消息2157条
- 最近消息滑窗全量召回准确率达95.9%，但远距离历史召回场景仅2.2%；BM25远距离召回准确率为24.8%
- 现有记忆需求检测器在真实对话上AUROC仅0.53，接近随机猜测；历史消息标注为「记忆」会让模型多10~14个百分点的不必要引用
- 三款主流大模型重建用户Persona的F1均为0.69~0.71，召回率0.86+但精准率仅0.56~0.59，普遍脑补用户未表述的特征
### 核心结论
真实交互中记忆调用需求远低于合成基准假设，记忆系统的核心难点不是召回准确率，而是判断什么时候需要调用记忆
