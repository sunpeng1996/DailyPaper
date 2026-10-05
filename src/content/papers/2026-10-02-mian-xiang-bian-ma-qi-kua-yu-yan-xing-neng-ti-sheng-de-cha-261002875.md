---
title: Query-aware routing for Cross-lingual performance gains in Encoders
title_zh: 面向编码器跨语言性能提升的查询感知路由方法
authors:
- Akshay Jain
- Edward Kim
affiliations:
- ConfidentialMind
arxiv_id: '2610.02875'
url: https://arxiv.org/abs/2610.02875
pdf_url: https://arxiv.org/pdf/2610.02875
published: '2026-10-02'
collected: '2026-10-05'
category: RAG
direction: 跨语言检索 · LoRA 适配器路由
tags:
- LoRA
- Cross-lingual Retrieval
- Dense Retrieval
- RAG
- Adapter Routing
one_liner: 通过查询侧LoRA适配器加语言路由策略，无需重建文档索引即可提升跨语言检索效果且保留单语性能
practical_value: '- 跨境电商多语言搜索场景可直接复用该架构：仅训练查询侧LoRA适配器，无需重新编码全量多语言商品索引，大幅降低存量系统改造成本

  - 可扩展到多场景路由机制：除语言外，可基于query类目、场景标签动态切换不同LoRA适配器，在保留基线效果的前提下实现场景化优化

  - 工程实现成本低：仅需在query编码层增加路由逻辑，单份base模型挂载多个轻量LoRA适配器，无需额外存储多份索引

  - 训练效率优化：训练LoRA时冻结文档编码器，直接复用存量文档embedding做正负样本对比，大幅降低训练算力消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多语言编码器跨语言检索效果远差于同语言场景，若重新微调全模型需要重建整个文档索引，算力和存储成本极高；跨境业务、多语言公共服务等场景急需在不改动原有索引、保留同语言检索效果的前提下提升跨语言召回质量。

### 方法关键点
- 仅在查询编码器侧增加LoRA适配器，文档编码器完全冻结，无需重新编码存量文档
- 设计确定性语言路由策略：当查询语言与索引语言一致时走原编码器路径，不一致时走LoRA适配路径，从机制上保证同语言检索效果完全不变
- 训练时采用对比学习，对齐适配后的查询向量与冻结的文档正样本向量，负样本使用BM25挖掘的同语言hard negative

### 关键实验
- 数据集：金融领域FIQA多语言数据集（英、芬兰、瑞典语），芬兰语全量检索数据集MIRACL-fi、Mr.TyDi-fi
- 对比基线：原Nemotron-3-Embed-1B编码器、不加路由的全量LoRA适配
- 核心结果：6个跨语言方向平均nDCG@10从0.241提升到0.291，相对增益20.9%；所有跨语言方向均有提升，同语言检索效果与基线完全一致；相同架构在harrier-oss-v1-0.6b上也取得约20%的跨语言增益，通用性较强。

### 最值得记住的一句话
通过场景化路由动态切换轻量适配器，是在保留基线系统效果、不改动存量索引的前提下实现场景定制化优化的最低成本方案。
