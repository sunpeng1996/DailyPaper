---
title: 'Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical
  Attribute Prediction'
title_zh: Pose-to-Biomechanics：3D人体姿态估计与生物力学属性预测的桥梁
authors:
- Ayda Eghbalian
- Kevin Desai
affiliations:
- University of Texas at San Antonio
arxiv_id: '2607.08725'
url: https://arxiv.org/abs/2607.08725
pdf_url: https://arxiv.org/pdf/2607.08725
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 3D人体姿态估计 · 生物力学属性预测
tags:
- 3D Human Pose Estimation
- Temporal Transformer
- Biomechanics
- Modular Plugin
- Cross-Modal Supervision
one_liner: 提出即插即用的轻量化时序Transformer BioModule，可对接任意3D姿态估计器输出生物力学属性
practical_value: '- 模块化无侵入的插件设计思路可复用，针对存量推荐/LLM系统新增下游能力时无需修改上游模型，大幅降低迭代成本

  - 跨数据集坐标系对齐、帧级精准跨模态监督的方法可迁移至多模态训练数据的对齐预处理环节

  - 若涉及运动健身、康复类电商/内容场景，生物力学属性可作为新的用户特征维度优化推荐精准度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有3D人体姿态估计模型仅优化几何关键点精度，无法输出康复、运动科学、人机交互等场景所需的生物力学属性，存在能力断层。
### 方法关键点
1. 提出轻量化时序Transformer插件BioModule，可对接任意3D姿态估计器的17关节3D骨架输出，无需修改上游模型即可扩展生物力学预测能力
2. 构建大规模对齐数据集，打通Human3.6M的3D关键点与Human3.6Mplus的生物力学标签空间，完成坐标系解剖学对应验证，实现帧级跨模态监督
3. 基于7个SOTA 3D姿态估计器做基准测试，首次系统性分析上游姿态估计质量对下游生物力学预测精度的传导影响
### 关键结果
BioModule作为低算力消耗的模块化组件，可高效补全现有姿态估计系统的可解释物理运动分析能力，成为视觉姿态估计到生物力学落地应用的高效衔接方案
