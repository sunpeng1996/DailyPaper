---
title: Handling Missing Data in Probabilistic Regression Trees
title_zh: 概率回归树的缺失数据处理方法
authors:
- Taiane Schaedler Prass
- Alisson Silva Neimaier
- Guilherme Pumi
arxiv_id: '2608.06195'
url: https://arxiv.org/abs/2608.06195
pdf_url: https://arxiv.org/pdf/2608.06195
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 树模型训练 · 缺失值处理
tags:
- Probabilistic Regression Tree
- Missing Data
- CART
- Tree-based Model
- Nonparametric Regression
one_liner: 为概率回归树设计3种无需预插补的缺失值处理策略，保留原概率特性且性能优于CART
practical_value: '- 电商推荐/广告排序场景的树模型（如GBDT、XGBoost）可复用3种无预插补缺失值处理策略，减少高缺失率用户行为特征的特征工程工作量

  - 树模型调优优先级可向缺失值处理倾斜：实验证明其对性能的影响大于平滑分布、代理选择准则，调优ROI更高

  - 无预插补的树内置缺失值处理可保留原始数据分布特性，适合对可解释性要求高的电商风控、广告归因场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统概率回归树（PRTree）要求输入特征完整，缺失值需提前插补，易引入分布偏差且增加预处理流程；经典CART等树模型的缺失值处理会破坏PRTree要求的概率守恒等核心特性。
### 方法关键点
提出3种无需预插补的PRTree缺失值处理策略：均匀概率分配法、部分观测法、降维平滑法，所有策略均适配任意缺失模式，且保留PRTree原有的概率守恒、边缘兼容等概率特性。
### 关键结果
- 多组不同缺失率的真实数据集测试显示：缺失值处理策略对树模型性能的影响权重高于平滑分布、代理选择准则
- 高缺失率数据集上，所提方法性能普遍优于CART，同时保留树模型的可解释性与灵活性
