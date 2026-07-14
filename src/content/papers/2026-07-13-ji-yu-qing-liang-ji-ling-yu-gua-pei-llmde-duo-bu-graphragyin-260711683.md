---
title: 'RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM'
title_zh: 基于轻量级领域适配LLM的多步GraphRAG引擎RAGU
authors:
- Mikhail Komarov
- Ivan Bondarenko
- Stanislav Shtuka
- Oleg Sedukhin
- Roman Shuvalov
- Yana Dementyeva
- Matvey Solovyov
- Nikolay O. Nikitin
affiliations:
- ITMO University
- Novosibirsk State University
- Far Eastern Federal University
- Independent Researcher
arxiv_id: '2607.11683'
url: https://arxiv.org/abs/2607.11683
pdf_url: https://arxiv.org/pdf/2607.11683
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: 检索增强生成 · 生产级GraphRAG优化
tags:
- GraphRAG
- RAG
- LLM
- KnowledgeGraph
- OpenSource
one_liner: 提出7B语言技能优化LLM与多步实体整合的开源生产级GraphRAG引擎
practical_value: '- 可复用多步KG构建流程：实体提取→关系提取（强制匹配已校验实体）→DBSCAN去重→社区检测的pipeline，适配电商商品/用户/评论知识图谱构建，大幅降低KG噪声

  - 成本优化思路：RAG管线内LLM只需优先优化理解/提取/推理等语言技能，无需大参数量世界知识，7B级小模型可达到32B通用模型的KG构建效果，单GPU即可部署，降本效果显著

  - 生产级RAG工程参考：三层可插拔存储（图/KV/向量）、Pydantic校验LLM结构化输出、异步API、Mock LLM支持CI的设计，可直接迁移到业务RAG系统落地

  - 评测避坑：多跳QA/检索类任务结果受回答格式影响极大，评测时需统一输出格式，避免误判不同算法的实际效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有GraphRAG多采用单步实体关系抽取，噪声多、实体重复严重，且普遍依赖大参数API模型成本高，开源框架工程成熟度低，难以直接落地生产。

### 方法关键点
- 多步KG构建管线：拆分实体提取、关系提取两步，关系提取强制匹配已校验实体，新增DBSCAN聚类去重+LLM实体/关系摘要的整合阶段，再用Leiden算法做社区检测生成社区摘要
- 轻量级提取模型Meno-Lite-0.1：7B参数，仅针对RAG所需的上下文理解、实体/关系提取、上下文推理等语言技能优化，不额外增加世界知识参数量，支持128K上下文窗口
- 工程优化：三层可插拔存储抽象，Pydantic校验LLM输出避免代码注入，异步API支持生产流量，单GPU即可部署，支持pip一键安装

### 关键实验
在GraphRAG-Bench医疗数据集上，证据召回最高达0.84，优于HippoRAG 2的≤0.76；创意生成任务Answer Correctness达59.0，超过HippoRAG 2的56.9；KG构建任务谐波均值较Qwen2.5-32B提升12.5%；多跳QA任务统一回答格式后与HippoRAG 2效果基本持平，索引成本仅为API类GraphRAG方案的1%。

### 核心结论
RAG管线内的LLM仅需语言技能而非世界知识，技能随参数量增长的速度远慢于世界知识，7B级小模型即可满足GraphRAG的抽取需求。
