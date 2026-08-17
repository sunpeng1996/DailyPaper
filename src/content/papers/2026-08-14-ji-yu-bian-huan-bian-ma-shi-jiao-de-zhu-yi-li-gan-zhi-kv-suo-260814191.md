---
title: KV Cache Compression Through the Lens of Transform Coding
title_zh: 基于变换编码视角的注意力感知KV Cache压缩方法
authors:
- Hannah Laus
- Claudio Mayrink Verdun
- Hao Wang
- Flavio du Pin Calmon
- Felix Krahmer
affiliations:
- Technical University of Munich
- Massachusetts Institute of Technology
- Harvard University
- Red Hat AI Innovation Team
- Technical University of Darmstadt
arxiv_id: '2608.14191'
url: https://arxiv.org/abs/2608.14191
pdf_url: https://arxiv.org/pdf/2608.14191
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM推理优化 · KV Cache压缩
tags:
- KV cache
- Transform Coding
- Quantization
- Long Context Inference
- Reverse Waterfilling
one_liner: 提出注意力感知变换编码AATC方法，实现5.8×KV Cache压缩下长上下文推理近无损
practical_value: '- 长会话Agent、长文本生成式推荐场景下可直接复用AATC方案，5.8倍无损KV Cache压缩可大幅降低单卡推理内存开销，提升长上下文请求的并发承载量，无需修改模型结构

  - 其注意力感知失真分解思路可迁移到推荐模型特征压缩、量化场景：无需一味追求原始特征的重建误差最小，而是基于误差对下游排序/召回结果的影响权重分配量化比特，可在同等压缩比下降低业务指标损失

  - 离线校准+在线轻量化变换的架构落地成本极低，仅需用业务场景的少量样本做校准即可得到适配业务数据分布的比特分配策略，无需重训模型，可快速接入现有推理链路'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理中，KV Cache随上下文长度线性增长，是内存和 latency 核心瓶颈；现有量化方法仅最小化缓存本身的重建误差，未考虑误差在注意力机制中的传播规律，容易在长上下文、复杂推理场景下出现明显精度下降。

### 方法关键点
- 推导白噪声量化假设下的注意力感知失真公式，将量化对输出的影响分解为独立的Key、Value贡献项，可因子化到token和通道维度，统一了现有KV压缩方法的优化目标
- 离线校准阶段先对Key/Value投影矩阵做基于白化的SVD变换，实现特征去相关和能量重排，符合变换编码的最优比特分配前提
- 基于校准集数据用反向注水算法做全局通道级比特分配：给对注意力输出影响大的通道分配更多比特，影响小的通道分配低比特甚至0比特，自动适配不同层、不同特征的重要性
- 在线推理阶段仅需对token做线性变换后量化缓存，重建开销极低，无需修改注意力计算逻辑

### 关键实验结果
在Llama-3.1-8B-Instruct和Qwen-2.5-7B-Instruct上，跨LongBench、RULER、GSM8K、MMLU-Pro、MATH-500等长上下文和推理基准测试，对比KIVI、PALU、KVQuant等SOTA基线，AATC在5.8×压缩比下所有测试指标均与FP16基线无统计差异；在Qwen的RULER-32k和MMLU-Pro数学任务上比最强基线分别高7.2和16.8个点，7×压缩下仍保持长上下文精度稳定。

最值得记住的一句话：KV Cache压缩的核心优化目标并非缓存本身的重建误差最小，而是注意力输出的失真最小，基于误差传播权重的比特分配可实现更高压缩比下的精度无损。
