---
title: 'LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of
  3D Intrinsic Proxies'
title_zh: LuxAvatar：基于3D内在代理因果神经着色的实时可重光照头像框架
authors:
- Yipengjing Sun
- Chenyang Wang
- Boyao Zhou
- Jiapeng Zhu
- Ka Leong Cheng
- Shengping Zhang
affiliations:
- Harbin Institute of Technology
- Tsinghua University
- HKUST
arxiv_id: '2611.34940'
url: https://arxiv.org/abs/2611.34940
pdf_url: https://arxiv.org/pdf/2611.34940
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 3D数字人 · 实时可重光照头像渲染
tags:
- 3D Avatar
- Neural Rendering
- Real-Time Rendering
- Relighting
- Diffusion Model
one_liner: 提出单肖像输入的实时可重光照3D头像生成方案，兼顾3D可控性、光影真实度与低延迟
practical_value: '- 电商虚拟主播/数字人场景可复用「3D高斯代理+轻量神经着色器」架构，单张肖像即可快速生成支持实时动效、适配直播间任意光线的数字人，大幅降低虚拟人制作与部署成本

  - 大模型轻量化技巧可迁移：用多步预训练教师模型蒸馏得到2步因果自回归推理模型，在保留效果的前提下大幅降低推理延迟，适合低算力端侧、实时交互场景落地

  - 垂类适配方案可借鉴：通用预训练模型搭配小批量领域定制数据集微调，可快速将通用光影先验迁移到人脸、商品等特定垂类，提升垂类场景渲染效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有可重光照3D头像生成方案要么依赖昂贵专业采集设备，要么推理延迟高，无法同时满足3D可控性、光影真实度与实时性要求，难以落地到虚拟直播、沉浸式电商交互等场景。
### 方法关键点
1. 将头像生成拆分为可动画3D内在高斯代理、因果自回归神经着色器两个模块，前者解耦canonical几何与反射属性，快速生成视角、运动一致的PBR缓冲；
2. 把前向渲染建模为条件视频扩散过程，绕过复杂显式PBR计算，直接生成目标光照下的真实着色效果；
3. 基于预训练多步双向重光照教师模型做异构蒸馏，得到仅需2步推理的轻量着色器，搭配人脸专属混合重光照数据集微调，兼顾泛化性与低延迟。
### 关键结果
实现单张肖像输入的实时3D可控头像动画与重光照，在视觉保真度、运动控制精度、光照准确性三个维度上均超越现有SOTA方法。
