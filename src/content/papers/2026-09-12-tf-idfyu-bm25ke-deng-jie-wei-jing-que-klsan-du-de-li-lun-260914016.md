---
title: TF-IDF and BM25 Are Exact KL Divergences
title_zh: TF-IDF与BM25可等价为精确KL散度的理论证明
authors:
- Ivan Silajev
affiliations:
- Independent Researcher
arxiv_id: '2609.14016'
url: https://arxiv.org/abs/2609.14016
pdf_url: https://arxiv.org/pdf/2609.14016
published: '2026-09-12'
collected: '2026-09-15'
category: RecSys
direction: 搜索相关性 · 基础理论框架
tags:
- TF-IDF
- BM25
- KL Divergence
- Relevance Scoring
- Information Retrieval
one_liner: 证明工业常用的TF-IDF与带+1修正的BM25均可等价为概率模型间的精确KL散度，提供统一理论框架
practical_value: '- 可基于KL散度框架统一校准TF-IDF、BM25与向量检索的相关性得分，解决电商混合检索场景的多源得分融合难问题

  - 业务侧调整BM25超参（k1、b）时，可结合KL散度的概率含义做可解释性调优，避免盲目网格搜索

  - 搭建RAG检索模块时，可复用该理论框架设计自定义词权重规则，适配电商商品标题/详情页的长短文本特殊分布'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
TF-IDF与BM25是工业界应用最广的query-doc相关性打分方法，但始终缺乏统一概率框架下的理论推导，仅能通过实验与其他检索方法对比，无法做理论层面的优劣分析。
### 方法关键点
对生产环境通用的带+1 IDF修正版BM25（如Milvus内置实现）、原始BM25、TF-IDF分别做概率建模，推导三类打分函数与概率分布KL散度的等价关系。
### 关键结果
严格证明了三类打分函数均可精确等价为查询词分布与语料背景分布的KL散度，给出统一理论框架，明确了k1、b等超参的概率含义，填补了两类工业级检索算法的理论空白
