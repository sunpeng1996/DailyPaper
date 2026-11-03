---
title: Federated Vector Retrieval across Heterogeneous VectorDBs
title_zh: 面向异构向量数据库的联邦检索框架HVMap
authors:
- Mintaek Lim
- Sieun Hyeon
- Geon Chio
- Jaeyoung Do
affiliations:
- Seoul National University
arxiv_id: '2611.01514'
url: https://arxiv.org/abs/2611.01514
pdf_url: https://arxiv.org/pdf/2611.01514
published: '2026-11-01'
collected: '2026-11-03'
category: RAG
direction: RAG · 异构向量库检索优化
tags:
- VectorDB
- Federated Retrieval
- Embedding Alignment
- Cross Domain Retrieval
- RAG
one_liner: 无需重训重索引，通过轻量双向映射层实现异构向量库的高效跨库联邦检索
practical_value: '- 多业务线异构向量库兼容场景无需全量重索引，用双向MLP映射层对齐不同embedding空间，仅需小批量配对样本训练，构建成本仅为全量重训的0.3%，适合电商多召回库合并、Agent多数据源RAG检索场景

  - 可直接复用提出的模糊对比损失做跨模型embedding对齐，比传统MSE/普通对比损失的对齐精度更高，nDCG最高可提3.59倍，可用于不同召回模型的向量分校准

  - 多库扩展采用hub-spoke架构，选轻量embedding空间作为hub，仅需O(N)个映射函数即可支持N个异构库，避免O(N²)的pairwise映射成本，适合业务迭代快的场景快速接入新向量库，无需改造现有索引'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
向量库是RAG、语义搜索、推荐召回的核心基建，实际业务中常存在多个用不同embedding模型构建的独立向量库（如模型迭代升级、跨领域专用模型），全量重嵌入重索引成本极高、业务影响大，现有方法在检索精度、构建成本、查询吞吐量三者间难以平衡。

### 方法关键点
- 轻量兼容层设计：无需修改存量向量或重建索引，仅学习不同embedding空间的双向映射函数即可实现跨库分数可比
- 模糊对比损失：自适应匹配不同负对的语义距离，比传统MSE/普通对比损失的对齐精度更高，适配检索场景的排序需求
- 多库扩展用hub-spoke架构：选一个轻量embedding空间作为hub，所有spoke仅和hub做映射，将N个库的映射成本从O(N²)降到O(N)，同时限制映射误差传播最多2步
- 跨库排序策略：结合原生空间相似度（权重0.7）和映射空间相似度（权重0.3），既保留原生精度又实现跨库分数校准

### 关键实验结果
在BEIR公开数据集、自建跨领域（金融/生物/科学）benchmark上对比全量迁移（MIG）、结果融合（RRF/CombMNZ）、CCA等基线：nDCG@10最高比基线高3.59倍，查询吞吐量最高提升2.01倍，10亿规模向量库场景下构建成本仅为基线的0.3%；扩展到6个异构库时仍能保持稳定检索精度，性能接近最优全量迁移方案。

最值得记住的一句话：异构向量库联邦的最优路径不是强制统一空间，而是通过轻量对齐层在不改造存量系统的前提下实现精度、成本、吞吐量的最优平衡
