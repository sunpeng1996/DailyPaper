---
title: 'SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health'
title_zh: SHAKTI：基于证据支撑的营养健康对话AI系统
authors:
- Chaitanya Pallerla
- Dongyi Wang
affiliations:
- University of Arkansas, USA
arxiv_id: '2611.29988'
url: https://arxiv.org/abs/2611.29988
pdf_url: https://arxiv.org/pdf/2611.29988
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: Agent 低幻觉RAG问答优化
tags:
- RAG
- Conversational Agent
- Hallucination Mitigation
- Evidence Verification
- Biomedical QA
one_liner: 面向营养健康场景构建基于全量学术文献的低幻觉可溯源对话RAG系统
practical_value: '- 可复用其零LLM调用的确定性证据校验逻辑：通过正则匹配、原文子串比对、数值范围校验实现引用、引语、数值的自动溯源，可直接迁移到电商商品属性问答、客服Agent场景，低成本降低虚假宣传风险

  - 多轮对话记忆优化trick：除滑动窗口保存最近k轮对话外，额外维护编号化的历史问题列表，可将长会话上下文召回准确率从仅支持3轮无关问题提升到至少16轮，适配客服、导购类长会话需求

  - RAG策略动态路由参考：对答案可信度要求高的场景（如售后、合规咨询）选deep-research RAG，对成本/latency敏感的场景选Corrective
  RAG（context precision达0.98），可按业务需求分配算力

  - 亿级语料检索优化方案：通用+领域专用双稠密检索融合+领域cross-encoder重排，在亿级语料下仍能稳定提升召回效果，可适配电商亿级商品、内容库的检索场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有通用LLM在营养健康问答场景幻觉率高，大量引用不存在的来源、给出错误营养数值，无法满足健康类场景对可信度的强需求；现有垂直领域RAG系统大多语料覆盖有限，仅评估单轮问答准确率，缺乏多轮会话能力、证据可溯源性、成本延迟的综合评估，难以落地到真实对话场景。
### 方法关键点
- 离线构建4.84亿篇OpenAlex学术文献的稠密索引，部署端采用乘积量化压缩为2.3亿摘要索引，同时接入USDA FoodData Central权威食品成分数据库作为结构化数据来源
- 在线推理分6个阶段：会话query重写→食品成分匹配→MiniLM+SPECTER2混合检索+MedCPT重排→来源有效性校验→基于检索结果生成带引用的回答→确定性证据校验（引用合法性、引语原文匹配、数值溯源、语义一致性），输出风险等级标签
- 统一基于Claude Sonnet对比4种RAG策略：single-shot RAG、multi-hop RAG、Corrective RAG、deep-research agent
### 关键结果
在NFCorpus、BioASQ等4个公开数据集共10065个问题上测试，混合检索+MedCPT重排MRR达0.21、MAP@100达0.14；所有RAG策略忠实度0.95-0.96，幻觉率仅0.5-0.8%，Corrective RAG context precision达0.98，deep-research agent的BioASQ问答准确率达73.2%。多轮会话测试中，系统上下文感知得分97.1%，可在16轮无关问题后正确召回首个问题上下文，所有引用链接全部有效，单回答平均成本0.06美元，中位数延迟24s。
### 核心结论
高可信度垂直领域RAG系统不能仅评估答案准确率，需同时覆盖检索、生成、可溯源性、效率、多轮会话能力的综合评估，零模型调用的机械校验可低成本大幅降低幻觉。
