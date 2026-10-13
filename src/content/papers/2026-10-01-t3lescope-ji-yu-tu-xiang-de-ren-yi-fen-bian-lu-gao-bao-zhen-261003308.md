---
title: 'T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction
  from Images'
title_zh: T3lescope：基于图像的任意分辨率高保真生成式表面重建
authors:
- Atsuhiro Noguchi
- Tianhan Xu
- Yiming Liang
- Yuta Kikuchi
- Masahiro Ishiyama
- Shintaro Takagi
- Hitoshi Murai
- Eiichi Matsumoto
affiliations:
- Preferred Networks, Inc.
- The University of Tokyo
arxiv_id: '2610.03308'
url: https://arxiv.org/abs/2610.03308
pdf_url: https://arxiv.org/pdf/2610.03308
published: '2026-10-01'
collected: '2026-10-13'
category: Other
direction: 3D生成 · 跨尺度表面重建
tags:
- 3D Reconstruction
- Generative Model
- Coarse-to-Fine
- Multi-scale
- Mesh Generation
one_liner: 提出推理时动态粗细级联的共享权重生成器，实现跨尺度无逐场景优化的高保真3D网格重建
practical_value: '- 电商商品3D建模场景可复用粗细级联权重共享方案，无需逐商品优化即可快速生成高保真3D模型，大幅降低3D素材制作成本

  - 推理时动态调整分辨率的策略可借鉴到3D商品展示场景，根据用户设备、带宽动态下发不同精度3D模型，平衡体验与带宽开销

  - 多尺度训练权重共享的思路可迁移到生成式推荐多粒度内容生成场景，降低多分辨率生成任务的训练与部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有逐场景优化3D重建方案在观测稀疏、表面高光/透明场景下效果差；固定分辨率生成式方法需分区处理大场景，全局一致性差，存在空间覆盖范围与细节精度的trade-off。
### 方法关键点
1. 推理阶段采用动态粗细级联策略，粗层级先确定全局场景布局，细层级在逐步细化的空间单元内对上层继承的几何信息做扰动、去噪以恢复表面细节
2. 单固定分辨率生成器权重跨所有层级共享，训练仅在多尺度独立单元上完成，推理时可自由确定层级数、单元尺度与位置，无固定层级限制
### 关键结果
在室内、户外、城市级多尺度场景上，效果优于所有前馈和生成式基线，性能持平甚至超过逐场景优化方法，可有效恢复精细结构、高光及透明表面
