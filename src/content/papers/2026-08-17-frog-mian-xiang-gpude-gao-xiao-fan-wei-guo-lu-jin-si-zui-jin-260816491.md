---
title: 'FROG: Efficient Range-Filtering Approximate Nearest Neighbor Search on GPUs'
title_zh: FROG：面向GPU的高效范围过滤近似最近邻搜索方法
authors:
- Xiaokun Cui
- Pengbo Liu
- Jiadong Xie
- Yingfan Liu
- Hui Li
- Jeffrey Xu Yu
- Jiangtao Cui
affiliations:
- Xidian University
- The Chinese University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- Xi'an University of Posts and Telecommunications
arxiv_id: '2608.16491'
url: https://arxiv.org/abs/2608.16491
pdf_url: https://arxiv.org/pdf/2608.16491
published: '2026-08-17'
collected: '2026-08-18'
category: Other
direction: 向量检索 · GPU RFANNS索引优化
tags:
- ANNS
- RFANNS
- GPU Acceleration
- Vector Database
- Similarity Search
one_liner: 提出全局感知顶点为中心的GPU RFANNS索引，混合选择性查询吞吐量超现有GPU基线4.5-7.6倍
practical_value: '- 业务中带属性过滤的向量检索场景（如限定价格区间的同款商品召回、RAG中限定发布时间的文档检索）可直接复用FROG的开源GPU索引，提升高并发场景下的查询吞吐量

  - 可借鉴融合距离设计思路：在向量邻居选择时引入结构化属性距离权重，提升过滤条件下的有效邻居召回率，减少无效距离计算开销

  - 工程上可复用SIMT适配优化技巧：控制流压缩、懒哈希校验、查询热点层定位，大幅降低GPU warp divergence，提升硬件利用率

  - 可直接将FROG集成到现有向量数据库/推荐系统的向量召回模块，替换原有RFANNS实现，无需大幅改造现有架构'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有范围过滤近似最近邻搜索（RFANNS）是向量数据库的核心算子，广泛应用于电商带属性约束的商品检索、推荐系统向量召回、RAG过滤等场景，但CPU索引并行扩展性有限，现有GPU方案存在选择性依赖强、搜索路径长、无效计算多等问题，无法满足高吞吐在线服务需求。
### 方法关键点
- 采用全局感知的顶点为中心设计，为每个顶点预存覆盖不同属性范围的扩展邻居候选（ENC），避免局部最优子图带来的长搜索路径问题
- 提出融合距离作为ENC选择标准，同时加权向量距离和属性距离，提升小范围查询下的有效邻居占比
- 构建阶段采用自底向上的GPU并行构造算法，配合提前终止策略，大幅降低建库开销
- 查询阶段引入热点层定位、控制流压缩、懒重复检查等SIMT感知优化，减少GPU全局内存访问和warp divergence
### 关键实验结果
在6个不同规模、维度的公开数据集（Deep10m、Audio、SIFT、Crawl、GIST、Wiki）上，对比44核CPU基线iRG/WoW、现有GPU最优基线Garfield、通用GPU过滤方案：混合选择性下查询吞吐量较CPU基线提升14.7~37.7倍，较最强GPU基线提升4.5~7.6倍；索引构建速度较GPU基线提升2.4~14.8倍，且在不同选择性下性能波动远小于其他方案。
### 核心结论
带属性过滤的向量检索仅靠GPU算力堆砌远不够，面向硬件特性优化的索引结构设计才能带来数量级的性能提升。
