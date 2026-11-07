---
title: Improving Context-Shift Robustness of Convolutional Networks via Context-Regularized
  Cross-Entropy
title_zh: 基于上下文正则化交叉熵提升卷积网络的上下文漂移鲁棒性
authors:
- Jinen Setpal
- Chaoyue Liu
affiliations:
- Elmore Family School of Electrical and Computer Engineering, Purdue University
arxiv_id: '2611.08157'
url: https://arxiv.org/abs/2611.08157
pdf_url: https://arxiv.org/pdf/2611.08157
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 模型训练 · 分布漂移鲁棒性优化
tags:
- Context-Shift
- Convolutional Network
- Feature Attribution
- Cross-Entropy
- Robustness
one_liner: 提出ContrastiveCAMs归因方法与CR-CE损失，提升卷积网络的上下文漂移鲁棒性
practical_value: '- 电商商品图识别、广告素材分类场景可复用CR-CE损失思路，抑制背景等上下文干扰，提升跨场景素材识别准确率

  - ContrastiveCAMs可复用在CV类模型可解释性分析中，定位模型预测依赖的有效特征，筛选非因果干扰特征

  - 推荐系统遇到用户兴趣迁移、节假日上下文漂移等场景时，可类比思路设计正则项抑制非因果上下文特征权重，提升推荐鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
图像分类模型测试阶段常遇到训练未覆盖的上下文场景（即context shift），若模型依赖非因果的上下文线索做预测，会出现显著的性能下降，同时现有特征归因方法存在理论缺陷，无法准确定位预测依赖的有效特征。

### 方法关键点
1. 提出特征归因变体ContrastiveCAMs，生成置信度更高的模型预测归因热力图，精准区分目标相关区域与上下文无关区域；
2. 基于ContrastiveCAMs设计上下文正则化交叉熵损失（CR-CE），在训练阶段抑制上下文区域对预测的影响，引导模型更多依赖目标本身的核心特征完成预测。

### 关键结果
在Waterbirds、Spawrious、ImageNet/ImageNet-BG、Hard-ImageNet等多个中大型数据集上验证，上下文漂移场景下的模型鲁棒性获得一致提升。
