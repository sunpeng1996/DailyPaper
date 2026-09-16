---
title: Pre-retrieval Query Clustering for Adaptive Top-k Document Retrieval in RAG
  Systems
title_zh: 面向RAG系统自适应Top-k检索的预检索查询聚类方法
authors:
- Ye Xia
- Emre Yamangil
- Haixun Wang
affiliations:
- Portland State University
- EvenUp
arxiv_id: '2609.13489'
url: https://arxiv.org/abs/2609.13489
pdf_url: https://arxiv.org/pdf/2609.13489
published: '2026-09-11'
collected: '2026-09-16'
category: RAG
direction: RAG优化 · 自适应Top-k检索
tags:
- RAG
- Query Clustering
- Adaptive Top-k
- Retrieval Optimization
- Query Performance Prediction
one_liner: 通过预检索查询聚类实现RAG自适应Top-k检索，兼顾效果提升与成本优化
practical_value: '- 电商RAG客服、商品问答、Agent垂域场景可直接复用框架：离线对历史query聚类+NDCG测算每个簇最优召回量，线上O(1)匹配，对比静态Top-k可同时降本提效

  - 语义聚类可复用配置技巧：UMAP降维后先用HDBSCAN识别天然簇数，再初始化K-means分配全量query，平衡簇语义一致性与覆盖率

  - 可搭建混合检索优化架构：预检索用本方法给出初始k值，后检索搭配CAR类截断逻辑进一步剪去冗余文档，双重降低token成本与latency

  - 可复用query复杂度双信号判断逻辑：先用「所有、全部、清单」等词法规则命中20%左右的高复杂度query直接拉满召回，剩余走聚类匹配，ROI极高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统普遍采用固定Top-k检索策略，简单query易过检索引入噪声、抬高token成本，复杂query易召回不足导致答案错误；后检索自适应方法需要先拉取大候选池，检索成本高、latency不可控，而垂域场景下query分布稳定，有条件提前预判查询复杂度。

### 方法关键点
- 离线阶段：对历史query做Embedding后用UMAP降维，结合HDBSCAN与K-means做语义聚类；对每个簇的抽样query做不同k值下的NDCG计算，取NDCG增益低于阈值的拐点作为单query最优k*，用均值加2倍标准差（覆盖95%场景）作为簇级推荐k，存入查询簇数据库。
- 在线阶段：先做词法规则匹配，命中范围标识的query直接用最大k；否则做Embedding后匹配最近簇，取对应k值执行检索，整体额外开销低于10ms。

### 关键实验
基于2万条法律领域历史query（清洗后6820条），对比静态k=50的生产基线，线上A/B测试整体F1提升36.64%，低复杂度簇token消耗降低14%（最高23%）无精度损失，高复杂度簇证据覆盖率提升17%。

### 最值得记住的一句话
垂域RAG系统的检索深度需求可以通过历史query语义聚类提前预判，预检索自适应是比后检索截断ROI更高的优化方向。
