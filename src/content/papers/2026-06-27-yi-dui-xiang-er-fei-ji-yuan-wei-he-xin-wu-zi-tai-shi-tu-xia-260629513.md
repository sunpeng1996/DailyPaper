---
title: 'Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from
  Unposed Views'
title_zh: 以对象而非基元为核心：无姿态视图下的实例结构化3D Token化方法
authors:
- Mijin Yoo
- In Cho
- Subin Jeon
- Jiwoo Lee
- Eunbyung Park
- Seon Joo Kim
affiliations:
- Yonsei University
- Seoul National University
arxiv_id: '2606.29513'
url: https://arxiv.org/abs/2606.29513
pdf_url: https://arxiv.org/pdf/2606.29513
published: '2026-06-27'
collected: '2026-07-01'
category: Other
direction: 3D场景表示 · 实例级Token化
tags:
- 3D Tokenization
- Instance Segmentation
- Novel View Synthesis
- Differentiable Rendering
- Open-vocabulary Retrieval
one_liner: 提出无3D标注的前馈框架，从无姿态多视图图像直接生成实例结构化3D Token组，支持重建、编辑与检索
practical_value: '- 3D电商商品建模可复用双级Token拆分方案：用实例Token存储商品身份、anchor Token存储外观几何，大幅降低商品编辑、替换的开发成本

  - 大规模3D商品库检索可借鉴该检索复杂度随实例数而非点云基元数缩放的思路，显著提升检索效率

  - 无3D标注的训练范式可迁移至多视图电商商品3D重建场景，降低3D训练数据的标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有前馈3D重建方法输出无结构点云或3D Gaussian，实例级结构需事后提取，且3D标注训练成本高。
### 方法关键点
1. 设计双级Token组结构：每个实例对应1个捕获实体身份的实例Token + 多个编码局部几何、外观的anchor Token，最终解码为3D Gaussian集合
2. 无需3D标注，通过可微渲染结合重建、分割联合监督完成训练
3. 实例结构为表示原生属性，无需额外后处理即可支持实例级操作
### 关键结果
类无关实例分割效果超越逐场景优化基线，新视角合成效果具备竞争力；同时原生支持实例级场景编辑（增删移对象）、开放词汇3D实例检索，检索复杂度随实例数而非基元数缩放。
