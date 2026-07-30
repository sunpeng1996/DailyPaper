---
title: 'Beyond Static Costs: Learning-Dynamics Aware Loss Functions for Long-Tailed
  Classification'
title_zh: 超越静态权重：面向长尾分类的学习动态感知损失函数
authors:
- Varad Shinde
- Nikhil Kumar Shrey
- Magesh Rajasekaran
- Md Saiful Islam Sajol
- Harshil Bhargava
- Subhajit Sidanta
- Supratik Mukhopadhyay
- Yimin Zhu
arxiv_id: '2607.25830'
url: https://arxiv.org/abs/2607.25830
pdf_url: https://arxiv.org/pdf/2607.25830
published: '2026-07-28'
collected: '2026-07-30'
category: Training
direction: 长尾分类 · 动态感知损失优化
tags:
- Long-Tailed Classification
- Loss Function
- Training Optimization
- Dynamic Weighting
- Imbalanced Learning
one_liner: 提出结合三类动态学习指标的长尾分类损失LDAL，性能优于SOTA静态重加权方法且计算开销极低
practical_value: '- 电商长尾商品召回、小众用户兴趣排序场景，可复用LDAL动态加权思路，替换传统基于品类/兴趣频次的静态重加权策略，提升尾类效果

  - 训练多分类任务（如用户意图识别、商品类目预测）时，可直接复用LDAL的三类动态指标调整类别权重，几乎无额外计算开销

  - 多分类训练出现震荡、陷入局部最优时，可借鉴LDAL的跨epoch预测偏移正则项，稳定训练过程'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有长尾分类的重加权方法依赖静态类频次调整损失权重，完全忽略模型训练过程中不同类别学习进度的动态差异，易导致尾类优化不足、训练陷入局部最优，最终模型泛化性差。

### 方法关键点
提出LDAL（Learning-Dynamics Aware Loss）损失函数，动态调整类别权重，核心包含三个维度：1）已学习特征的语义强度；2）基于预测结果香农熵度量的单类别固有学习难度；3）跟踪连续epoch间预测偏移的正则项，稳定训练避免局部最优。LDAL仅为目标函数层面优化，几乎无额外计算开销。

### 关键结果
在多个长尾分类基准数据集上效果显著超越SOTA静态重加权损失，实现精度与泛化性的最优平衡，代码已开源。
