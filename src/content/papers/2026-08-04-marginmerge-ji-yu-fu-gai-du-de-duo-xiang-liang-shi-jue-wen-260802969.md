---
title: 'Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document
  Retrievers'
title_zh: MarginMerge：基于覆盖度的多向量视觉文档检索器压缩方法
authors:
- Ailar Mahdizadeh
- Aria Salari
- Sohail Rajabi
- Shahriar Mirabbasi
- Panos Nasiopoulos
- Alireza Morsali
affiliations:
- University of British Columbia
- Vector Institute
- Global Relay
arxiv_id: '2608.02969'
url: https://arxiv.org/abs/2608.02969
pdf_url: https://arxiv.org/pdf/2608.02969
published: '2026-08-04'
collected: '2026-08-05'
category: RAG
direction: 多模态RAG检索 · 多向量索引压缩
tags:
- Multi-Vector Retrieval
- Index Compression
- MaxSim
- ColPali
- Visual Retrieval
one_liner: 提出覆盖度感知的MarginMerge压缩方法，大幅降低多向量检索索引存储同时保留几乎全部检索效果
practical_value: '- 电商多模态商品检索、知识库RAG等多向量检索场景的索引压缩可复用覆盖度优先思路，放弃单patch重要性排序剪枝，优先保留互补语义区域的代表向量，避免长尾query匹配证据丢失

  - 压缩优化时优先对齐排序margin而非绝对匹配分的思路可直接迁移到推荐/检索业务，相比分数拟合更贴合用户对排序顺序的核心需求，能大幅降低压缩带来的排序翻转

  - MarginMerge离线压缩、在线完全兼容原有MaxSim检索pipeline的设计，适合存量检索系统升级，无需修改在线逻辑，迁移落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
ColPali、ColQwen等多向量视觉文档检索器靠存储细粒度patch embedding实现高精度检索，但单文档需存数百到数千向量，索引体积大、检索延迟高；现有压缩方法多基于单patch重要性剪枝，容易丢失长尾query所需的匹配证据，导致检索效果大幅下降，亟需在不修改在线检索逻辑的前提下实现高倍率、低效果损失的索引压缩。

### 方法关键点
- 核心遵循query相关覆盖度原则：压缩目标是覆盖可能成为不同query最佳匹配的互补文档区域，而非保留单个高重要性patch
- 覆盖度感知锚点选择：基于训练query embedding构造原型库，贪心选择覆盖最多原型方向的patch作为锚点，聚类所有patch
- 轻量共享网络合成每个聚类的代表向量，融合锚点相似度、原型相关性和学习残差计算聚类内权重
- 排序margin蒸馏优化，对齐压缩前后正负样本的得分差而非绝对得分，降低排序翻转

### 关键实验
在ArxivQA、DocVQA等6个数据集，基于ColQwen2.5、ColPali两个backbone测试，对比Light-ColPali、SAP等基线：5%/10%向量保留率下nDCG@5为同配置最优，保留原始索引97%~99%的nDCG@5同时减少90%~95%的存储向量，5%保留率下比几何合并平均降低41%的排序翻转，模型可跨数据集、跨保留率迁移无需重训。

**最值得记住的结论**：多向量检索压缩的核心是覆盖不同query的潜在匹配区域，而非筛选单个最相关的patch，多样性比单样本重要性更重要。
