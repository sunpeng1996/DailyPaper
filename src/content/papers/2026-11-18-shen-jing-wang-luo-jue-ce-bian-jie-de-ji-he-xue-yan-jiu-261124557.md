---
title: The geometry of neural network decision boundaries
title_zh: 神经网络决策边界的几何学研究
authors:
- Dylan M Paiton
- David L Schultheiss
- Matthias Kümmerer
- Zac Cranko
- Matthias Bethge
affiliations:
- University of Tübingen
arxiv_id: '2611.24557'
url: https://arxiv.org/abs/2611.24557
pdf_url: https://arxiv.org/pdf/2611.24557
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 神经网络可解释性 · 决策边界分析
tags:
- NeuralNetwork
- Interpretability
- DecisionBoundary
- AdversarialTraining
- HighDimensionalAnalysis
one_liner: 提出高维输入空间下无失真的神经网络决策边界几何测量与可视化方法
practical_value: '- 对抗训练可缩小样本附近决策边界距离与曲率，可借鉴该结论优化电商分类、召回模型的抗噪鲁棒性

  - 训练策略对决策边界的影响远大于架构选择，调优CTR/CVR、广告排序模型时优先迭代训练方法而非盲目更换大模型架构

  - 高维空间无失真决策边界测量方法可迁移用于推荐模型的可解释性分析，定位误分类/排序异常样本的根因'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统基于降维投影的神经网络决策边界分析方法存在高维信息失真、距离扭曲、无法逆映射回原空间等缺陷，难以支撑高维输入场景下的模型可解释性与鲁棒性优化。
### 方法关键点
提出直接在高维输入空间测量、可视化决策边界几何特征的无失真方法，可量化分析不同输入、模型架构、训练范式下的边界曲率、样本到边界距离两个核心指标。
### 关键结果
1. 随子空间维度提升，边界距离平滑缓慢增长且曲率稳定，证明连续大子空间内决策边界与输入样本距离较近；
2. 对抗训练后样本附近的边界距离、曲率显著降低；
3. 训练策略对边界几何特征的影响强度远高于模型架构、测试集准确率。
