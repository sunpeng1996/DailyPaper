---
title: Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement
  Learning with Verifiable Rewards
title_zh: 面向可验证奖励LLM强化学习的频谱驱动自适应秩优化器
authors:
- Zhipeng Chen
- Wayne Xin Zhao
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2610.16533'
url: https://arxiv.org/abs/2610.16533
pdf_url: https://arxiv.org/pdf/2610.16533
published: '2026-10-11'
collected: '2026-10-14'
category: Training
direction: LLM RLVR训练 · 自适应秩优化
tags:
- RLVR
- Optimizer
- Adaptive Rank
- Spectral Analysis
- Low Rank Optimization
one_liner: 提出适配RLVR动态梯度特性的Ares优化器，多尺度LLM上稳定超过主流优化器
practical_value: '- 电商导购Agent、推荐文案生成的RLHF/RLVR偏好对齐训练，可直接替换AdamW为Ares，相同训练步数下提升任务效果，额外计算开销极低

  - LoRA微调、大推荐模型低秩更新类任务，可借鉴其动态秩估计思路：基于梯度频谱能量熵计算有效秩，用EMA平滑，避免固定秩导致的梯度信息丢失或资源浪费

  - 需高效做梯度分解的场景，可复用随机块幂迭代（RBPI）方法，相比全SVD大幅降低计算量，梯度频谱集中场景下精度损失可忽略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前RLVR（可验证奖励强化学习）是LLM训练推理能力的核心范式，但现有优化器均继承自SFT阶段，未适配RLVR特有的梯度特性。实验发现RLVR训练中梯度能量会逐渐向少量前导奇异分量集中，有效更新秩随训练持续下降，固定秩的低秩优化器（如GaLore）无法适配这种动态变化，容易出现梯度信息丢失或算力浪费，因此需要适配RLVR动态梯度几何特性的专用优化器。

### 方法关键点
- 梯度分解：用随机块幂迭代（RBPI）替代全SVD提取梯度前导奇异子空间，计算复杂度由$O(mn^2)$降至$O(qmn(k+p))$，大幅降低分解开销，适配RLVR梯度频谱集中的特性
- 动态秩估计：基于梯度奇异值的能量分布计算香农熵得到有效秩，通过EMA平滑秩的波动，实时适配训练过程中有效秩下降的趋势，避免固定秩的缺陷
- 低秩更新：截断梯度到当前有效秩对应的子空间，2D权重矩阵用低秩梯度执行类AdamW更新，1D参数保留原生AdamW更新，兼顾效果与稳定性

### 关键实验
在DAPO数学推理数据集上训练，7个数学推理benchmark测试，对比AdamW、GaLore、Muon等主流优化器：1.7B/4B/8B参数的Qwen3模型上，Ares比AdamW平均准确率分别高5.0/2.7/2.3个百分点，训练收敛速度比AdamW快约60%，单步更新开销仅略高于AdamW。

最值得记住的一句话：不同训练范式的梯度几何特性存在本质差异，优化器设计不能直接跨范式复用，需要适配目标训练场景的动态梯度特性。
