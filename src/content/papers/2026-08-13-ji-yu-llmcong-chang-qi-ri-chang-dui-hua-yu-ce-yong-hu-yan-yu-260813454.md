---
title: 'Before You Say It: Anticipating Verbal Behavior from Longitudinal Everyday
  Conversations with LLMs'
title_zh: 基于LLM从长期日常对话预测用户言语行为
authors:
- Yasith Samaradivakara
- Valdemar Danry
- Paul Liang
- Pattie Maes
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.13454'
url: https://arxiv.org/abs/2608.13454
pdf_url: https://arxiv.org/pdf/2608.13454
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: 主动式Agent · 用户行为预测
tags:
- Proactive Agent
- User Behavior Modeling
- LLM Personalization
- Longitudinal Conversation
- Wearable AI
one_liner: 提出无需训练的情境推理方法，从长时日常对话挖掘可解释模式预测用户言语行为
practical_value: '- 可复用「IF-情境 THEN-行为 BUT NOT-例外」的可解释规则结构，在电商客服Agent、用户购物意图预判场景落地，相比全量长上下文输入，既降低推理token成本，又方便运营介入修正规则，避免黑盒预测出错

  - 做个性化用户建模时，优先用结构化行为模式代替全量历史喂入大模型，在用户复购、犹豫下单、冲动消费等高频固定行为场景下，预测准确率提升显著，且积累的用户行为数据越多效果越好

  - 对于用户明确标记的高价值行为（比如想要克制的冲动消费、想要促进的复购行为），规则匹配的预测效果远好于零样本和全量上下文基线，可用于前置性的消费提醒、权益推送等主动干预场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有AI助手大多为被动响应式，无法基于用户长期行为预判其言语与决策倾向，而提前预判用户行为可在用户偏离预设目标、做出后悔决策（如冲动消费）前及时干预。现有个性化预测方法要么无历史数据支撑、效果差，要么直接将全量长对话历史喂入大模型，易丢失深埋的用户个性化规律，且预测结果不可解释，无法落地真实业务场景。
### 方法关键点
- 数据：采集14名用户7-10天的智能手表日常对话数据，共1000+小时，经去重、去冗余、speaker标注后，清洗保留9901条有效utterance
- 核心框架：无需训练的情境推理方法，从长时对话中挖掘「IF-触发情境 THEN-行为倾向 BUT NOT-例外场景」的可解释行为规则，基于正反样本计算规则置信度；预测时先匹配当前上下文激活高置信度规则，再输入LLM生成行为预测
- 对比基线：零样本（无用户历史）、全量历史上下文输入、自然语言摘要压缩历史三种主流方案
### 关键实验结果
- 情境推理方法的LLM评委综合得分0.597，较零样本基线提升28.9%，较全量上下文基线提升18.9%，且用户数据量越大效果提升越明显
- 在用户主动标记的想要改变的行为子集上，得分达0.858，较零样本提升41.3%，较全量上下文提升38.5%
- 跨用户替换行为规则后得分骤降29.8%，证明挖掘的规则是用户专属的，而非通用行为规律
### 核心结论
用户行为是高度情境依赖的，用结构化的可解释规则捕捉特定情境下的稳定行为模式，比直接投喂全量历史给大模型的预测效果好得多
