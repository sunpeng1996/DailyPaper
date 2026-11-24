---
title: 'Zarc: Exact Nearest Neighbors over a Billion Vectors in Seconds'
title_zh: Zarc：秒级完成十亿级向量的精确最近邻搜索
authors:
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2611.29252'
url: https://arxiv.org/abs/2611.29252
pdf_url: https://arxiv.org/pdf/2611.29252
published: '2026-11-22'
collected: '2026-11-24'
category: RAG
direction: RAG向量检索 · 精确KNN加速
tags:
- Exact KNN
- Vector Search
- GPU Acceleration
- RAG
- Sparse Attention
one_liner: 通过GPU半精度认证筛选+分层存储实现十亿级向量秒级精确KNN搜索
practical_value: '- 高精准向量召回场景（如电商高价值商品召回、Agent RAG精确知识匹配）可直接复用Zarc的分层架构：GPU仅存半精度投影行，全量向量放主存，显存占用降为暴力搜索的1/4以下，结果100%精确

  - 带属性过滤的向量召回场景（如电商类目/价格过滤召回），可借鉴Zarc的标签分块+路由筛选设计，0.1%选择性下性能比过滤式CAGRA高692倍，无召回漏判

  - 长上下文LLM Agent的稀疏注意力模块可替换现有bf16矩阵乘+topk方案为Zarc，百万Token上下文下推理提速3.1倍，完全避免精度损失导致的注意力偏移

  - 大规模训练数据/商品库语义去重场景，可直接用Zarc构建精确KNN图，速度比暴力搜索快42倍，避免近似去重导致的有效数据丢失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有精确KNN搜索要么依赖GPU暴力扫描，十亿级向量下1万查询需耗时5分钟，且全量向量存GPU显存占用极高，要么使用近似索引存在召回误差，在LLM稀疏注意力、RAG精确知识召回、训练数据语义去重等对精度要求极高的场景下，误差会直接传导至上层应用效果。此前的CertEx认证筛选方案仅支持单GPU全量数据存储，无法扩展到十亿级规模，也不支持动态更新、属性过滤、内积查询等生产级需求。
### 方法关键点
- 分层存储设计：GPU仅存储半精度的向量投影筛选行，全量高精度向量存储在主存，仅需为通过筛选的少量候选向量读取主存，大幅降低GPU显存占用
- 分区紧界优化：通过k-means分区生成更紧的距离阈值，配合分区局部投影进一步降低候选向量数量，单查询候选数可降低一个数量级以上
- 多GPU分片扩展：跨GPU分片存储筛选行，通过全局统一阈值保证搜索精确性，弱扩展效率接近线性
- 兼容cuVS、Faiss、PyTorch、FlashInfer等现有库接口，支持动态更新、属性过滤、欧氏/余弦/内积多种距离查询，替换成本极低
### 关键实验结果
在4张H100 GPU上测试：十亿级BIGANN数据集下，1万查询仅需1.1s，比cuVS暴力搜索快270倍；11个开源LLM（7B~1.6T参数）的稀疏注意力场景下，比FlashInfer bf16方案快3.1倍，结果100%精确；带属性过滤的召回场景0.1%选择性下比CAGRA快692倍；MS MARCO passage检索上比最高精度的CAGRA更快，MRR@10比CAGRA最高高0.017。
### 核心结论
精确向量搜索的性能已经可以超过多数近似索引的最高精度配置，在对召回准确性有要求的场景下无需再为性能牺牲精度。
