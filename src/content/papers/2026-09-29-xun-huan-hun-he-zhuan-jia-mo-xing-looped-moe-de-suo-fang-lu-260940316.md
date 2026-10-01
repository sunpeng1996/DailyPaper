---
title: Scaling Laws for Looped Mixture of Experts
title_zh: 循环混合专家模型（Looped MoE）的缩放定律
authors:
- Yanbei Chen
- Anirudh Goyal
- Raghuraman Krishnamoorthi
affiliations:
- Meta AI
arxiv_id: '2609.40316'
url: https://arxiv.org/abs/2609.40316
pdf_url: https://arxiv.org/pdf/2609.40316
published: '2026-09-29'
collected: '2026-10-01'
category: Training
direction: 大模型训练 · Looped MoE 缩放定律
tags:
- Scaling Law
- Looped Transformer
- MoE
- Parameter Efficiency
- Model Training
one_liner: 首次提出统一建模循环、稀疏、模型、数据的Loop缩放定律，指导资源约束下Looped MoE架构设计
practical_value: '- 做端侧轻量化LLM（如电商端侧智能导购Agent、端侧个性化推荐小模型）的团队，可复用循环+MoE的架构组合，在有限端侧显存下提升模型效果，还能根据设备算力动态调整循环次数，平衡推理时延与效果

  - 训练LLM服务于生成式推荐（GenRec）、广告文案生成、个性化推荐理由生成等任务时，可参考本文给出的资源约束下最优R、E选型公式，在固定训练算力/显存预算下最大化模型性能，降低训练成本

  - 面对电商大促等流量波动场景，可利用Looped MoE支持测试时动态调循环次数的特性，流量高峰时降低R提升吞吐，流量低峰时升高R提升推荐/交互效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往缩放定律仅单独建模循环（Looped Transformer）或稀疏（MoE）的缩放规律，未覆盖两者的联合作用，无法指导兼具参数复用与稀疏扩容能力的Looped MoE模型的资源分配，难以在训练算力、部署显存约束下最大化模型效能。

### 方法关键点
- 引入带边界的稀疏条件循环映射：建模循环带来的有效参数增益边际递减，存在有限上限，且MoE稀疏度越高（专家数越多），增益上限越高、饱和速度越慢
- 统一Loop缩放定律同时纳入模型大小、训练数据量、循环次数R、MoE专家数E四个维度，可退化到标准稠密、非循环MoE、稠密循环Transformer的经典缩放定律
- 给出固定训练算力、部署显存约束下的最优R与E的选型方法，平衡性能与资源消耗

### 关键结果
在14个下游基准（含推理、常识、知识类任务）上验证：稀疏度带来~3×活跃参数效率，循环带来~2×总参数效率（推理任务）；万亿token规模下，同训练算力的Looped MoE（0.3B活跃/1.3B总参数）仅需1.5×推理算力，即可匹配2倍大小的非循环MoE（0.6B活跃/2.9B总参数）的推理效果，测试时调整R可实现最高10.3个百分点的性能提升。

最值得记住的结论：固定训练算力下，显存紧张优先提升循环次数，显存充足优先提升MoE稀疏度，两者联合可大幅推高模型的效能边界
