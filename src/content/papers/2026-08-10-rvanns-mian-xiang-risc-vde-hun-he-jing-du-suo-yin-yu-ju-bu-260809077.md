---
title: 'RVANNS: Mixed-Precision Indexing and Locality-Aware Graph Traversal on RISC-V'
title_zh: RVANNS：面向RISC-V的混合精度索引与局部感知图遍历
authors:
- Chengying Huan
- Yudong Liu
- Jianguo Wang
- Lizheng Chen
- Renling Yin
- Weijia Chen
- Ji Qi
- Jiageng Yu
- Junjie Xu
- Jie Zhang
affiliations:
- Nanjing University
- Institute of Software, Chinese Academy of Sciences
- Purdue University
- Sichuan University
- Putian University
arxiv_id: '2608.09077'
url: https://arxiv.org/abs/2608.09077
pdf_url: https://arxiv.org/pdf/2608.09077
published: '2026-08-10'
collected: '2026-08-11'
category: Other
direction: 向量检索引擎 · RISC-V架构优化
tags:
- ANNS
- RISC-V
- Mixed-Precision
- Graph Traversal
- Vector Search
one_liner: 面向RISC-V RVV优化的ANNS引擎，混合精度索引+图局部性优化，性能大幅领先各类基线
practical_value: '- 混合精度索引MPMI思路可直接复用至向量检索链路：用8bit稠密仿射基+FP16/FP32稀疏残差表征向量，融合重构与距离计算，消除低精度转码开销，适配向量寄存器分组提升检索吞吐

  - ROrder图节点重排技巧可迁移到HNSW类图索引：将共访问概率高的节点邻接存储，把随机内存访问转为正向顺序流，大幅提升缓存命中率，降低检索延迟

  - 适配RISC-V国产硬件的向量检索业务可直接参考其寄存器对齐、指令融合优化方案，可实现3倍以上的检索性能提升'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前CPU侧ANNS性能瓶颈已从算术算力转为向量移动、解码开销；RISC-V RVV扩展虽提供通用向量能力，但通用低精度解码存在转换开销，不规则图遍历的散列访问也会严重降低缓存局部性与内存并行度。
### 方法关键点
1. 设计混合精度多层索引MPMI：每个向量用8bit稠密仿射基+稀疏FP16/FP32残差表示，融合向量重构与距离累加逻辑，对齐LMUL大小的寄存器组消除转码开销；
2. 提出ROrder节点重排策略：将大概率共访问的图节点共址存放，重排邻接表，把分散访问转为稠密的正向地址流，提升缓存命中率。
### 关键结果
集成到Milvus后，在128/256位RVV处理器上比标量执行提速3.39x/4.94x；相同HNSW配置下，比RVV SIMD+FP32吞吐高2.27~2.76x，比AVX-512、SVE基线高1.18~1.59x；Cohere10M数据集上QPS/W比GPU基线高1.82~2.27x
