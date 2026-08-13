---
title: A corpus-specific clinical RAG system matches or outperforms newer frontier
  LLMs on HealthBench
title_zh: 面向特定语料的临床RAG系统在HealthBench上媲美甚至超越前沿大模型
authors:
- Praveen Reddy
- Charuta Mandke
- Suvrankar Datta
- Sarah Khan
- Siddharth Reddy Anthireddy
- Shitij Arora
- Vishal Singh
arxiv_id: '2608.12138'
url: https://arxiv.org/abs/2608.12138
pdf_url: https://arxiv.org/pdf/2608.12138
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: 垂直领域专用RAG性能优化与评估
tags:
- RAG
- Domain-Specific System
- Benchmark
- LLM Evaluation
- Grounding
one_liner: 面向中低收入国家场景的专用临床RAG系统VITA在医学基准上性能媲美前沿通用LLM
practical_value: '- 做垂直领域Agent/问答/导购系统时，优先选择「领域专属语料RAG+轻量基座」方案，比盲目追新通用大模型成本更低、效果更可控，尤其适配电商平台专属规则、地域限售政策、类目规范等强规则场景

  - 垂直系统效果评估时，除了用通用大模型打分，需引入无谱系关联的中立开源大模型做二次校验，避免评估偏差，可直接复用在电商生成式文案、推荐理由、客服回复的效果评测流程中

  - 领域RAG的核心优势是事实准确性与规则匹配度，若要提升用户体验可单独增加通用基座做表达润色，兼顾准确率和友好度，适合电商导购、售后Agent等交互场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
通用前沿LLM被报道在医学基准上优于专用临床AI工具，但现有评估覆盖的专用系统样本少，且未适配中低收入国家等差异化临床场景，结论普适性不足。
### 方法关键点
自研面向印度等LMIC场景的临床RAG系统VITA，检索语料包含专属疾病指南、印度本地耐药数据、国家处方限制、低资源诊疗协议；采用公开HealthBench基准、医师制定的评分规则，分别用GPT-4.1和无谱系关联的开源中立Judge DeepSeek-V4-Pro打分。
### 关键结果
在4023道HealthBench题目上，VITA得分率51.9%，超过GPT-5.4（46.1%）、Gemini 3.1 Pro（42.6%）等前沿通用LLM，45.4%的题目得分最高；500题子集用中立Judge评估时，VITA与最新GPT-5.5平均得分无统计差异，加权得分、获胜题目数领先，仅表达流畅度得分更低
