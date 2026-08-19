---
title: Whether LLMs Can Navigate Beliefs and Facts Depends on How You Phrase It
title_zh: 大语言模型区分信念与事实的能力取决于提问表述方式
authors:
- Quang Minh Nguyen
- Luis Frentzen Salim
affiliations:
- KAIST
- National Taiwan University of Science and Technology
arxiv_id: '2608.17809'
url: https://arxiv.org/abs/2608.17809
pdf_url: https://arxiv.org/pdf/2608.17809
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM信念与事实区分能力研究
tags:
- LLM
- Belief Tracking
- Fact Checking
- Prompt Engineering
- Model Evaluation
one_liner: 揭示LLM对用户信念的识别准确率受信念表达动词的显著影响，归因于任务混淆并给出干预方向
practical_value: '- 设计用户交互类Agent的prompt时，需明确标注当前任务是响应用户信念还是校验事实，避免LLM默认触发事实校验导致答非所问

  - 做用户信念感知的个性化推荐/客服场景时，可针对不同认知强度的用户表述（如“我记得”“我怀疑”）做prompt模板适配，提升任务准确率

  - 若需要LLM优先识别用户意图而非纠偏事实，可在系统prompt中增加单条明确指令即可跨表达类型修复任务混淆问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前用户-facing LLM应用需同时处理用户主观信念与客观事实，此前研究发现LLM普遍存在对错误信息支撑的用户信念识别偏差，但偏差的影响因素与成因未明确。
### 方法关键点
覆盖10款主流LLM，测试18种不同认知动词引导的用户信念表述，定位偏差成因与可行干预方案。
### 关键结果
- 事实与错误信息下的信念识别准确率差跨度极大：对应“我隐约记得”表述时差为+50%，对应“我严重怀疑”表述时差为-14%
- 偏差来源于LLM默认触发事实校验任务，覆盖用户的信念追踪需求；带显式事实校验的CoT在错误信息场景下准确率更低
- 增加单条明确任务指令即可跨动词类型修复该失效问题，解码时抑制错误信念注意力仅能部分恢复部分模型的准确率
