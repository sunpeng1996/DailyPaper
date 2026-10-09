---
title: 'ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy
  Learning'
title_zh: ReSPO：解决离策略学习梯度饥饿的序列策略优化算法
authors:
- Yihang Chen
- Yuanhao Ban
- Cho-Jui Hsieh
affiliations:
- University of California, Los Angeles
arxiv_id: '2609.35433'
url: https://arxiv.org/abs/2609.35433
pdf_url: https://arxiv.org/pdf/2609.35433
published: '2026-09-27'
collected: '2026-10-09'
category: Training
direction: LLM离策略训练 · 策略优化
tags:
- Policy Optimization
- Off-policy Learning
- RLHF
- MoE
- Gradient Starvation
one_liner: 提出双分支序列权重重塑的ReSPO算法，解决离策略RLHF梯度饥饿问题，适配MoE与高rollout复用场景
practical_value: '- 生成式推荐、Agent决策的RL微调场景：可直接替换现有PPO/GRPO的clipping逻辑为ReSPO双分支核，在高rollout复用场景下保留低权重正样本信号，同时抑制负样本噪声，提升训练稳定性和最终效果，降低生成成本。

  - MoE大模型（如推荐排序、文案生成MoE）的RL训练场景：ReSPO无需额外Routing Replay机制即可稳定训练，减少工程实现复杂度，适配MoE的训练波动特性。

  - 推荐系统离线RL优化场景：可借鉴正负样本分治的重要性权重设计思路，针对历史反馈的正负样本分布特性定制权重核，避免高复用比下的梯度饥饿/爆炸问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR（如RLHF、RLAIF）为降低生成成本会复用rollout做多轮策略更新，新旧策略偏差随复用次数提升逐渐变大，现有GRPO/GSPO的硬clipping机制存在符号依赖的梯度饥饿问题：低重要性权重的正样本梯度几乎消失，高重要性权重的负样本梯度占比过高，在MoE模型、高rollout复用比场景下训练不稳定、性能衰减严重。

### 方法关键点
1. 采用序列级重要性权重替代token级/长度归一化权重，避免长度偏差，对齐序列级奖励的信号粒度；
2. 设计双分支平滑核替代硬clipping：正样本分支用α>1的α散度目标，保证W→0时仍有非零梯度，保留低权重正样本的学习信号；负样本分支用α=1的KL散度目标，保证W→0和W→∞时梯度都为0，抑制极端负样本的梯度噪声；
3. 增加指数倾斜项控制权重方差，训练时核权重加stop-gradient，仅作为梯度缩放系数使用。

### 关键实验
在Qwen3-1.7B（稠密）、Qwen3-30B-A3B（MoE）上基于DAPO-MATH数据集训练，对比GRPO、GSPO、VESPO基线：rollout复用比N=32时，ReSPO后期训练分数比最优clipping基线高7.9pp（1.7B）、8.4pp（30B），AIME等难例数学推理benchmark平均精度最高提升6.3pp。

**最值得记住的一句话**：离策略RL训练中正负样本的重要性权重分布特征完全不同，分治设计权重核比统一的clipping/平滑机制能同时兼顾训练稳定性和信号利用率。
