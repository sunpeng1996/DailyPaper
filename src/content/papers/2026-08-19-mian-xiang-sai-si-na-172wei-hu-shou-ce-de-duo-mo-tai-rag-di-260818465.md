---
title: 'Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance
  Manual'
title_zh: 面向赛斯纳172维护手册的多模态RAG 降低技师检索负担
authors:
- Seongjun Ha
- Md Rashedul Islam
- Gaurav Nanda
- Damon Lercel
affiliations:
- Purdue University
- Clemson University
arxiv_id: '2608.18465'
url: https://arxiv.org/abs/2608.18465
pdf_url: https://arxiv.org/pdf/2608.18465
published: '2026-08-19'
collected: '2026-08-20'
category: RAG
direction: 多模态RAG 工业知识库问答检索
tags:
- Multimodal RAG
- Vision-Language Model
- Knowledge Base Retrieval
- Industrial QA
- Recall Metric
one_liner: 针对赛斯纳172维护手册开发多模态RAG pipeline，实现图文内容高效检索与高质量答案生成
practical_value: '- 多模态RAG架构可直接复用在电商商品说明书、售后手册智能问答场景，用户咨询安装、故障问题时同步召回图文内容，提升解答准确率

  - 可复用该工作的多模态RAG落地评估框架：同时验证检索效果、生成质量、推理耗时、单次成本、可解释性五个维度，对齐业务落地要求

  - 用热力图可视化多模态检索匹配点的方案，可迁移到电商内容召回的bad case排查，提升问题定位效率'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
航空维护手册包含大量文本、示意图、规范表格，技师手动检索耗时久，现有维护场景RAG仅支持文本召回，无法覆盖多模态内容的查询需求。
### 方法关键点
针对通用航空广泛使用的赛斯纳172维护手册，开发多模态手册检索器（MMR）实现图文页统一召回，再将召回内容输入视觉语言模型生成答案，同时从推理耗时、运营成本、可解释性三个维度验证落地可行性。
### 关键结果
检索阶段recall@5达93.37%，生成答案与真值语义相似度达87.20%；单查询平均检索耗时11.93s、生成耗时4.95s，单次查询成本0.0091美元，可解释性通过热力图可视化验证。
