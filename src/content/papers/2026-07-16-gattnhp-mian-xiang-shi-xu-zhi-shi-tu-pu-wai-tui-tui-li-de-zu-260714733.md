---
title: 'GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning
  in Temporal Knowledge Graphs'
title_zh: GAttNHP：面向时序知识图谱外推推理的分组注意力神经霍克斯过程
authors:
- Xiangni Tian
- Kaixian Yu
- Runpeng Dai
- Niansheng Tang
- Hongtu Zhu
affiliations:
- Yunnan University
- Insilicom
- University of North Carolina (UNC)
arxiv_id: '2607.14733'
url: https://arxiv.org/abs/2607.14733
pdf_url: https://arxiv.org/pdf/2607.14733
published: '2026-07-16'
collected: '2026-07-18'
category: Reasoning
direction: 时序知识图谱 · 外推推理
tags:
- Temporal Knowledge Graph
- Hawkes Process
- Attention Mechanism
- Quantile Regression
- Temporal Reasoning
one_liner: 提出融合分组注意力、软聚类与分位数回归的TKG外推框架，大幅提升长尾场景事件与时间预测性能
practical_value: '- 处理用户行为/商品上架等时序序列时，可复用语义软分组模块，无需全量 pairwise 计算即可跨序列共享模式，降低长时序建模复杂度

  - 时序预测场景（如用户复购时间、热点事件发生时间）遇到重尾稀疏分布时，可替换均值预测为 Non-Crossing Quantile 回归头，提升预测稳定性

  - 长时序依赖建模可借鉴注意力+神经霍克斯过程的融合思路，捕捉历史事件的长期激发/抑制效应，优化序列召回/排序的时序特征提取'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
时序知识图谱（TKG）未来事件预测存在三大痛点：长程时序依赖难编码、不同事件链的相互激发/抑制效应无法被快照模型表达、事件间隔重尾稀疏导致确定性时间预测不可靠。
### 方法关键点
1. 自注意力编码器将主-关系链建模为连续时间点过程，捕捉远距离历史的持续激发效应；
2. 语义软分组模块将全局可学习的霍克斯先验转换为交叉注意力掩码，通过隐式分组共享激发模式，避免全量 pairwise 计算；
3. 非交叉分位数（NCQ）回归头替代均值时间预测，输出校准的单调有序分位数估计，在重尾间隔分布下保持稳定。
### 关键结果
在6个TKG基准数据集上，实体预测和时间预测均优于SOTA基线，在现有模型表现最差的长尾事件链上增益最显著。
