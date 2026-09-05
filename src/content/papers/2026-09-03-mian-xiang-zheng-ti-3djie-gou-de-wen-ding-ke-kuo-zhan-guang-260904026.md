---
title: Stable and Scalable Bundle Adjustment of Holistic 3D Structures
title_zh: 面向整体3D结构的稳定可扩展光束法平差方法
authors:
- Shaohui Liu
- Rémi Pautrat
- Daniel Barath
- Richard Hartley
- Viktor Larsson
- Marc Pollefeys
affiliations:
- ETH Zurich
- Microsoft Spatial AI Lab
- Australian National University
- Lund University
arxiv_id: '2609.04026'
url: https://arxiv.org/abs/2609.04026
pdf_url: https://arxiv.org/pdf/2609.04026
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 3D视觉 · 光束法平差优化
tags:
- BundleAdjustment
- 3DReconstruction
- GeometricOptimization
- SparseOptimization
- 3DPerception
one_liner: 将高阶几何约束建模为类相机实体，实现兼顾效率与稳定性的富结构光束法平差
practical_value: '- 普通电商/推荐/Agent从业者无直接可借鉴价值，属于3D视觉领域学术贡献

  - 3D商品建模、AR试穿等电商3D场景重建可复用该约束建模方法，控本提效

  - 多约束稀疏优化任务可参考将高阶约束转化为类观测实体的范式，保留稀疏性降本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统光束法平差（BA）仅支持点、线等基础几何特征联合优化，引入平行、共面等高阶几何约束后会大幅提升计算成本、降低数值稳定性，无法支撑富结构3D重建需求。
### 方法关键点
1. 定义特征分类框架，将可直接2D观测的点、线等基础特征与编码高阶关系的特征组分离
2. 将高阶约束特征组建模为BA框架内的类相机实体，把组约束、跨特征关联统一转化为2D重投影误差
3. 保留传统点BA的稀疏矩阵结构，可通过Schur消元优化，避免引入破坏数值稳定性的3D正则项
### 关键结果
真实/合成数据集上运行速度与仅用点的传统BA相当，生成的3D结构更丰富，几何精度显著提升。
