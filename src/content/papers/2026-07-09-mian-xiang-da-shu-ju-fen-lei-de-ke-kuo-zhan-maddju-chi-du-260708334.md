---
title: A scalable version of MADD for big-data classification
title_zh: 面向大数据分类的可扩展MADD距离度量实现
authors:
- Annesha Ghosh
- Adrija Saha
- Soham Sarkar
affiliations:
- Indian Statistical Institute
- UBS Business Solutions (India) Pvt. Ltd.
arxiv_id: '2607.08334'
url: https://arxiv.org/abs/2607.08334
pdf_url: https://arxiv.org/pdf/2607.08334
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 高维大数据分类 · 距离度量优化
tags:
- MADD
- Distance Metric
- Scalability
- Random Fourier Features
- High Dimensional Classification
one_liner: 通过代表性样本选择与随机傅里叶特征优化，实现低开销可扩展MADD度量，适配高维大数据分类场景
practical_value: '- 高维用户/物品特征的距离计算场景可复用MADD优化思路，解决欧氏距离高维退化问题，提升召回/粗排的特征区分度

  - 大规模训练集下的距离类算法提速可借鉴「代表性样本采样+Random Fourier Features」的组合优化框架，在保证效果的前提下降低计算开销

  - 高维小样本的冷启动分类/召回场景可直接尝试可扩展MADD替代现有距离度量，规避高维距离浓度问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
欧氏距离等常用距离度量在高维场景下存在距离浓度、邻域结构失效、hub点问题；原有MADD半度量可解决上述问题，但计算复杂度随训练样本量二次增长，无法适配高维大样本大数据场景。
### 方法关键点
1. 通过代表性样本集筛选减少MADD计算时的样本配对量，降低复杂度
2. 引入Random Fourier Features进一步优化超大样本下的计算效率，理论上保证优化后度量与原MADD性能对齐
### 关键结果
理论推导与数值实验均验证，优化后的可扩展MADD性能与原MADD基本一致，计算耗时仅为原版本的极小比例，可支持高维大样本数据集的落地应用。
