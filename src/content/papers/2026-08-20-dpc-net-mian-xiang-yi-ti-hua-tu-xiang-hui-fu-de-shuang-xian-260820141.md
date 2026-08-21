---
title: 'DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration'
title_zh: DPC-Net：面向一体化图像恢复的双先验协作网络
authors:
- Zhaokun He
- Kangbiao Shi
- Axi Niu
- Jian Jin
- Peng Wu
- Wei Dong
- Qingsen Yan
affiliations:
- Northwestern Polytechnical University
- Singapore Management University
- Xi'an University of Architecture and Technology
arxiv_id: '2608.20141'
url: https://arxiv.org/abs/2608.20141
pdf_url: https://arxiv.org/pdf/2608.20141
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 一体化图像恢复 · 双先验协作建模
tags:
- Image Restoration
- VLM
- Dual Prior
- Feature Modulation
- Knowledge Base
one_liner: 结合VLM引导的退化语义先验与底层视觉先验实现SOTA多退化场景图像恢复
practical_value: '- 可复用VLM约束低层视觉特征分布的思路，优化电商商品图去噪、去模糊、去雾等预处理流程

  - 双先验协作建模架构可迁移至多模态商品素材修复场景，提升劣化素材的可用性

  - 退化语义调制模块设计可参考用于劣化商品图的语义保持修复，避免商品核心特征失真'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有一体化图像恢复（AiOIR）方法在退化建模阶段忽略图像语义信息，重建阶段缺乏底层视觉先验支撑，易产生结构扭曲、语义不一致问题，无法适配复杂多退化的真实场景。
### 方法关键点
1. 设计退化感知网络（DAN）提取退化-语义耦合特征，引入VLM约束特征分布，将图像语义注入退化模式编码过程；
2. 新增退化语义调制模块（DSMM）实现退化与语义的深度耦合，将耦合表征传递给解码器；
3. 解码阶段从知识库引入低层视觉先验，通过双先验协作重建模块（DPCR）融合双先验信息，在去除退化的同时保留图像结构与语义信息。
### 关键结果
在多个公开图像恢复基准数据集上，性能全面优于现有SOTA的AiOIR方法。
