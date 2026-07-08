---
title: Advances in Neural Controlled Differential Equations
title_zh: 神经受控微分方程（NCDE）的研究进展
authors:
- Benjamin Walker
affiliations:
- Balliol College
- University of Oxford
arxiv_id: '2607.05280'
url: https://arxiv.org/abs/2607.05280
pdf_url: https://arxiv.org/pdf/2607.05280
published: '2026-07-06'
collected: '2026-07-08'
category: Training
direction: 时序建模 · 神经微分方程训练优化
tags:
- Neural CDE
- Time Series
- Training Efficiency
- Model Optimization
- Dynamical System
one_liner: 提出三类NCDE优化方案，训练速度最高提升3个数量级同时保持时序任务SOTA表现
practical_value: '- 处理用户不规则行为序列时，可尝试Linear NCDE替换RNN/Transformer，既保留连续时序建模能力又支持并行加速

  - 训练NCDE类时序模型时，可复用Log-ODE近似方案，大幅降低训练成本，适配大规模用户时序建模/行为预测任务

  - 线上低延迟时序推理场景，可采用结构化Linear NCDE方案，在效果无损前提下降低推理耗时'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前主流时序模型默认将输入处理为离散序列，无法适配真实场景中大量不规则采样/过采样的时序数据；NCDE作为表达能力最强的连续时间时序模型，前向计算开销高且天然串行，难以规模化落地。

### 方法关键点
1. 基于神经粗糙微分方程提出Log-NCDE，训练阶段用Log-ODE方法近似NCDE的解，同时提升计算速度与效果；
2. 提出Linear NCDE，用线性向量场替换传统非线性向量场，支持时间维度并行计算且不损失理论表达性；
3. 进一步提出结构化Linear NCDE，采用结构化线性向量场进一步提升效率，同时保留理论表达性与实际效果。

### 关键结果
NCDE单训练步耗时最高降低3个数量级，在多个时序基准数据集上达到SOTA表现。
