---
title: 'UniK: Universal Knowledge Perception for Digital and Physical AI'
title_zh: UniK：面向数字与物理AI的通用知识感知平台
authors:
- Nirmit Desai
- Kunal Sawarkar
- Aditya Mahakali
- Dongkon Lee
- Kevin Park
- Eric Song
affiliations:
- AIntropy AI
arxiv_id: '2609.23971'
url: https://arxiv.org/abs/2609.23971
pdf_url: https://arxiv.org/pdf/2609.23971
published: '2026-09-21'
collected: '2026-09-23'
category: RAG
direction: 通用多模态RAG · 跨数字/物理AI场景
tags:
- RAG
- Multimodal Retrieval
- Knowledge Perception
- Polymath Retrieval
- Hybrid Search
one_liner: 无任务微调多索引融合RAG架构，70B开源模型性能超大规模闭源LLM
practical_value: '- 电商垂类RAG可直接复用Polymath Retrieval的BM25+稠密+稀疏多索引RRF融合方案，搭配自动实体/同义词/关键短语元数据增强流程，无需域内微调即可提升商品QA、售后知识库、合规检索的准确率，降低大模型调用成本

  - 布局电商/零售实体AI（如拣货机器人、线下导购Agent）时，可复用UniK统一架构，同时支撑数字侧商品/规则知识库检索、物理侧传感器/演示视频训练数据检索，无需搭建两套独立数据系统

  - 所有知识密集型Agent应用可优先优化检索层而非盲目升级大模型，实验验证70B开源模型搭配优质检索的效果远超GPT-5等超大规模闭源模型的记忆输出，兼具成本、隐私、可控性优势'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
数字AI（Agent、企业RAG、聊天机器人）与物理AI（机器人、具身智能、自动驾驶）均面临核心瓶颈：多模态异源知识（文本、视频、分子、传感器数据等）分散在私域语料，现有单路检索架构在大规模语料下精度退化严重，垂类场景泛化差，单纯依赖大模型参数存储知识成本高且时效、准确性无法保障。

### 方法关键点
- 全链路覆盖知识生命周期：从 ingestion、enrichment、indexing、retrieval 到 continuous evaluation，无任务专属微调要求
- Polymath Enrichment：自动抽取多模态数据的元数据增强索引，文本侧提取实体、同义词、关键短语，视频/传感器侧提取动作标签、运动特征、目标检测结果
- Polymath Indexing：同时构建BM25词法索引、稠密向量索引、稀疏向量索引三类异构索引
- Polymath Retrieval：查询路由至多类索引后采用RRF融合排序，无需域内训练即可适配不同场景

### 关键实验
跨5个数字AI领域（医疗文本、化学分子、法律视频、政府公开数据、开放域QA）测试，搭配Llama3.3-70B开源模型：政府公开数据集RAG准确率76%，较GPT-5高29pp；医疗PubMedQA准确率77.9%，无需微调超过所有非微调基线，较GPT-3.5+RAG高6.3pp；化学MolInstruct任务EM为64.5%，较GPT-4o高11.3pp；法律视频检索与GPT-4.1打平，模型参数量仅为后者约1/20。

### 核心结论
对于知识密集型任务，检索层质量的影响远大于模型规模，在垂类场景投入优化知识感知基础设施的ROI远高于追逐更大参数的模型。
