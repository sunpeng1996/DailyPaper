---
title: 'MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval'
title_zh: MIDR：面向多模态文档检索的增强型索引框架
authors:
- Debanjan Mahata
- Atharva Tendle
- Daniel Preotiuc-Pietro
- Yong Zhuang
- Ozan Irsoy
affiliations:
- Bloomberg
arxiv_id: '2609.01316'
url: https://arxiv.org/abs/2609.01316
pdf_url: https://arxiv.org/pdf/2609.01316
published: '2026-09-01'
collected: '2026-09-02'
category: RAG
direction: 多模态检索 · 索引阶段增强
tags:
- Multimodal Retrieval
- Index Augmentation
- BM25F
- MLLM
- Cross-lingual Retrieval
- RAG
one_liner: 将多模态推理移至索引阶段，以文本检索实现媲美视觉检索的效果，索引小9倍延迟低2倍
practical_value: '- 电商/广告多模态物料检索可复用「索引期MLLM增强+查询期文本检索」架构：商品海报、详情页的图表、布局信息在入库阶段转成结构化文本字段，复用现有ES/向量检索栈，无需上线复杂的视觉多向量检索系统，大幅降低查询成本

  - 跨语言搜索场景可落地索引期语言对齐：面向多语言市场的商品/内容搜索，入库时把当地语言的物料信息统一转成目标语言增强字段，上层直接做单语言检索，避免查询期跨语言匹配开销

  - 可复用extract-verify-refine增强流程：生成的索引字段先做一致性校验再入库，降低MLLM幻觉导致的检索错误，尤其适合sku、金融产品等对准确性要求高的场景

  - 资源受限场景可优先用QA-only轻量增强：仅生成页面对应的问答对就能拿到90%以上的全架构收益，大幅降低索引期算力成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有ColPali系列视觉多模态检索需在查询阶段处理页面图像、维护大尺寸多向量索引，查询成本高，难以支撑企业级RAG大规模部署；而纯OCR会丢失表格、图表、布局等关键结构化信息，纯文本检索效果差，成本与效果的矛盾突出。
### 方法关键点
- 训练-free框架，将多模态推理完全前置到索引阶段，查询阶段仅复用成熟文本检索栈，无需处理图像
- 分两级增强：文档级生成全局主题、核心实体等上下文，页面级结合渲染图、OCR文本、文档上下文生成标签、关键短语、图表摘要、粗细粒度QA对等结构化字段
- 采用extract-verify-refine校验流程：生成字段先核对是否与原图/OCR一致，仅修正错误字段，降低MLLM幻觉影响
- 索引层：增强字段与原文本用BM25F做稀疏检索，各字段单独embedding后均值池化做稠密检索，用RRF融合两路结果
### 关键结果
在ViDoRe V3基准测试：
- 5个英文域平均nDCG@10达0.6219，较纯BM25相对提升23%，效果与ColQwen2.5相当，索引体积小9倍，查询延迟低2倍
- 2个法语文档+英文查询的跨语言场景，nDCG@10从纯BM25的0.1532提升至0.5448，超过ColQwen2.5
- 仅保留QA对的轻量配置即可达到0.6200的nDCG@10，接近全配置效果
### 核心结论
多模态理解无需绑定查询阶段，前置到索引期做成本摊销，结合成熟文本检索栈即可在大部分场景下实现效果与部署成本的最优平衡。
