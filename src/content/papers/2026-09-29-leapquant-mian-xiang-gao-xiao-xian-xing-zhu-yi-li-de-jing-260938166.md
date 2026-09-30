---
title: 'LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization'
title_zh: LeapQuant：面向高效线性注意力的精准循环状态量化
authors:
- Yi Pan
- Haocheng Xi
- Kan Zhu
- Xingyang Li
- Yibo Wu
- Mayank Mishra
- Hongtao Zhang
- William X. Zheng
- Baris Kasikci
- Song Han
affiliations:
- UC Berkeley
- University of Washington
- MIT
- Perplexity AI
- NVIDIA
arxiv_id: '2609.38166'
url: https://arxiv.org/abs/2609.38166
pdf_url: https://arxiv.org/pdf/2609.38166
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM推理优化 · 线性注意力量化
tags:
- Quantization
- Linear Attention
- LLM Inference
- Recurrent State
- Low-bit Optimization
one_liner: 训练免微调的线性注意力循环状态量化方案，近无损8bit量化，推理最高加速3.7倍
practical_value: '- 线性注意力部署时可复用per-window量化思路，降低量化误差累积，适配长上下文Agent、电商长文本商品理解场景的低延迟需求

  - 量化前抽取高秩离群点作为Compensator Token保留高精度的思路，可迁移到KV cache、语义向量量化等场景，在压缩率和精度间取得平衡

  - 训练免微调的量化方案无需重新训练模型，可直接落地到现有基于Qwen、GLM等大模型的推荐文案生成、用户意图理解业务'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前长上下文LLM广泛采用GDN、KDA等线性注意力架构，其固定大小循环状态的反复读写是推理HBM带宽瓶颈，直接低比特量化会因误差累积、状态离群点导致精度暴跌，现有量化方案多适配KV缓存或Mamba架构，无法直接用于通用线性注意力的循环状态压缩。

### 方法关键点
- 采用per-window量化：默认每16个token才对循环状态做一次量化，窗口内保留高精度更新缓存，大幅降低误差累积频率
- 引入Compensator Token：量化前用幂迭代抽取状态的前4个秩1离群分量，保留为高精度令牌，复用常规token更新路径无额外开销
- 量化前对残差做通道平滑，进一步降低残差动态范围，提升低比特量化精度；整体方案训练免微调，无需校准数据

### 关键实验
在Qwen、Kimi、GLM三大模型族的12组模型-任务对（AIME、GPQA、MMLU-Pro、LiveCodeBench等）上测试，对比FP32、BF16、KVQuant、TurboQuant等基线：8bit量化下精度与FP32完全持平，状态内存带宽降低3.4倍，端到端内存占用最高降56%，B200/RTX 5090等GPU上核级加速2.05~3.70倍，端到端推理平均加速1.47倍。

### 核心结论
线性注意力的循环状态量化不需要每步都做，通过窗口化+离群点保留即可在完全免训练的前提下实现近无损的低比特压缩。
