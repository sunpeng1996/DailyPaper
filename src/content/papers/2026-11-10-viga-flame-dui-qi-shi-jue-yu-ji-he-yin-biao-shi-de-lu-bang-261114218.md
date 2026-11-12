---
title: 'ViGA-FLAME: Aligning Latent Visual and Geometric Representations for Robust
  3D Head Expression Estimation'
title_zh: ViGA-FLAME：对齐视觉与几何隐表示的鲁棒3D头部表情估计方法
authors:
- Wen Hao He
- Jiacheng Wu
- Jie Chen
affiliations:
- Department of Computer Science, Hong Kong Baptist University
arxiv_id: '2611.14218'
url: https://arxiv.org/abs/2611.14218
pdf_url: https://arxiv.org/pdf/2611.14218
published: '2026-11-10'
collected: '2026-11-12'
category: Multimodal
direction: 多模态表征学习 · 3D人脸建模
tags:
- Multimodal Alignment
- VAE
- Adapter
- Attention
- 3D Reconstruction
one_liner: 提出两阶段视觉-几何对齐框架，实现大视角、强形变场景下鲁棒高效的3D头部表情估计
practical_value: '- 跨模态对齐两阶段架构可复用：先训练领域专属结构化隐空间VAE，再用轻量Adapter对接预训练大模型，无需改动大模型权重，适合业务快速上线

  - 双解码分支+一致性约束的VAE训练范式，可迁移到电商图文统一表征、多模态召回等场景，提升异构信息融合效果

  - 不对称注意力Adapter设计，可用于跨域特征适配任务，比如搜索推荐中的用户/物品跨域表征对齐，适配成本低'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单图3D头部表情估计需完成视觉外观到面部几何的映射，现有方法在极端表情、大视角遮挡场景下鲁棒性差，优化类方案推理延迟高难以落地。
### 方法关键点
1. 两阶段跨模态对齐架构：第一阶段训练PG-VAE，学习融合标准头部曲面与FLAME参数的统一隐空间，双解码分支同时输出高细节曲面重建结果与可解释参数，通过几何监督、参数监督加双分支一致性约束，关联曲面细节与结构化参数信息
2. 第二阶段训练轻量ViGA Adapter，采用不对称注意力机制将预训练语义视觉编码器的输出特征映射到上述几何隐空间，全程不修改预训练视觉模型权重
### 关键结果
在严重面部形变、大viewing angle场景下鲁棒性显著优于现有前馈方法，推理效率同时提升
