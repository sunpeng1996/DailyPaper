---
title: Gradient Concentration, Not Weight Saliency, Explains Representation-Level
  Class Unlearning
title_zh: 梯度集中度而非权重显著性可解释表征层面的类别遗忘
authors:
- Billel Habbati
- Alessio Merlo
- Luca Verderame
- Meriem Guerar
affiliations:
- University of Genova
- Centre for Defense Higher Studies (CASD)
arxiv_id: '2607.21353'
url: https://arxiv.org/abs/2607.21353
pdf_url: https://arxiv.org/pdf/2607.21353
published: '2026-07-23'
collected: '2026-07-25'
category: Training
direction: 机器遗忘 · 表征级类别遗忘机制
tags:
- Machine_Unlearning
- Gradient_Concentration
- Weight_Saliency
- Representation_Learning
- Parameter_Selection
one_liner: 通过受控消融证明表征层面类别遗忘的核心驱动为梯度集中度而非权重显著性
practical_value: '- 电商/推荐模型满足合规性做用户/类别级数据遗忘时，无需优化基于权重显著性的参数选择策略，可直接用随机掩码或无约束更新降低工程复杂度

  - 遗忘更新可优先针对模型顶层几层（92%的遗忘梯度能量集中在顶层），大幅降低计算开销的同时保证遗忘效果与全量更新一致

  - 若需实现更彻底的表征级遗忘，应优先设计直接作用于隐层表征的损失目标，无需在参数选择策略上做过度优化'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前主流机器遗忘方案多基于梯度显著性筛选参数子集执行遗忘更新，但该策略对表征级遗忘的实际贡献长期未被验证，存在大量无效优化。
**方法关键点**：针对SalUn框架的显著性掩码机制做受控消融实验，在CIFAR-10/100数据集、ResNet-18模型下，固定遗忘目标、优化调度、计算预算，对比等稀疏度的显著性掩码、随机掩码、无约束更新三类方案的表征级遗忘效果。
**关键结果**：三类方案的表征级可恢复性无统计差异；遗忘梯度约92%的平方梯度能量集中在网络顶层，所有掩码策略均作用于同一表征子空间；显著性掩码类别特异性仅0.09-0.11，不同遗忘类别的参数选择重合度极高；表征级遗忘核心由梯度集中度和表征几何结构决定，与显著性选参无关。
