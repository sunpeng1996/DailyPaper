---
title: Parallel gradient boosting for flexible estimation of conditional distributions
title_zh: 面向条件分布灵活估计的并行梯度提升算法
authors:
- Rémy Chapelle
- Nicolas Vayatis
- Bruno Falissard
- Mohammed Sedki
affiliations:
- Université Paris-Saclay, UVSQ, Inserm, CESP
- Université Paris-Saclay, Université Paris Cité, ENS Paris-Saclay, CNRS, SSA, Inserm,
  Centre Borelli
- École du Val-de-Grâce, Service de Santé des Armées
arxiv_id: '2607.13550'
url: https://arxiv.org/abs/2607.13550
pdf_url: https://arxiv.org/pdf/2607.13550
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 梯度提升训练优化 · 多输出回归
tags:
- Gradient Boosting
- Multi-output Regression
- Quantile Regression
- High-dimensional Learning
- Efficient Training
one_liner: 提出通用并行梯度提升算法，多输出任务精度比肩XGBoost同时速度提升多个数量级
practical_value: '- 电商多阈值预测场景（如多分段销量预测、客群消费能力分层预测）可直接复用该并行梯度提升框架，替换现有XGBoost多输出训练逻辑，不损失精度的前提下大幅降低训练耗时

  - 高维稀疏特征+存在缺失值的推荐场景（如行为特征不全的冷启动用户建模）可直接使用该条件分布估计器，效果优于传统半参数估计器

  - 自研树模型训练框架时可借鉴公共下降方向的设计思路，无需绑定特定损失函数与基学习器，大幅提升多输出任务的训练扩展性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统梯度Boosting扩展至多输出任务（如多阈值分位数回归、条件分布估计）时，每次迭代需为每个目标单独训练基模型，计算成本极高；现有加速方案大多绑定特定损失函数与决策树基学习器，通用性差。
### 方法关键点
并行梯度提升算法核心是为所有训练样本采用统一公共下降方向，每次迭代仅需训练1个基模型，不受输出目标数量限制，且不绑定特定损失与基学习器类型，同时给出了算法收敛的充分条件。
### 关键结果
多阈值分位数回归任务上，预测精度与XGBoost持平，训练速度快数个数量级；高维特征、混合/缺失协变量场景下，条件分布估计效果显著优于其他非参数、半参数估计器。
