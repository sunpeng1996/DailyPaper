---
title: Pragmatic DML with AI-Learned Representations
title_zh: 基于AI学习表征的实用双机器学习（DML）方法
authors:
- Andres Aradillas Fernandez
- Victor Chernozhukov
- Carlos Cinelli
- Sven Klaassen
- Whitney Newey
- Martin Spindler
- Jan Teichert-Kluge
- Suhas Vijaykumar
arxiv_id: '2610.01935'
url: https://arxiv.org/abs/2610.01935
pdf_url: https://arxiv.org/pdf/2610.01935
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 因果推断 · 学习表征增强DML
tags:
- Causal_Inference
- Double_Machine_Learning
- Learned_Representations
- Embedding
- Sensitivity_Analysis
one_liner: 验证AI学习表征用于因果推断的有效性，提出兼容表征学习的实用DML框架与敏感度分析方案
practical_value: '- 电商定价/营销活动效果的因果评估场景，可直接复用交叉拟合DML+多模态表征的方案，降低商品图文、用户行为序列等复杂协变量带来的估计偏差

  - 表征拟合效果较差的场景，可采用论文提出的敏感度区域分析方法，快速判断因果结论的鲁棒性，避免策略迭代时误判效果

  - 多源表征融合的因果推断任务，可复用fold-wise表征微调+star聚合管线，兼顾推断有效性与表征拟合能力'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前文本、图像、用户行为序列等复杂协变量常被压缩为AI学习表征后用于因果分析，但该范式的有效性缺乏理论支撑，表征误差会导致因果参数估计失真，缺乏可落地的工程化框架。

### 方法关键点
1. 证明 imperfect 表征带来的因果参数偏差等于结果回归误差与平衡权重（Riesz表示器）误差的乘积；
2. 提出交叉拟合DML框架，对表征依赖的目标参数可提供有效Wald推断，小误差下可达半参数效率界；
3. 兼容折内表征学习/微调，配套凸聚合、star聚合管线融合多源表征；
4. 大表征误差场景下可输出可解释敏感度区域与端点的root-n推断。

### 关键结果
多模态商品需求预测任务中，7种表征的单独估计与star聚合结果均显示排名定价的价格弹性接近-1，且在全部敏感度网格下保持鲁棒。
