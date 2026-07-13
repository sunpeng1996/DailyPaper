---
title: 'Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System
  for Generating Investor Briefs'
title_zh: 基于RAG的大语言模型基本面分析增强系统：自动生成投资者简报
authors:
- Bartosz Ziółko
- Kacper Dobrzeniewski
affiliations:
- Faculty of Computer Science, AGH University of Krakow, Poland
arxiv_id: '2607.09121'
url: https://arxiv.org/abs/2607.09121
pdf_url: https://arxiv.org/pdf/2607.09121
published: '2026-07-10'
collected: '2026-07-13'
category: RAG
direction: RAG 垂直领域多源文档摘要生成
tags:
- RAG
- LLM
- Document Summarization
- Vertical Domain Application
- Decision Support
one_liner: 搭建融合多源金融文档的RAG系统，自动生成投资者简报并验证实用性
practical_value: '- 垂直领域RAG落地可参考「领域规则文档+动态更新多源非结构化数据」的召回逻辑，电商场景可叠加平台规则、品类趋势文档提升生成内容合规性与时效性

  - 多源异构文档预处理+API调用商用LLM的轻量架构，可快速复用在电商商家经营简报、用户消费决策参考内容生成等场景，无需全量微调模型

  - 面向C端用户的生成内容验证方法可复用：邀请真实目标用户盲测生成内容实用性，比离线指标更贴合业务实际需求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统公司基本面分析需要人工处理大量非结构化财报、宏观经济数据、监管披露文档，耗时耗力，现有自动化分析工具难以兼顾多源数据整合与行业专业逻辑适配。
### 方法关键点
1. 构建RAG框架，接入三类数据源：公司公开财报、GDP/通胀等宏观经济数据、SEC EDGAR披露的监管文档
2. 预注入基于Kitchin周期的专业投资者知识作为系统基础规则，数据预处理后调用GPT-4o生成投资者简报
3. 连续4周跟踪9家公司的动态数据更新生成简报，邀请9名个人投资者开展实用性评估
### 关键结果
面向个人投资者的用户调研验证了该RAG系统生成的投资简报实用性达标，可有效降低人工基本面分析的信息处理成本
