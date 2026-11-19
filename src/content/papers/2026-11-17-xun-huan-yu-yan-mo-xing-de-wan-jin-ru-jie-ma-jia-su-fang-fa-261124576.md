---
title: Late Entry in Looped Language Models
title_zh: 循环语言模型的晚进入解码加速方法
authors:
- Ziqi Jin
- Jiaxi Li
- Weiwen Xu
- Aixin Sun
affiliations:
- Nanyang Technological University
- Singapore University of Technology and Design
- The Chinese University of Hong Kong
arxiv_id: '2611.24576'
url: https://arxiv.org/abs/2611.24576
pdf_url: https://arxiv.org/pdf/2611.24576
published: '2026-11-17'
collected: '2026-11-19'
category: LLM
direction: 循环大语言模型 · 推理加速优化
tags:
- Looped-LLM
- Inference-Optimization
- KV-Cache
- Early-Exit
- Wake-Verification
one_liner: 提出循环LLM晚进入+Wake验证机制，无损/可控损失下最高实现12.5倍推理加速
practical_value: '- 面向Agent实时交互、生成式推荐文案批量生成等低延迟场景，可复用晚进入思路，将有限的串行计算资源分配给模型最后K轮，复用深KV缓存替代token本地早期计算，大幅降低延迟

  - 推理精度与速度的trade-off可复用Wake验证的logit margin阈值设计，根据业务对输出错误的容忍度调整τ，在可控损失范围内获取最大速度提升，适配电商推荐不同场景的精度要求

  - KV缓存跨步流水线补全的工程思路可迁移到生成式推荐的自回归解码流程，利用GPU内存绑定特性，将全量缓存补全的计算并行嵌入现有解码步骤，几乎无额外延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
循环语言模型（Looped LLM）通过迭代共享Transformer层栈，在小参数量下实现了媲美大模型的推理能力，但自回归解码时每生成一个token需执行T次前向传播，迭代深度直接转化为串行延迟。传统早退出策略仅执行前K轮后停止，会将上下文KV缓存截断为浅层状态，导致后续token只能访问不成熟的上下文表示，无法兼顾速度与推理精度。

### 方法关键点
- **晚进入（Late Entry）策略**：新生成的token跳过前T-K轮计算，直接输入到最后K轮，基于已完成全T轮计算的深上下文KV缓存做推理，仅需轻量微调即可解决输入隐藏态的范数不匹配问题。
- **Wake验证机制**：已暂存的token在后续解码步骤中作为并行批量行搭便车完成全T轮计算，在同一次输出GEMM中验证结果，通过logit-margin阈值τ支持三种模式：τ=0时完全匹配全T轮解码的输出，0<τ<∞时可控损失，τ=∞时无回滚最大速度，三种模式统一在单个静态CUDA图中运行。
- **流水线缓存补全**：利用单序列解码时GPU为内存带宽绑定的特性，补全全量KV缓存的并行计算几乎不增加额外延迟。

### 关键实验结果
在Ouro-2.6B（T=4）上，K=2的τ=0无损模式实现5.2×速度提升，GSM8K精度比K=4块解码高26%；τ=∞模式达6.8×速度，比同速度的训练后早退出方案高16.9个精度点。在Huginn-3.5B上，随着T从32扩大到64，τ=0无损模式速度达6.1~8.4×，τ=∞模式最高达12.5×，回滚率随T增大降低21.5×。

### 核心结论
循环LLM中，深上下文KV缓存的价值远高于token本地的早期轮次计算，将有限的串行计算资源分配给最后几轮的效果显著优于前几轮。
