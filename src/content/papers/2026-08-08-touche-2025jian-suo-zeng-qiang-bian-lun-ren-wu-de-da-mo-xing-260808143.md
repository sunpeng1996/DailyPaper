---
title: 'DS@GT ARC at Touché: Large Language Models for Retrieval-Augmented Debate'
title_zh: Touché 2025检索增强辩论任务的大模型实现与评估分析
authors:
- Anthony Miyaguchi
- Conor Johnston
affiliations:
- Georgia Institute of Technology
arxiv_id: '2608.08143'
url: https://arxiv.org/abs/2608.08143
pdf_url: https://arxiv.org/pdf/2608.08143
published: '2026-08-08'
collected: '2026-08-11'
category: RAG
direction: 检索增强生成 · LLM自动评估
tags:
- RAG
- LLM
- Automatic Evaluation
- Conversational AI
- Prompt Engineering
one_liner: 基于RAG+多LLM pipeline完成辩论生成与评估，验证同模型族评估共识与官方指标相关性低
practical_value: '- 商品种草文案、客服对话等内容生成场景可复用多LLM+RAG的pipeline，通过多模型结果投票提升生成质量

  - 做LLM自动评估时，不要直接复用同模型族的共识评分作为业务指标，需提前和人工标注结果做相关性校准，尤其是内容真实性（Quality维度）相关的评估项

  - 多厂商LLM统一接入的架构可快速支撑业务/竞赛任务迭代，开源代码可直接参考搭建RAG链路和prompt工程框架'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
Touché 2025检索增强辩论任务包含两个核心子任务：基于当前辩论上下文生成下一轮发言、基于Gricean四准则（数量、质量、相关性、表达方式）评估辩论响应质量，需同时实现高性能生成链路，以及验证多LLM自动评估的可靠性。
### 方法关键点
基于ClaimRev论证语料构建RAG检索链路，接入3家厂商的6款前沿LLM，通过统一的检索增强prompt pipeline完成辩论生成任务；同时测试多LLM作为评估器的组内一致性，与官方人工/规则评估结果做相关性分析。
### 关键结果
前沿LLM搭配RAG在辩论生成任务上表现优异；同模型族LLM作为评估器时内部一致性高，但该共识与官方评估目标的相关性极低，其中内容真实性（Quality）准则维度的差距最大。
