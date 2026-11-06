---
title: Probabilistic Relevance Decisions for Semantic Retrieval
title_zh: 语义检索场景下概率相关性决策方案的实证对比
authors:
- Bahadır Tatar
- Cevat Şener
affiliations:
- Recruspace LLC
- Middle East Technical University
arxiv_id: '2611.08014'
url: https://arxiv.org/abs/2611.08014
pdf_url: https://arxiv.org/pdf/2611.08014
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 语义检索 · 概率相关性重排
tags:
- Dense Retrieval
- Reranking
- Relevance Scoring
- BEIR
- API Evaluation
one_liner: 在SciFact基准上实证对比稠密检索与两类概率相关性API的重排效果、成本与延迟
practical_value: '- 电商搜索/商品推荐的重排阶段可引入概率相关性决策API，在SciFact场景下nDCG@10相对BGE-M3稠密检索可提升17.6%~21.7%，可快速拿到效果收益；

  - 重排候选集深度不要盲目扩容，实验中从Top50扩容到Top100，API成本翻倍但效果提升不显著（95%置信区间含0），业务中可优先测试Top50/Top30的深度，平衡效果与成本；

  - 若使用OpenAI这类返回大量0分的相关性API，需新增同分排序策略（如随机/业务规则排序），避免同分导致的指标波动，实验中OpenAI同分情况下nDCG@10波动可达1个百分点以上；

  - 可复用历史相关性判定缓存，实验中缓存复用可降低Top100扩容的增量成本约50%，业务中相同query/物品对的判定结果可长期缓存减少API调用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前稠密语义检索依赖向量相似度打分，无法精准捕捉query与文档的细粒度相关性，而基于大模型的概率相关性决策API可实现query依赖的精细化打分，但业界缺乏对这类方案的效果、成本、延迟的系统性对比，难以指导业务落地选型。

### 方法关键点
- 数据集采用BEIR SciFact基准，含5183篇文档、300个测试查询、339个正例标注；
- 基线采用BGE-M3稠密检索，仅使用其稠密向量的余弦相似度打分；
- 对比两种API方案：Jev Noul接口、OpenAI Decisions Predicate接口，均独立返回query-文档对的相关性概率，按概率重排稠密检索召回的候选集；
- 新增候选集深度对比（Top50 vs Top100）、同分敏感性分析、成本延迟测算多维度评估。

### 关键结果
- 受控正例富集池场景下，Jev的Recall@5达0.993、nDCG@10达0.979，均优于OpenAI的0.96、0.946和BGE-M3的0.93、0.899；
- 全语料Top50重排场景下，Jev的nDCG@10达0.780，相对BGE-M3的0.641提升21.7%，OpenAI的nDCG@10为0.754，相对提升17.6%；
- 候选集从Top50扩容到Top100，API成本翻倍，两类方案的效果提升均不显著（95%置信区间含0）；
- 成本方面Jev单query成本约0.0015美元，仅为OpenAI的55%，延迟也低30%左右。

最值得记住的一句话：概率相关性决策API可作为稠密检索的有效补充，但选型需同时权衡效果、分数行为、运营延迟与成本，不要盲目扩大重排候选深度。
