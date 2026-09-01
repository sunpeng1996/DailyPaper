---
title: Adaptive Doubly Robust Off-Policy Evaluation for Ranking Policies under Diverse
  User Behavior
title_zh: 面向异质用户行为的排序策略自适应双稳健离线评估
authors:
- Kosuke Iguchi
- Ren Kishimoto
affiliations:
- Institute of Science Tokyo
arxiv_id: '2608.29600'
url: https://arxiv.org/abs/2608.29600
pdf_url: https://arxiv.org/pdf/2608.29600
published: '2026-08-30'
collected: '2026-09-01'
category: RecSys
direction: 排序策略 · 反事实离线评估
tags:
- OPE
- Doubly Robust
- Ranking Policy
- Offline Evaluation
- Counterfactual Estimation
one_liner: 结合自适应重要性加权与双稳健修正，提出异质行为下低误差的排序OPE方法
practical_value: '- 电商搜索/推荐排序的离线A/B测试场景，可替换原有IPS/DR类OPE estimator为ADR，尤其用户浏览行为异质性高（如不同人群浏览深度、点击依赖差异大）时，能显著降低评估误差

  - 长列表推荐/搜索的OPE可直接复用ADR的self-normalized自适应权重设计，能大幅降低排序组合爆炸带来的高方差问题，即使引入少量偏差整体MSE仍有明显收益

  - 优化ADR效果可优先提升位置级reward模型精度，实验显示理想reward模型可进一步降低30%左右MSE，无需额外依赖未观测的用户行为隐变量

  - 日志量≥2k的场景下，ADR在偏差和方差上均优于AIPS，可直接作为排序OPE的首选方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
排序是电商搜索推荐的核心模块，在线A/B测试成本高且可能损伤用户体验，OPE可基于历史日志评估新策略，但传统IPS类方法因排序组合爆炸方差极高；IIPS/RIPS等假设固定用户浏览行为易引入偏差；AIPS虽适配异质行为但未引入reward模型修正，长列表下精度仍不足。

### 方法关键点
- 结合AIPS的上下文自适应重要性加权（基于用户行为交互矩阵c，对每个位置奖励仅关联对应影响动作的边际概率计算权重）与双稳健残差修正框架，构造ADR estimator
- 理论证明当观测到真实用户行为模型时ADR无偏，且当reward模型的加权残差方差小于原奖励加权方差时，ADR方差低于AIPS
- 工程实现采用self-normalized权重限制极端值影响，reward模型用位置独立的梯度提升树拟合，通过交叉拟合避免过拟合

### 关键实验
基于合成排序OPE环境，对比IPS、IIPS、RIPS、AIPS共4个baseline，单条件下1万次模拟：数据量32k、排序长8时，ADR MSE为0.105，比AIPS的1.356降低92.2%；排序长14、数据量8k时，ADR MSE为6.645，比AIPS的10.581降低37.2%，比IPS的796.97降低99.1%；当reward模型接近理想时，ADR可进一步降低30%左右MSE。

### 核心结论
异质用户行为下的排序OPE，自适应权重+双稳健残差修正的收益远高于固定行为假设的OPE方法，长列表下收益更显著
