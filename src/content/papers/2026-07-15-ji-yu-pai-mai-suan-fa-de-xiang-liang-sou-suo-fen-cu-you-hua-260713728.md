---
title: Cluster with Auctions for Vector Search
title_zh: 基于拍卖算法的向量搜索分簇优化方法
authors:
- Swann Bessa
- Pierre Fernandez
- Gergely Szilvasy
- Matthijs Douze
- Hervé Jégou
affiliations:
- Meta FAIR
arxiv_id: '2607.13728'
url: https://arxiv.org/abs/2607.13728
pdf_url: https://arxiv.org/pdf/2607.13728
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 向量检索 · 分簇索引性能优化
tags:
- Vector Search
- Approximate Nearest Neighbor
- Auction Algorithm
- Clustering
- Neural Probing
one_liner: 联合优化平衡向量库分簇与查询感知神经探测函数，大幅提升OOD场景向量搜索吞吐量
practical_value: '- 电商跨模态搜索、新品冷启动等查询与向量库分布不一致的OOD场景，可复用CwA的分簇与探测函数解耦设计，面向真实查询分布优化，同等召回下最高可提升4.7倍吞吐量

  - 线上业务向量索引的分簇平衡问题可采用拍卖算法实现，天然支持GPU并行，严格控制分簇大小上限，避免长尾查询延迟过高

  - 100M+级超大规模向量库场景可落地CwA-Prod的笛卡尔积分簇设计，参数规模从O(d|C|)降至O(d√|C|)，大幅降低内存与计算开销

  - 训练数据不足时可借鉴k''>k的宽邻居监督策略平滑信号，索引规模扩大100倍仅需增加4倍训练数据，数据效率适配大库落地需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有分簇式向量检索方法通常用同一函数完成向量库分簇和查询探测，当查询与向量库分布不一致（OOD，比如文本搜图、用户长尾查询）时性能骤降；同时分簇大小不平衡会导致查询延迟波动大，现有联合优化方案因分簇与探测函数耦合，设计空间受限，无法适配查询分布优化需求。

### 方法关键点
- 采用交替优化框架：固定分簇结果时，用查询的真实近邻分布作为监督训练神经探测函数，优化交叉熵损失；固定探测函数时，将分簇转化为带容量约束的线性分配问题，用GPU并行的拍卖算法求解，天然保证分簇大小平衡。
- 扩展CwA-HNSW适配万级以上分簇场景：将输出层重参数化为L2距离形式，接入HNSW索引加速top-m分簇查询，降低探测开销。
- 扩展CwA-Prod适配超大规模向量库：用两个小码本的笛卡尔积构造大码本，参数规模降低一个数量级，支持100M级向量库的细粒度分簇。

### 关键结果
1M向量OOD场景下，同等Recall@10=0.8时，CwA吞吐量最高达K-Means的4.7倍，线性版本CwA即可超过参数更多的深度基线；10M向量场景下CwA-HNSW吞吐量达IVF-HNSW的1.6~5倍；100M向量OOD场景下CwA-Prod吞吐量超基线10倍以上，分簇大小接近完全均衡。

最值得记住的一句话：向量检索索引优化必须面向真实查询分布，分簇与探测函数解耦+联合优化可带来数量级的性能提升，尤其OOD场景收益更显著
