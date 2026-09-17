---
title: 'NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting'
title_zh: NormLift：面向3D高斯泼溅的特征升维语义可靠性优化方法
authors:
- Yihan Zang
- Da Li
- Dominik Engel
- Shinkyu Park
- Ivan Viola
affiliations:
- King Abdullah University of Science and Technology
arxiv_id: '2609.18898'
url: https://arxiv.org/abs/2609.18898
pdf_url: https://arxiv.org/pdf/2609.18898
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 3D视觉 · 开放词汇语义理解
tags:
- 3D Gaussian Splatting
- CLIP
- Feature Lifting
- Semantic Reliability
- Open-vocabulary Segmentation
- Training-free
one_liner: 从3D侧推导特征升维闭式解，提出无需训练的语义可靠性校准框架提升开放词汇3D任务性能
practical_value: '- 可复用特征范数作为语义可靠性信号的思路，在多模态召回、跨域特征对齐等场景中过滤低置信度特征，提升匹配精度

  - 无需训练的模式投票优化策略可迁移至多视图特征聚合任务，避免线性平均破坏预训练embedding的语义有效性

  - 余弦对齐视角推导特征聚合规则的方法论，可用于优化跨模态embedding融合逻辑，适配下游余弦匹配的检索场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有将2D语义特征升维至3D高斯的免训练加权聚合方案仅从渲染侧做理论解释，假设特征为线性可组合的欧氏变量，未匹配下游3D任务中基于余弦的独立查询场景，语义可靠性缺乏支撑。
### 方法关键点
1. 从3D侧将单高斯特征分配建模为CLIP单位球上的余弦对齐问题，推导得出L2归一化语义反投影特征为闭式解，补全了标准升维规则的理论解释；
2. 分解特征范数为视图内/视图间一致性指标，提出直接用特征幅值作为语义可靠性信号；
3. 基于多视图校准的可靠性分数引导模式投票优化，避免线性平均破坏CLIP特征原生有效性，全程无需训练。
### 关键结果
在开放词汇3D语义分割任务上，NormLift在所有评估协议下均取得优异性能，计算效率远高于需训练的同类方案。
