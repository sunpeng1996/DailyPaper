---
title: 'The Quadrilateral Loss: Additivity as a Measurable Behavior of Dense Neural
  Networks'
title_zh: 四边形损失：将加性作为稠密神经网络的可度量行为
authors:
- Antonio Di Cecco
arxiv_id: '2607.20201'
url: https://arxiv.org/abs/2607.20201
pdf_url: https://arxiv.org/pdf/2607.20201
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 神经网络训练 · 加性可解释正则
tags:
- Loss Function
- Additive Model
- Model Interpretability
- Neural Regularization
- Feature Interaction
one_liner: 提出可微分四边形损失，动态调控神经网络加性程度，替代刚性架构级加性约束
practical_value: '- 可解释推荐/广告预估场景可直接引入四边形损失作为正则项，无需重构网络架构就能动态平衡可解释性（加性）与业务精度

  - 小样本推荐/冷启动预估场景下，施加中等强度的四边形损失正则，可同时提升模型精度与可解释性，降低特征交互过拟合

  - 做特征重要性/交互性后解释时，不要依赖正则前的交互大小排序，可基于四边形损失的per-feature surrender曲线得到更可信的结果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统加性模型靠架构强制禁止特征交互获得可解释性，刚性极强，需提前锁定加性假设、无法复用预训练稠密网络，无灵活调整加性程度的中间态，事后交互排序的有效性也缺乏验证。
### 方法关键点
提出可微分的四边形损失：基于交换单特征坐标的训练点对计算二阶混合差，期望等于干预Shapley-GAM的单特征交互量，可直接作为正则项加入训练，无需修改网络架构，就能动态调控模型的加性程度。
### 关键结果
1. 大部分模型学到的特征交互可几乎无精度损失移除；
2. 小数据集上施加中等强度的四边形损失正则，可同时提升模型精度与加性；
3. 正则前的特征交互大小几乎无法预测正则后模型保留的交互，推翻事后交互排序的有效性；
4. 先约束行为再固化结构的加性实现方案，效果显著优于权重空间约束方案。
