---
title: 'OR Else: A Differentiable Trust Region for Policy Optimization'
title_zh: OR Else：面向策略优化的可微置信域方法
authors:
- Chinmay Rane
- Kanishka Tyagi
- Michael Manry
affiliations:
- Quantiphi Inc
- Self Machines Inc
- The University of Texas at Arlington
arxiv_id: '2607.18163'
url: https://arxiv.org/abs/2607.18163
pdf_url: https://arxiv.org/pdf/2607.18163
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: LLM对齐 · RLHF策略优化
tags:
- RLHF
- PPO
- GRPO
- Policy Optimization
- LLM Alignment
one_liner: 提出PPO-OR/GRPO-OR策略优化方法，用平滑Output Reset规则替代截断损失优化RLHF训练
practical_value: '- 做RLHF对齐LLM生成推荐文案/Agent回复时，可直接用PPO-OR替代原生PPO截断损失，在GAE配置下能显著提升reward
  model得分，减少梯度跳变问题

  - 对GRPO小群体（G=2）训练场景，GRPO-OR可大幅降低跨种子训练波动，适合对训练稳定性要求高的业务对齐任务，无需改动原有优势估计逻辑

  - 做策略优化时可参考OR的单侧平方margin设计，将梯度从跳变改为连续趋近0，避免截断边界的梯度突变导致的训练震荡，适配LoRA低资源训练场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
PPO、GRPO等RLHF常用策略优化方法依赖截断代理目标，在有利方向饱和时会出现目标导数的跳变，导致训练不稳定、reward提升受限，当前缺少平滑可微的单侧饱和规则适配LLM post-training场景。

### 方法关键点
- 提出Output Reset（OR）平方margin损失，在token级对数概率比空间计算损失：仅用advantage的符号确定更新方向，当token对数概率比跨过有利方向的预设margin后，直接将损失残差置0，梯度在饱和边界连续趋近0，无跳变
- 衍生PPO-OR和GRPO-OR两个变体：PPO-OR保留GAE优势估计和价值头，GRPO-OR保留群体相对优势估计且无需critic，仅替换原有截断损失模块，改动侵入性极低
- 训练适配LoRA低资源配置，梯度计算仅依赖token级对数概率差和advantage符号，无需额外改造现有训练流水线

### 关键实验
在Anthropic hh-rlhf数据集上，基于Llama-3.2-1B-Instruct做对齐，对比原生PPO、GRPO：GAE配置下PPO-OR最终reward model得分比PPO-clip高0.305；G=2的GRPO配置下，GRPO-OR得分略低0.031，但跨种子标准差从0.080降至0.027，训练稳定性大幅提升。

### 核心结论
策略优化的reward提升、损失数值稳定性、策略漂移三个指标并不完全正相关，平滑单侧饱和损失无法替代置信域约束解决策略漂移问题。
