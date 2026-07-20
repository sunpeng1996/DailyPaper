---
title: Efficient and Effective In-place Graph-based Vector Index Updates
title_zh: 高效高性能的图结构向量索引原地更新系统Yi
authors:
- Haotian Liu
- Yujun He
- Bo Tang
affiliations:
- Southern University of Science and Technology
arxiv_id: '2607.15576'
url: https://arxiv.org/abs/2607.15576
pdf_url: https://arxiv.org/pdf/2607.15576
published: '2026-07-17'
collected: '2026-07-20'
category: Other
direction: 向量索引 · 图结构原地更新优化
tags:
- Vector Index
- ANN Search
- Graph Index
- In-place Update
- RAG Infrastructure
one_liner: 提出全原地更新的图向量索引系统Yi，800M数据集下更新吞吐量较SOTA高1.75倍资源占用更低
practical_value: '- 电商/推荐/Agent的RAG系统可复用Yi的存储布局设计，分离图拓扑索引块与原始向量块，更新时仅访问小体积索引块，降低I/O开销，提升实时更新性能

  - 借鉴向量级统一更新机制，将插入、删除的邻居连接/剪枝操作合并为单向量粒度任务，消除不同更新请求的冗余节点访问，大幅降低计算开销

  - 任务let+异步缓冲管理器的设计可迁移至高并发向量检索服务，用C++20协程做细粒度任务调度，重叠I/O与计算，减少锁冲突，提升CPU利用率

  - 亿级规模商品/内容向量库可直接替换现有DiskANN/OdinANN方案，无需定期离线合并索引，降低运维成本的同时提升更新与检索吞吐量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM时代RAG、推荐系统、多模态检索等场景需要高频更新向量库，现有图结构向量索引（如SOTA方案OdinANN）采用out-of-place更新策略，需定期离线合并更新批次，数据规模越大合并开销越高，甚至出现更新堆积；现有仅支持删除的原地更新方案IP-DiskANN不支持插入，且存在节点重复访问、CPU利用率低、缓存效率差、数据布局冗余等问题，无法兼顾高更新吞吐量、高检索召回率和低资源占用。
### 方法关键点
- 核心遵循「分解促合并」设计思路，提出向量级更新机制，统一插入、删除操作的邻居连接、剪枝逻辑为单向量粒度的connect任务，合并不同更新请求的冗余节点访问；删除向量暂存LRU列表，无插入请求时随机采样少量节点触发更新，保证图结构质量
- 系统包含三大核心组件：1）基于C++20协程的tasklet执行引擎，把检索、更新拆解为细粒度可调度任务，挂起等待I/O的任务，大幅提升CPU利用率；2）异步缓冲管理器，通过引用计数、冲突时挂起机制实现轻量并发，缓存热点索引页减少重复I/O；3）向量文件系统，分离图拓扑索引块和原始向量数据块，更新时仅需访问更小的索引块，提升缓存命中率
### 关键结果
在DEEP100M、SIFT800M公开向量数据集上与SOTA方案对比：800M数据集下，Yi更新吞吐量较OdinANN高1.75倍，并发检索吞吐量高1.8倍，峰值内存仅为OdinANN的73%，CPU核心占用少一半，同时检索召回率与OdinANN持平；100M数据集下更新吞吐量是OdinANN的2.8倍，内存波动极小。
### 核心结论
图向量索引的原地更新不需要复杂算法优化，通过操作粒度拆解、存储布局分离、异步调度的工程优化，就能实现远超现有out-of-place方案的综合性能
