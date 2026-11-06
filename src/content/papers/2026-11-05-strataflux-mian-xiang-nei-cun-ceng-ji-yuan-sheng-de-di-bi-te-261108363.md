---
title: 'StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference'
title_zh: StrataFlux：面向内存层级原生的低比特LLM推理框架
authors:
- Jake Hyun
- Ziyu Zhao
- Jae-sun Seo
- Mohamed S. Abdelfattah
affiliations:
- Cornell University
- Carnegie Mellon University
arxiv_id: '2611.08363'
url: https://arxiv.org/abs/2611.08363
pdf_url: https://arxiv.org/pdf/2611.08363
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM推理优化 · 低比特量化+KV缓存
tags:
- Low-bit Quantization
- KV Cache
- Inference Optimization
- Memory Hierarchy
- LLM Serving
one_liner: 通过跨内存层级的选择性精度流实现低比特LLM推理兼顾精度、速度与显存占用
practical_value: '- 低比特量化精度修复思路可迁移到推荐侧LLM服务：商品文案生成、Agent交互场景的小参数量化部署，用分层内存存精度补全数据，不增显存前提下提升精度，几乎无吞吐损失

  - KV cache选择性精度优化可直接用于长上下文电商导购Agent：处理100K+长度的用户历史、商品详情时，仅对高attention权重的token补全精度，降低长上下文显存占用且不损失应答准确率

  - fetch lead/lag异步调度思路可复用在推荐异构计算场景：CPU/GPU混合部署的召回/排序服务，将非核心计算异步延迟执行，掩盖数据传输延迟，提升整体吞吐'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
低比特量化是LLM部署降低显存、提升吞吐的核心手段，但会显著损失精度；传统精度卸载方案又会因数据传输延迟拖慢推理速度，两者的权衡一直是LLM落地（尤其是消费级GPU、端侧部署）的核心痛点，迫切需要同时兼顾低显存、高速度、高精度的推理方案。

### 方法关键点
- 选择性精度流设计：GPU显存仅存放2-4bit低比特权重与KV cache作为计算基底，更高精度的补全残差存储在主机内存/SSD中，仅对激活值大的权重通道、attention权重高的KV token按需拉取补全
- 异步精度调度：引入fetch lead（提前数个Transformer块预测需要补全的通道预拉取）、fetch lag（延后数个块补全精度），将数据传输与计算完全重叠，掩盖异构内存的访问延迟
- 跨解码步精度复用：缓存拉取过的精度补全数据，避免重复传输，进一步降低开销

### 关键结果
在RTX 5090上测试：2bit权重的Llama-3.1-8B-Instruct的WikiText-2困惑度从9.46降至8.40，保留基础量化版95.4%的吞吐；2bit权重+2bit KV的Qwen3-8B的AIME 2024/2025准确率从11.0%提升至47.1%，显存占用完全不变；128K长上下文场景下，3bit权重+2bit KV的方案显存占用仅为vLLM 4bit AWQ+8bit KV的一半，精度与吞吐完全相当。

**最值得记住的一句话**：GPU显存里的低比特精度不需要是推理的精度上限，异构内存的传输延迟也不需要决定解码速度。
