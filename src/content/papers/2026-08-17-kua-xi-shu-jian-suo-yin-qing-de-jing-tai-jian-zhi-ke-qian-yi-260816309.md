---
title: 'Static Pruning Across Sparse Retrieval Regimes: What Transfers, What Breaks,
  and What Still Helps'
title_zh: 跨稀疏检索引擎的静态剪枝：可迁移性、失效场景与优化收益
authors:
- Zirui Song
- Yuye Zhu
- Yang Yang
affiliations:
- Amazon Web Services
arxiv_id: '2608.16309'
url: https://arxiv.org/abs/2608.16309
pdf_url: https://arxiv.org/pdf/2608.16309
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 稀疏检索 · 静态剪枝跨引擎优化
tags:
- sparse_retrieval
- static_pruning
- inverted_index
- cross_engine_eval
- efficiency_optimization
one_liner: 通过1140组跨引擎实验明确稀疏检索静态剪枝的可迁移性、失效场景与最优组合策略
practical_value: '- 稀疏检索优化优先做索引侧（文档/倒排表）剪枝，优先选α-Mass准则保留前90%权重即可，跨BMP/聚类倒排等主流引擎通用，可降低18-82%索引大小、提升1.2-6.6倍
  latency，NDCG@10损失小于0.005

  - 无需额外做查询侧静态剪枝，现代检索引擎内置的β、query_cut参数已经实现等价效果，额外剪枝无增益，且在短搜索词等稀疏query场景会出现严重效果下降

  - 静态剪枝可与动态剪枝叠加使用，在BMP引擎上组合两者可拿到2.5倍 latency 提升，NDCG@10仅比基线低0.003，适配电商搜索大流量低延迟需求

  - 剪枝停止准则可直接复用：当Recall@10落在85-95%区间时NDCG@10已饱和，用户无感知排名下降，无需追求更高Recall浪费性能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有稀疏检索静态剪枝的结论均基于单一自定义验证管道，无法确定在不同索引结构、内置动态剪枝的现代引擎上是否有效；而SPLADE等稀疏编码器的查询膨胀问题导致检索 latency 大幅高于传统BM25，工业界亟需通用的剪枝优化指导。

### 方法关键点
- 覆盖3类典型检索引擎：自定义C++全量倒排扫描管道、BMP块最大动态剪枝引擎、SEISMIC聚类倒排引擎
- 测试2类剪枝准则：α-Mass（保留权重和占比前α的项）、Max-Ratio（保留权重不小于最高权重τ倍的项）
- 测试3类剪枝方案：查询侧在线剪枝、文档侧离线剪枝、倒排表侧离线剪枝
- 覆盖2种查询密度编码器：高查询密度SPLADE（平均44个查询词）、低查询密度V3-GTE（平均7个查询词）

### 关键结果
在MS MARCO（8.8M段落）、Natural Questions（2.7M段落）、TREC DL 2019/2020深度标注数据集上共完成1140组实验：
1. 索引侧剪枝跨引擎通用：latency 降低1.2-6.6倍，索引大小降低18-82%，NDCG损失<0.005
2. 查询侧剪枝仅在全量扫描管道有效（4-11倍提速），在BMP/SEISMIC上被内置机制完全覆盖，无额外收益
3. 静态+动态剪枝叠加在BMP上可获2.5倍提速，NDCG@10仅比基线低0.003

**最值得记住的一句话**：稀疏检索本质是内存受限负载，所有能降低内存流量的优化（如索引侧剪枝）都具备跨架构通用性，仅降低计算量的优化（如查询侧剪枝）很容易被引擎内置机制替代
