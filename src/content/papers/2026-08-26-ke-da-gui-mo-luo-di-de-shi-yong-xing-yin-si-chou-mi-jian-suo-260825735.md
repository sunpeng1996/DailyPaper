---
title: 'Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval
  at Scale'
title_zh: 可大规模落地的实用型隐私稠密检索技术框架
authors:
- Peichun Hua
- Danyang Chen
- Junan Zhang
- Haifeng Sun
- Jingyu Wang
- Diwen Xue
- Mingyu Li
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- State Key Laboratory of Internet Architecture, Tsinghua University
- Beijing University of Posts and Telecommunications
- The Chinese University of Hong Kong
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2608.25735'
url: https://arxiv.org/abs/2608.25735
pdf_url: https://arxiv.org/pdf/2608.25735
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: RAG隐私优化 · 差分隐私稠密检索
tags:
- Private Retrieval
- Differential Privacy
- Homomorphic Encryption
- RAG
- Dense Retrieval
- Oblivious Transfer
one_liner: 基于差分隐私深度哈希与同态加密的低开销高准确率隐私稠密检索方案
practical_value: '- 涉及用户查询隐私的RAG/语义搜索场景，可复用「差分隐私哈希粗筛+短名单密码学重排」的两级架构，既降低隐私计算开销，又几乎不损失检索效果

  - 针对连续embedding泄露问题，可借鉴无零点int8对称量化方案，将浮点相似度计算转为低开销整数点积，适配同态加密的同时保留排序精度

  - LoRA微调预训练编码器生成哈希码的方案可直接迁移，无需重新训练完整backbone，即可得到高召回率粗筛索引，存储开销仅32B/doc

  - 需保护用户选择行为的电商推荐场景，可复用k-out-of-K 不经意传输设计，仅返回用户授权结果，不泄露用户选择偏好'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG与语义搜索规模化落地过程中，用户查询、服务端私有语料均存在泄露风险，传统密码学隐私检索方案要么需全库计算开销极高，要么聚类剪枝严重损失检索质量，嵌入反演攻击还可从连续embedding还原用户敏感信息，亟需兼顾隐私、效果、效率的大规模落地方案。

### 方法关键点
- 两级检索架构：第一级用LoRA微调预训练编码器生成符合方向度量差分隐私（mDP）的随机二进制哈希码，服务端仅通过汉明搜索得到200~3000条候选短名单，大幅缩小隐私计算范围；第二级用BFV同态加密对候选做精准重排，用户侧解密后选top-k结果，通过k-out-of-K不经意传输获取对应内容，不泄露最终选择
- 效率优化：采用无零点int8对称量化将浮点相似度转为整数点积，适配同态加密的同时保留99%以上排序精度；哈希模型与排序模型分离，推理阶段做流水线并行，隐藏编码和加密延迟
- 隐私保障：哈希码满足mDP，相近查询的候选分布不可区分，大幅降低嵌入反演、属性推理攻击成功率

### 关键结果
在5个BEIR零样本数据集（25K~5.4M文档规模）上测试，K=500的候选短名单即可保留98.84%~100%的全库检索NDCG@10，甚至在Climate-FEVER数据集上提升0.0158的NDCG；在2.68M条目的NQ语料上，配合Qwen3-32B的RAG管线仅额外增加0.73秒延迟，占原管线开销的10%；对比P2RAG、RemoteRAG等同类方案，latency最高降低69.2倍，百万级语料下无内存溢出问题。

最值得记住的结论：隐私计算不需要覆盖全流程，对粗粒度环节引入可证明的轻量隐私保护、仅对小范围核心环节做高强度密码学计算，是兼顾效果、效率、隐私的工程落地核心思路。
