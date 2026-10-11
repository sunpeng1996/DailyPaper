---
title: Efficient and Generalizable Archetypal Analysis for Discrete Data
title_zh: 面向离散数据的高效可泛化原型分析算法框架
authors:
- A. Emilie J. Wedenborg
- Jesper Løve Hinrich
- Morten Mørup
arxiv_id: '2610.12035'
url: https://arxiv.org/abs/2610.12035
pdf_url: https://arxiv.org/pdf/2610.12035
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 离散数据建模 · 可解释低维表征
tags:
- Archetypal Analysis
- Discrete Data
- Model Selection
- SMO
- Interpretable Representation
one_liner: 提出适配离散数据的似然驱动原型分析框架，搭配高效优化策略与预测似然模型选择准则
practical_value: '- 电商/推荐场景中，可基于该框架对点击/购买/收藏等离散用户行为做可解释分群，支持用户多标签刻画，效果优于硬聚类方法

  - AA输出的低维可解释表征可直接作为下游召回/排序模型特征，降维同时满足广告推荐合规性要求

  - 可复用其提出的交叉验证预测似然准则做聚类数/特征维度选择，替代传统手肘法等启发式调参方法，降低调参玄学'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
经典Archetypal Analysis（AA）基于最小二乘目标，无法适配二值、计数、分类等离散数据，传统模型选择依赖重建误差启发式方法，在推荐、生物信息等离散数据场景落地受限。
### 方法关键点
1. 提出基于似然的通用AA框架，支持Bernoulli、Poisson、Multinomial三类离散观测模型；
2. 优化采用负对数似然的局部二次近似，结合SMO和主动集方法做约束更新，通过限制主动集规模、保留单纯形可行性提升扩展性；
3. 提出交叉验证预测似然准则做archetype数量选择，替代传统启发式方法。
### 关键结果
合成实验可100%恢复预设的真实模型复杂度，在三类离散真实数据集上，似然拟合效果优于传统最小二乘AA及基线方法，解的稳定性提升20%以上，计算效率比现有似然类AA方法高2~4倍。
