---
title: 'Know Your Source: A Public Knowledge Store for Media Background Checks'
title_zh: 了解信息来源：面向媒体背景核查的公开知识库
authors:
- Benjamin Nichols
- Michael Schlichtkrull
- Nedjma Ousidhoum
affiliations:
- Cardiff University
arxiv_id: '2607.02383'
url: https://arxiv.org/abs/2607.02383
pdf_url: https://arxiv.org/pdf/2607.02383
published: '2026-07-02'
collected: '2026-07-03'
category: RAG
direction: RAG事实核查 · 来源可信度评估
tags:
- RAG
- Fact Checking
- Knowledge Base
- Source Credibility
- Media Background Check
one_liner: 开源覆盖200家媒体的知识库MEDIAREF，支持低成本可复现的媒体背景核查生成评估
practical_value: '- 构建业务RAG系统时可复用来源可信度评估逻辑，对召回的商品评价、舆情、竞品信息等来源做分层加权，避免虚假评论/黑公关内容干扰输出，提升生成内容准确性

  - 自建领域知识库时可参考MEDIAREF的可复现构建+更新方法论，降低依赖第三方搜索API的成本，提升知识库迭代的可控性

  - 开发高风险场景（如医药/美妆合规宣传、消费维权内容生成）的Agent时，可引入媒体背景核查模块，对引用的外部信息源先做可信性校验，降低合规风险'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有RAG驱动的自动事实核查系统普遍默认检索证据可靠，但现实中公开信息常存在冲突、过时、来源带偏见/不可信等问题；当前媒体背景核查（MBC）技术依赖昂贵的专有搜索API，可复现性极低，难以规模化落地。

### 方法关键点
1. 构建公开知识库MEDIAREF，收录200家媒体来源的网页文档，支持MBC生成任务的低成本评测
2. 配套可复现的知识库构建、更新方法论，完全脱离对商用搜索API的依赖

### 关键结果
经自动指标+定性评估验证，基于MEDIAREF生成的MBC质量显著优于依赖商用搜索API的方案，同时支持各类主流LLM在MBC任务上的可复现性能评测。
