---
title: 'OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing
  Optimization'
title_zh: OREO：基于实时渲染-编辑优化的3D生成保真度对齐框架
authors:
- Zhiyuan Ma
- Wenbo Hu
- Wang Zhao
- Pengfei Wang
- Ying Shan
- Lei Zhang
arxiv_id: '2609.29788'
url: https://arxiv.org/abs/2609.29788
pdf_url: https://arxiv.org/pdf/2609.29788
published: '2026-09-24'
collected: '2026-09-25'
category: Other
direction: 3D生成保真度对齐优化
tags:
- 3D Generation
- Diffusion Prior
- Fidelity Alignment
- Rendering Optimization
- Self-supervised Optimization
one_liner: 提出动态渲染编辑优化框架OREO，利用2D扩散先验提升3D生成资产的视觉保真度
practical_value: '- 电商3D商品素材生成场景可复用该自监督优化框架，无需额外标注数据集，用2D扩散精修的渲染图作为伪标签迭代3D生成模型，降低素材制作成本

  - 可迁移Reinforced Editing思路，在AIGC业务生成素材时保留核心结构（如商品外形、展示视角）的前提下提升视觉保真度，满足电商展示一致性要求

  - 做3D虚拟试穿、AR商品展示的业务可直接借鉴该动态闭环优化架构，快速提升现有3D生成模型的输出质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D生成模型输出的资产普遍存在视觉保真度不足的问题，传统依赖静态数据集的训练优化方式难以适配不同生成样本的个性化缺陷，且2D扩散模型已经验证的强大保真度优化能力没有被充分融入3D生成链路。
### 方法关键点
1. 搭建无需静态标注数据集的动态优化闭环，实时生成编辑后的渲染图作为2D伪监督目标，降低训练数据依赖；
2. 核心提出Reinforced Editing模块，调用2D模型精修3D输出的多视角渲染视图，优化过程严格保留原始3D资产的几何结构、渲染视角、核心内容，避免精修后与原始3D结构脱节；
3. 用精修后的高保真视图作为监督信号，让3D生成器从自身生成的样本中自学习，逐步迭代提升整体输出质量。
### 关键结果
实验验证OREO框架对各类预训练3D生成基线均有明确提升效果，最终输出的3D资产视觉真实度显著优于基线模型。
