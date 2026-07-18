---
title: 'From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation
  and Fast Planting'
title_zh: 从草稿到无草稿：基于特权蒸馏与快速植入的单步视频物体移除
authors:
- Zizhao Chen
- Ping Wei
- Guang Dai
- Jingdong Wang
- Mengmeng Wang
affiliations:
- 西安交通大学
- 国家电网SGIT AI Lab
- 浙江工业大学
- 百度
arxiv_id: '2607.14976'
url: https://arxiv.org/abs/2607.14976
pdf_url: https://arxiv.org/pdf/2607.14976
published: '2026-07-16'
collected: '2026-07-18'
category: Other
direction: 视频编辑 · 单步生成蒸馏优化
tags:
- Video Editing
- Diffusion Distillation
- One-Step Generation
- Knowledge Distillation
- Latent Generation
one_liner: 提出D2DF框架，实现1秒级无外部依赖的高质量单步视频物体移除
practical_value: '- 多步扩散模型蒸馏为单步生成模型的PPCD蒸馏方法可直接复用，可迁移到电商商品视频/营销素材的AI编辑场景，大幅降低生成延迟

  - SGFP模块隐空间自动生成伪前置输入的思路，可用于降低生成式素材处理对外部预处理结果的依赖，简化生产链路

  - 1秒级单步视频生成的轻量化架构设计思路，可支撑实时素材生产、端侧视频编辑等对延迟要求高的业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频物体移除方案存在明显缺陷：传统光流/注意力类方法易生成明显artifact，效果不自然；扩散类方案视觉质量更优，但需多步denoising，推理速度慢，落地实用性受限。
### 方法关键点
1. 训练多步扩散教师模型，实现将低质量移除草稿（传统方法输出）优化为高保真视频的能力；
2. 提出Prior-Privileged Consistency Distillation（PPCD），将教师能力蒸馏到单步学生模型，实现基于草稿的单步移除；
3. 设计Self-Guided Fast Planting（SGFP）模块，基于时序掩码Transformer在隐空间自动生成场景一致的伪草稿，消除对外部草稿的依赖，实现完全无草稿的单步推理。
### 关键结果
在多个公开数据集指标上达到SOTA，单视频推理仅需约1秒，效果和效率均超过传统方法与多步扩散方案。
