---
title: 'AVQ-Attention: Adaptive Vector-Quantized Attention'
title_zh: AVQ-Attention：自适应向量量化注意力机制
authors:
- Winfried van den dool
- Patrick Forré
- Amir Habibian
- Yuki M. Asano
- Max Welling
arxiv_id: '2607.12789'
url: https://arxiv.org/abs/2607.12789
pdf_url: https://arxiv.org/pdf/2607.12789
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: LLM底层优化 · 注意力计算效率提升
tags:
- Attention Optimization
- Vector Quantization
- Triton Kernel
- Flash Attention
- Computational Efficiency
one_liner: 基于注意力权重自适应分配VQ码本容量，实现优于固定码本VQ注意力的精度效率trade-off
practical_value: '- 做长序列推荐/长对话Agent时，可替换原有VQ注意力，在不显著增加开销的前提下提升长序列（用户长行为、长对话上下文）建模精度

  - 可复用自适应码本分配思路，用于用户行为序列、商品特征的向量量化压缩，降低召回/排序阶段的向量存储与计算成本

  - 基于Triton内核适配Flash Attention tiled计算范式的工程实现思路可直接复用，最小化自定义注意力算子的落地 overhead'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 动机
Transformer 注意力 O(N²) 复杂度是长序列场景核心计算瓶颈，现有固定码本VQ注意力采用统一容量分配，高注意力区域量化精度不足、低注意力区域浪费容量，精度效率trade-off较差

### 方法关键点
1. 提出自适应向量量化注意力，前向传播时基于注意力重要度动态分配码本容量：对高注意力权重的码本用预训练子码本做细粒度量化，其余区域保持粗量化，整体复杂度仍维持 O(MN)
2. 基于自定义Triton内核实现全流程，适配Flash Attention的tiled计算范式，重要度打分、子码本插入、父码本替换等操作额外开销极低

### 关键结果
同等计算复杂度下，相比固定码本VQ注意力实现更优的精度效率trade-off
