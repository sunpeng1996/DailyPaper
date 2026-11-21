---
title: 'SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention'
title_zh: SGAR：基于稀疏几何引导注意力的前馈3D重建方法
authors:
- Aoxiang Fan
- Maria Pilligua
- Corentin Dumery
- Oliver Heinimann
- Pascal Fua
affiliations:
- CVLab, EPFL, Switzerland
arxiv_id: '2611.26493'
url: https://arxiv.org/abs/2611.26493
pdf_url: https://arxiv.org/pdf/2611.26493
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 3D重建 · 稀疏注意力计算优化
tags:
- Sparse Attention
- 3D Reconstruction
- Feed-Forward Network
- Attention Acceleration
- Geometry Prior
one_liner: 通过轻量3D临近预测模块筛选稀疏注意力候选，千视图3D重建速度较稠密方案提升12倍
practical_value: '- 稀疏注意力候选预筛选思路可迁移至长序列推荐、大Batch广告排序场景：先用轻量规则/模型选出高相关候选再做注意力计算，可大幅降低推理延迟

  - 基于业务先验过滤冗余注意力计算的设计逻辑，可复用在跨域推荐、多模态召回的注意力模块优化环节

  - 存量稠密注意力模型可通过微调适配稀疏结构的方案，可用于现有推荐/广告模型的推理加速改造，无需全量重训

  - 若团队涉及电商3D商品建模，可直接复用SGAR框架实现多视图商品3D重建的效率提升'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
前馈3D重建模型依赖稠密全局注意力关联多视图特征，计算复杂度随视图数量呈平方级增长，无法适配大规模多视图重建场景；从经典运动恢复结构先验来看，绝大多数稠密注意力计算是冗余的。
### 方法关键点
1. 提出稀疏几何引导注意力框架SGAR，新增轻量可学习Key选择模块，预测不同视图Token的3D空间临近度，仅为每个Patch Token选择少量跨视图高相关候选Token做注意力计算
2. 结构通用可插拔，可通过微调适配任意现有前馈3D重建模型，无需重构原有模型架构
### 关键结果数字
千视图场景下推理速度比稠密注意力基准快12倍，Pose AUC@30仅下降1.9个百分点；相同时间预算下几何重建覆盖率优于所有对比稀疏方案，是当前精度最高的稀疏前馈3D重建方法
