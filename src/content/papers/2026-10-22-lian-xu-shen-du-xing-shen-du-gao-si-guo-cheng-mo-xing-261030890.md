---
title: Continuous-depth Deep Gaussian Processes
title_zh: 连续深度型深度高斯过程模型
authors:
- Ying Li
- Sanyou Wu
- Zi Yang
- Qiaochu Xu
- Yuhao Liu
- Zhidi Lin
- Michael Minyi Zhang
- Petar Djuric
- Alexandre H. Thiery
affiliations:
- National University of Singapore
- Columbia University
- The University of Hong Kong
- Capital One
- Stony Brook University
arxiv_id: '2610.30890'
url: https://arxiv.org/abs/2610.30890
pdf_url: https://arxiv.org/pdf/2610.30890
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 贝叶斯回归 · 深度高斯过程优化
tags:
- Deep Gaussian Process
- Bayesian Regression
- Continuous Depth
- Stochastic Differential Equation
- Probabilistic Modeling
one_liner: 提出两种连续深度参数化DGP模型，解决离散深度DGP随深度增加优化困难的问题
practical_value: '- 做CTR/CVR预估的不确定性量化时，可参考连续深度参数化思路优化离散堆叠的贝叶斯模型，缓解深度增加时的训练不稳定问题

  - FlowDGP的低训练成本流演化先验设计，可迁移到轻量级概率召回/用户兴趣建模场景的模型结构设计

  - 路径敏感性分析方法可直接复用，用于诊断多阶堆叠的推荐模型的层间梯度/输出波动问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统离散深度Deep Gaussian Processes（DGPs）作为贝叶斯回归模型，随深度增加，层叠变换会不断放大单样本目标函数的敏感性，优化难度陡增，实际应用中通常只能用浅层结构，大幅损失了层次建模的原生优势。
### 方法关键点
1. 将深度定义为连续隐演化过程而非离散层堆叠，用带GP先验的深度索引漂移族的随机微分方程建模隐表示的深度演化逻辑，核心优化漂移族先验而非Neural ODE/SDE的纯神经连续参数化
2. 实现两个落地变体：CDGP（直接对状态-深度漂移施加GP先验）、FlowDGP（采用流演化先验，可在更低训练成本下捕捉更丰富的深度依赖关系）
3. 配套给出连续深度公式的路径敏感性分析方法，可用于诊断模型训练波动原因
### 关键结果
实验覆盖合成数据、公开基准、大规模回归三类任务：残差DGP效果优于普通DGP，CDGP与FlowDGP在所有测试场景下综合表现均最优。
