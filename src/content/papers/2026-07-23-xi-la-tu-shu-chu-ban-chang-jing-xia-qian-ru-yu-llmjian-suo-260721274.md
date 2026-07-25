---
title: A Comparative Evaluation of Embeddings and LLMs in a Greek Book Publisher Setting
  - The CUP Dataset
title_zh: 希腊图书出版场景下嵌入与LLM检索效果对比评估及CUP数据集
authors:
- Katerina Papantoniou
- Panagiotis Papadakos
- Theodore Patkos
- Dimitris Garefalakis
- Nikos Vardakis
- Dimitris Plexousakis
affiliations:
- ICS-FORTH
- Crete University Press
arxiv_id: '2607.21274'
url: https://arxiv.org/abs/2607.21274
pdf_url: https://arxiv.org/pdf/2607.21274
published: '2026-07-23'
collected: '2026-07-25'
category: Eval
direction: 低资源语种图书检索方案对比评估
tags:
- Retrieval Benchmark
- Hybrid Retrieval
- Multilingual Embedding
- Low-resource NLP
- LLM for Retrieval
one_liner: 发布希腊图书检索基准CUP，对比多种检索方案，给出不同查询类型的选型参考
practical_value: '- 多语种检索选型可参考：命名实体类查询优先用BM25，自然语言、跨语种、模糊查询优先用稠密/混合检索

  - 商品结构化稀疏内容（如图书目录、商品参数）可先通过LLM做摘要再灌入检索库，提升召回效果

  - 小语种低资源场景优先选型通用多语种嵌入，效果优于小语种专属模型

  - 高优检索场景可采用LLM后置过滤提升初排效果，但需额外权衡算力成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源形态丰富语种（如希腊）缺少垂直领域检索基准，图书搜索场景查询类型跨度大（从短关键词到复杂自然语言），现有检索方案效果无明确参考。

### 方法关键点
构建希腊图书检索基准CUP，包含868条图书目录记录、104条专家标注的分级relevance查询；对比测试4类检索方案：稀疏检索（BM25）、稠密检索（Sentence-Transformers）、混合检索、LLM辅助检索，同时验证字段感知Prompt、LLM目录摘要、LLM后置过滤三类优化手段的效果。

### 关键结果
1. 混合检索整体效果最优，多语种嵌入效果优于希腊专属嵌入模型；2. BM25在命名实体类查询上表现最优，稠密/混合检索在自然语言、噪声、跨语种、概念类查询上效果提升明显；3. LLM目录摘要可提升仅用目录的检索效果，LLM后置过滤可提升初排效果但算力成本极高。
