---
title: An Efficient Newton Algorithm for Nonnegative Matrix Factorization with the
  Kullback-Leibler Divergence
title_zh: 基于KL散度的非负矩阵分解高效牛顿优化算法
authors:
- Damien Lesens
- Jérémy E. Cohen
- Bora Uçar
affiliations:
- ENS de Lyon
- Univ. Lyon, INSA-Lyon, CNRS, Inserm, CREATIS
- CNRS, LIP, Université de Lyon
arxiv_id: '2607.13919'
url: https://arxiv.org/abs/2607.13919
pdf_url: https://arxiv.org/pdf/2607.13919
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 非负矩阵分解优化 · 损失二阶逼近
tags:
- NMF
- KL-divergence
- Newton-method
- HALS
- Optimization
one_liner: 针对KL散度NMF提出二阶牛顿型优化方法，泛化HALS算法，收敛可证且性能优于现有SOTA
practical_value: '- 推荐场景中用户-物品交互计数矩阵（点击、购买等泊松分布数据）的NMF建模可替换原KL-NMF优化器，提升收敛速度与拟合精度

  - 现有基于HALS的Frobenius范数NMF实现可直接复用本文提出的HALS泛化逻辑，低成本扩展支持KL散度损失

  - 泊松分布计数类特征（搜索词频次、用户行为频次）的降维、隐语义建模可直接采用该算法，获得更优可解释性因子'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有KL-NMF算法大多通过最小化损失的可分上界迭代求解，优化性能已触及瓶颈；而计数类数据（如用户行为计数、词频矩阵）符合泊松分布，KL散度是最优拟合指标，亟需更高效的优化方案。
### 方法关键点
1. 放弃传统可分上界逼近，改用损失的二阶泰勒展开构造牛顿型优化代理函数
2. 泛化经典HALS（分层交替最小二乘）算法，对不可分解的二阶代理函数做高效求解
3. 算法提供严格收敛性证明，无需额外调参即可稳定运行
### 关键结果
在多类公开数据集上性能全面优于现有SOTA KL-NMF算法，收敛速度与拟合精度均有显著提升，无精度下降情况。
