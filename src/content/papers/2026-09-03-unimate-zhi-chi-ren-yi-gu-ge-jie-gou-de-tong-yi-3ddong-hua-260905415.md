---
title: 'UniMate: One Unified Model to Animate Diverse Skeletons'
title_zh: UniMate：支持任意骨骼结构的统一3D动画生成基础模型
authors:
- Linzhan Mou
- Jiahui Lei
- Zhiyang Dou
- Chenyue Cai
- Chaoyue Song
- Adam Finkelstein
- Szymon Rusinkiewicz
affiliations:
- Princeton University
- University of California, Berkeley
- Massachusetts Institute of Technology
- Nanyang Technological University
arxiv_id: '2609.05415'
url: https://arxiv.org/abs/2609.05415
pdf_url: https://arxiv.org/pdf/2609.05415
published: '2026-09-03'
collected: '2026-09-08'
category: Other
direction: 3D动画生成 · 拓扑通用基础模型
tags:
- Diffusion Transformer
- 3D Animation
- Topology-aware Modeling
- Zero-shot Generation
- Graph Embedding
one_liner: 提出拓扑感知扩散Transformer，单模型实现任意骨骼零样本文本驱动动画生成
practical_value: '- 该论文属于计算机图形学领域，核心面向3D动画生成，对搜推广核心业务可迁移性有限，仅方法层可参考

  - 图感知注意力偏置+谱旋转位置嵌入的设计，可迁移到用户行为异构图、商品关联图表征建模，提升跨结构泛化能力

  - 全局拓扑条件器的注意力池化思路，可用于冷启动用户/商品的全局结构特征提取，降低微调成本

  - 若业务涉及虚拟主播动作生成、3D商品动态展示，可直接复用该模型实现文本驱动动画生成'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有骨骼动画生成模型受拓扑强约束，依赖类别特定模板，推理时需逐骨骼微调或提供参考动作，无法适配规模化自动绑定后的3D资产动画生成需求。

### 方法关键点
1. 提出拓扑感知扩散Transformer，通过三个机制将骨骼拓扑融入注意力：基于关节对关系与测地距离的图感知注意力偏置、通过图拉普拉斯将RoPE扩展到任意运动树的谱旋转位置嵌入、从静止姿态骨架注意力池化得到的全局拓扑条件器。
2. 构建UniML3D数据集，包含13006条覆盖双足、四足、鸟类、海洋生物、昆虫、蛇形、关节刚性物体的动作序列，完成统一规范化与文本配对。

### 关键结果
效果全面超越SOTA基线，支持零样本跨拓扑迁移、动作补间、扩展、文本引导编辑，推理无需测试时优化或逐骨骼重训练。
