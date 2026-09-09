---
title: Robust conditional dimension reduction for dissimilarity data
title_zh: 面向异质性相似度数据的鲁棒条件降维方法
authors:
- Xiao Ling
- Anh Bui
arxiv_id: '2609.06284'
url: https://arxiv.org/abs/2609.06284
pdf_url: https://arxiv.org/pdf/2609.06284
published: '2026-09-05'
collected: '2026-09-09'
category: Other
direction: 异质性数据 · 鲁棒降维算法优化
tags:
- Dimension Reduction
- Multidimensional Scaling
- M-estimation
- Outlier Robustness
- Optimization
one_liner: 鲁棒条件多维缩放rcMDS通过Fair M估计替代平方损失提升降维对异常值鲁棒性
practical_value: '- 电商用户/物品Embedding、行为相似度矩阵降维场景，可借鉴Fair M估计替代平方损失，降低爬虫、恶意点击等离群行为对降维结果的干扰

  - 商品搭配、用户社交关系等相似度类数据降维，可复用带重加权的SMACOF优化算法，兼顾计算效率与收敛稳定性

  - 存在多渠道用户分布偏差等已知协变量的场景，可引入条件降维框架对齐不同来源的低维表征'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
条件多维缩放（cMDS）是直接处理带协变量的相似度数据的常用降维方案，但其采用的平方应力损失对异常值高度敏感，离群样本会主导优化目标，扭曲最终学习到的低维表征结构，无法适配带噪声的真实业务数据。
### 方法关键点
1. 鲁棒条件多维缩放rcMDS用Fair M估计目标替代原平方应力准则，动态削弱异常值对损失的贡献；
2. 配套设计带重加权机制的条件SMACOF优化算法，迭代更新计算复杂度可控，目标值单调递减且可收敛到有限极限。
### 关键结果
合成数据与真实数据实验验证，rcMDS在存在异常值污染的相似度数据上，降维表征的信息保留度显著优于原生cMDS，计算开销与收敛速度与原有算法基本持平。
