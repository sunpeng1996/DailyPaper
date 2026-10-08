---
title: 'Tetris3D: 3D Scene Generation With Objects That Fit Together'
title_zh: Tetris3D：面向物体适配的3D场景生成框架
authors:
- Jaeyeong Kim
- Jinhyuk Jang
- Jongmin Lee
- Kyehong Park
- Seungryong Kim
affiliations:
- KAIST AI
arxiv_id: '2610.10539'
url: https://arxiv.org/abs/2610.10539
pdf_url: https://arxiv.org/pdf/2610.10539
published: '2026-10-06'
collected: '2026-10-08'
category: Other
direction: 3D场景生成 · 物理一致性建模
tags:
- 3DSceneGeneration
- PhysicsAwareGeneration
- 3DReconstruction
- AutoregressiveGeneration
- Dataset
one_liner: 提出物理感知的3D场景生成框架Tetris3D及1.2M标注物理关系的ComOb数据集，性能达SOTA
practical_value: '- 仅电商AR导购、3D商品场景搭建类业务可参考其邻域物体几何/物理约束的生成思路，提升3D场景合理性

  - 构建包含实体间关系的标注数据集时，可借鉴ComOb基于物理仿真批量生成标注数据的范式

  - 普通搜索推荐、LLM+Agent搜推优化场景无直接可迁移价值'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有单图3D场景重建方法多独立生成物体或隐式耦合，对邻接交互物体的细粒度空间兼容性指导不足，无法保证场景整体的几何、物理一致性。
### 方法关键点
1. 提出Tetris3D自回归生成框架，显式将每个物体的生成条件绑定周边物体的几何特征与物理关系，约束其形状、位姿的合理性；
2. 发布ComOb数据集，基于物理仿真生成1.2M包含多类别物体交互的场景，提供逐物体网格与成对物理关系标注。
### 关键结果
在合成与真实场景测试中，即使交互区域被遮挡仍可恢复一致的物体形状与位姿，生成质量、物理稳定性均达SOTA。
