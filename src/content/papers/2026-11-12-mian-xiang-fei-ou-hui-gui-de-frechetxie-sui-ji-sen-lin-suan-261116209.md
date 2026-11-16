---
title: Fréchet Oblique Forest for Non-Euclidean Regression
title_zh: 面向非欧回归的Fréchet斜随机森林算法
authors:
- Jiaye Chen
- Rui Qiu
- Zhou Yu
affiliations:
- East China Normal University
arxiv_id: '2611.16209'
url: https://arxiv.org/abs/2611.16209
pdf_url: https://arxiv.org/pdf/2611.16209
published: '2026-11-12'
collected: '2026-11-16'
category: Other
direction: 非欧度量空间回归算法优化
tags:
- Fréchet Regression
- Random Forest
- Non-Euclidean
- Metric Space
- Regression
one_liner: 提出适配度量空间特征与响应的Fréchet斜森林非欧回归方法，效果优于现有基准
practical_value: '- 涉及非欧结构数据（用户行为图、商品关联网络、时空流量序列）的回归预测场景，可尝试FOF替代传统树模型

  - 度量空间特征拆分环节可复用 pairwise 响应距离评估逻辑，省去重复计算均值的开销，提升训练效率

  - 商圈到店流量、区域订单量、配送运力预测等时空网络任务，可直接复现FOF方案做基准对比'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有回归方法默认欧氏空间假设，无法适配预测因子/响应为分布、协方差矩阵、网络等非欧度量空间对象的场景，传统随机森林的坐标阈值拆分逻辑也不适用于无自然标量坐标的非欧特征。

### 方法关键点
1. 基于Alexandrov内积得分定义度量空间特征的方向拆分规则，欧氏空间下可对齐传统斜拆分逻辑；
2. 采用成对响应距离评估候选拆分效果，避免拆分搜索阶段重复计算Fréchet均值，降低计算开销；
3. 预测阶段跨树平均叶节点权重，最小化加权Fréchet准则生成结果，理论上证明了积分一致性与多项式风险界。

### 关键结果
在矩阵、分布、球面数据、混合特征的模拟实验，以及出租车流量网络预测任务上，预测性能显著优于现有基准方案。
