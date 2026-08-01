---
title: 'Breaking the Curse with BAND: Nonparametric Distribution Estimation in High
  Dimensions'
title_zh: 用BAND突破维数灾难：高维场景下的非参数分布估计
authors:
- Shuo-Chieh Huang
- Chien-Ming Chi
- Jau-er Chen
affiliations:
- Rutgers University
- Academia Sinica
- National Taiwan University
arxiv_id: '2607.26955'
url: https://arxiv.org/abs/2607.26955
pdf_url: https://arxiv.org/pdf/2607.26955
published: '2026-07-29'
collected: '2026-08-01'
category: Other
direction: 高维统计 · 非参数分布估计
tags:
- High-Dimensional Statistics
- Nonparametric Estimation
- Bayesian Network
- Distribution Regression
- Time Series Modeling
one_liner: 基于稀疏贝叶斯网络的BAND估计器，实现高维非参数分布估计的多项式收敛速率
practical_value: '- 高维用户/商品特征分布建模场景可引入稀疏贝叶斯网络假设，缓解维数灾难对估计效果的影响

  - 高维时序数据采样、置信区间预测任务可尝试用BAND替换传统直方图/核密度估计

  - 用户画像OOD检测、特征缺失补全场景可复用BAND的稀疏感知条件概率估计思路'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维非参数分布估计长期受维数灾难困扰，传统核估计、直方图、分布随机森林等方法收敛速度随维度升高急剧下降，仅在特征维度远小于log样本量时有效，无法适配高维混合类型时序数据的建模需求。

### 方法关键点
基于稀疏贝叶斯网络框架构建BAND（贝叶斯网络分布回归）估计器，每个条件概率采用稀疏感知的条件均值方法估计，支持混合数据类型的高维时序数据处理。

### 关键结果
实现多项式级总变差收敛速率，允许特征维度随样本量多项式增长，收敛速度显著快于无稀疏假设的传统多元直方图密度估计；在数据采样、置信区域预测任务上性能与SOTA基准相当。
