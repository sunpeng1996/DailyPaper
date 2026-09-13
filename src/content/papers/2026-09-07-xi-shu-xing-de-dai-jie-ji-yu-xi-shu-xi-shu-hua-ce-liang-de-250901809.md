---
title: 'The Price of Sparsity: Sufficient Conditions for Sparse Recovery using Sparse
  and Sparsified Measurements'
title_zh: 稀疏性的代价：基于稀疏/稀疏化测量的稀疏恢复充分条件
authors:
- Youssef Chaabouni
- David Gamarnik
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2509.01809'
url: https://arxiv.org/abs/2509.01809
pdf_url: https://arxiv.org/pdf/2509.01809
published: '2026-09-07'
collected: '2026-09-13'
category: Other
direction: 稀疏信号恢复 · 理论阈值推导
tags:
- sparse_recovery
- sample_complexity
- information_theory
- measurement_sparsity
- theoretical_threshold
one_liner: 推导稀疏二进制信号稀疏恢复的信息论阈值，明确测量稀疏化的精度损失与计算增益权衡
practical_value: '- 稀疏测量仅带来对数级样本复杂度损失、可获近线性计算增益的结论，可作为推荐特征稀疏化、稀疏用户兴趣建模的精度效率权衡参考

  - 主动稀疏化所需样本量$O(p/\psi^2)$的理论界，可用于召回/排序阶段特征矩阵压缩的样本量需求预估

  - 高SNR下的恢复阈值结论，可用于高置信度用户行为信号的稀疏特征选择方案选型'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有稀疏恢复研究多基于稠密测量矩阵，对稀疏测量下的恢复边界、精度与计算代价的量化权衡缺乏明确理论结论，无法支撑稀疏化方案的选型决策。
### 方法关键点
1. 针对稀疏高斯测量矩阵场景，推导高SNR regime下最大似然恢复的最小样本量充分条件，结合已有下界得到统一信息论阈值
2. 针对主动稀疏化场景（观测来自稠密设计，估计采用独立稀疏化设计+重缩放响应），推导比例regime下的样本量理论界
### 关键结果数字
1. 稀疏测量下恢复阈值为$O(s\log(p/s)/\log(ds/p))$，存在特定区间样本复杂度损失为对数级，计算增益接近线性
2. 主动稀疏化场景下，任意小$\psi$时，支持恢复的样本量需求为$O(p/\psi^2)$即可满足任意固定误差要求
