---
title: 'PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space'
title_zh: PixWorld：像素空间下统一3D场景生成与重建
authors:
- Sensen Gao
- Zhaoqing Wang
- Qihang Cao
- Dongdong Yu
- Changhu Wang
- Jia-Wang Bian
affiliations:
- Nanyang Technological University
- AISphere
arxiv_id: '2607.05373'
url: https://arxiv.org/abs/2607.05373
pdf_url: https://arxiv.org/pdf/2607.05373
published: '2026-07-05'
collected: '2026-07-08'
category: Other
direction: 3D视觉 · 统一3D生成与重建
tags:
- 3D Generation
- 3D Reconstruction
- Diffusion Model
- Pixel Space
- Foundation Model
one_liner: 提出像素空间统一扩散范式，单模型同时实现3D场景生成与SOTA级重建
practical_value: '- 电商3D商品建模场景可复用无VAE的像素空间统一范式，省去预训练VAE/RAE成本，降低隐编码带来的信息损失

  - 可引入预训练3D基础模型的几何感知损失，补充2D渲染监督缺失的3D几何约束，提升3D商品模型的结构保真度

  - 单模型同时覆盖3D内容生成与重建需求，适合电商商品3D化批量生产场景，降低多模型部署与维护成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D重建和生成分属独立范式，近期隐空间统一方案存在三大缺陷：扩散损失定义在隐特征而非底层3D表示上、隐编码引入信息损失、依赖预训练VAE/RAE。
### 方法关键点
1. 提出像素空间统一扩散范式PixWorld，单模型同时处理3D场景生成与重建，直接对渲染图像做扩散监督，消除隐编码损失且无需预训练VAE/RAE；
2. 新增几何感知损失，基于预训练3D基础模型的几何感知特征空间对齐渲染视图与真值，补充3D结构监督，弥补2D损失缺少几何感知的缺陷。
### 关键结果
生成效果全面优于此前隐空间生成方案，重建效果追平现有SOTA重建方法，验证了像素空间统一框架的优越性。
