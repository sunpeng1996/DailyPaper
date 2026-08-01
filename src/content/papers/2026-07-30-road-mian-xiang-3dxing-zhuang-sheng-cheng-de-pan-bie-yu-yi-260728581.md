---
title: 'ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape
  Generation'
title_zh: ROAD：面向3D形状生成的判别语义双向目标对齐框架
authors:
- Xiao Luo
- Mingyang Du
- Xin Zhou
- Tianrui Feng
- Xiwu Chen
- Xiaofan Li
- Jiangning Zhang
- Dingkang Liang
affiliations:
- Huazhong University of Science and Technology
- Megvii
- Zhejiang University
arxiv_id: '2607.28581'
url: https://arxiv.org/abs/2607.28581
pdf_url: https://arxiv.org/pdf/2607.28581
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 3D生成 · 判别模型先验迁移对齐
tags:
- 3D_Generation
- Diffusion_Transformer
- Knowledge_Distillation
- Feature_Alignment
- Training_Efficiency
one_liner: 迁移判别式3D基础模型先验，仅用1.5%训练数据实现媲美工业基线的3D生成效果降低训练成本
practical_value: '- 训练阶段引入外部大模型做监督信号、推理阶段卸载大模型的范式可复用，能在不增加推理耗时的前提下提升生成式推荐、商品素材生成等业务的效果

  - 跨隐空间异质性对齐思路（全局语义约束+局部细节二分图匹配）可迁移到跨模态推荐、多源用户/物品特征融合场景

  - 少样本训练下迁移成熟判别模型先验的思路，可降低商品3D素材生成、生成式个性化内容推荐的训练数据门槛'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高保真3D生成依赖模型容量与数据规模扩容，训练计算成本极高，现有范式从零学习几何特征，未利用判别式3D基础模型已沉淀的丰富语义与结构先验。

### 方法关键点
提出ROAD框架将判别式3D基础模型的先验迁移到Diffusion Transformer，降低训练成本；设计双向目标对齐策略，通过全局语义浓缩保证跨隐空间语义一致性，将微观几何细节对齐建模为二分图匹配问题，解决生成/判别隐空间的语义-结构异质性；判别式3D基础模型仅用于训练阶段监督，推理阶段不引入额外开销。

### 关键结果
对比工业基线Step1X-3D，仅用1.5%的训练数据就达到极具竞争力的生成性能，大幅降低高保真3D生成的训练计算开销。
