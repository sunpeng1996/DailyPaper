---
title: 'Look Before You Leap: Re-Architecting Disk-Resident Vector Search with TriVS'
title_zh: TriVS：三阶段解耦的高性能磁盘驻留向量检索架构
authors:
- Yizou Chen
- Baotong Lu
- Peiqi Yin
- Zhisheng Hu
- Qi Chen
- Ming-Chang Yang
affiliations:
- The Chinese University of Hong Kong
- Microsoft Research
arxiv_id: '2611.29948'
url: https://arxiv.org/abs/2611.29948
pdf_url: https://arxiv.org/pdf/2611.29948
published: '2026-11-23'
collected: '2026-11-24'
category: RAG
direction: 磁盘驻留ANNS 向量检索I/O优化
tags:
- ANNS
- Vector Search
- I-O Optimization
- SSD
- Retrieval
one_liner: 基于粗细粒度解耦的三阶段磁盘向量检索架构，大幅降低I/O开销，提升吞吐降低延迟
practical_value: '- 电商推荐向量召回、Agent/RAG知识库检索场景的磁盘ANNS系统可直接复用三阶段设计：内存聚类粗筛→内存量化向量精筛→仅读取磁盘最终候选，大幅降低I/O开销，尤其适配高并发查询场景

  - 可将聚类粒度调粗，省出的路由索引内存用于存放蒸馏用的量化向量，无需额外扩容内存，还能省去聚类边界向量复制的存储开销

  - 可复用渐进式精度筛选trick：先用低精度量化快速过滤大部分负例，仅对小范围候选升精度计算，平衡CPU开销和I/O开销

  - 高并发场景下可将磁盘I/O和重计算逻辑拆分到独立线程池，提升SSD利用率，进一步拉高系统吞吐'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有磁盘驻留ANNS系统分为聚类和图两大范式，均受限于I/O瓶颈：聚类范式收敛阶段需读取完整簇数据，I/O放大严重；图范式逼近阶段需做向量级图遍历，依赖大量随机I/O。即使搭配PCIe 5.0 SSD，高并发下I/O等待占总延迟的87%~93%，现有优化（如I/O计算重叠）无法降低单查询I/O总量，亟需从架构层面突破。

### 方法关键点
- 解耦逼近和收敛阶段的检索粒度：逼近阶段用粗粒度聚类做内存路由，完全省去逼近阶段I/O；收敛阶段用细粒度向量级I/O，避免全簇读取浪费
- 新增内存蒸馏阶段衔接粗细粒度：先用低精度量化向量快速过滤簇内大部分负例，仅对候选升精度筛选，将候选集缩小3个数量级后再访问磁盘
- 内存复用设计：调粗聚类粒度缩小路由索引内存占用，省出的空间存放蒸馏用的量化向量，总内存不增反降；每个向量仅归属一个簇，省去边界复制的存储开销
- 配套TriSearch算法，支持渐进式精度提升、早期终止、下界剪枝，平衡CPU计算和I/O开销

### 关键结果
在5个覆盖100M~1B规模、不同维度的数据集（含RAG场景Wiki数据集、跨模态Text-to-Image数据集）上对比SOTA基线，Recall@10=0.9时，平均吞吐量达PipeANN的3.42倍，延迟降低51.2%，磁盘I/O减少63.7%，同时内存和存储占用均低于基线。

**最值得记住的一句话**：磁盘ANNS的核心瓶颈是I/O而非计算，通过内存多级过滤减少磁盘访问的收益远大于新增的内存计算开销。
