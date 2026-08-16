---
title: High-dimensional networks and mean squared error for possibly misspecified
  models
title_zh: 模型可能误设场景下的高维网络与均方误差研究
authors:
- Lourens Waldorp
affiliations:
- University of Amsterdam
arxiv_id: '2608.13171'
url: https://arxiv.org/abs/2608.13171
pdf_url: https://arxiv.org/pdf/2608.13171
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 高维模型选择 · 双 descent 邻域估计
tags:
- high-dimensional-network
- model-selection
- double-descent
- MSE
- minimum-description-length
one_liner: 高维场景下采用最小描述长度准则可实现低假阳率节点邻域估计，不受线性模型假设是否成立影响
practical_value: '- 构建电商商品关联网络、用户行为共现网络时，高维少样本场景下用最小描述长度准则替代Lasso/AIC/BIC，可大幅降低虚假关联的假阳率

  - 调优高维线性模型的ridge惩罚系数时，可参考模型空间体积纳入惩罚项，有效降低测试方差

  - 训练参数量大于样本量的小域推荐模型时，可结合双 descent 规律调整正则强度，跳出传统bias-variance权衡的认知误区'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维网络分析中为避免遗漏变量关联，常出现参数量远大于观测样本的场景，传统邻域估计方法（Lasso、AIC、BIC）假阳率高，且当模型假设误设（如真实为非线性但假设线性）时效果严重退化。

### 方法关键点
分析ridge惩罚系数对均方误差的影响，结合机器学习双 descent 现象规律，将模型空间体积纳入惩罚项，采用最小描述长度准则完成节点邻域选择。

### 关键结果
理论证明高维场景下，无论线性模型假设是否成立，最小描述长度准则均可实现低假阳率的邻域估计；调整ridge参数可降低测试方差，得到边量更大的有效邻域，对比传统方法假阳率显著下降。
