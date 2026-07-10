---
title: 'LiST: Lipschitz Scaling Training for Robust and Calibrated Neural Networks'
title_zh: LiST：面向鲁棒可校准神经网络的利普希茨缩放训练方法
authors:
- Arthur Chiron
- Franck Mamalet
- Thomas Massena
- Thomas Deltort
- Mathieu Serrurier
affiliations:
- IRIT
- IRT Saint Exupéry
- SNCF
- Airbus
arxiv_id: '2607.07745'
url: https://arxiv.org/abs/2607.07745
pdf_url: https://arxiv.org/pdf/2607.07745
published: '2026-07-08'
collected: '2026-07-10'
category: Training
direction: 深度学习模型鲁棒校准训练方法
tags:
- Lipschitz Constraint
- Model Calibration
- Robustness
- Training Paradigm
- Temperature Scaling
one_liner: 建立利普希茨约束与温度缩放的关联，提出LiST训练范式同时兼顾模型准确率、鲁棒性与校准度
practical_value: '- 推荐/广告排序模型可引入Lipschitz约束+动态调整全局L值的思路，在保证排序准确率的同时提升分布外样本鲁棒性，避免流量波动时效果大幅下跌

  - 可借鉴用校准度作为准确率-鲁棒性权衡的选择标准，替代人工调参，解决排序模型预估置信度与实际CTR/CVR偏差过大的问题

  - 校准数据可直接融入LiST训练流程，无需单独后处理温度缩放步骤，节省线上推断开销同时提升样本利用率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有Lipschitz约束模型需人工选择约束值权衡准确率与鲁棒性，校准特性未被充分研究，无法同时满足高准确率、强鲁棒性、置信度校准三个可靠模型的核心要求。
### 方法关键点
1. 论证Lipschitz约束与SOTA校准方法温度缩放存在理论关联，存在最优约束值L*可让模型开箱即校准，校准度可作为准确率-鲁棒性Pareto前沿的选择标准；
2. 提出LiST训练范式，迭代调整全局Lipschitz常数收敛到最优工作点，通过损失的margin参数构建全校准Pareto前沿，灵活调整权衡全程保持校准；
3. 收敛后可直接融合校准数据训练，提升样本效率不损失校准效果。
### 关键结果
在CIFAR-10/100、Tiny-ImageNet数据集上验证，效果优于有约束/无约束基线，同时保持开箱校准能力，准确率、鲁棒性均达可比SOTA水平。
