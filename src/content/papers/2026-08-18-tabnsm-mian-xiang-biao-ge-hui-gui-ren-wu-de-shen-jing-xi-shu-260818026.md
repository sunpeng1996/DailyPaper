---
title: 'TabNSM: Neural Sparse Mixer for Tabular Regression'
title_zh: TabNSM：面向表格回归任务的神经稀疏混合器框架
authors:
- Ali Eslamian
- Qiang Cheng
affiliations:
- University of Kentucky
- Department of Computer Science, University of Kentucky
- Institute for Biomedical Informatics, University of Kentucky
arxiv_id: '2608.18026'
url: https://arxiv.org/abs/2608.18026
pdf_url: https://arxiv.org/pdf/2608.18026
published: '2026-08-18'
collected: '2026-08-19'
category: Other
direction: 深度学习 · 高维表格回归建模
tags:
- Tabular Modeling
- Sparse Attention
- Regression
- Loss Design
- Sampling Strategy
one_liner: 提出面向高维表格回归的稀疏交互框架，搭配专项损失与采样策略，兼顾预测效果与可扩展性
practical_value: '- 电商高维用户/物品特征的CTR、转化率、销量等回归任务，可复用ASIM的稀疏交互思路，降低高维特征建模计算开销

  - 回归类预估场景可尝试GridLoss序感知软分箱损失，引入目标序列结构信息优化表征学习效果

  - 难样本挖掘场景可复用RISE难度感知采样策略，基于损失分桶重加权样本，提升难样本拟合精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维表格回归场景下，树模型鲁棒但不支持端到端表征学习，深度模型特征学习灵活但交互建模成本高、对噪声/冗余特征敏感，现有方案难以兼顾效果与可扩展性。
### 方法关键点
核心为Adaptive Sparse Interaction Module (ASIM)，融合前景特征发现、稀疏局部交互编码、Feature-Token Mixing，固定稀疏配置下复杂度接近线性；搭配三个回归专项优化：Multi-Stage Regression Head渐进式优化预测结果、GridLoss序感知软分箱目标引入标签结构信息、RISE基于损失分桶的难度感知重采样策略。
### 关键结果
在9个真实世界回归基准数据集上预测表现领先，在高维、异构数据集上增益尤其稳定，同时具备良好的工程可扩展性。
