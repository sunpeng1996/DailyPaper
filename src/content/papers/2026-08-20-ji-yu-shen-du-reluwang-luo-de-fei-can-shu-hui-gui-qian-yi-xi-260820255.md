---
title: Transfer Learning in Nonparametric Regression with Deep ReLU Networks
title_zh: 基于深度ReLU网络的非参数回归迁移学习框架
authors:
- Junpeng Ren
- Carlos Misael Madrid Padilla
- Yanzhen Chen
- Oscar Hernan Madrid Padilla
affiliations:
- University of California, Los Angeles
- Washington University in St. Louis
- Hong Kong University of Science and Technology
arxiv_id: '2608.20255'
url: https://arxiv.org/abs/2608.20255
pdf_url: https://arxiv.org/pdf/2608.20255
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: 迁移学习 · 非参数回归训练优化
tags:
- Transfer Learning
- Nonparametric Regression
- ReLU Network
- Convergence Rate
- Multi-domain Learning
one_liner: 提出两阶段偏移学习的多组非参数回归迁移框架，推导ReLU网络实例的收敛率边界
practical_value: '- 多场景推荐任务可复用两阶段训练范式：先 pooling 全场景数据训通用底座，再单独训各场景偏移项，缓解小场景样本不足问题

  - 小样本场景可借鉴跨组数据 pooling 逻辑，在公共结构可加性假设成立的前提下，复用其他域样本做数据增强，提升收敛速度

  - 多场景回归类任务（如CTR预估、商品定价预测）可先验证公共结构+场景偏移的可加假设，成立即可直接套用框架降低训练成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多组/多域非参数回归场景下，传统单组拟合方法对小样本组精度差、收敛慢，高维场景易受维数灾难困扰，缺乏通用的迁移学习范式。

### 方法关键点
采用两阶段偏移学习流程：首先 pooling 全量组数据拟合全局公共均值函数，再为每个组独立估计加性偏移项，最终组级预测结果为公共项加偏移项的组合；框架兼容各类非参数估计器，同时提供深度ReLU网络的实例化方案。

### 关键结果
推导得到框架的L2误差上界，ReLU网络实例在层次组合模型下可突破维数灾难；满足正迁移条件时收敛速度显著优于单组训练方案，仿真及真实数据实验均验证方法有效性。
