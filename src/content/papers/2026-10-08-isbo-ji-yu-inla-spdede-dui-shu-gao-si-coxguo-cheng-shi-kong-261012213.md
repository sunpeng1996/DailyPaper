---
title: 'ISBO: Scalable Spatio-Temporal Bayesian Optimization with Log Gaussian Cox
  Process Models via the INLA-SPDE Approach'
title_zh: ISBO：基于INLA-SPDE的对数高斯Cox过程时空贝叶斯优化框架
authors:
- Kaichuang Yang
- Håvard Rue
- Jakob Zeitler
affiliations:
- KAUST
- University of Oxford
arxiv_id: '2610.12213'
url: https://arxiv.org/abs/2610.12213
pdf_url: https://arxiv.org/pdf/2610.12213
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 时空贝叶斯优化 · 黑盒函数优化
tags:
- Bayesian Optimization
- Spatio-Temporal Model
- LGCP
- INLA-SPDE
- Black-box Optimization
one_liner: 首次提出适配时空点过程的可扩展贝叶斯优化框架ISBO，实现更快更准的峰值定位
practical_value: '- 电商线下到店流量、区域营销效果这类时空维度的黑盒优化场景，可复用ISBO的LGCP+INLA-SPDE建模方案，替代标准GP提升时空数据拟合效率

  - 时序动态的推荐超参调优、AB实验分流最优参数搜索，可借鉴带mask的时变UCB采集函数，避免重复采样无效空间，减少调优轮次

  - 小样本冷启动的贝叶斯优化任务，可复用惩罚复杂度先验的正则思路，降低早期迭代的过拟合风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
标准贝叶斯优化（BO）采用的高斯过程无法适配时空场景常用的双随机Cox过程，时空黑盒优化任务（如区域流量建模、营销效果优化）普遍存在采样成本高、推理效率低的痛点。
### 方法关键点
1. 用Log-Gaussian Cox Process（LGCP）建模对数强度，结合INLA-SPDE实现快速精准的后验推理；
2. 基于网格的Matern场生成稀疏高斯马尔可夫随机场，大幅降低计算复杂度；
3. 采用带掩码的时变UCB采集函数避免重复采样无效区域，引入惩罚复杂度先验对早期迭代做正则。
### 关键结果
在合成与真实时空数据集上，相比RKHS基线实现量级级速度提升，同时保持高精度的峰值发现与强度恢复能力，所需评估采样次数远低于传统BO方案
