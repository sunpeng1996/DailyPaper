---
title: Real-Time Hybrid Retrieval in Hyperbolic Space for Retrieval-Augmented Generation
  on Edge Devices
title_zh: 面向边缘设备RAG的双曲空间实时混合检索系统
authors:
- Aradhya Chakrabarti
affiliations:
- International Institute of Information Technology Bangalore
arxiv_id: '2608.01450'
url: https://arxiv.org/abs/2608.01450
pdf_url: https://arxiv.org/pdf/2608.01450
published: '2026-08-02'
collected: '2026-08-04'
category: RAG
direction: RAG检索优化 · 边缘端部署
tags:
- RAG
- Hyperbolic Retrieval
- Edge Deployment
- BM25
- Hybrid Retrieval
one_liner: 基于双曲几何洛伦兹模型的轻量混合检索框架，实现边缘端RAG低延迟高准确率召回
practical_value: '- 端侧RAG场景可复用轻量投影思路：仅训练<200k参数的2层投影层，即可将预训练嵌入映射到双曲空间适配层级语义，无需微调基座大模型，适合端侧电商导购Agent、离线推荐场景

  - 两阶段混合检索pipeline可直接迁移到业务：先BM25捞候选保证长尾关键词/专业术语召回，再双曲相似度重排序提语义精度，适配电商商品检索、客服问答RAG等场景

  - 双曲空间层级编码特性可用于分层召回：径向坐标代表概念泛化/细分程度，可根据query语义粒度动态调整召回层级，宽泛query召回通用类商品、精准query召回细分商品

  - 端侧工程优化方案可直接复用：索引拆分为二进制嵌入块、zlib压缩文本、路径元数据三个文件，通过内存映射直接加载，适配端侧存储、算力受限场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
欧氏空间稠密检索无法适配语言的层级结构：指数增长的语义分支塞进多项式体积增长的欧氏空间会出现「拥挤问题」，导致层级相关但语义不同的文档距离过近，降低召回精度；同时现有RAG检索依赖大模型微调、GPU算力，无法在资源受限的边缘设备上实现实时交互。

### 方法关键点
- 轻量HyTE-H投影模块：仅2层非线性变换（参数量<200k），在MS MARCO数据集上对比训练，将冻结的BGE-small词嵌入映射到洛伦兹双曲空间，保留层级语义，无需微调基座模型
- 两阶段混合检索pipeline：第一阶段用BM25做初始候选召回，第二阶段用洛伦兹内积相似度重排序，可调节α参数加权两个得分，平衡关键词匹配与语义匹配效果
- 端侧工程优化：滑动窗口分块处理文档，索引采用二进制序列化+zlib压缩文本的存储方案，整个pipeline封装为C++共享库，支持arm架构端侧部署

### 关键结果
在BEIR基准的5个数据集上测试，SciFact/NFCorpus/ArguAna/SciDocs/FiQA的NDCG@10分别达0.654/0.304/0.342/0.150/0.217，无需微调神经编码器、无需交叉注意力重排器；中端安卓设备上单查询延迟仅3ms，包含5.9万条文档的FiQA数据集单查询延迟仅29ms，支持实时动态新增索引。

> 最值得记住：双曲几何的指数体积增长特性完美匹配语言的层级结构，仅用极小的投影层开销即可大幅提升检索精度，同时适配边缘端算力约束。
