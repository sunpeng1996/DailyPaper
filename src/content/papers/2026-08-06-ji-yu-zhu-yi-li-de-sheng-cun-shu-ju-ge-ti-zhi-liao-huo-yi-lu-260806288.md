---
title: 'Surv-IPTB: An Attention-Based Model for Estimating Individual Probability
  of Treatment Benefit with Survival Data'
title_zh: 基于注意力的生存数据个体治疗获益概率估计模型Surv-IPTB
authors:
- Lev V. Utkin
- Stanislav K. Kogan
- Andrei V. Konstantinov
affiliations:
- Higher School of Artificial Intelligence Technologies
- Peter the Great St.Petersburg Polytechnic University
arxiv_id: '2608.06288'
url: https://arxiv.org/abs/2608.06288
pdf_url: https://arxiv.org/pdf/2608.06288
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 生存分析 · 因果治疗效应估计
tags:
- survival-analysis
- treatment-effect
- attention-mechanism
- censored-data
- classification
one_liner: 提出基于注意力的Surv-IPTB框架，将IPTB估计转为分类问题，适配右删失生存数据
practical_value: '- 右删失数据的区间概率建模思路可迁移到电商用户LTV预估、广告转化延迟等存在未观测样本的场景，降低不确定样本的噪声干扰

  - 跨组pairwise比较+注意力聚合的框架可复用在个性化uplift建模，实现不同运营/投放策略对用户增益的精准预估

  - 把因果增益估计重构为分类任务的范式可大幅降低uplift模型的工程落地门槛，减少建模复杂度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
生存分析场景中传统个体治疗获益概率（IPTB）估计方法在非线性特征空间、高删失率下性能退化严重，且缺乏对右删失观测的统一 principled 处理方案。
### 方法关键点
1. 将IPTB估计重构为二分类任务，通过治疗组和对照组的样本pairwise比较构造训练样本；
2. 采用不精确概率表示处理右删失观测，将不确定治疗效应建模为区间值概率；
3. 引入带可学习query-key变换的注意力机制，数据驱动地聚合pairwise比较结果，同时学习删失样本的软分类概率。
### 关键结果
在螺旋、钟形、圆形等非线性特征空间的合成数据集上，不同删失率和治疗效应强度下性能稳定，较配备随机生存森林、Cox比例风险、Beran估计器的T-learner、S-learner基线性能平均提升15%以上，强非线性高删失场景下提升超30%。
