---
title: 'ParaTTT: Parallelizing Test-Time Training Layers with Deep Memories'
title_zh: ParaTTT：面向深度记忆的测试时训练层并行化算法
authors:
- Noel Loo
- Neehal Tumma
- T. Konstantin Rusch
- Mathias Lechner
- Alexander Amini
- Daniela Rus
affiliations:
- MIT CSAIL
- Liquid AI
- Max Planck Institute for Intelligent Systems
arxiv_id: '2610.38255'
url: https://arxiv.org/abs/2610.38255
pdf_url: https://arxiv.org/pdf/2610.38255
published: '2026-10-28'
collected: '2026-10-30'
category: LLM
direction: LLM 循环记忆层并行训练优化
tags:
- Test-Time-Training
- Parallel-Computing
- Recurrent-LLM
- Mamba
- Nonlinear-Memory
one_liner: 提出迭代优化梯度轨迹的ParaTTT算法，实现非线性TTT层高效并行，性能超Mamba-2等线性循环模型
practical_value: '- 长序列用户行为建模、Agent会话记忆等场景可直接复用ParaTTT架构，在近似Mamba-2推理延迟的前提下，记忆召回率提升10%以上

  - 迭代逼近精确梯度的思路可迁移到推荐系统的在线实时训练模块，2次迭代即可兼顾并行训练效率与逐样本更新的精度

  - 解码无额外开销的特性完美适配搜推场景的离线预训练+在线低延迟推理架构，不需要改造线上推理链路即可落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有测试时训练（TTT）非线性记忆层表达能力显著优于Gated DeltaNet、Mamba-2等线性循环架构，能更好建模长序列依赖，但无法实现块级并行训练：现有块近似方案精度损失大，训练速度比线性循环慢数倍，存在不可调和的精度-速度权衡，制约了非线性TTT层在大模型中的落地。
### 方法关键点
- 提出迭代优化内层梯度轨迹的并行框架，每次迭代包含三次块级并行遍历：前向传播计算特征轨迹、门控delta规则计算读入轨迹与特征梯度、反向传播更新梯度估计，精确的在线梯度下降是迭代的不动点
- 仅需2次迭代即可逼近精确的逐token梯度更新效果，解码阶段完全不需要迭代，仅预训练/预fill阶段产生额外开销
- 支持任意深度的TTT记忆层，核心算子可复用现有Mamba、Gated DeltaNet的块级并行实现，工程改造成本极低
### 关键实验
在SlimPajama数据集训练340M、1.3B参数模型，对比Gated DeltaNet、Mamba-2、Transformer、TTT-MLP等基线：4K上下文下，2次迭代的ParaTTT在匹配TTT-MLP块近似精度时速度快32倍，340M全模型训练速度比TTT-MLP快4.9倍；效果上，Perplexity优于所有线性循环基线，SWDE、FDA等记忆召回任务指标比Mamba-2高10~20pct，32K上下文针在草堆（NIAH）召回率达16%，是同参数Mamba-2的13倍。
### 核心结论
非线性TTT记忆层的并行瓶颈可以通过迭代梯度估计的方式突破，仅2次迭代即可兼顾训练效率与表达能力，大幅缩小了非线性循环与线性循环架构的效率差距。
