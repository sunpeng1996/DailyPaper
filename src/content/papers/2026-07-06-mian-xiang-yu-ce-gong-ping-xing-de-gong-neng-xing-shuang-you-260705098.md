---
title: Functional Bilevel Optimization for Predictive Fairness
title_zh: 面向预测公平性的功能性双层优化方法
authors:
- Ieva Petrulionyte
- Julien Mairal
- Michael Arbel
affiliations:
- Univ. Grenoble Alpes
- Inria
- CNRS
- Grenoble INP
- LJK
arxiv_id: '2607.05098'
url: https://arxiv.org/abs/2607.05098
pdf_url: https://arxiv.org/pdf/2607.05098
published: '2026-07-06'
collected: '2026-07-09'
category: Other
direction: 机器学习公平性 · 双层优化
tags:
- Fairness
- Bilevel Optimization
- Hypergradient
- Regression
- Predictive Modeling
one_liner: 针对连续高维敏感属性公平性问题，提出两种双层优化算法，高效平衡预测公平性与准确率
practical_value: '- 电商推荐/广告场景中连续高维敏感属性（收入分、用户画像向量）的公平性评估，可直接复用DPVar指标替代传统离散分群方案，更贴合业务实际

  - 排序/CTR预估的公平性调优可借鉴本文双层优化框架，直接优化公平-精度权衡，规避对抗训练不稳定的问题

  - 平方损失类预估任务做公平性约束时，可复用论文推导的闭式伴随超梯度计算方法，降低调优的计算开销'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有公平性方法多针对离散敏感属性设计，对连续高维敏感属性（如收入分、人口统计向量）的统计独立性约束过严，间接依赖惩罚或对抗方案无法直接优化公平性与准确率的权衡。

### 方法关键点
1. 定义DPVar指标（给定敏感属性的条件均值预测方差）实现均值人口平价，将公平性优化问题转化为功能性双层优化问题；
2. 针对平方损失场景提出FBO算法，通过推导的闭式伴随得到精确超梯度，计算效率更高；
3. 提出ITD算法，通过展开内步求导，支持非平方损失的通用场景。

### 关键结果数字
在合成数据及60个表格回归数据集构建的半合成基准上，两种方法的公平性-准确率综合regret最低或接近最低，效果全面优于HSIC、对抗方法、线性依赖、广义DP等强基线。
