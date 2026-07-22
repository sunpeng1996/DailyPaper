---
title: COVAriance-Induced Fairness Gap Penalty for Subgroup-Fair Clustering
title_zh: 面向子群体公平聚类的协方差诱导公平性差距惩罚方法
authors:
- Kyungseon Lee
- Hankyo Jeong
- Kunwoong Kim
- Kwanho Lee
- Yongdai Kim
affiliations:
- Department of Statistics, Seoul National University
- KAIST AI
arxiv_id: '2607.18119'
url: https://arxiv.org/abs/2607.18119
pdf_url: https://arxiv.org/pdf/2607.18119
published: '2026-07-20'
collected: '2026-07-22'
category: Other
direction: 公平聚类 · 多敏感属性子群体优化
tags:
- Fair Clustering
- Covariance Penalty
- Subgroup Fairness
- Gradient Optimization
- Efficiency Optimization
one_liner: 提出基于协方差替代的子群体公平聚类算法COVA-FC，解决多敏感属性下聚类效率与稳定性问题
practical_value: '- 可借鉴协方差公平性gap替代思路，优化推荐场景中多敏感属性（性别/年龄/地域）子群体的流量公平分配策略，避免传统约束带来的计算爆炸

  - 连续松弛梯度优化的方法可复用在召回/粗排层的公平约束模块，替代原有整数规划类公平约束，提升线上推理效率

  - 子群体公平≠边际公平的结论可指导电商合规风控场景的公平性指标设计，避免单一维度公平性校验遗漏交叉群体歧视问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有公平聚类算法多针对单敏感属性设计，当多敏感属性联合定义的子群体数量指数级增长、部分子群体样本量极小时，直接扩展原有方案会出现计算成本过高、数值不稳定问题，且易忽略子群体公平与边际公平的不兼容性。

### 方法关键点
1. 定义聚类任务的子群体公平性差距，推导完全匹配该差距的协方差替代指标，避免直接枚举所有子群体；
2. 对替代指标做连续松弛，支持高效梯度优化，得到COVA-FC算法；
3. 扩展框架同时覆盖子群体-边际公平性差距约束，解决两类公平不互洽问题。

### 关键结果
基准数据集实验显示，COVA-FC在子群体、高阶边际公平场景下均取得与基线相当的成本-公平权衡，计算效率较基线有明显提升
