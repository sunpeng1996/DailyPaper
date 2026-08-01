---
title: Feature Bagging Provides Stability
title_zh: 特征Bagging的算法稳定性提升效果研究
authors:
- Yuheng Ma
- Qiang Sun
affiliations:
- East China Normal University
- University of Toronto
- MBZUAI
arxiv_id: '2607.26964'
url: https://arxiv.org/abs/2607.26964
pdf_url: https://arxiv.org/pdf/2607.26964
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 模型训练 · 特征Bagging稳定性优化
tags:
- Feature Bagging
- Algorithmic Stability
- Random Forests
- Ensemble Learning
- Generalization
one_liner: 从算法稳定性视角分析特征Bagging，提出特征不稳定性指标，给出其稳定性提升的理论保证
practical_value: '- 推荐/广告排序模型训练可引入特征Bagging策略，降低单特征波动对模型效果的影响，提升线上泛化性

  - 模型迭代评估中新增FI指标，和传统II指标互补，更全面判断模型的泛化能力与稳定性

  - 落地特征Bagging时无需设置过多轮次，少量轮次即可接近无限轮的稳定性水平，控制训练算力成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
工业界高维特征场景下（如推荐/广告排序），单特征扰动易导致模型输出波动、泛化性下降，现有稳定性分析多聚焦样本维度，缺少特征维度的系统性研究框架。
### 方法关键点
提出**Feature Instability (FI)** 指标，衡量单特征移除对模型输出的影响，与传统Instance Instability (II)互补捕捉泛化信息；分别在参数化线性模型、随机森林启发的无模型两类场景下，对特征Bagging的稳定性进行理论推导。
### 关键结果
特征Bagging相比非Bagging版本可显著提升稳定性，特征子采样比例越低，稳定性提升幅度越大；仅需少量Bagging轮次即可接近无限轮次的稳定性上限，实验验证FI可捕捉II遗漏的泛化相关信息。
