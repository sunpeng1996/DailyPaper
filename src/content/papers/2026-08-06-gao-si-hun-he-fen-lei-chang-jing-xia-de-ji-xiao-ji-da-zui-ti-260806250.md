---
title: Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification
title_zh: 高斯混合分类场景下的极小极大最优早停梯度下降算法
authors:
- Alex Buna
- Shirley Xiaoqi Liu
- Patrick Rebeschini
affiliations:
- Department of Statistics, University of Oxford
arxiv_id: '2608.06250'
url: https://arxiv.org/abs/2608.06250
pdf_url: https://arxiv.org/pdf/2608.06250
published: '2026-08-06'
collected: '2026-08-09'
category: Training
direction: 模型训练 · 梯度下降早停策略优化
tags:
- Gradient Descent
- Early Stopping
- Minimax Optimization
- Gaussian Mixture Model
- Classification
one_liner: 证明带标签翻转噪声的高斯混合模型下合适时机早停的GD可达极小极大最优分类风险
practical_value: '- 电商/广告分类任务（如点击率预测、商品类目预测）过参数训练时，可优先测试早停策略替代全量插值训练，大幅降低达到相同泛化精度所需的样本量

  - logistic loss训练的分类任务做风险评估时，可复用论文提出的logistic风险到0-1风险的校准方法，消除标准界的平方根率损失，得到更紧的风险上界

  - 高维稀疏特征的分类场景（如用户行为标签建模），协方差谱衰减快时，早停时机可参考文中的极小极大最优停止规则做调参'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
过参数分类场景下，训练数据常线性可分但底层真实分布不可分，logistic loss上的梯度下降（GD）训练收敛到最大间隔插值分类器，其隐含偏置导致统计性能次优，全量插值训练泛化效率极低。
### 方法关键点
针对带标签翻转噪声的高斯混合分类场景，推导最优早停时机的GD策略，提出新校准方法将excess logistic risk转换为excess 0-1风险，适配标签翻转噪声带来的模型误配，同时消除标准界的平方根率损失。
### 关键结果
1. 协方差谱快速连续衰减（含多项式、指数衰减）场景下，早停GD可达极小极大最优excess 0-1风险；
2. 线性插值分类器达到相同excess风险所需样本量比早停GD高指数级；
3. 所有理论结论均通过实验验证
