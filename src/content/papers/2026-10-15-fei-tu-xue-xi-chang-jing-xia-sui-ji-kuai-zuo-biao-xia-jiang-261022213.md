---
title: Generalization Guarantees of Randomized Block Coordinate Descent for Nonconvex
  Learning
title_zh: 非凸学习场景下随机块坐标下降法的泛化性保证
authors:
- Ruixi Hu
- Liang Wu
affiliations:
- Center of Statistical Research, School of Statistics and Data Science, Southwestern
  University of Finance and Economics
arxiv_id: '2610.22213'
url: https://arxiv.org/abs/2610.22213
pdf_url: https://arxiv.org/pdf/2610.22213
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 大规模机器学习优化 · 非凸场景泛化理论
tags:
- RBCD
- Nonconvex Optimization
- Generalization Bound
- Early Stopping
- Large-scale ML
one_liner: 为非凸场景的RBCD算法推导高概率泛化界，给出优化与泛化平衡方案
practical_value: '- 训练大规模推荐/广告排序模型采用RBCD优化时，可参考论文给出的多项式衰减步长+早停阈值调参方案，平衡训练效率和泛化性能，降低过拟合风险

  - 高维稀疏特征的非凸推荐模型训练，可复用论文给出的维度无关泛化界作为模型泛化能力的预评估参考

  - 分布式RBCD训练框架设计时，可基于推导的泛化边界定分块更新的迭代次数上限，减少不必要的训练资源消耗'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有RBCD算法的理论分析多聚焦优化收敛性，非凸场景下的泛化行为缺乏系统量化支撑，无法指导大规模非凸ML任务的算法调优。

### 方法关键点
1. 仅基于标准平滑假设，推导通用非凸场景下经验风险与群体风险的梯度高概率边界
2. 采用多项式衰减步长，通过迭代次数调优平衡优化效果与泛化性能，量化早停对群体梯度最优收敛速率的增益
3. 梯度主导场景下推导的函数次优性边界接近凸/低噪场景的最优速率，特定结构损失函数下给出维度无关泛化界

### 关键结果
梯度主导场景下泛化速率接近凸/低噪场景最优值，特定结构损失下泛化界不受维度限制，可直接支撑高维非凸学习任务的RBCD算法调优
