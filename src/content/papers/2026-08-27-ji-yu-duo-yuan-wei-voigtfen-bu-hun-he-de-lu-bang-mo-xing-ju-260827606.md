---
title: Robust model-based clustering via mixtures of multivariate pseudo-Voigt distributions
title_zh: 基于多元伪Voigt分布混合的鲁棒模型聚类方法
authors:
- Babak F. Dehkordi
- Jeffrey L. Andrews
- Andrew Jirasek
affiliations:
- Department of Statistics, University of British Columbia-Okanagan
- Department of Physics, University of British Columbia-Okanagan
arxiv_id: '2608.27606'
url: https://arxiv.org/abs/2608.27606
pdf_url: https://arxiv.org/pdf/2608.27606
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 鲁棒聚类 · 重尾数据异常检测
tags:
- Clustering
- Outlier Detection
- EM Algorithm
- Mixture Model
- Heavy-tailed Data
one_liner: 提出融合高斯与柯西的多元伪Voigt混合模型，提升重尾数据聚类与异常检测性能
practical_value: '- 电商用户/商品聚类、羊毛党识别场景可替换原GMM，适配交易、行为等重尾数据，无需额外做长尾截断预处理，提升聚类鲁棒性

  - 簇内高斯、柯西分量共享位置/尺度参数的设计，可直接复用在现有混合模型改造中，在保证效果的同时降低参数量

  - 采用EM算法做参数估计，现有GMM的工程训练、推理链路改造成本极低，可快速上线验证'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统高斯混合模型对重尾分布、含异常值的数据集聚类效果衰减明显，现有鲁棒聚类方案普遍存在参数量冗余、簇内一致性差的问题，无法高效适配高噪声的真实业务数据。
### 方法关键点
1 提出多元伪Voigt分布的有限混合框架，单分量为高斯与柯西分布的加权凸组合，天然适配重尾特征；
2 约束同一簇内高斯、柯西分量共享位置和尺度参数，既压缩参数量也保证簇内特征一致性；
3 基于EM算法实现参数估计，通过引入隐变量简化似然推断过程，训练效率高。
### 关键结果
在仿真与真实重尾数据集上，对比污染正态分布混合等主流鲁棒聚类基线，聚类准确率与异常检测能力均更优，对重尾特征数据集的适配性提升显著。
