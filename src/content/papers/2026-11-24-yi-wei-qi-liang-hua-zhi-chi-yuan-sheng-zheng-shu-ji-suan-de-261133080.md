---
title: 'Shifter Quantization: Compact Representations for Native Integer Computation'
title_zh: 移位器量化：支持原生整数计算的LLM紧凑表示方法
authors:
- Yufeng Huang
affiliations:
- Columbia University
arxiv_id: '2611.33080'
url: https://arxiv.org/abs/2611.33080
pdf_url: https://arxiv.org/pdf/2611.33080
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM低比特量化 · 原生整数推理加速
tags:
- Quantization
- LLM_Inference
- INT4
- INT8
- GPU_Acceleration
one_liner: 提出Shifter Quantization系列低比特量化方案，兼顾LLM推理精度与硬件利用效率
practical_value: '- 可将小粒度组量化+移位重构思路迁移到KV cache量化，降低长上下文对话Agent、长序列推荐场景的显存占用，同时避免传统组量化MMA利用率低的问题

  - 端侧部署的电商导购Agent、生成式推荐场景可优先考虑2bit SHI2方案，RTX 5090下可达3.77× llama.cpp Q2_K的prefill吞吐量，KL仅下降6.6-7.8%，适配低预算本地化部署需求

  - SHI的分组校正多乘积路径设计可复用在现有INT4推理框架中，无需更换硬件即可提升生成式推荐服务的推理速度，精度损失可控'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM组量化方法虽然能提升低比特精度，但不同组的缩放系数会导致GPU整数矩阵乘累加（MMA）无法跨全维度计算，硬件利用率低，推理速度瓶颈明显，无法满足长上下文Agent、大流量生成式推荐等场景的低延迟需求。

### 方法关键点
- 核心Shifter Quantization（SQ）：通过附加共享位、组移位、截断三个轻量位运算，将低比特存储的权重重构为原生宽度整数 operand，支持MMA跨全归约维度计算，采用G4/G8的更小量化组降低量化误差
- 衍生Shifter Integer（SHI）变体：主乘积采用INT4运算，分组校正通过更短的整数乘积实现，额外计算量仅为主乘积的1/8（G8组），充分利用INT4硬件算力
- 配套signed Hadamard旋转预处理权重，消除离群值影响，进一步降低量化误差

### 关键结果
基于WikiText-2数据集验证，对比llama.cpp Q2_K/Q4_K、NInfer组量化、vLLM在线FP8等基线：2bit场景下SQ2/SHI2实现2.71-3.77× 4096-token prefill吞吐量，KL下降6.6-7.8%；4bit场景下SQ4实现1.43-2.47× prefill吞吐量，KL比基线低24-40%；8bit场景下SQ8比vLLM在线FP8单batch prefill吞吐量高27.4%，KL低72.7%。

> 最值得记住：低比特量化的效率提升不能只看存储压缩，更要让存储格式匹配硬件原生指令的计算模式，才能真正把压缩收益转化为推理速度提升。
