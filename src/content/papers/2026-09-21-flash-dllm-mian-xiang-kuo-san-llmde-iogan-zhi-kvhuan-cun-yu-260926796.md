---
title: 'Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient
  Diffusion LLMs'
title_zh: Flash-dLLM：面向扩散LLM的IO感知KV缓存与并行解码加速框架
authors:
- Quan Nguyen-Tri
- Mukul Ranjan
- Zhiqiang Shen
affiliations:
- VILA Lab, MBZUAI
arxiv_id: '2609.26796'
url: https://arxiv.org/abs/2609.26796
pdf_url: https://arxiv.org/pdf/2609.26796
published: '2026-09-21'
collected: '2026-09-23'
category: LLM
direction: 扩散大模型 · 推理加速 · KV缓存优化
tags:
- dLLM
- KV cache
- Parallel Decoding
- Inference Acceleration
- IO Optimization
one_liner: 无需训练的扩散LLM推理加速框架，联合优化IO感知KV缓存与自验证并行解码，兼顾速度与内存效率
practical_value: '- 生成式推荐/Agent服务使用dLLM时，可直接复用IO感知fused KV kernel设计，合并QKV投影、RoPE、缓存写入步骤，减少HBM读写开销，提升单卡推理吞吐量，降低响应延迟

  - dLLM做批量文案生成、query推荐任务时，可复用Flash-Verify自验证机制，无需额外小模型做草稿生成，靠同一模型的双视图注意力做token校验，在不损失生成质量的前提下提升单步解码token数

  - 高并发dLLM推理服务（如大促个性化文案生成）可借鉴选择性缓存更新策略，仅保留attention权重最高的top-k token的KV缓存，降低峰值显存占用，支撑更大batch
  size

  - 可参考论文的accuracy-throughput帕累托调优方法，根据业务对延迟和准确率的要求，动态调整track budget、置信度阈值，找到最优运营点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Diffusion LLM（dLLM）作为非自回归生成方案，在可控生成、并行性上优于传统自回归LLM，但现有推理缺乏适配的KV缓存和并行解码机制，联合使用缓存复用与并行token校验时会出现严重GPU IO瓶颈，同时dLLM迭代解码过程中存在大量冗余KV读写、低影响token计算，导致推理效率低、落地门槛高。

### 方法关键点
- 提出IO感知的Flash-Cache：设计融合CUDA内核，将QKV投影、RoPE、KV缓存写入合并为单步操作，消除中间张量的HBM读写；新增调度式Flash Attention，用块表管理变长序列批次，避免padding开销；仅缓存attention权重最高的top-k关键token，进一步降低计算和显存开销。
- 提出Flash-Verify自验证并行解码策略：dLLM自身同时充当草稿生成器和校验器，无需额外辅助模型；单次迭代先生成候选token，对低于置信度阈值的token构造双视图（草稿视图+MASK视图）查询，用因果掩码隔离视图，仅当双视图预测一致且MASK视图置信度达标时才接受token，大幅提升单步可解码token数。
- 整个框架完全无需训练，适配现有开源dLLM。

### 关键结果
在A100 80GB上基于LLaDA-1.5测试，对比SOTA baseline Elastic-Cache，在GSM8K上获得5.1×速度提升，HumanEval上获得11.0×速度提升；batch size 16时显存占用比Fast-dLLM低48%，吞吐量线性扩展到batch size 32无OOM，生成准确率损失控制在1.8个百分点以内。

### 核心结论
dLLM推理的核心瓶颈并非浮点计算，而是GPU内存IO开销，通过内核融合、选择性缓存、自验证并行解码的联合优化，可以在几乎不损失生成质量的前提下实现数量级的推理加速。
