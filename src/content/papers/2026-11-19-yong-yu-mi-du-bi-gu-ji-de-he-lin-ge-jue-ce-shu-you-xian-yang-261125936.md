---
title: 'Hellinger Decision Trees for Density Ratio Estimation: Finite-Sample Guarantees'
title_zh: 用于密度比估计的赫林格决策树：有限样本理论保障
authors:
- Ren-Rui Liu
- Zheng-Chu Guo
affiliations:
- School of Mathematical Sciences, Zhejiang University
arxiv_id: '2611.25936'
url: https://arxiv.org/abs/2611.25936
pdf_url: https://arxiv.org/pdf/2611.25936
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 密度比估计 · 统计学习理论
tags:
- Density Ratio Estimation
- Decision Tree
- Newton Boosting
- Finite Sample Analysis
- Hellinger Risk
one_liner: 提出基于Newton boosting训练的树集成对数密度比直接估计算法，配套有限样本收敛理论保障
practical_value: '- 可借鉴本文的密度比估计方法做推荐/广告系统的分布漂移校正，降低线上线下效果gap

  - 密度比估计可直接用于生成式推荐模型的效果评估，替代部分昂贵的人工标注评估环节

  - 基于Newton boosting的树集成训练方法可迁移到转化率预估等任务的小样本场景，提升收敛速度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
密度比是双样本对比、分布漂移适配、生成模型评估的核心组件，传统分两次估计密度再求比的方案复杂度高、误差累积大。

### 方法关键点
提出直接估计对数密度比的方案，在轴对齐决策树加法集成上最小化平衡Hellinger风险，采用Newton boosting训练；利用Hellinger风险的指数结构做优化分析，证明经验风险的二阶泰勒近似下降量可控制实际风险下降，无需依赖理想化的经验风险最小化假设即可保障优化效果。

### 关键结果
推导得到明确收敛速率，在满足尾分布、Hölder平滑及每轮迭代进度假设条件下，收敛速率（含对数因子）达到函数估计的经典极小最优$\mathscr{L}^2$速率；合成数据验证收敛特性符合理论预期，公开数据集实验证明估计器实际效果优异。
