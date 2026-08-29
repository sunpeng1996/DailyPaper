---
title: Reconstructing Humans and Objects in Interaction using Large Reconstruction
  Models
title_zh: 基于大型重建模型的交互场景下人与物体3D重建
authors:
- Agniv Chatterjee
- Georgios Pavlakos
affiliations:
- University of Texas at Austin
arxiv_id: '2608.27407'
url: https://arxiv.org/abs/2608.27407
pdf_url: https://arxiv.org/pdf/2608.27407
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 3D人-物交互 · 大型重建模型应用
tags:
- 3D HOI
- Large Reconstruction Models
- Single-view Reconstruction
- Embodied AI
- Computer Vision
one_liner: 提出MILO框架，借助LRM几何能力从单图实现高精度3D人-物交互重建
practical_value: '- 本研究核心为3D计算机视觉领域技术，面向电商/推荐/广告通用业务场景可迁移价值极低

  - 若业务涉及AR/VR商品试用、具身Agent交互场景，可参考其基于大模型输出几何支架简化下游任务的思路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D人-物交互（3D HOI）是AR/VR、具身AI等领域的核心基础问题，现有单图重建方案受深度歧义、遮挡、物体形状多变限制，依赖重投影、接触约束拟合参数化模型，流程复杂泛化性不足。
### 方法关键点
1. 提出MILO框架，借助大型重建模型（LRM）输出的几何支架作为基础，其天然保留人-物相对位置、邻近关系等核心线索，大幅简化重建流程
2. 将任务重构为LRM网格后处理：先分割为人、物组件，再对人体部分拟合参数化人体模型，物体部分可选对齐预定义模板（如有）
### 关键结果
在多个公开基准、交互场景下的重建精度显著优于现有所有基线方案
