---
title: 'WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms'
title_zh: WUSH-KV：基于数据自适应变换的KV缓存量化方法
authors:
- Jiale Chen
- Vage Egiazarian
- Eldar Kurtić
- Torsten Hoefler
- Dan Alistarh
affiliations:
- Institute of Science and Technology Austria (ISTA)
- Red Hat AI
- ETH Zürich
arxiv_id: '2609.38121'
url: https://arxiv.org/abs/2609.38121
pdf_url: https://arxiv.org/pdf/2609.38121
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM推理优化 · KV cache量化
tags:
- KV cache
- Quantization
- LLM Inference
- Adaptive Transform
- Low-bit Compression
one_liner: 提出数据自适应WUSH变换实现低比特KV缓存量化，2比特精度显著优于现有SOTA方案
practical_value: '- 部署LLM驱动的电商Agent、生成式推荐系统时，可直接集成WUSH-KV降低长上下文推理显存占用，2比特下精度损失远低于OSCAR等现有方案，支持单卡部署更大模型或更长用户行为上下文

  - Value侧变换可提前折叠进模型权重无额外在线开销，仅需承担Key侧轻量变换计算，工程落地性价比高，可直接兼容SGLang等主流推理框架

  - 保留注意力sink和最近窗口全精度缓存的设计可复用在其他KV压缩方案中，平衡压缩比和推理精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理中，KV缓存的显存和带宽开销随序列长度、批量大小线性增长，成为性能瓶颈。低比特量化是核心优化方向，但现有方案要么量化误差大，要么正交变换的优化空间受限，2比特下精度下降明显，无法支撑长上下文Agent、生成式推荐等场景的稳定推理。

### 方法关键点
- 基于WUSH数据感知变换，针对Key、Value分别构建独立的自适应变换，Value侧变换可提前折叠进模型权重，无在线开销，Key侧变换在RoPE后应用，避免位置依赖的额外计算
- 变换可与任意裁剪量化器搭配，理论证明搭配QuEST INT量化器时WUSH变换在敏感度均衡的变换族中接近最优
- 保留前S_sink个注意力sink token和最近S_keep个token为全精度，其余token批量量化，进一步降低误差

### 关键实验
校准采用FineWeb-Edu数据集，在Qwen3 4B/8B/32B模型上测试，对比OSCAR、Hadamard变换等基线：2比特量化下，WikiText-2困惑度仅10.51，远低于OSCAR的13.74，接近全精度基线的9.72；下游任务上，Qwen3-8B的4个测试任务（AIME2025、MATH-500、GPQA、LiveCodeBench）精度全部超过OSCAR，32B模型LiveCodeBench任务精度比OSCAR高15.3个百分点。

### 核心结论
针对KV缓存的量化不能只关注分布压缩，还要结合下游计算的敏感度设计自适应变换，才能在极低比特下保留接近全精度的推理效果
