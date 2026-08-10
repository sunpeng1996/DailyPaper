---
title: 'InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene
  Understanding'
title_zh: InstanceSplat：面向场景理解的实例感知前馈3D高斯溅射方法
authors:
- Minchao Jiang
- Xiaoxuan Ma
- Shunyu Jia
- Haoru Wang
- Zhang Liang
- Wentao Zhu
affiliations:
- Shanghai Jiao Tong University
- Eastern Institute of Technology, Ningbo
- Carnegie Mellon University
- Xidian University
- Peking University
arxiv_id: '2608.07144'
url: https://arxiv.org/abs/2608.07144
pdf_url: https://arxiv.org/pdf/2608.07144
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 3D场景理解 · 3D高斯溅射
tags:
- 3DGS
- Scene Understanding
- 3D Reconstruction
- Instance Segmentation
- Open-Vocabulary
one_liner: 提出无位姿多视图输入的统一前馈3DGS框架，同步实现高泛化性3D重建与实例感知场景理解
practical_value: '- 可借鉴到电商3D商品建模场景：无需精准相机位姿即可从多图快速生成带实例语义的3D商品模型，大幅降低商家3D内容生产成本

  - 实例中心多任务联合学习策略可复用：针对电商多模态内容理解场景，用共享结构关联重建、实例识别、语义理解三个任务，提升整体效果

  - 语言对齐语义增强同类别实例区分的思路，可迁移到同款商品识别、细粒度商品分类等业务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有前馈3DGS场景理解方法多为类别导向，而实例感知3DGS方法依赖逐场景优化，且重建与实例、语义学习解耦，限制了任务间的正向交互，无法满足无位姿输入下的高泛化场景理解需求。
### 方法关键点
1. 仅需一次前向传播，即可构建联合编码外观、几何、实例ID、语言对齐语义的实例感知高斯表示；
2. 用共享3D高斯锚定跨视图实例身份，生成可渲染、跨视图一致的实例特征；
3. 设计实例中心学习策略，通过共享实例结构关联三类任务：实例线索引导重建，语言对齐语义增强同类易混淆实例区分度，实例区域聚合语义证据生成连贯的物体级预测。
### 关键结果
在新视角合成、实例分割、开放词汇语义理解三类任务，以及不同输入视图设置、未见数据集上均取得SOTA性能，兼具高推理效率与强泛化能力。
