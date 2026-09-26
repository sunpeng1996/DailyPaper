---
title: Sufficiently Reduced Distributional Regression
title_zh: 充分降维分布回归（SRDR）方法
authors:
- Alexander Henzi
- Tiange Liu
- Xinwei Shen
affiliations:
- Tsinghua University, Department of Statistics and Data Science
- University of Washington
arxiv_id: '2609.29291'
url: https://arxiv.org/abs/2609.29291
pdf_url: https://arxiv.org/pdf/2609.29291
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 通用机器学习 · 充分降维方法
tags:
- Dimension Reduction
- Distributional Regression
- Generative Model
- Energy Score
- Representation Learning
one_liner: 结合条件分布估计与非线性充分降维，提出无需密度计算或对抗训练的生成式降维预测框架
practical_value: '- 特征降维环节可复用基于严格 Proper Scoring Rule 的充分性判定准则，降低高维用户/物品特征冗余的同时保证预测效果无损失

  - 联合训练降维映射与预测模型的范式可迁移到召回/粗排阶段，无需单独预训练降维模块，端到端优化减少信息损耗

  - 高维多变量输出的预测场景（如多目标排序、用户多行为预测）可采用 Energy Score 作为损失，规避密度计算或 GAN 训练的复杂度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维协变量下的多变量分布回归存在维数灾难，传统方法需计算密度或依赖对抗训练，落地复杂度高，且无法保证降维后特征的预测信息充分性。

### 方法关键点
基于严格 Proper 评分规则定义降维充分性：降维后特征做预测的期望得分与全量特征无差异，将降维转化为风险最小化问题；端到端联合训练降维映射与生成式预测模型，采用可通过采样估计的 Energy Score 作为损失，无需密度评估或对抗训练；框架可扩展到多环境数据与分类任务，理论证明估计的条件分布依能量距离收敛到真实分布，降维表示渐近充分。

### 关键结果
在CT切片定位、超导性预测、手写数字分类任务上，恢复低维充分结构效果优异，表征质量与预测性能持平或超越 SOTA 非线性充分降维方法。
