---
title: Towards Full Pipeline FP8 Reinforcement Learning for LLMs
title_zh: 面向大语言模型全流水线FP8量化的强化学习优化方法
authors:
- Fanchao Chen
- Ziheng Jiang
- Ziyun Wei
- Zheng Zhong
- Du Li
- Chi Zhang
- Haibin Lin
- Shivaram Venkataraman
affiliations:
- University of Wisconsin–Madison
- ByteDance Seed
arxiv_id: '2609.22870'
url: https://arxiv.org/abs/2609.22870
pdf_url: https://arxiv.org/pdf/2609.22870
published: '2026-09-18'
collected: '2026-09-23'
category: Training
direction: LLM低精度训练 · FP8 RL稳定性优化
tags:
- FP8
- Reinforcement Learning
- LLM Training
- Quantization
- GRPO
- DAPO
one_liner: 提出动态校准裁剪机制解决全流水线FP8 LLM RL训练不稳定问题，最高可获1.5倍BF16训练吞吐量
practical_value: '- 业务侧做LLM RL对齐（如电商Agent、个性化文案生成模型的RLHF/RLAIF）时，可直接复用Calibrated Clipping实现全流水线FP8量化，在不损失效果的前提下最高提升1.5倍训练吞吐量，降低大模型对齐成本

  - 若使用PPO/GRPO/DAPO等带裁剪的RL算法时遇到低精度训练不稳定、输出乱码/熵爆炸问题，可优先排查量化噪声放大导致的重要性比过裁剪问题，无需盲目调整学习率或batch
  size

  - 全流水线FP8训练时可采用论文的周期性校准策略，每10~40步做一次BF16影子前向计算校准裁剪边界，额外计算开销极低，同时避免固定裁剪边界带来的过罚或训练崩溃'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
FP8量化已在LLM预训练、推理阶段广泛落地，可显著提升计算效率，但全流水线FP8 LLM RL训练存在严重不稳定问题，表现为训练中途熵突增、输出乱码。此前研究仅解决rollout与训练的精度不匹配问题，未发现量化噪声放大导致的重要性比过裁剪问题，导致RL训练效果大幅下降甚至崩溃，亟需低成本的稳定解决方案。

### 方法关键点
- 定位不稳定根源：FP8量化噪声在重要性比计算时被放大1.7~2.9倍，导致负优势token的重要性比被过度裁剪，本该惩罚的坏输出梯度被清零，乱码样本不断累积
- 提出Calibrated Clipping两步校准：首先用BF16参考分布对齐负优势token的下裁剪分位数，避免下边界过裁剪；再重平衡上下裁剪边界使正负更新比与BF16一致，避免过罚
- 采用低开销周期性校准：每20步做一次BF16影子前向计算更新裁剪边界，加入边界平滑更新机制避免训练波动，额外开销可忽略

### 关键结果
在8B~32B模型、GRPO/DAPO两种主流RL算法、三种FP8缩放粒度下验证：纯FP8训练平均效果比BF16低3.5~11.5分，加入Calibrated Clipping后效果恢复到BF16水平，差距缩小到0.2~1.7分；全流水线FP8训练吞吐量最高达BF16的1.5倍，叠加FP8 rollout的30%生成加速，全流程效率提升显著。

最值得记住的一句话：全流水线FP8 RL的不稳定核心不是训练-推理精度差，而是量化噪声放大扭曲了PPO类算法的信任区域，仅需动态校准裁剪边界即可在几乎无额外开销的情况下解决问题。
