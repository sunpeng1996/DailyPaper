---
title: 'Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution'
title_zh: 无需推理时多候选采样：序列级幂分布的在策略蒸馏方法OPPD
authors:
- Erfan Baghaei Potraghloo
- Seyedarmin Azizi
- Arya Fayyazi
- Saeid Shokoufa
- Mehdi Kamal
- Souvik Kundu
- Massoud Pedram
affiliations:
- University of Southern California
- Intel AI
arxiv_id: '2610.06804'
url: https://arxiv.org/abs/2610.06804
pdf_url: https://arxiv.org/pdf/2610.06804
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: LLM训练 · 无标注自蒸馏提升推理性能
tags:
- On-policy Distillation
- Power Sampling
- Sequence-level Sharpening
- SMC
- LLM Reasoning
one_liner: 将推理时幂采样的成本转移到训练阶段，单代生成即可拿到16候选幂采样94%的收益
practical_value: '- 生成式推荐、广告文案生成场景可复用OPPD，把推理时多候选best-of-N的收益蒸馏到模型参数中，单步生成即可拿到90%+的多候选收益，大幅降低推理延迟

  - 已通过RLHF/GRPO优化过的业务模型（如智能导购Agent、query推荐模型）可叠加OPPD做二次迭代，无需额外标注数据，仅用问题prompt即可进一步提升效果

  - 序列级幂分布思路可迁移到推荐重排序、Agent多步路径规划场景，比单纯降低采样温度的token级sharpening更能筛选出全局最优的序列结果

  - 调参可直接复用论文规则：先测基线模型降低温度的效果收益，收益大的场景用λ=0，收益小的用λ=1，大幅减少调参成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
推理时采用幂采样（将完整序列的生成概率取α次方后重归一，把概率集中到模型置信度最高的结果上）可大幅提升LLM推理效果，但需要为每个query生成数十个候选再筛选，推理成本极高；普通token级蒸馏无法拟合序列级的幂分布，难以将该能力迁移到模型参数中。
### 方法关键点
- 采用序列蒙特卡洛（SMC）采样框架，训练中student模型自生成16个候选，每64个token为一个块，用frozen teacher的幂分布为候选加权，权重同时用于SMC重采样和student更新
- 损失由两部分组成：序列级加权最大似然项拟合幂分布，token级KL anchor项控制sharpening强度，通过系数λ调节两者权重
- 全程无需参考答案、奖励模型，仅用问题prompt即可完成训练，支持自蒸馏
### 关键结果
在数学推理任务上，单代生成效果比公开64候选幂采样高2.4（MATH500）、3.5（GSM8K）个点，拿到16候选幂采样94%的收益；比同预算、使用参考答案训练的GRPO高3.8（MATH500）、4.0（GSM8K）、5.4（AIME）个点；已通过RL优化的模型叠加OPPD可再提升最高9.3个点，泛化到代码生成任务HumanEval可涨5.3个点。
### 核心结论
序列级幂分布的sharpening效果远优于单纯降低采样温度，且可通过在策略蒸馏将推理成本一次性转移到训练阶段，无标注即可大幅提升模型性能
