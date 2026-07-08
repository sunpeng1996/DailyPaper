---
title: Leveraging Extragradient for Effective Sharpness-Aware Minimization in Deep
  Learning
title_zh: 利用外梯度实现深度学习中高效的锐度感知最小化
authors:
- Yao Fu
- Chunxia Zhang
- Junmin Liu
- Yihang Jin
- Haishan Ye
- Yuanao Yang
arxiv_id: '2607.06151'
url: https://arxiv.org/abs/2607.06151
pdf_url: https://arxiv.org/pdf/2607.06151
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 深度学习训练优化 · 泛化性提升
tags:
- Optimizer
- Sharpness-Aware Minimization
- Extragradient
- Generalization
- Training Efficiency
one_liner: 提出基于外梯度的EISAM优化器，泛化性、训练效率优于SAM，对扰动半径敏感度更低
practical_value: '- 推荐系统召回/排序/CTR预估模型训练时，可尝试用EISAM替换现有Adam/SAM优化器，降低过拟合风险，提升离线/线上泛化效果

  - 可复用EISAM对扰动半径低敏感的特性，减少多场景推荐模型训练的调参成本，适配不同业务的数据分布

  - 两阶段参数更新的思路可迁移到推荐领域大模型微调场景，平衡训练效率和泛化性能，减少小样本场景下的过拟合'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统SGD、Adam等优化器易收敛到损失曲面的尖锐极小值，导致模型泛化性差、过拟合风险高；现有SAM优化器虽能寻找平坦极小值提升泛化，但对扰动半径敏感，调参成本高，适配不同场景难度大。
### 方法关键点
提出外梯度启发的锐度感知最小化优化器EISAM，采用两步更新流程：预测步探索损失曲面几何结构，扰动步结合基础优化器完成参数更新，从理论上收紧泛化界，引导参数收敛到曲率更低的平坦极小值。
### 关键结果
在多架构多基准数据集上，测试精度、训练效率均优于SGD、Adam、SAM；对扰动半径的敏感度显著降低，调参难度大幅下降。
