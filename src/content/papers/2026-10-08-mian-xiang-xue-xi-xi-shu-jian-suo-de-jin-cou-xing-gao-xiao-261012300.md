---
title: Compact and Efficient Indexes for Learned Sparse Retrieval
title_zh: 面向学习稀疏检索的紧凑型高效索引
authors:
- Franco Maria Nardini
- Luca Rizzo
- Cosimo Rulli
- Rossano Venturini
affiliations:
- ISTI-CNR
- University of Pisa
- Linkup
arxiv_id: '2610.12300'
url: https://arxiv.org/abs/2610.12300
pdf_url: https://arxiv.org/pdf/2610.12300
published: '2026-10-08'
collected: '2026-10-09'
category: RAG
direction: RAG召回 · 稀疏索引压缩优化
tags:
- Learned Sparse Retrieval
- Index Compression
- SIMD
- RAG Retrieval
- Forward Index
- Inverted Index
one_liner: 优化学习稀疏检索的双索引结构与压缩方案，同等精度下速度超SOTA 5.3倍内存占比降3倍
practical_value: '- 稀疏检索倒排索引的块摘要可替换为块内medoid文档ID，单块元数据内存占比降低75%，适配内存受限的电商搜推广、RAG召回场景

  - 前向索引可采用词汇重排序+∆间隙编码+DOTPACKING8方案，压缩30%内存的同时基本不损失检索延迟，可直接嵌入现有稀疏向量检索引擎

  - 极短稀疏query场景优先采用JUMPDOT点积核，相比传统稠密化方案获得2倍以上速度提升，适配电商短query搜索、轻量RAG召回需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前SPLADE等学习稀疏检索（LSR）模型已成为RAG、语义搜索的主流召回方案，但现有LSR索引（如SEISMIC）内存占用高（MSMARCO场景下达7GiB），传统倒排索引压缩方法不适配LSR非Zipf分布的稀疏向量，无法兼顾内存效率与查询延迟。

### 方法关键点
- 倒排索引优化：将原有每块稀疏向量摘要替换为块内medoid文档ID，单块元数据从~400字节压缩到8字节，通过调整heap_factor参数补偿召回损失
- 前向索引压缩：先通过递归图二分重排序词汇缩小共现词ID间隙，再用自研DOTPACKING8 SIMD友好位打包方案编码∆间隙，值部分采用每维度独立4bit量化，压缩比提升且解码与点积计算融合
- 点积计算优化：针对极稀疏查询（如无推理检索器，query非零项仅6个左右）提出JUMPDOT分块点积核，支持跳过无匹配块，兼顾向量化效率与内存占用

### 关键实验结果
在MSMARCO数据集上测试SPLADE、LILSR、SPLADE-v3三种稀疏编码器，对比SINDI、KANNOLO、原生SEISMIC等SOTA索引：同等精度下，优化后的SEISMIC比SINDI快5.3倍、内存少3倍；内存极度受限场景下仍快1.9倍、内存少3.9倍；前向压缩方案嵌入KANNOLO后内存占用降低41%~50%且无延迟损失。

学习稀疏检索的索引优化不能只看压缩率，必须适配硬件特性实现解码、点积计算融合才能落地到低延迟业务场景。
