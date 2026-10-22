---
title: 'PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States'
title_zh: PACE：线性注意力模型四比特循环状态的周期通道对齐编码方法
authors:
- Patrick Haller
- Filipe Laitenberger
- Alan Akbik
affiliations:
- Humboldt-Universität zu Berlin
arxiv_id: '2610.29545'
url: https://arxiv.org/abs/2610.29545
pdf_url: https://arxiv.org/pdf/2610.29545
published: '2026-10-20'
collected: '2026-10-22'
category: LLM
direction: 大语言模型推理优化 · 循环状态量化
tags:
- State Quantization
- Linear Attention
- Inference Optimization
- Low Precision
- Mamba
one_liner: 无训练的线性注意力4比特循环状态量化器，仅用8bit方案2/3内存达相近精度，保留解码加速
practical_value: '- 落地线性注意力LLM（如Mamba系列）做Agent/推荐推理时，可直接复用PACE的4比特量化方案，无需微调即可在仅2/3内存开销下接近8bit精度，大幅提升单卡并发序列数

  - 循环状态量化可借鉴通道对齐分组策略：针对delta值通道的幅值分布选择按列做量化分组，大幅降低4比特量化带来的精度损失

  - 推理部署可复用「8token周期刷新+解码缓冲」设计，既减少量化误差积累，又保留解码缓冲的吞吐量提升，实测batch>16时TPOT比bf16方案低18.6%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
线性注意力模型（如Mamba、Gated DeltaNet）用固定大小的循环状态替代KV cache，推理时单卡可承载的并发序列数受限于循环状态的内存占用；现有4比特状态量化方案每生成1个token就刷新量化一次，误差积累快，要么精度掉点严重，要么需要微调模型，无法直接落地。

### 方法关键点
- 周期量化：每dP（默认取8）个token才对循环状态做一次量化刷新，中间生成的token存在小解码缓冲里，减少量化次数降低误差积累，同时兼容现有解码缓冲的吞吐量优化
- 通道对齐量化分组：发现循环状态的大值集中在列（对应delta值的通道），因此按列（key轴）做量化分组共享scale，比传统按行分组的量化误差小
- 混合精度头分配：离线校准每层头的误差保留程度，把1/4误差保留最长的头保持8bit，其余用4bit，进一步平衡精度和内存

### 关键结果
实验覆盖4B~35B参数的Qwen3.5/3.6混合模型，对比基线包括全精度、DAMP INT8/INT4、Q-Mamba DSQ：
- PACE-4/8内存仅为DAMP INT8的2/3，在9B/27B/35B三个大模型上平均精度和DAMP INT8持平，比同内存的DAMP INT4高1~9个点
- PACE-4与Q-Mamba DSQ内存相同，平均精度高4~6个点
- 解码吞吐量方面，batch>16时，PACE-4的TPOT比bf16状态方案低18.6%，完全保留解码缓冲的加速效果

### 核心结论
线性注意力的循环状态量化不需要逐token刷新，适度降低量化频次+适配数据分布的分组策略，就能在无微调的前提下实现4比特量化的精度和性能双收益
