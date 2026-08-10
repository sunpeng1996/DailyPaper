---
title: 'MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation'
title_zh: MirrorWorld：面向镜像反射生成的视频扩散模型优化
authors:
- Youjun Zhao
- Alex Warren
- Gary K. L. Tam
- Rynson W. H. Lau
affiliations:
- City University of Hong Kong
- Swansea University
arxiv_id: '2608.07463'
url: https://arxiv.org/abs/2608.07463
pdf_url: https://arxiv.org/pdf/2608.07463
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态视频生成 · 场景一致性优化
tags:
- Video Diffusion Model
- Semantic Distillation
- Geometric Alignment
- Video Inpainting
- Multimodal Generation
one_liner: 提出结合语义关系蒸馏与几何变换对齐的视频镜像反射生成框架
practical_value: '- 电商AR试穿、商品3D展示视频生成场景可复用SRD+GTA组合思路，优化镜面/高反光面的内容一致性，避免视觉穿帮

  - 生成带反光物体（玻璃/金属/水面）的电商营销短视频时，可引入语义关系蒸馏约束关联区域内容匹配，提升真实感

  - 对需保证空间一致性的AIGC内容生成任务，可借鉴「语义内容匹配+几何位置对齐」的双模块互补架构设计'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有视频扩散模型（VDM）未专门建模场景与镜像的对应关系，生成的镜像反射常出现内容错误、空间排布不一致问题，无法满足高保真视频合成需求。
### 方法关键点
1. 提出反射感知视频补全框架MirrorWorld，同步解决「反射内容是什么」「反射如何空间排布」两个互补问题
2. 设计Semantic Relation Distillation（SRD）模块，从冻结视觉基础模型迁移关系信息，约束可见场景与镜像区域的语义关联
3. 设计Geometric Transformation Alignment（GTA）模块，学习变换函数引导反射内容的空间排布，与SRD能力互补
4. 重构4个现有视频镜像数据集，构建统一的反射重建任务基准
### 关键结果
相比代表性图像级反射生成方法、主流视频补全基线，MirrorWorld的反射重建质量实现显著提升
