---
title: Representation Distribution Matching for One-Step Visual Generation
title_zh: 面向单步视觉生成的表征分布匹配方法
authors:
- Lan Feng
- Wuyang Li
- Eloi Zablocki
- Matthieu Cord
- Alexandre Alahi
affiliations:
- EPFL, Switzerland
- Valeo.ai, France
- Sorbonne Université, France
arxiv_id: '2607.02375'
url: https://arxiv.org/abs/2607.02375
pdf_url: https://arxiv.org/pdf/2607.02375
published: '2026-07-01'
collected: '2026-07-03'
category: Multimodal
direction: 多模态生成 · 单步图像生成与扩散蒸馏
tags:
- Distribution Matching
- One-step Generation
- Diffusion Distillation
- MMD
- Multimodal Generation
one_liner: 优化表征分布匹配范式，提出iRDM实现SOTA单步图像生成，可快速蒸馏多步扩散为单步
practical_value: '- 电商商品图/营销图生成场景可复用iRDM蒸馏方案，将多步扩散模型压缩为单步版本，推理时延降低75%以上同时生成质量不下降，大幅降低推理成本

  - 生成内容对齐场景可复用「多编码器联合分布匹配」思路，避免单表征过拟合/作弊问题，提升生成内容的真实感与用户偏好匹配度

  - 生成质量评估环节可借鉴SW_r14的多编码器聚合指标设计，替代单一FID/高成本人工评估，降低评估成本的同时提升结果鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有单步图像生成质量普遍弱于多步扩散模型，且蒸馏成本高，表征分布匹配（RDM）范式的设计空间未被系统梳理，性能瓶颈不明确。
### 方法关键点
1. 拆解RDM两大设计轴：分布对比方式、表征空间选择，经对照实验得到三大核心结论：正确估计的MMD可成为强可扩展训练目标、最优生成batch size≥2048远高于常规设置、单一表征易被作弊需匹配多编码器集合；
2. 整合最优设计得到改进版iRDM，提出跨14个预训练编码器的Sliced-Wasserstein距离指标SW_r14，可实现鲁棒的生成质量评估，抗过拟合。
### 关键结果
- ImageNet单步生成SW_r14达1.30，为当前SOTA，PickScore偏好度超此前最优单步模型71.2%；
- 仅用90 H200 GPU小时即可将4步FLUX.2蒸馏为单步版本，GenEval从0.794升至0.826，PickScore从22.58升至22.76，性能超过原4步模型。
