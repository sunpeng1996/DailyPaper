---
title: A Latent Semiparametric Mixture Model for Robust Heterogeneity Learning in
  High Dimensions
title_zh: 面向高维鲁棒异质性学习的潜在半参数混合模型
authors:
- Lyuou Zhang
- Boxiang Wang
- Lulu Wang
- Wen Zhou
- Hui Zou
affiliations:
- School of Statistics and Data Science, Shanghai University of Finance and Economics
- Department of Statistics and Actuarial Science, University of Iowa
- Gilead Sciences
- Department of Biostatistics, New York University
- Department of Applied Mathematics and Statistics, Johns Hopkins University
arxiv_id: '2611.15827'
url: https://arxiv.org/abs/2611.15827
pdf_url: https://arxiv.org/pdf/2611.15827
published: '2026-11-11'
collected: '2026-11-14'
category: Other
direction: 高维数据无监督聚类 · 半参数模型
tags:
- Clustering
- High-dimensional Data
- Semi-parametric Model
- Unsupervised Learning
- Heterogeneity Learning
one_liner: 提出高维半参数混合聚类方法CESME，突破传统模型聚类的参数分布限制，性能优于现有方案
practical_value: '- 可复用CESME的半参数混合框架，对用户行为、商品属性等高维非高斯分布数据做无监督聚类，避免传统高斯混合模型的分布假设偏差

  - 高维稀疏聚类的优化思路可迁移到用户分群、冷启动用户画像建模场景，提升异质性数据下的分群准确率

  - 潜在空间坐标单调变换的trick可用于推荐系统特征预处理，降低非标准化特征对排序/召回模型的负面影响'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维数据异质性学习是数据驱动领域的核心基础任务，传统基于参数分布的模型聚类方法理论保证清晰、计算简单，但受固定分布假设限制实际泛化性差，现有高维聚类算法多依赖稀疏约束，灵活性不足。
### 方法关键点
提出新型潜在半参数混合模型，观测数据经隐空间逐坐标单调变换后服从高斯混合分布；基于隐空间稀疏最优聚类规则，定制高维聚类方法CESME，无需指定具体变换形式，鲁棒性远优于传统模型聚类方案。
### 关键结果
理论上CESME的聚类误差收敛速度与已知真实变换时的最优误差收敛速度一致；仿真及真实数据集测试中，性能全面优于现有各类高维聚类方法，包括单细胞RNA测序专用聚类算法。
