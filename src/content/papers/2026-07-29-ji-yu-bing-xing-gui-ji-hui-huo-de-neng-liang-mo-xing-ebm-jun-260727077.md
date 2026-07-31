---
title: Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering
title_zh: 基于并行轨迹回火的能量模型（EBM）均衡训练算法
authors:
- Nicolas Béreux
- Aurélien Decelle
- Cyril Furtlehner
- Beatriz Seoane
affiliations:
- Université Paris-Saclay, CNRS, INRIA, LISN
- Universidad Politécnica de Madrid
- Universidad Complutense de Madrid
arxiv_id: '2607.27077'
url: https://arxiv.org/abs/2607.27077
pdf_url: https://arxiv.org/pdf/2607.27077
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 生成模型训练 · EBM训练优化
tags:
- Energy-Based Models
- Parallel Trajectory Tempering
- MCMC
- Generative Modeling
- Maximum Likelihood Training
one_liner: 提出并行轨迹回火EBM训练算法，解决MCMC混叠差问题，低成本优于现有训练方案
practical_value: '- 可将并行轨迹回火（PTT）方法迁移到EBM类召回/用户兴趣模型的训练中，缓解小样本/冷启动场景的过拟合问题

  - 计算成本与传统Persistent Contrastive Divergence相当，可直接作为工业级EBM训练的替代方案，无需额外算力开销

  - 训练过程无额外成本输出的均衡采样结果，可用于生成高质量稀疏行为用户的兴趣表征，提升小众品类推荐效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

## 动机
Energy-Based Models (EBM)是可解释性较强的生成建模框架，但传统训练依赖的Markov Chain Monte Carlo采样混叠效果差，大幅限制模型可靠性，尤其在高多模态、数据稀缺场景表现不佳。
## 方法关键点
提出基于Parallel Trajectory Tempering (PTT)的训练算法，利用优化路径连续性保证训练全程均衡采样，结合reservoir sampling与自适应优化，计算成本与传统Persistent Contrastive Divergence相当，还可无额外成本获得热化时间估计、模型均衡样本、准确log-likelihoods。
## 关键结果
- 受限玻尔兹曼机实验中，PTT效果始终优于现有EBM训练方法
- 离散表格数据场景下，效果超过当前SOTA深度生成模型，样本质量更高，过拟合抵抗性与小数据集鲁棒性更优
