---
title: Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training
title_zh: 精度感知的大模型后训练跨Transformer块数学习率迁移方法
authors:
- Nan Chen
- Soledad Villar
- Soufiane Hayou
affiliations:
- Johns Hopkins University
arxiv_id: '2611.31166'
url: https://arxiv.org/abs/2611.31166
pdf_url: https://arxiv.org/pdf/2611.31166
published: '2026-11-23'
collected: '2026-11-24'
category: Training
direction: 大模型后训练 · 学习率超参搜索优化
tags:
- LLM Post-training
- Learning Rate Tuning
- Mixed Precision Training
- Hyperparameter Transfer
- Low Resource Training
one_liner: 提出TipSweep方法，仅训练最后少量块即可按精度规则迁移最优学习率到全模型，大幅降低调参成本
practical_value: '- 微调垂直领域LLM（如电商文案生成、商品语义理解、推荐系统语义召回模型）时，可直接复用TipSweep的学习率缩放规则：FP32主权重下最优学习率与可训练块数k成反比，BF16无主权重下与√k成反比，省去全量网格搜索的算力成本

  - 算力资源有限的团队可选择仅训练最后k0=1个块做学习率搜索，配合冻结前缀特征缓存，6.7B级模型可在16GiB消费级GPU完成调参，无需占用高端GPU资源，适合快速迭代小流量实验

  - 做LoRA微调时，结合Init[B]初始化方案，仅用最后1块的LoRA搜索得到的学习率即可按规则迁移到全量微调场景，进一步降低调参的显存开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM后训练（SFT、DPO、RLVR等）对学习率高度敏感，传统全量网格搜索需多次跑通全模型训练，算力、时间成本极高；预训练阶段的超参迁移方法依赖模型宽度缩放，无法直接用于预训练checkpoint固定的后训练场景。

### 方法关键点
- TipSweep框架：仅训练Transformer最后k0个块（默认k0=1）搜索最优学习率，再按精度规则迁移到任意k个可训练块的场景，包括全模型微调（k=L）
- 精度依赖的缩放规则：FP32主权重更新时最优学习率η_k ≈ (k0/k)·η_k0；无FP32主权重的直接BF16/FP16更新时η_k ≈ √(k0/k)·η_k0
- 特征缓存优化：冻结前缀层的输出缓存到磁盘或GPU显存，避免多轮搜索重复计算前缀，进一步降低算力开销

### 关键实验
覆盖1B~7B参数模型，验证SFT、DPO、RLVR三类后训练任务，缩放规则拟合度：FP32下拟合指数-0.81~-1.04接近理论值-1，BF16下拟合指数-0.5~-0.57接近理论值-0.5；20候选学习率搜索场景下，高端GPU上比全量sweep提速10倍，6.7B模型调参可在16GiB消费级GPU完成，调参后模型性能与全量搜索得到的学习率训练效果相当。

### 最值得记住的一句话
LLM后训练的最优学习率缩放规则完全由参数更新的数值精度决定，无需依赖模型结构或预训练初始化的先验假设。
