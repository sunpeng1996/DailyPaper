---
title: Scaling Laws for Grid-Based Approximate Nearest Neighbor Search in High Dimensions
title_zh: 高维场景下基于网格的近似最近邻搜索的缩放定律
authors:
- Matthew J Liu
- Wei Hang Zheng
- Vidhan Purohit
- Siqi Xie
- Chieh-En Li
- Jerry Li
- Noah Flynn
affiliations:
- University of California, Berkeley
- University of Toronto, St. George
- Independent Researcher
- University of Waterloo
arxiv_id: '2607.01283'
url: https://arxiv.org/abs/2607.01283
pdf_url: https://arxiv.org/pdf/2607.01283
published: '2026-06-30'
collected: '2026-07-04'
category: RecSys
direction: 近似最近邻搜索 · 向量检索优化
tags:
- ANN
- Scaling Law
- Vector Retrieval
- Grid-based Search
- Approximate Nearest Neighbor
one_liner: 量化多探针网格ANN的维度与数据量缩放规律，验证其高维高召回场景的性能优势
practical_value: '- 向量召回/ RAG 向量检索场景如果使用高维embedding（≥128维）且索引重建频率高（如小时级更新商品/用户兴趣向量），可优先评估多探针网格方案，其索引构建速度比HNSW快190倍，总持有成本更低

  - 高召回要求（召回@10≥0.7）的高维检索场景，多探针网格的维度鲁棒性优于图/树/IVF类ANN算法，吞吐量随维度上升的衰减速率比主流方法慢50%以上

  - 可复用论文的「索引成本+查询成本+存储成本」总计算框架量化业务场景下的ANN选型阈值：当重建与查询比低于1:2600~20400时，多探针网格性价比更高

  - 多探针网格的「PCA降维分桶+高维重排」设计可直接复用在现有召回链路的向量粗排阶段，降低高维向量检索的计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有ANN缩放分析普遍忽略基于网格的方法，而高维embedding（大模型语义向量、用户兴趣向量等）在推荐、搜索、RAG场景应用越来越广，主流图/树/IVF类ANN算法在高维下性能衰减严重，且索引重建成本高，亟需明确不同场景下最优ANN方案的选型依据。

### 方法关键点
- 改进多探针网格ANN：先将高维向量通过PCA降维到低维子空间划分为均匀网格，多源BFS预计算空单元格到最近非空单元格的映射
- 查询时将query投影到降维子空间，探测主单元格和n_probe个按墙距离排序的相邻单元格，所有候选返回原生高维空间重排
- 推导QPS与召回率的log线性关系，以及数据集大小N、维度d的缩放幂律模型

### 关键实验
在GloVe（25~200维，1.18M点）、SIFT-128数据集上对比Voyager（HNSW）、PyNNDescent、Annoy、FAISS-IVF四类主流ANN，核心结果：
1. 召回@10=0.8时，多探针网格的d缩放指数仅0.9左右，远低于基线的1.5~1.9，吞吐量随维度上升的衰减慢50%以上
2. 索引构建速度比Voyager快190倍，比FAISS-IVF快24倍
3. 当索引重建与查询的频率比低于1:2600~20400时，总持有成本显著低于所有基线

### 核心结论
ANN选型不能只看单场景QPS，要结合维度、数据量、索引重建频率综合计算总成本，高维高重建频率场景下网格类方法的表现远好于主流认知
