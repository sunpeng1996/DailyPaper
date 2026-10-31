---
title: 'PhysInsert: Physically Plausible Object Insertion with Geometric Priors and
  Bidirectional Object-Scene Interactions'
title_zh: PhysInsert：结合几何先验与双向物景交互的物理可信物体插入
authors:
- Yue Gong
- Le Zhang
- Rui Chen
- Song Chang
- Xiaochao Qu
- Luoqi Liu
- Ting Liu
- Yebin Liu
affiliations:
- Beihang University
- Meitu Inc.
- Tsinghua University
arxiv_id: '2610.40453'
url: https://arxiv.org/abs/2610.40453
pdf_url: https://arxiv.org/pdf/2610.40453
published: '2026-10-28'
collected: '2026-10-31'
category: Multimodal
direction: 多模态生成 · 物理可信物体插入
tags:
- Object Insertion
- Geometric Prior
- Multimodal Generation
- Synthetic Dataset
- Evaluation Benchmark
one_liner: 提出融合几何先验与双向物景交互的物理可信物体插入框架及配套数据集与评测基准
practical_value: '- 电商商品主图/场景图生成可复用几何引导适配模块，解决不同场景下商品摆拍的光照、透视匹配问题，降低素材制作成本

  - 搭建虚拟试穿、家居商品入户预览等功能时，可参考双向物景交互监督思路，补全反射、阴影等物理细节提升真实感

  - 需构建多视角/多光照配对训练数据时，可复用InsertWorld数据集的Blender渲染构建流程，降低标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有参考式物体插入方法受限于掩码输入、训练对视角变化少等问题，物体姿态、光照适配及物景双向交互约束不足，生成结果物理可信度低。

### 方法关键点
1. 构建InsertWorld数据集，包含322个场景、1710个物体、12951对严格对齐的Blender渲染反事实样本，覆盖多视角、多光照及不同材质物体；
2. 设计几何引导适配模块，耦合VGGT几何流、图像流、文本流，在目标场景特征监督下实现空间一致的插入；
3. 新增2D物景空间监督，联合约束物体占用与环境变化，通过图文注意力对齐空间指令与物体区域；
4. 发布PhysInsert-Bench评测基准，覆盖跨环境、跨视角等需光照/姿态适配的案例。

### 关键结果
在PhysInsert-Bench和DreamBooth上图像保真度显著提升，用户研究显示物体放置准确率、光照融合、透视、姿态合理性均优于基线。
