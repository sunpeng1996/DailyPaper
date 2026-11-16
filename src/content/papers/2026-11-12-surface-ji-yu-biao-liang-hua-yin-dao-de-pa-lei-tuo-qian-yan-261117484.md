---
title: 'SURFACE: Preference Distribution Matching on Pareto Fronts via Scalarization
  Steering'
title_zh: SURFACE：基于标量化引导的帕累托前沿偏好分布匹配
authors:
- Liuyuan Jiang
- Prasanna Sattigeri
- Lisha Chen
affiliations:
- University of Rochester
- IBM Research
arxiv_id: '2611.17484'
url: https://arxiv.org/abs/2611.17484
pdf_url: https://arxiv.org/pdf/2611.17484
published: '2026-11-12'
collected: '2026-11-16'
category: Other
direction: 多目标优化 · 帕累托前沿分布匹配
tags:
- Multi-Objective Optimization
- Pareto Front
- Scalarization
- Distribution Matching
- SURFACE
one_liner: 提出自适应调整标量化权重的SURFACE方法，实现帕累托前沿偏好分布精准匹配
practical_value: '- 电商推荐多目标排序（兼顾点击率、转化率、客单价等）场景可复用SURFACE的权重自适应调整逻辑，避免固定标量权重导致的帕累托前沿覆盖不均问题

  - 多目标优化任务可直接复用其权重网格-帕累托区域映射估计方法，降低非线性权重-解映射带来的分布失真

  - 工程上支持并行、热启动优化的特性可直接落地，无需替换现有单目标求解器，迁移成本低'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
多目标优化中通过调整标量化权重生成帕累托解的方案存在非线性失真，权重分布无法直接对应帕累托前沿上的解分布，无法满足指定偏好的解分配需求。
### 方法关键点
1. 提出SURFACE框架，基于当前已生成的标量化解估计权重网格各区域与帕累托前沿区域的映射关系
2. 自适应调整权重分布匹配目标偏好分布，兼容现有单目标求解器，支持并行、热启动、非精确优化
### 关键结果数字
理论上证明偏好分布不匹配度线性收敛到$oldsymbol{{O}(N^{-2/(M-1)})}$的有限分辨率误差下界，其中$N$为自适应权重数量，$M$为目标数；实验相比基线在目标质量平衡、帕累托前沿覆盖度上均有显著提升。
