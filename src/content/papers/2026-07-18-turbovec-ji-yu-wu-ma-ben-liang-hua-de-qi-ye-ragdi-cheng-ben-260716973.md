---
title: 'TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise
  RAG via Codebook-Oblivious Quantization'
title_zh: TurboVec：基于无码本量化的企业RAG低成本私有检索案例研究
authors:
- Navnit Shukla
- Kamal Pandey
- Omsankar Tiwari
affiliations:
- Snowflake Inc.
- Rivian Automotive Inc.
- Google Deepmind
arxiv_id: '2607.16973'
url: https://arxiv.org/abs/2607.16973
pdf_url: https://arxiv.org/pdf/2607.16973
published: '2026-07-18'
collected: '2026-07-21'
category: RAG
direction: 企业级RAG · 向量检索量化优化
tags:
- RAG
- Vector Quantization
- Multi-Tenant
- ANN Search
- Privacy-Preserving
one_liner: 提出无需语料训练的无码本量化向量索引TurboVec，平衡多租户RAG场景的召回、内存开销与隐私安全
practical_value: '- 企业多租户RAG/电商推荐向量检索场景，可复用TurboQuant无训练量化方案，省去码本训练流程，降低内存4-8倍的同时召回损失极小，适合百万级以内向量库快速落地

  - 多租户隔离检索场景可借鉴内核级白名单过滤机制，在SIMD块层面提前跳过非租户数据，避免过取后过滤的召回损耗与计算浪费

  - 对向量检索隐私有要求的用户画像、商品向量库场景，无码本量化可避免码本泄露带来的语料成员推断风险，无需承担加密ANN方案的高昂开销

  - 百万级以下CPU部署的RAG/推荐召回场景，可直接复用TurboVec的Rust实现，比同比特FAISS PQ快9倍，成本仅为商用向量库的1/3-1/5'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前企业多租户RAG系统的向量检索层存在两大痛点：一是PQ等量化方案的训练码本会泄露语料统计特征，存在多租户场景下的隐私泄露风险；二是传统过取后过滤的租户隔离方案会大幅降低选择性查询的召回率，同时浪费计算资源，而加密类隐私ANN方案开销过高无法落地生产。

### 方法关键点
- 采用TurboQuant无码本量化：基于L2归一化高维向量随机旋转后的边际分布（Beta/高斯分布）预计算量化边界，无需任何语料依赖的训练流程
- 向量压缩流水线：L2归一化→固定随机正交矩阵旋转→预计算边界的Lloyd-Max标量量化→位打包，1536维4-bit压缩比达8:1，搭配长度重归一化打分修正量化误差
- 内核级多租户过滤：搜索内核接收租户白名单，32向量块粒度提前跳过无权限块，块内无效结果在堆插入阶段直接丢弃，避免过取后过滤
- 索引支持在线写入、持久化、SIMD加速（ARM NEON/x86 AVX-512）

### 关键实验
基于DBpedia 100K-999K条OpenAI 1536维嵌入数据集，对比FAISS PQ、HNSW-Flat、IVF-PQ、仓库暴力扫描等基线：
- 4-bit TurboQuant在100K-999K规模下Recall@5比同比特FAISS PQ高8.5-8.9pp，检索速度快9倍，内存仅为HNSW的1/4-1/8
- 4-bit TurboQuant Hit@5达100%，MRR@20达0.987，量化损失对RAG下游任务几乎无影响
- Snowpark部署100K向量时，中位查询延迟11ms，比仓库暴力扫描快64倍；内核级过滤在10-1000租户场景下Recall@10达0.86-0.93，远高于过取后过滤的0.09-0.19
- 成员推断攻击下，TurboVec攻击准确率仅为随机水平50%，远低于PQ的57.3%

**最值得记住的结论**：无训练的无码本量化在高维L2归一化嵌入场景下，完全可以超越传统有训练PQ的效果，同时兼顾隐私、成本与性能，是中小规模企业RAG/推荐向量检索的高性价比方案
