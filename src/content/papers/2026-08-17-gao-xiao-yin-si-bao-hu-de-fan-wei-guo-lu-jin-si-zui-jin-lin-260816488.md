---
title: Efficient Privacy-Preserving Range Filtered Approximate Nearest Neighbor Search
title_zh: 高效隐私保护的范围过滤近似最近邻搜索方案
authors:
- Haoyu Wang
- Yandi Zhang
- Jiadong Xie
- Yingfan Liu
- Hui Li
- Jeffrey Xu Yu
- Jiangtao Cui
affiliations:
- Xidian University
- The Chinese University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- Xi’an University of Posts and Telecommunications
arxiv_id: '2608.16488'
url: https://arxiv.org/abs/2608.16488
pdf_url: https://arxiv.org/pdf/2608.16488
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG · 加密向量库范围检索
tags:
- Privacy-Preserving
- RFANNS
- HNSW
- Vector Database
- Encrypted Search
one_liner: 提出N叉树+HNSW混合索引的隐私保护RFANNS方案，性能较现有安全基线提升2个数量级以上
practical_value: '- 电商/广告隐私合规场景可复用「本地属性范围映射+云端分块向量索引检索」架构，避免明文传输用户价格、年龄等筛选条件，满足数据出境、云服务隐私合规要求

  - 可直接复用DCPE粗筛+DCE精排的两级加密检索pipeline，在损失极小精度的前提下大幅降低加密向量检索算力开销，适配端云协同的隐私检索场景

  - N叉树预拆分属性区间构建HNSW子索引的方法可迁移到明文多条件过滤检索场景，提前按价格、销量等属性预拆分向量索引，降低检索时的过滤开销，提升QPS'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
范围过滤近似最近邻搜索（RFANNS）是向量数据库核心原语，可支撑电商带价格范围的同款检索、多媒体带时间范围的内容检索等场景，但现有方案要求向量、属性、查询明文存储，不适用于外包云部署的诚实但好奇服务器场景；现有隐私保护ANNS方案不支持范围过滤，简单适配的安全方案存在计算开销极高、性能随查询选择性波动大的痛点。
### 方法关键点
- 混合索引架构：用户侧本地维护属性N叉树，云端为每个树节点存储对应区间的加密向量HNSW子索引，查询时用户本地将范围映射为匹配的树节点集合，云端仅检索对应子索引，无需在线执行加密范围校验
- 两级检索pipeline：先用保留近似距离序的DCPE加密方案从匹配子索引召回粗候选，再用支持精确距离比较的DCE加密方案对小范围候选重排，大幅降低高开销的精确加密比较次数
- 仅需单云服务器即可完成查询处理，无需额外非串通辅助服务器支持
### 关键实验
在Sift1M、Gist、GloVe、Deep1M四个公开向量数据集上，和安全预过滤、安全后过滤、PP-iRangeGraph三个基线对比，在Recall@10=0.95时，QPS较基线提升至少2个数量级，跨1%~40%的不同查询选择性下均保持稳定性能优势，最高可达2600倍加速。
### 核心洞察
把范围筛选逻辑下沉到可信用户端执行，而非在不可信云端做加密校验，是隐私保护带过滤向量检索性能突破的核心思路
