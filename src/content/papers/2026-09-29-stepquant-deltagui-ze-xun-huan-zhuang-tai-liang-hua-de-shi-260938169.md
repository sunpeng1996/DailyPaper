---
title: 'STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization'
title_zh: STEPQuant：Delta规则循环状态量化的时空误差感知优化框架
authors:
- Bingchen Yao
- Haobo Xu
- Haokun Lin
- Yichen Wu
- Ziyu Guo
- Renrui Zhang
- Zhichao Lu
- Zhenan Sun
- Ying Wei
affiliations:
- Zhejiang University
- Institute of Automation, CAS
- Tsinghua University
- City University of Hong Kong
- Harvard University
arxiv_id: '2609.38169'
url: https://arxiv.org/abs/2609.38169
pdf_url: https://arxiv.org/pdf/2609.38169
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: 大模型推理优化 · 循环状态低比特量化
tags:
- Quantization
- Linear Attention
- Recurrent State
- LLM Serving
- SGLang
one_liner: 针对线性注意力循环状态量化误差传播问题，提出时空感知训练后量化框架，6bit精度接近FP32性能
practical_value: '- 业务中用到线性注意力/RetNet类大模型做Agent推理、文案生成时，可直接复用STEPQuant量化逻辑，几乎无损前提下将循环状态压缩5倍以上，大幅提升并发承载量、降低推理成本

  - 量化bit分配思路可迁移到KV cache压缩、RAG召回向量量化、用户/商品Embedding存储场景：优先给生命周期长、对输出影响大的组分分配更高精度，仅保留极小比例高风险组分用高精度，平衡压缩比和效果

  - 双轴拟合缩放方法可迁移到多维度特征的低比特存储：分别对行、列维度按影响权重拟合缩放因子，比单轴量化的重建误差低30%以上

  - 工程实现可参考其SGLang核优化思路：融合量化/反量化与状态更新算子，用多CUDA流重叠计算，抵消量化带来的latency开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
线性注意力用固定大小循环状态替代随序列长度增长的KV cache，解决长上下文推理内存瓶颈，但高并发场景下每个请求独占的循环状态会成为新的内存瓶颈：Qwen3.8-27B在70并发时FP32状态池内存超过BF16模型权重；直接用均匀量化会导致误差随解码步传播，6bit均匀量化的推理精度就出现暴跌，8bit也有明显精度gap。

### 方法关键点
- 时空联合误差分析：时间维度上生命周期越长的状态单元误差累积越严重，空间维度上不同key行的量化误差对输出的影响差异可达10倍以上
- 生命周期感知bit分配：离线校准每个状态单元的内存保留时长，固定比特预算下给误差大、生命周期长的单元分配更高精度，仅保留1.39%的高风险单元用FP16作为稀疏pivot
- key行感知双轴拟合：分别给key行、value列分配独立缩放因子，行缩放同时考虑行数值大小和输出影响权重，列缩放优先降低高影响行的重建误差，适配状态矩阵双维度数值分布
- 工程优化：和SGLang深度整合，融合状态重建、Delta更新、输出计算算子，用独立CUDA流做量化回写，重叠计算降低延迟

### 关键实验
在Qwen3.8-27B、Kimi-Linear-48B两个工业级大模型上测试，覆盖7个长生成推理任务、6个短生成理解任务，对比均匀INT4/6/8、Q-Mamba等基线：6bit STEPQuant精度和FP32状态几乎持平，长任务平均精度仅差0.01个百分点，比均匀INT6高35个百分点以上；4bit STEPQuant精度超过均匀INT8，Qwen上短任务平均精度仅比FP32低0.15个百分点；工程上6bit配置下循环状态压缩5倍以上，Qwen+4bit AWQ权重的全服务内存最高降低68.7%，状态更新速度提升2.91倍。

最值得记住的一句话：循环状态量化的误差影响由时间维度的生命周期、空间维度的误差位置共同决定，针对性分配精度和缩放因子可以在极低比特下实现几乎无损的压缩。
