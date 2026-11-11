---
title: Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic
  Rounding
title_zh: 基于随机舍入消除RL后训练中BF16与FP16的收敛速度差距
authors:
- Mahdi Nazemi
- Oleg Rybakov
- Tijmen Blankevoort
- Asit Mishra
- Carlo del Mundo
affiliations:
- NVIDIA
arxiv_id: '2611.13545'
url: https://arxiv.org/abs/2611.13545
pdf_url: https://arxiv.org/pdf/2611.13545
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 大模型RL后训练 · 混合精度优化
tags:
- Mixed Precision Training
- Reinforcement Learning
- Stochastic Rounding
- BF16
- RLHF
one_liner: 用随机舍入优化BF16量化逻辑，消除RL后训练中BF16与FP16的收敛速度差距且漂移更低
practical_value: '- 做电商导购Agent、生成式推荐模型的RL对齐（RLHF/RLAIF/GRPO）时，若用BF16低学习率训练，可直接在FP32影子权重转BF16的步骤加随机舍入，无需调高学习率，既能匹配FP16收敛速度，还能降低模型漂移，避免对齐后丢失基础能力

  - 工程实现成本极低：仅需在每次optimizer step后做1次随机舍入，其余逻辑无需修改，也不需要FP16的loss scaling，可避免大模型训练溢出问题

  - 用vLLM做RL rollout时若出现BF16 reward掉点，优先关闭TorchInductor优化，额外开销不到2%即可解决大部分训练-推理数值不匹配问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
BF16因动态范围与FP32一致，在LLM预训练中被广泛使用，但在带可验证奖励的RL后训练（如RLHF、GRPO，常用于Agent、推理模型对齐）场景下，学习率通常低至1e-6级别，标准四舍五入的BF16训练收敛速度远慢于FP16；调高BF16学习率会导致与基座模型的KL漂移大幅上升，FP16则需要loss scaling且大模型训练易溢出，现有方案均存在明显缺陷。

### 方法关键点
- 定位收敛慢根因为**权重粘滞**：BF16仅7位尾数，FP32影子权重用四舍五入转BF16时，小梯度更新不足以让BF16权重跳变，多步更新都无法生效
- 用随机舍入（SR）替换四舍五入：量化时按FP32权重在两个相邻BF16值的距离分配舍入概率，期望上BF16权重更新与FP32完全对齐，消除系统性误差
- 工程简化方案：仅需在每次optimizer更新后做1次随机舍入，前向/rollout全用舍入后的BF16权重，其余数值转换仍用四舍五入即可，无需修改其他训练逻辑

### 关键实验
数据集覆盖MATH-1460、DAPO-Math-17k，测试模型含1.5B、14B、30B等规格，对比baseline为标准BF16（四舍五入）、原生FP16：
- BF16+SR收敛速度完全匹配FP16，比标准BF16快2倍以上
- 相同reward水平下，BF16+SR的KL漂移比调高2倍学习率的BF16低33%，与FP16漂移水平相当
- 关闭vLLM的TorchInductor优化即可解决BF16 reward崩溃问题，额外开销<2%

### 核心结论
低学习率RL后训练场景下，BF16的权重粘滞问题比数值溢出影响更大，随机舍入是性价比极高的优化方案。
