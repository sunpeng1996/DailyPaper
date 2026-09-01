---
title: 'RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search'
title_zh: RSLM：面向近似最近邻搜索的免训练向量量化方案
authors:
- Rastislav Lenhardt
- Teodora Dobos
- Thomas Vecchiato
- Jiri Isa
- Igor Ginzburg
affiliations:
- Google
- Technical University of Munich
- University of Copenhagen
arxiv_id: '2608.30384'
url: https://arxiv.org/abs/2608.30384
pdf_url: https://arxiv.org/pdf/2608.30384
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 召回底层 · 免训练向量量化优化
tags:
- Vector Quantization
- ANN Search
- Training-Free
- IVF
- MIPS
- RAG
one_liner: 提出1-4bit免训练向量量化家族RSLM，降低ANN内存带宽开销同时保持/提升召回
practical_value: '- 推荐/搜索召回的IVF索引系统可直接替换现有4bit/8bit量化方案为Rslm4Lite，无召回损失前提下向量内存占用减半，同时通过cacheline对齐优化提升QPS

  - RAG系统的向量数据库可采用相对量化+全局norm修正的trick，2bit量化即可实现99%+ recall@20@40，内存带宽降为原来的1/4，适配高吞吐批量查询场景

  - 处理非2的幂次维度嵌入时，可复用块级级联FWHT的设计，避免零填充带来的额外计算与带宽开销，比全局FWHT/稠密旋转矩阵性能提升1~2个数量级

  - 多阶段召回链路可借鉴最终重构向量L2 norm修正的思路，替代复杂的各向异性损失训练，无需离线训练即可保证MIPS排序准确性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前十亿级规模ANN搜索系统的核心瓶颈是DRAM容量与内存带宽，传统数据依赖的量化方案需要离线训练适配数据集，迭代成本高；现有免训练低比特量化方案要么采用二次方复杂度的稠密旋转矩阵，要么需要零填充适配2的幂次维度，计算开销大，且大多未结合ANN链路特性优化，低比特下召回损失严重。

### 方法关键点
- 块级级联FWHT变换：仅在128大小的块内做变换，复杂度为O(D)，无需零填充即可适配任意维度嵌入，同时用AVX SIMD优化计算效率
- 全局L2 norm修正：直接对齐最终重构向量的范数，而非仅修正残差范数，无需训练即可达到甚至超过各向异性损失优化的MIPS排序效果
- Rslm4Lite变种：将缩放因子隐写在量化向量的低比特位中，实现零元数据开销，完美适配cacheline对齐，进一步提升内存访问效率
- 支持残差相对量化，适配IVF等多阶段ANN链路，量化粗筛后的残差向量进一步降低压缩损失

### 关键结果
在glove、OpenAI文本嵌入等5个不同维度的公开数据集上，对比Faiss、ScaNN的内置量化方案：残差模式下4bit RSLM实现与8bit SQ完全一致的recall@20@30，2bit RSLM实现99%+ recall@20@40；端到端对比中1-2bit低比特场景下RSLM比ScaNN/Faiss的训练式PQ方案召回高4%~12%，编码速度比基于稠密旋转的TurboQuant快36倍。

最值得记住的结论：针对ANN链路特性优化的免训练低比特量化，完全可以达到甚至超过需要离线训练的量化方案的效果，同时大幅降低系统复杂度与硬件开销。
