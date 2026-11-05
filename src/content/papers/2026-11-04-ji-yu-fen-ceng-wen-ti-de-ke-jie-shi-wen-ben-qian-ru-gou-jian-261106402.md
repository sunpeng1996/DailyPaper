---
title: Interpretable Text Embeddings Based on Hierarchical Questions
title_zh: 基于分层问题的可解释文本嵌入构建方法
authors:
- Kohei Oda
- Po-Min Chuang
- Kiyoaki Shirai
- Natthawut Kertkeidkachorn
affiliations:
- Japan Advanced Institute of Science and Technology
- Independent Researcher
arxiv_id: '2611.06402'
url: https://arxiv.org/abs/2611.06402
pdf_url: https://arxiv.org/pdf/2611.06402
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: 可解释文本嵌入 · 问答式向量构建
tags:
- Text Embedding
- Interpretability
- Hierarchical QA
- Contrastive Prompting
- Clustering
one_liner: 通过递归聚类等方法构建分层问答式文本嵌入，降低可解释性所需人工核验成本且维持性能
practical_value: '- 电商搜索/推荐语义召回场景可复用分层思路：粗粒度问题快速筛选候选，细粒度问题做精排，兼顾效率与可解释性

  - 可直接复用「递归聚类+对比提示+问题对齐」流程，为商品、用户评论等垂直领域构建自定义可解释嵌入，降低人工标注成本

  - 低算力/端侧部署场景优先使用浅层级粗粒度问题构建嵌入，同等问题数量下性能优于细粒度问题，可大幅压缩计算开销'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于QA的可解释文本嵌入需人工核验大量问题，且问题数量与粒度的匹配关系缺乏研究，难以平衡可解释性、性能与人工成本。
### 方法关键点
1. 采用递归聚类、对比提示、问题对齐三步构建分层问题体系，层级越深问题越具体、数量越多；
2. 可解释性核验阶段用浅层级对齐问题替代深层问题，大幅减少人工需要核验的问题数量。
### 关键结果
通用NLP任务上维持原有嵌入性能的同时显著提升可解释性；同等问题数量下，有限问题配额时浅层级粗粒度问题的任务表现优于深层细粒度问题。
