---
title: Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings
  and Faster Convergence
title_zh: 用于灵活几何最优嵌入与更快收敛的对比坍缩损失CoCo
authors:
- Blanca Cano-Camarero
- Ángela Fernández-Pascual
- José R. Dorronsoro
arxiv_id: '2607.12916'
url: https://arxiv.org/abs/2607.12916
pdf_url: https://arxiv.org/pdf/2607.12916
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: 表征学习 · 损失函数优化
tags:
- Contrastive Loss
- Representation Learning
- Embedding
- Convergence Optimization
- Loss Function
one_liner: 提出对比坍缩损失CoCo，实现类内紧聚类类间大角距，加快表征收敛同时保持SOTA级预测性能
practical_value: '- 召回/粗排阶段的用户/物品表征学习可替换交叉熵损失为CoCo，加快模型收敛速度，降低训练成本

  - 多模态语义表征训练中引入CoCo损失，可强化类内聚类、增大不同类目/意图表征的角距，提升召回准确率

  - 冷启动场景的小样本表征训练可复用CoCo梯度更优、初始化更接近最优配置的特性，减少冷启动迭代轮次'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
对比学习、交叉熵等常用表征学习损失要么难以保障类内表征紧聚类，要么类间角距不足，且收敛速度慢，无法满足大规模推荐场景下表征学习的效率与效果双重需求

### 方法关键点
1. 提出CoCo（Contrastive-Collapsed）损失，同时约束类内表征坍缩聚类、类间表征对比分离，保留神经网络灵活性以学习类间大角距的几何最优嵌入
2. 理论论证相比点回归、交叉熵损失，CoCo初始化更接近最优配置，梯度信息量更高，类内坍缩约束更强

### 关键结果
在OpenML-CC18基准多类表格数据集上，CoCo性能与核SVM、随机森林、交叉熵基神经网络等SOTA方法持平；类内聚类紧密度显著提升，收敛速度较基线明显加快
