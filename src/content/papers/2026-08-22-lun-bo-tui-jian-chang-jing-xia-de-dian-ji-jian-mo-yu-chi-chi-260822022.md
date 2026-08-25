---
title: From Click Modeling to Offline and Off-Policy Evaluation in Carousel Recommendation
title_zh: 轮播推荐场景下的点击建模与离线、离策略评估
authors:
- Jingwei Kang
affiliations:
- University of Amsterdam
arxiv_id: '2608.22022'
url: https://arxiv.org/abs/2608.22022
pdf_url: https://arxiv.org/pdf/2608.22022
published: '2026-08-22'
collected: '2026-08-25'
category: RecSys
direction: 推荐系统评估 · 轮播界面点击建模
tags:
- Carousel Recommendation
- Click Model
- Offline Evaluation
- Off-Policy Evaluation
- User Behavior Analysis
one_liner: 基于眼动实验推翻传统点击假设，构建轮播场景专属的点击建模体系与离线、离策略评估方法
practical_value: '- 电商首页多轮播（猜你喜欢/品类专区等）场景可直接复用论文提出的L型曝光模式修正位置偏差，替换原有单列表的位置权重

  - 轮播场景的点击建模可放弃传统「曝光→点击」两阶段假设，改用基于考虑集的离散选择模型，更贴合用户实际交互行为

  - 轮播推荐的离线评估可替换原有N2DCG为论文改进版，解决原有指标不符合真实用户行为、归一化错误的问题

  - 做轮播场景的Off-Policy Evaluation时，可优先尝试将2D布局降维为单有效排序列的方案，复用现有成熟的Slate OPE工具'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前流媒体、电商首页广泛采用多轮播交互界面，传统单列表场景下的点击建模、离线评估、离策略评估（OPE）方法全部基于单维度排序假设，无法适配轮播2D布局下用户交互受行位置、列位置、视口限制、上下文共同影响的特点，导致点击偏差消除不准确、策略评估结果与线上真实效果偏差大，严重阻碍轮播推荐的迭代优化。

### 方法关键点
- 发布首个轮播场景眼动数据集RecGaze，覆盖87名用户的3477次有效交互，包含眼动轨迹、点击、光标移动、用户解释等多维度信号
- 通过眼动实验推翻4个传统点击行为假设：全局F型曝光模式不成立、点击条件下的级联浏览模式不成立（实际为L型浏览）、曝光后点击与位置无关的检查假设不成立、用户优先浏览轮播标题的假设不成立
- 提出基于可观测变量而非隐式行为假设的点击模型设计框架，覆盖全局依赖、序列性、因子分解3个核心设计维度，可统一单列表、网格、轮播场景的点击模型设计
- 改进原有N2DCG指标适配轮播布局，提出基于考虑集的离散选择点击模型，规划2种轮播OPE适配路径：2D布局降维为单有效排序列、分层子Slate建模

### 关键结果
在RecGaze数据集上验证，改进后的N2DCG相比原版对真实用户行为的拟合度提升更显著，传统4个点击假设的适配度均低于30%，曝光后同列不同行的点击概率差异最高达4倍。

### 核心结论
所有轮播场景的建模与评估工作必须基于2D布局下的真实行为观测，不能直接复用单列表的经典假设与方案。
