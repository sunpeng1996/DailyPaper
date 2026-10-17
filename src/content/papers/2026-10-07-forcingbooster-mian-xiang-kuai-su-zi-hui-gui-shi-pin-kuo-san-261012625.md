---
title: 'ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video
  Diffusion'
title_zh: ForcingBooster：面向快速自回归视频扩散的自适应分块去噪框架
authors:
- Zekai Gu
- Peng Wang
- Jiahao Lu
- Yongsen Mao
- Cheng Lin
- Yuan Liu
affiliations:
- HKUST
- VAST
- Macau University of Science and Technology
arxiv_id: '2610.12625'
url: https://arxiv.org/abs/2610.12625
pdf_url: https://arxiv.org/pdf/2610.12625
published: '2026-10-07'
collected: '2026-10-17'
category: Other
direction: 视频生成 · 扩散模型推理加速
tags:
- Diffusion Model
- Video Generation
- Inference Acceleration
- Autoregressive Model
- Patch-wise Processing
one_liner: 提出自适应分块去噪框架，按需分配视频patch去噪步数，在质量无损前提下减少50%总去噪步数
practical_value: '- 电商内容生成场景（商品短视频、直播数字人）可复用动态算力分配思路：对静态背景、重复商品纹理等简单区域减少计算量，重点给动态人物、商品细节分配算力，降低生成成本

  - 多模态推荐系统的生成分发链路中，可借鉴patch级早停策略，对低复杂度的生成内容（如商品文案配图的简单区域）提前终止迭代，提升推理QPS

  - Agent交互场景下的实时内容生成（如数字人对话视频）可复用轻量路由模块设计，仅需少量训练即可适配现有生成模型，实现性能与质量的平衡'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频扩散是实时交互式视频生成、视频世界建模的主流方案，但现有方法对所有空间patch采用统一去噪步数，忽略视频内容空间异质性：静态、简单/重复区域去噪难度低，统一算力分配会造成冗余，降低固定步数又会导致高难度区域生成质量不足。
### 方法关键点
提出ForcingBooster通用框架，新增轻量路由模块动态给每个patch分配去噪步数：简单patch早停节省算力，复杂patch分配更多步数保证质量，可兼容现有少步自回归扩散模型，仅需少量训练即可接入。
### 关键结果
实验显示，相比4步基线模型，ForcingBooster可将所有视频patch的总去噪步数减少约50%，同时视觉效果与基线持平
