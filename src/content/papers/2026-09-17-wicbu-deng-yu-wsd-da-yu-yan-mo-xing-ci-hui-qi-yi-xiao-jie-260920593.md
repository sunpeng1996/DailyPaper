---
title: 'WiC is Not WSD: A Study on LLMs and Lexical Ambiguity Resolution'
title_zh: WiC不等于WSD：大语言模型词汇歧义消解研究
authors:
- Yi Zhou
- Kiamehr Rezaee
- Danushka Bollegala
- Mohammad Taher Pilehvar
- Jose Camacho-Collados
affiliations:
- Cardiff University
- University of Liverpool
- Amazon
arxiv_id: '2609.20593'
url: https://arxiv.org/abs/2609.20593
pdf_url: https://arxiv.org/pdf/2609.20593
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 大语言模型 · 词汇歧义消解
tags:
- LLM
- WiC
- WSD
- Lexical Ambiguity
- Semantic Evaluation
one_liner: 揭示LLM在WiC任务表现差的核心原因是义项粒度缺失 加入候选义项可显著提升任务表现
practical_value: '- 做搜索Query改写、用户意图识别时，可给LLM提供预定义的业务义项候选集，降低因义项粒度不一致导致的意图判断错误

  - 评估LLM语义理解能力时，需先对齐评估标注的义项粒度边界，避免误判LLM实际性能

  - 电商商品标题/评论语义理解场景，可引入显式义项标注约束，减少LLM过度细粒度区分导致的分类误差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
WiC（上下文词汇匹配）任务长期是LLM的性能短板，过往普遍将误差归因于LLM词汇理解能力不足，未深入挖掘底层原因，且WiC与传统WSD任务的性能差异一直缺乏对齐评测支撑。

### 方法关键点
在统一实验设置下对开源LLM的WiC、WSD任务表现做横向对比，验证显式义项候选集对WiC性能的增益效果，结合人工标注拆解WiC误差的具体来源。

### 关键结果
- 给WiC任务补充类似WSD的预定义候选义项后，所有实验设置下LLM的WiC性能均有明显提升，显式义项信息可让模型判断一致性、针对性显著增强
- 人工评估显示，多数WiC表观误差来自标签歧义、模型与标注者的义项边界不匹配，而非LLM词汇理解能力失效
- LLM普遍存在过度细化义项区分的问题，是WiC任务的核心误差来源之一
