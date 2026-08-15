---
title: 'MapRoute++: Surrogate-Guided Semantic Routing for Visual Concept Unlearning'
title_zh: MapRoute++：面向视觉概念遗忘的代理引导语义路由方法
authors:
- Ashok Urlana
- L. D. M. S. Sai Teja
- Vivek Hruday Kavuri
- Ponnurangam Kumaraguru
affiliations:
- IIIT Hyderabad
- TCS Research
- NIT Silchar
arxiv_id: '2608.13478'
url: https://arxiv.org/abs/2608.13478
pdf_url: https://arxiv.org/pdf/2608.13478
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: 扩散模型训练 · 视觉概念遗忘
tags:
- Concept Unlearning
- Semantic Routing
- Stable Diffusion
- Diffusion Model
- Model Optimization
one_liner: 基于MapRoute优化训练目标与语义路由，Stable Diffusion概念遗忘性能较SOTA提升12.1%
practical_value: '- 电商生成式素材生产的扩散模型可复用该语义路由架构，快速移除侵权/违规概念同时保留其他生成能力

  - 概念分层的语义路由逻辑可迁移到推荐系统用户兴趣遗忘场景，快速下线低质/违规内容关联的兴趣标签

  - 任务定制化训练目标设计思路可复用在LoRA微调场景，平衡特定能力删除与其他能力保留的trade-off'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前文本到图像扩散模型生成能力成熟，但会习得版权内容、社会偏见等不良概念，现有概念遗忘方案难以平衡目标概念移除与相邻/无关概念的生成能力保留，需适配高鲁棒性的工业级遗忘方案。
### 方法关键点
基于MapRoute架构优化，新增三类核心改进：1）设计任务专属训练目标；2）引入多源富语义概念表征强化概念区分度；3）新增代理引导的语义路由模块，实现按概念特征匹配专属mapper做遗忘处理。
### 关键结果
在Stable Diffusion v1.4上测试，采用ERR（擦除-保留-鲁棒性）指标评估，5类概念平均性能较SOTA基线提升12.1%，同时完好保留无关、语义相邻概念的生成质量。
