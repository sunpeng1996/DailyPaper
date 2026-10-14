---
title: AiSAQ-in-Filtering for DRAM-free Filtered Information Retrieval
title_zh: 无DRAM依赖的过滤式向量检索方案AiSAQ-in-Filtering
authors:
- Kento Tatsuno
- Daisuke Miyashita
- Kazunari Sumiyoshi
- Hiroaki Yamanaka
- Kosuke Nakata
- Jun Deguchi
affiliations:
- Kioxia Corporation
arxiv_id: '2610.17627'
url: https://arxiv.org/abs/2610.17627
pdf_url: https://arxiv.org/pdf/2610.17627
published: '2026-10-13'
collected: '2026-10-14'
category: RecSys
direction: 过滤式向量检索 · 乘积量化优化
tags:
- ANNS
- Product Quantization
- Filtered Search
- DRAM Optimization
- Vector Retrieval
one_liner: 标签包含式乘积量化LiPQ实现无DRAM依赖的高性能过滤式近似最近邻检索
practical_value: '- 可复用LiPQ量化思路，将商品类目、属性等标签与商品向量合并编码，无需额外分配DRAM存储标签，大幅降低大规模向量检索引擎的内存成本

  - 针对电商标签普遍服从Zipf分布的场景，该方案单标签检索recall@1较Filtered-DiskANN最高提升55%，且磁盘IO更低，可直接落地到商品召回、广告检索链路

  - 无DRAM依赖的设计将索引加载时间缩短两个数量级以上，适合多类目分索引、多租户等需要频繁切换索引的业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模过滤式向量检索是电商商品召回、广告检索、RAG知识库检索的核心底层能力，现有主流方案如Filtered-DiskANN需要在DRAM中存储压缩向量和标签数据，内存开销随数据集规模线性增长，且多索引切换时加载成本极高，无法满足超大规模多标签检索场景的成本与性能要求。

### 方法关键点
1. 标签包含式乘积量化（LiPQ）：将稠密向量与稀疏标签向量按相同子段拆分后配对，采用融合距离（向量距离+标签距离加权）做聚类量化，编码后向量大小与纯向量PQ完全一致，无需额外存储空间存储标签。
2. AiSAQ-in-Filtering架构：所有索引数据（PQ向量、图结构、全精度向量）全部存储在SSD，仅需极少量DRAM即可运行，完整保留了AiSAQ零DRAM依赖、索引切换速度快的核心优势。

### 关键实验结果
在SIFT1M、KILT E5 1M数据集上对比基线Filtered-DiskANN：Zipf分布标签下单标签检索recall@1最高提升55%，磁盘IO更低；DRAM开销最高降至基线的1/78，索引加载时间从近16分钟降至10ms级，仅为基线的万分之一。

### 核心结论
对于标签服从Zipf分布的工业级检索场景，将标签与向量合并量化可在不增加存储开销的前提下，同时实现内存成本的大幅降低和检索性能的提升。
