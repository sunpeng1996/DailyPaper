---
title: Orthogonal Polynomial Approximation for Matrix Log Normalization in Global
  Covariance Pooling
title_zh: 全局协方差池化中矩阵对数归一化的正交多项式逼近方法
authors:
- Md Rifat Ur Rahman
- Md Raihan Khan
- Md Sakib Hossain Shovon
- Pietro Liò
- Mohammad Ali Moni
affiliations:
- NeuronAITree
- Cambridge University
arxiv_id: '2608.19021'
url: https://arxiv.org/abs/2608.19021
pdf_url: https://arxiv.org/pdf/2608.19021
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 二阶特征统计 · 矩阵归一化优化
tags:
- Global Covariance Pooling
- Matrix Normalization
- Polynomial Approximation
- SPD Manifold
- Numerical Stability
one_liner: 用8阶切比雪夫多项式逼近矩阵对数，解决GCP归一化的梯度数值不稳定问题
practical_value: '- 涉及用户/物品协方差特征建模的推荐场景，可复用均值特征预归一化+标量后补偿的trick，规避log函数奇点问题

  - 涉及矩阵运算的特征归一化模块，可借鉴切比雪夫多项式逼近方案替代特征分解，降低计算开销同时提升数值稳定性

  - 多模态特征融合场景中，二阶协方差特征归一化可直接复用该方案提升下游分类/排序精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
全局协方差池化（GCP）可捕捉二阶特征统计提升细粒度识别效果，但SPD流形上的协方差矩阵需先归一化才能输入欧氏分类器；传统矩阵对数归一化依赖特征分解，梯度数值不稳定，长期被矩阵平方根方案替代。

### 方法关键点
1. 证明不稳定性来自谱域求对数的计算方式而非对数本身，用有限多项式逼近矩阵对数，前向/反向传播均无需特征分解，所有运算转为GEMM，消除不稳定的1/(λ_i-λ_j)项；
2. 加入均值特征预归一化将谱中心调整到1附近，规避log奇点，配套标量后补偿还原对数奇异项；
3. 最优方案为8阶切比雪夫展开，采用三项矩阵递推计算，反向传播用匹配的反向递推实现。

### 关键结果
在3个细粒度基准+ImageNet-1k上，无分解的对数归一化比谱域对数、平方根逼近方案速度更快、精度更高，同基同阶下对数目标效果优于平方根目标。
