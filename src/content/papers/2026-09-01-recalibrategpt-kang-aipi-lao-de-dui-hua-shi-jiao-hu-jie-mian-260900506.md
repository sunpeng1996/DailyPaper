---
title: 'RecalibrateGPT: AI Fatigue Resilient Conversational Interfaces'
title_zh: RecalibrateGPT：抗AI疲劳的对话式交互界面
authors:
- Nikhil Wani
affiliations:
- OpenThreads AI Research
arxiv_id: '2609.00506'
url: https://arxiv.org/abs/2609.00506
pdf_url: https://arxiv.org/pdf/2609.00506
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 对话交互疲劳优化
tags:
- Conversational AI
- Human-AI Interaction
- LLM Interface
- Cognitive Load
- Usability
one_liner: 提出5种单点击跨轮对话操作符，解决四类对话AI疲劳，将用户认知负载降低一半
practical_value: '- 电商智能客服、导购Agent可直接复用5种跨轮操作符：Anchor拉回用户初始购物意图解决会话漂移、Replay输出已确认需求/待确认点/下一步行动降低信息检索成本、Delta对比两次推荐差异降低决策负担

  - 交互设计可参考三种布局适配不同场景：高频操作配侧边Vertical布局、快速纠错配扇形Arc布局、高负载场景配底部Tablet布局，适配用户不同使用状态

  - 所有操作基于全会话历史+轻量语义匹配（余弦相似度、KL散度、句子Embedding）实现，不需要大模型微调，工程落地成本极低，可快速接入现有对话系统'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM对话界面普遍陷入「输入→阅读→重输」的循环，催生重输、信息扫描、决策瘫痪、上下文漂移四类对话AI疲劳，大幅提升用户认知负载，高风险场景下甚至直接导致任务放弃。现有交互优化方案均仅针对单轮响应设计，未覆盖会话级疲劳痛点。

### 方法关键点
- 定义5种跨轮操作符，分别对应四类疲劳：Anchor修正上下文漂移、Replay输出会话摘要降低扫描成本、Delta对比响应语义差异减少重输、Scope一键聚焦子主题减少重输、Steer生成推荐追问解决决策瘫痪，所有操作均支持单点击触发
- 提供三种操作面板布局适配不同场景：侧边Vertical布局适配高频跨轮操作、扇形Arc布局适配快速微校正、底部Tablet布局适配高认知负载场景
- 底层基于轻量语义能力实现：用句子Embedding的余弦相似度计算意图对齐度、KL散度计算相邻响应语义差异、Embedding聚类提取子主题，无需微调大模型，仅需调用LLM API即可落地

### 关键结果
12名高频LLM用户参与组内对照实验，对比标准聊天界面，RecalibrateGPT的NASA-TLX认知负载得分从5.4降至2.7（下降50%），SUS系统可用性得分达86.5（属于优秀区间），其中Anchor、Replay、Delta三类操作符被评为最实用。

### 最值得记住的结论
AI疲劳很大程度上并非模型质量问题，而是可通过界面优化消除的交互流程成本。
