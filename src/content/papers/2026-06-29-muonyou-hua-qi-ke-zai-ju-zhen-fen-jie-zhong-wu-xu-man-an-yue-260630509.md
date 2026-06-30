---
title: Muon learns balanced solutions in matrix factorization without slow saddle-to-saddle
  dynamics
title_zh: Muon优化器可在矩阵分解中无需慢鞍点跃迁学习平衡解
authors:
- Mark Rhee
- Jamie Simon
- Dhruva Karkada
affiliations:
- UC Berkeley
- Imbue
arxiv_id: '2606.30509'
url: https://arxiv.org/abs/2606.30509
pdf_url: https://arxiv.org/pdf/2606.30509
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 优化器训练 · 矩阵分解动力学分析
tags:
- Muon Optimizer
- Matrix Factorization
- Gradient Descent
- Learning Rate Scheduling
- Optimization Dynamics
one_liner: 揭示Muon对比梯度下降在矩阵分解的三大动力学差异，提出两步达近完美对齐的学习率调度
practical_value: '- 推荐系统召回/排序模块的矩阵分解训练可替换为Muon优化器，规避鞍点跃迁慢问题，大幅提升收敛速度

  - 可复用文中的指数退火学习率调度方案，不受问题条件数限制，大学习率下仍能保持训练稳定

  - Embedding预训练场景可尝试Muon的正交更新特性，加快不同维度语义表征的对齐速率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
矩阵分解是推荐系统协同过滤、表征学习的核心基础方法，传统梯度下降训练存在鞍点跃迁慢、学习率受问题条件数限制导致收敛效率低的痛点，新型Muon优化器的训练动力学特性尚未得到系统性分析。
### 方法关键点
对比Muon与梯度下降在矩阵分解场景下的参数更新轨迹差异，推导二者的不同守恒量与小初始化下的权重对齐速率，基于Muon的正交更新结构特性设计专属学习率调度策略。
### 关键结果
1. Muon可避免小初始化下的慢鞍点到鞍点动力学，所有目标矩阵的top模式同速率学习，小模式优先收敛；
2. 学习率可超过局部损失锐度阈值仍保持稳定，无需受限于问题条件数，配合指数退火可实现快速收敛；
3. 专属学习率调度仅需2步优化即可实现近完美的权重对齐。
