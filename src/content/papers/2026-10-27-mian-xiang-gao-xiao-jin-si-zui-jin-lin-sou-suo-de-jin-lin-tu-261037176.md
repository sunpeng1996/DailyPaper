---
title: Lossless Compression of Proximity Graph Indexes for Efficient Approximate Nearest
  Neighbors Search
title_zh: 面向高效近似最近邻搜索的近邻图索引无损压缩方法
authors:
- Francesco Benocci
- Leonard Dahlmann
- Francesco Gargiulo
- Tobias Heuer
- Silvio Martinico
- Franco Maria Nardini
- Cosimo Rulli
- Rossano Venturini
affiliations:
- ISTI-CNR
- eBay Inc.
- University of Pisa
arxiv_id: '2610.37176'
url: https://arxiv.org/abs/2610.37176
pdf_url: https://arxiv.org/pdf/2610.37176
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 向量检索 · HNSW索引无损压缩优化
tags:
- ANN Search
- HNSW
- Graph Compression
- Stream VByte
- Vector Retrieval
one_liner: 通过离线节点重排+SIMD加速的Stream VByte压缩，实现HNSW索引降内存且无延迟损失
practical_value: '- 电商向量检索场景可直接复用该方案：离线用EGB做节点重排+Stream VByte压缩邻接表，eBay生产实测降低44.3%边存储且无查询延迟损失，无需修改现有HNSW检索核心逻辑

  - 工程实现可参考两个优化点：邻接表按列表粒度对齐压缩，解压结果用栈分配缓存避免堆开销；仅在返回最终结果时做ID映射，不影响检索关键路径性能

  - 低维向量、量化向量场景下，图边存储占总索引内存的40%以上，优先落地图压缩的投入产出比远高于继续优化向量压缩'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
HNSW是当前大规模向量检索的主流索引架构，完全内存驻留的特性使其成为电商搜索、推荐召回的核心基础设施。随着向量量化技术的广泛落地，图邻接表的内存占比已经上升到总索引的40%~80%，成为新的内存瓶颈。现有压缩方案要么解压延迟过高无法满足在线检索要求，要么压缩比不足，缺乏可落地的工业级方案。
### 方法关键点
- 离线执行图节点重排：采用EGB（Enhanced Graph Bisection）算法对节点ID重新分配，让拓扑上相邻的节点获得数值接近的ID，大幅降低间隙编码后的序列熵，同时还能提升CPU缓存命中率
- 邻接表压缩：对重排、间隙编码后的邻接表采用Stream VByte压缩，利用其字节对齐、SIMD加速的特性实现无分支快速解压，延迟损失可忽略
- 辅助结构优化：邻接表偏移数组采用Elias-Fano压缩，检索过程全程使用重排后的本地ID，仅在返回最终结果时做ID映射，完全不占用检索关键路径耗时
### 关键结果
在Sift1M、稀疏文本向量CoCondenser、量化密集向量SnowFlake、eBay7M商品向量4个数据集上对比Bitpacker、Elias-Fano、Zeta等主流压缩方案：最高压缩比达52.7%，eBay生产环境实测降低44.3%的HNSW边存储，无任何查询延迟损失，部分场景下延迟甚至降低11%。
> 最值得记住：向量量化成熟后，HNSW图结构压缩的ROI远高于进一步优化向量压缩，且可做到完全无损检索性能
