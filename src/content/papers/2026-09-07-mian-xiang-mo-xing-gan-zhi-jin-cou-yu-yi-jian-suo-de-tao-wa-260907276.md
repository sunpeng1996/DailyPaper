---
title: Matryoshka Hash Representations for Model-Aware Compact Semantic Retrieval
title_zh: 面向模型感知紧凑语义检索的套娃哈希表示
authors:
- Peichun Hua
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2609.07276'
url: https://arxiv.org/abs/2609.07276
pdf_url: https://arxiv.org/pdf/2609.07276
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: RAG检索 · 向量哈希压缩
tags:
- Matryoshka Hash
- Semantic Retrieval
- Vector Quantization
- RAG
- FAISS
- LoRA
one_liner: 提出两阶段套娃哈希表示MHR，支持多存储预算下零重编码的高效语义检索
practical_value: '- 向量压缩场景可直接复用两阶段训练范式：先训练最优全长度哈希码对齐检索排序信号，再训练零初始化残差适配器生成可截断前缀，避免全长度精度损失，适配多存储预算无需重训编码器

  - 工程落地可直接复用MHR+FAISS FastScan适配方案：文档侧存储二值化哈希码降低存储96%，查询侧保留连续logits保障精度，单线程检索速度比同预算PQ快7-9倍

  - 电商推荐召回、RAG检索粗筛阶段可采用8/16字节MHR前缀做候选初筛，后续接高精度重排，可比同存储PQ提升30%+NDCG，接近全精度浮点向量效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG、推荐召回等场景依赖的密集检索在亿级语料下，全精度向量存储成本成为核心瓶颈；传统量化方法（如PQ）以向量重建误差为优化目标，未对齐检索排序信号，精度损失大；现有套娃嵌套表示方法同时训练多长度前缀，会导致短码精度提升、长码精度下降的 trade-off，二值哈希场景下冲突更严重，无法适配多存储预算灵活切换的业务需求。

### 方法关键点
- 两阶段训练解耦全长度与前缀优化：Stage1 用LoRA微调预训练双编码器，学习对齐排序信号的最优256位全长度哈希码；Stage2 冻结编码器，仅训练2层零初始化残差适配器，生成64/128/256位可直接截断的嵌套前缀，保留全长度精度同时满足多存储预算需求。
- 非对称打分策略：文档侧存储二值化哈希码，单文档仅需8/16/32字节，压缩比达96倍；查询侧保留连续logits，无额外存储开销的前提下大幅提升检索精度。
- 原生适配FAISS FastScan/IVF索引，无需改造现有ANN架构即可落地。

### 关键结果
在MS MARCO训练，零样本迁移到7个BEIR数据集，对比PQ、OPQ、JPQ等主流基线：32字节下NDCG@10达0.556、Recall@100达0.653，比最优基线JPQ-FT提升0.032 NDCG、0.015 Recall；16字节下NDCG@10达0.502，超出JPQ-FT 0.098；单线程检索速度比同精度PQ快7-9倍；8字节前缀作为粗筛接全精度重排，NDCG@10达0.561，超过32字节PQ的精度。

低存储语义检索的优化核心是对齐排序信号而非向量重建误差，两阶段嵌套哈希可以在不损失全长度精度的前提下实现多预算灵活适配。
