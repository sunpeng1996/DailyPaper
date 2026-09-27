---
title: 'Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo
  Captures'
title_zh: Ego-Exo4D人体网格数据集：面向主客视角采集的4D人体运动重构
authors:
- Abhiram Maddukuri
- Georgios Pavlakos
affiliations:
- The University of Texas at Austin
arxiv_id: '2609.30187'
url: https://arxiv.org/abs/2609.30187
pdf_url: https://arxiv.org/pdf/2609.30187
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 具身AI · 4D人体运动数据集构建
tags:
- Ego-Exo4D
- Human Mesh Reconstruction
- 4D Human Motion
- Dataset
- Embodied AI
one_liner: 为Ego-Exo4D数据集补充大规模稠密4D人体运动重构标注及配套处理管道
practical_value: '- 从事电商AR试穿、虚拟数字人带货、直播动作交互业务的团队，可直接复用该数据集的SMPL-H人体运动序列训练动作生成模型

  - 配套的多视角同步人体运动重构管道可迁移到线下用户行为采集、直播场景动作识别的预处理环节

  - 非视觉交互/具身方向的搜推、LLM Agent从业者无直接可复用价值'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Ego-Exo4D作为大规模主客视角同步视频数据集，是具身AI、技能学习、动作理解等方向的核心数据源，但仅提供稀疏3D人体姿态标注，现有3D人体重构方案在其大规模多视角数据上鲁棒性差，大幅提升了下游任务的数据处理成本。
### 方法关键点
1. 适配Ego-Exo4D的同步多相机采集架构，基于SOTA 3D人体姿态重构方法优化，构建端到端4D人体运动恢复管道
2. 生成全量SMPL-H格式的稠密人体网格运动序列，形成Ego-Exo4D-HM数据集，同步开源管道代码、数据集及配套文档
### 结果
覆盖Ego-Exo4D全量采集序列的4D人体运动标注，可支撑后续技能评估、具身Agent交互、动作识别等任务直接调用，无需重复处理原始视频数据
