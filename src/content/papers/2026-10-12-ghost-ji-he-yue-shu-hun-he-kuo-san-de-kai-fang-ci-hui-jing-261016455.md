---
title: 'GHOST: Geometry-Constrained Hybrid Diffusion for Open-Vocabulary 3D Scene
  Graph Generation'
title_zh: GHOST：几何约束混合扩散的开放词汇3D场景图生成
authors:
- Changqun Feng
- Wangxiandi Yin
- Xin Hu
- Ruiting Dai
- Feiyang Yang
- Jielei Wang
- Tao He
affiliations:
- University of Electronic Science and Technology of China
- Jilin University
arxiv_id: '2610.16455'
url: https://arxiv.org/abs/2610.16455
pdf_url: https://arxiv.org/pdf/2610.16455
published: '2026-10-12'
collected: '2026-10-18'
category: Other
direction: 3D场景图生成 · 扩散模型空间推理
tags:
- Diffusion Model
- 3D Scene Graph
- Open Vocabulary
- Spatial Reasoning
- Geometry Constraint
one_liner: 提出几何约束混合扩散框架GHOST，实现开放词汇3D场景图生成SOTA性能
practical_value: '- 语言嵌入映射可微几何约束的思路，可复用在AR电商场景3D商品属性与文本描述的对齐任务

  - 离散标签+连续特征混合扩散建模方法，可迁移到同时生成结构化语义和连续属性的GenRec任务

  - 空间谓词推理逻辑，可借鉴给室内场景导购Agent做3D空间商品关联推荐'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有开放词汇3D场景图生成方法空间谓词预测效果差，核心问题是语言相似度仅反映语义共现，无法建模显式几何约束，导致关系预测与实际空间布局冲突。
### 方法关键点
1. 提出混合扩散框架GHOST，联合建模连续节点几何特征与离散边谓词，采用几何-约束-谓词的去噪流程，保证关系预测的几何一致性；
2. 设计语言锚定的约束归纳模块，将谓词嵌入映射为可微几何约束，同步引导布局优化和谓词重加权；
3. 实现几何-拓扑协同去噪器，通过噪声自适应交互、朝向感知建模耦合节点与边推理。
### 关键结果
在3DSSG数据集上闭集、开放词汇设置均达SOTA，空间谓词预测效果较RelationField提升超17个百分点。
