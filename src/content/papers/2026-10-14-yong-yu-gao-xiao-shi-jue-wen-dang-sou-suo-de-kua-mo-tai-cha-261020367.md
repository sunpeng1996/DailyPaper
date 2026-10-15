---
title: Cascaded Retrieval with Cross-Modal Query Refinement for Efficient Visual Document
  Search
title_zh: 用于高效视觉文档搜索的跨模态查询优化级联检索框架
authors:
- Diana Turmakhan
- Aseem Srivastava
- Vivek Gupta
- Iryna Gurevych
- Thamar Solorio
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Arizona State University
- Ubiquitous Knowledge Processing Lab (UKP Lab)
arxiv_id: '2610.20367'
url: https://arxiv.org/abs/2610.20367
pdf_url: https://arxiv.org/pdf/2610.20367
published: '2026-10-14'
collected: '2026-10-15'
category: RAG
direction: 多模态RAG · 级联检索效率优化
tags:
- Multimodal Retrieval
- Cascaded Retrieval
- Cross-Modal Fusion
- Query Refinement
- Visual Document Search
one_liner: 提出SCOUT双轨级联检索框架，降低视觉文档检索平均延迟28.8倍同时精度优于SOTA
practical_value: '- 级联检索架构可直接复用：粗召阶段用轻量单向量模型过滤全库得到小候选集，仅对候选集执行高精度多向量重排，大幅降低在线latency，适配电商多模态商品检索、内容检索等高QPS场景

  - 离线分层摘要构建思路可迁移：用VLM生成物料的全局+局部描述并索引，补充视觉embedding的语义信号，提升相似商品、冷门商品的召回率，解决纯视觉召回容易漏召的问题

  - 跨模态查询优化（CMQR）可替换现有rank级融合：用语义检索的分数作为软监督调整查询embedding，实现表征级融合，在几乎不增加额外成本的前提下提升排序精度，比RRF效果提升最高14%

  - 候选集大小K可灵活调优：实验验证K=25即可达到接近峰值的性能，可根据业务对精度、延迟的要求动态调整，平衡用户体验和算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前视觉文档检索存在明显痛点：文本OCR检索丢失布局、表格等视觉信息导致精度不足；多向量视觉检索需对全库做逐页匹配，查询延迟随语料规模线性增长，无法落地到大规模企业级多模态RAG、文档搜索场景；同时传统级联检索易因第一阶段漏召损失精度，跨模态rank级融合丢失大量表征信息。

### 方法关键点
- 离线阶段：用VLM生成每个文档的全局摘要+单页面局部摘要，拼接后生成语义embedding，同时生成页面的单向量视觉embedding完成索引，成本可平摊到所有查询
- 在线双轨检索：视觉轨先用轻量单向量模型召回Top-K候选，再用多向量late interaction模型仅对Top-K重排；语义轨直接检索离线摘要索引得到Top-T候选
- 跨模态查询优化（CMQR）：合并双轨候选，用语义检索分数作为软监督优化视觉查询的多向量embedding，再用优化后的查询做最终排序，重排优化复杂度为O(K+T)，与语料规模无关

### 关键实验
在ViDoRe、ViDoSeek、SlideVQA、REAL-MM-RAG共4个基准数据集上，对比ColEmbed-3B-v2等6个SOTA基线，平均查询延迟降低28.8倍（最高80.7倍），NDCG@5平均提升3.1%，最高提升7.8%，抗query扰动能力也显著优于基线。

### 核心结论
多模态检索的效率优化无需牺牲精度，通过离线分层语义索引+级联粗筛+表征级跨模态融合的组合，可在延迟-精度帕累托边界上取得远超现有方案的表现。
