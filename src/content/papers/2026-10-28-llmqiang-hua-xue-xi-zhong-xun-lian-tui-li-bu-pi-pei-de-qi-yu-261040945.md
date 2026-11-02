---
title: On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement
  Learning
title_zh: 《LLM强化学习中训练-推理不匹配的起源、演化与校正方法》
authors:
- Yu Li
- Yufa Zhou
- Tian Lan
affiliations:
- George Washington University
- Duke University
arxiv_id: '2610.40945'
url: https://arxiv.org/abs/2610.40945
pdf_url: https://arxiv.org/pdf/2610.40945
published: '2026-10-28'
collected: '2026-11-02'
category: Training
direction: LLM强化学习 训练推理不匹配优化
tags:
- LLM
- Reinforcement Learning
- Training-Inference Mismatch
- Off-Policy Correction
- Async Training
one_liner: 拆分LLM RL训练推理不匹配为两类误差，提出DLC校正方案稳定异步训练
practical_value: '- 做LLM+推荐的RL微调（如个性化文案生成、Agent决策调优）时，可将训练推理不匹配拆分为数值差异+策略滞后两类分别处理：数值类用score
  centering消偏移，滞后类用ratio clip控偏差，比单一校正方案稳定性提升显著

  - 异步RL训练场景（如大流量下推荐系统在线RL调优），可监控lag ratio的有效样本量，低于0.5时立即同步采样器与训练器权重，避免训练崩溃，比固定间隔同步效率高3倍以上

  - 用低精度推理引擎做RL样本生成时，新增1次训练器在采样器权重下的前向传播拆分两类误差，额外开销极低，还能规避量化带来的训练漂移，适合资源受限的线上推荐推理节点落地'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM强化学习普遍采用异步采样+训练架构，推理引擎的精度/kernel差异、异步采样的权重过时两类问题会导致训练-推理不匹配，现有校正方案仅适配单一场景，切换不匹配源就失效甚至崩溃，严重影响大模型RL（如推荐系统个性化生成、Agent决策微调）的训练稳定性。

### 方法关键点
- 引入训练器在采样器权重下的前向传播，将采样token的误差精确拆分为固定的数值差异（来自推理引擎精度、kernel差异）和自增长的策略滞后（来自异步训练的权重差）两类
- 针对数值差异：对每个前缀做score centering消除固定偏移；针对策略滞后：clip滞后ratio切断正反馈循环
- 监控滞后ratio的有效样本量，低于0.5阈值时立即同步采样器与训练器权重，避免超出校正有效区间
- 整套DLC方案仅新增1次轻量前向传播，计算开销可忽略

### 关键实验
基于Countdown数学推理任务，训练Qwen3-0.6B、Qwen3-1.7B两个模型，对比Policy Gradient、PPO、重要性采样、score centering等基线：异步stale采样场景下，DLC将与同配置on-policy训练的KL divergence控制在2倍噪声以内，Qwen3-1.7B测试准确率达51.9%，仅比on-policy低5.7个百分点，比重要性采样基线高51.4个百分点，有效避免无同步时的训练崩溃问题。

### 核心结论
训练推理不匹配的两类来源演化规律完全不同，固定的数值差异消偏移即可，自增长的策略滞后需要clip+动态权重同步联合处理，有效样本量低于0.5是校正失效的明确临界值。
