---
title: As We May Search
title_zh: 本地优先信息检索（Local-First IR）框架与规模化可行性验证
authors:
- Saber Zerhoudi
- Adam Roegiest
- Jelena Mitrovic
- Michael Granitzer
affiliations:
- University of Passau
- Zuva
- Interdisciplinary Transformation University Austria
arxiv_id: '2606.29652'
url: https://arxiv.org/abs/2606.29652
pdf_url: https://arxiv.org/pdf/2606.29652
published: '2026-06-28'
collected: '2026-06-30'
category: RAG
direction: 隐私优先端侧RAG架构优化
tags:
- Local-first IR
- On-device RAG
- Privacy-preserving Retrieval
- Dense Retrieval
- BM25
one_liner: 验证消费级硬件端侧隐私无损的检索生成全链路可行性，给出规模化性能边界
practical_value: '- 端侧个性化检索/推荐可复用分层索引策略：先启BM25实现秒级可用，后台异步生成embedding构建HNSW索引逐步切流，平衡用户体验与性能

  - 敏感场景（如用户本地消费记录查询Agent、私域内容推荐）可复用embedding-only对外查询方案，实现0实体泄漏、99.9%检索质量保留的隐私增强

  - 100K doc量级个人/细分场景知识库可完全跑在消费级端侧，nDCG@10>91%、latency<30ms，可直接落地端侧私域推荐、个人消费助手类产品

  - 本地7B SLM做RAG生成质量可接受：对比gpt-4o-mini仅低4个百分点答案包含率，可大幅降本同时避免用户隐私数据上传'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前云原生RAG需要用户上传个人文档、医疗/法律记录等敏感数据到远程服务器，存在严重隐私泄漏风险；现有端侧检索仅支持关键词匹配，规模上限极低，缺乏系统化的设计框架与规模化性能验证，无法满足用户对隐私可控的个人知识库检索需求。
### 方法关键点
- 提出Local-first IR设计框架，从隐私控制、能力、可访问性三个维度划分5类检索架构，核心原则为索引、模型、推理全链路部署在用户设备，远程服务仅作为可选扩展
- 端侧检索采用分层上线策略：先用BM25实现秒级冷启动可用，后台异步生成embedding，优先构建IVF索引快速切换到语义检索，再逐步构建HNSW索引优化精度与延迟
- 对外跨域查询采用embedding-only传输方案，仅向外发送本地计算的query embedding，不泄漏原始查询文本与实体
### 关键实验结果
基于MS MARCO（1K~1M文档子集）、4个BEIR领域基准测试，对比云原生RAG基线：
- 消费级M1笔记本100K文档规模下，稠密检索nDCG@10>91%，单查询延迟<30ms；1M文档规模下HNSW索引仅损失2%精度，延迟低至11ms
- 端侧7B小模型生成答案的包含率仅比gpt-4o-mini低4个百分点，质量差距极小
- embedding-only跨域查询方案实现0 token/实体泄漏，检索质量保留99.9%
### 核心结论
本地优先IR的核心tradeoff是可搜索范围而非检索质量，100K文档量级以内的个人/细分场景知识库完全可在消费级硬件上实现隐私无损、体验不逊于云服务的检索能力
