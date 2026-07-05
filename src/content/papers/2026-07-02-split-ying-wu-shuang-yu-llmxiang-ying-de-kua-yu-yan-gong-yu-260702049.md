---
title: 'SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian
  LLM Responses'
title_zh: SPLIT：英乌双语LLM响应的跨语言共情与文化适配基准
authors:
- Anna Chorna
arxiv_id: '2607.02049'
url: https://arxiv.org/abs/2607.02049
pdf_url: https://arxiv.org/pdf/2607.02049
published: '2026-07-02'
collected: '2026-07-05'
category: Eval
direction: 跨语言LLM · 共情评测基准
tags:
- Cross-lingual LLM
- Empathy Evaluation
- Cultural Grounding
- Benchmark
- LLM-as-jury
one_liner: 发布含500条prompt的英乌双语危机场景共情评测基准SPLIT，验证跨语言LLM共情性能差异与AI评审局限
practical_value: '- 做跨区域多语种情感化客服Agent时，不能仅验证语言生成正确性，需补充目标区域文化适配、情绪适配的专项评测项，避免语法正确但不符合当地情绪文化的回复

  - 采用LLM-as-jury做自动评测时，共情、文化适配这类主观维度不可完全信任AI结果，必须搭配一定比例人工标注校准

  - 低资源语言的LLM应用落地可优先测试DeepSeek系列模型，其跨语言稳定性优于Gemini、LLaMA系列同规格模型，可降低小语种场景性能衰减'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM已广泛应用于情感支持、危机响应场景，但低中资源语种的危机场景共情能力、文化适配性缺乏专项评测，现有多语言基准未覆盖该垂直场景需求。
### 方法关键点
构建SPLIT评测基准，覆盖压力、恐慌、孤独、境内流离、紧张5类危机场景共500条英乌双语prompt，从共情准确率、语言自然度、上下文与文化适配三个维度评测LLM性能，同时验证LLM-as-jury评审范式的可靠性。
### 关键结果数字
- Gemini-2.5-Flash、LLaMA-3.3-70B-Instruct切换到乌克兰语时性能显著衰减，DeepSeek-V3表现相对稳定
- 人类与AI评审在共情、自然度维度一致性较弱，在文化适配维度判断完全偏离
- 乌克兰语文本生成能力不等同于乌克兰语情感支持能力
