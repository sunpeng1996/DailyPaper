---
title: Retrieval-Augmented Large Language Models as Components of Cognitive Computing
  architecture for Regulatory Knowledge Management
title_zh: RAG增强大语言模型作为监管知识管理认知计算架构组件
authors:
- Dariusz Nowak-Nova
affiliations:
- WSB University, Poland
arxiv_id: '2607.24352'
url: https://arxiv.org/abs/2607.24352
pdf_url: https://arxiv.org/pdf/2607.24352
published: '2026-07-27'
collected: '2026-07-28'
category: RAG
direction: RAG增强本地LLM 领域知识管理落地
tags:
- RAG
- LLM
- On-Premises AI
- Knowledge Management
- Semantic Retrieval
one_liner: 验证消费级硬件部署的RAG增强本地LLM可作为高可靠监管知识管理计算组件
practical_value: '- 电商合规审核、广告规则校验、平台政策解读类场景可直接复用「本地轻量LLM+RAG」架构，消费级硬件即可部署，大幅降低算力成本

  - 易变业务知识库（如平台规则、合规要求、商品参数）的更新可复用RAG层设计，无需重训LLM即可完成知识迭代，缩短上线周期

  - 客服、商家培训类Agent可借鉴该架构实现生成内容的来源溯源，大幅降低幻觉风险，同时满足内容可审计的合规要求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
监管知识管理场景对内容事实准确性、可审计性、知识更新效率要求极高，通用大模型幻觉问题突出，云端部署存在数据泄露风险，现有本地LLM方案依赖高端GPU、知识迭代需重训，落地成本高。
### 方法关键点
设计混合认知架构，在消费级硬件上通过Ollama、LM Studio部署本地开源小参数LLM（Bielik、PLLuM），搭配RAG层：LLM负责语义解析，RAG层实现可控知识检索、上下文注入、信息来源溯源，无需高端GPU加速器。
### 关键结果
RAG增强后，生成内容事实一致性、领域特异性、规范精度显著提升，无依据内容生成风险大幅降低；同时支持知识可审计、监管信息动态更新，无需重训LLM，可直接作为高合规要求场景的语义处理模块
