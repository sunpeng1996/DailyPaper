---
title: 'miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement
  Learning'
title_zh: miniTE：消除原生NVFP4强化学习执行差异的轻量训练框架
authors:
- Zhen Li
- Mingfa Feng
- Yiming Zhang
- Yang Yu
- Changhai Zhou
- Pengxiang Li
- Dongkuan Wu
- Congkai Xie
- Hongxia Yang
affiliations:
- InfiX.ai
- NVIDIA
arxiv_id: '2610.23928'
url: https://arxiv.org/abs/2610.23928
pdf_url: https://arxiv.org/pdf/2610.23928
published: '2026-10-06'
collected: '2026-10-27'
category: Training
direction: 低比特LLM强化学习训练优化
tags:
- Low-bit Training
- NVFP4
- Reinforcement Learning
- MoE
- LLM
one_liner: 提出轻量框架miniTE，实现稳定高效的原生W4A4低比特LLM RL训练，效果接近BF16、吞吐量大幅领先
practical_value: '- 做电商导购LLM、推荐Agent的RL对齐训练时，可直接复用miniTE的W4A4前向+BF16反向配置，在损失不到3%效果的前提下提升39%训练吞吐量，大幅降低大模型RL的计算成本

  - 遇到低比特量化后RL训练不稳定的问题时，可复用miniTE的三层跨引擎诊断逻辑（量化操作数/专家输出/策略评估边界校验），快速定位采样器与学习器的数值差异来源

  - 部署MoE结构的电商排序/生成式推荐模型时，可复用per-token激活缩放+联合优化量化与分组GEMM的trick，降低低比特MoE的推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
原生NVFP4低比特计算可大幅加速LLM RL训练，但现有方案仅匹配权重和数值格式，忽略采样器与学习器的跨引擎执行差异，导致RL训练不稳定、效果损失严重，无法充分释放低比特计算的性能优势。

### 方法关键点
- 三层跨引擎执行诊断机制：分别校验量化操作数、专家输出、策略评估三个边界的数值一致性，精准定位执行差异来源
- 原生W4A4训练路径：专家前向采用per-token激活缩放+FP32 epilogue重缩放，反向保留BF16精度，无需修改原有RL目标即可实现数值对齐
- 联合优化量化与分组GEMM数据通路：共享量化元数据，消除冗余的operand预处理开销，提升低比特计算的实际吞吐量

### 关键实验结果
基于Qwen3-30B-A3B MoE模型，对比BF16、原生TE NVFP4 baseline：
1. 数学基准测试平均得分56.35%，仅比BF16低2.49个百分点，比naive NVFP4高1.78个百分点
2. 单B300 GPU节点学习器吞吐量达33540 tokens/s，是BF16的1.39倍、TE NVFP4的1.47倍
3. 专家前向速度相比TE U3045提升2.46倍

### 核心洞察
低比特RL训练的核心瓶颈不是量化误差，而是跨引擎的执行一致性，仅匹配数值格式无法保证稳定训练，需要从算子实现到执行路径全链路对齐
