---
title: Progressive Alignment of Recommender Foundation Model through Multi-Phase Post-Training
title_zh: 推荐基础模型多阶段后训练的渐进式对齐方法
authors:
- Oseong Choi
- Hoeinn Kim
- Jihoon Lee
- Byungsoo Kang
- Taeyeong Jang
affiliations:
- NAVER WEBTOON
arxiv_id: '2608.06792'
url: https://arxiv.org/abs/2608.06792
pdf_url: https://arxiv.org/pdf/2608.06792
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 推荐大模型 · 多阶段后训练对齐
tags:
- Recommender Foundation Model
- Multi-phase Post-Training
- Reinforcement Fine-Tuning
- Reward Modeling
- GRPO
one_liner: 提出三阶段渐进式后训练框架，实现推荐基模下游适配与业务指标对齐
practical_value: '- 推荐大模型下游适配可复用LP→FFT两阶段SFT范式：先冻住基模训练下游头，再用小1个量级的学习率微调基模，大幅降低灾难性遗忘风险，落地门槛低

  - 业务指标对齐不要直接将奖励模型作为排序服务：先用稠密点击/ dwell信号训练基础排序策略，再用RFT将稀疏业务信号作为对齐信号，兼顾全库排序区分度与业务收益

  - 业务奖励模型训练可加入截断逆倾向得分（IPS）纠偏，解决日志数据的曝光偏差问题，提升奖励信号置信度

  - 对齐方法可按业务目标选型：优先提升深层转化（付费、深度消费）选GRPO+奖励模型，优先提升浅层点击选DPO+直接观测的漏斗偏好'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐大模型预训练后通常直接通过SFT适配下游，但SFT优化的点击、点赞等任务目标与业务核心指标（如转化、深度消费、留存）存在天然gap；直接用稀疏业务标签训练模型排序区分度差，单阶段全量微调还易导致预训练知识灾难性遗忘，缺乏稳定兼顾排序能力与业务对齐的后训练方案。

### 方法关键点
- 三阶段渐进式后训练架构：阶段1 Linear Probing（LP）冻住预训练基模，仅优化下游任务头、奖励头、曝光倾向头，对齐下游模块与基模表征空间；阶段2 Full Fine-Tuning（FFT）解冻基模，基模用比下游模块小1个量级的学习率联合微调，稳定适配下游任务；阶段3 Reinforcement Fine-Tuning（RFT）冻住奖励与倾向头，用GRPO/DPO基于奖励信号微调排序策略，加KL正则控制策略漂移。
- 奖励模型设计：用序数回归建模用户6级消费漏斗深度（从曝光到付费完成），加入截断IPS修正曝光偏差，输出连续奖励信号。

### 关键结果
离线实验基于NAVER WEBTOON三周生产交互日志，两阶段LP→FFT比单阶段SFT Rank NDCG提升1.9%；GRPO+奖励模型比两阶段SFT Rank NDCG提升5.9%、Funnel NDCG提升1.9%，同时达到奖励模型直接排序的Funnel NDCG水平，保留强全库排序区分度。线上A/B测试对比生产非基模基线，三阶段GRPO方案点击提升~2.5%、深度阅读提升~3.2%、付费完成提升~4.1%，所有指标均统计显著（p<0.001）。

**最值得记住的一句话**：业务奖励信号最有效的用法是作为RFT的对齐信号，而非直接作为排序得分使用。
