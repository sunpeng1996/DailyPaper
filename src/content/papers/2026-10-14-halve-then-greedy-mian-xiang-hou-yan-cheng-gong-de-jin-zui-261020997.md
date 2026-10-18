---
title: 'Halve-Then-Greedy: Adaptive Sampling for Posterior Success with Near-Optimal
  Instance Dependence'
title_zh: Halve-Then-Greedy：面向后验成功的近最优实例依赖自适应采样
authors:
- Yinan Li
- Kwang-Sung Jun
- Kapilan Balagopalan
- Tuan Nguyen
- Yao Zhao
- Abbas Zaidi
- Houssam Nassif
affiliations:
- University of Arizona
- POSTECH CSE/GSAI
- Meta Inc.
arxiv_id: '2610.20997'
url: https://arxiv.org/abs/2610.20997
pdf_url: https://arxiv.org/pdf/2610.20997
published: '2026-10-14'
collected: '2026-10-18'
category: RecSys
direction: 多臂老虎机 · 自适应实验采样
tags:
- Multi-Armed Bandit
- Adaptive Sampling
- Bayesian Posterior
- Sample Efficiency
- Experiment Design
one_liner: 提出三段式HTG自适应采样方法，固定预算下显著提升后验验证达标候选的效率
practical_value: '- 电商新选品/推荐策略AB验证场景可复用HTG逻辑，固定预算下比均匀采样、连续减半分别省线性、对数级样本，更快锁定达标候选

  - 推荐系统冷启动候选Item筛选、广告定向策略验证等无需找最优、仅需验证是否达阈值的场景，可直接适配HTG框架，兼顾采样效率和后验置信度

  - 多臂老虎机类任务可参考「初始均衡分配+连续减半筛差臂+后验贪心采优臂」的三段式架构，平衡探索利用效率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
固定预算自适应实验场景中，现有方法多聚焦最优臂识别，而大量业务场景无需找最优方案，仅需验证推荐设计的均值性能是否达标（即后验成功），现有采样方案样本浪费严重、效率偏低。
### 方法关键点
针对带高斯先验的高斯老虎机场景，提出Halve-Then-Greedy（HTG）三段式自适应采样方法：1）初始阶段对所有臂做均衡大样本分配；2）用连续减半逻辑快速淘汰明显不达标臂；3）剩余候选采用后验贪心采样。
### 关键结果
1. 证明后验失败概率的实例依赖有限预算指数界，可覆盖差臂分离度、多达标臂两类场景；
2. 单达标臂场景下，采样复杂度与渐近下界仅差对数因子，达到近最优；
3. 仿真显示比均匀采样节省线性级样本，比连续减半节省对数级样本。
