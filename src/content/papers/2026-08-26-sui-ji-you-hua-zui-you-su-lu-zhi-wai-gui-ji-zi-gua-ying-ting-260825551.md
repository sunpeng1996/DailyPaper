---
title: 'Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping
  Rules'
title_zh: 随机优化最优速率之外：轨迹自适应停止规则
authors:
- Liviu Aolaritei
- Lucas Lévy
- Francis Bach
- Michael I. Jordan
affiliations:
- UC Berkeley, USA
- Inria, École Normale Supérieure, PSL Research University, France
arxiv_id: '2608.25551'
url: https://arxiv.org/abs/2608.25551
pdf_url: https://arxiv.org/pdf/2608.25551
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 随机优化 · SGD自适应停止策略
tags:
- SGD
- Stochastic Optimization
- Confidence Sequence
- Adaptive Stopping
- Strongly Convex
one_liner: 针对强凸随机优化构建轨迹自适应上置信序列，实现统计有效的SGD精度达标即停规则
practical_value: '- 电商推荐/广告CTR/CVR排序模型训练可引入该自适应停止规则，替代人工设定的固定epoch，在保证精度达标的前提下大幅减少训练迭代次数，降低训练算力成本

  - 实时召回、增量训练等在线学习场景可复用轨迹自适应置信序列构造方法，实现训练停止时机的自动决策，避免最坏-case固定迭代次数的资源浪费

  - 小批量SGD训练场景可复用论文提出的批次内二阶矩利用方法优化经验伯恩斯坦界，进一步提升停止判定的准确性，减少冗余迭代'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统SGD采用预定义固定迭代步长的分析范式，和实际中依赖训练轨迹自适应判定停止时机的实践存在 mismatch：固定时长的统计保证在数据依赖的停止点失效，基于最坏case推导的固定迭代界过于保守，造成大量算力浪费。
### 方法关键点
针对强凸随机优化场景，构造全可观测的轨迹自适应上置信序列，可同时对最终迭代点到最优解的平方距离、加权平均次优度给出统一上界；提出新型递归置信序列技术，及适用于时变条件均值、无界可预测范围自适应过程的时间一致经验伯恩斯坦不等式；扩展到小批量SGD，利用批次内二阶矩结构优化边界紧度。
### 关键结果
最坏情况下边界达到最优1/t衰减率（仅额外引入对数因子）；数值实验显示该停止规则所需迭代次数比常规固定迭代界少几个数量级，且全程保证统计有效性。
