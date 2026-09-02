---
title: Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law
  Entropy Search
title_zh: 基于幂律熵搜索的最优超参数缩放律高效估计方法
authors:
- Zhiliang Chen
- Sebastian Ament
- David Eriksson
- Maximilian Balandat
- Eytan Bakshy
- Jihao Andreas Lin
affiliations:
- Meta
- National University of Singapore
- Atomic Machines
arxiv_id: '2609.01431'
url: https://arxiv.org/abs/2609.01431
pdf_url: https://arxiv.org/pdf/2609.01431
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: LLM训练 · 超参缩放律高效估计
tags:
- Hyperparameter Optimization
- Bayesian Optimization
- Scaling Law
- LLM Training
- Multi-fidelity
one_liner: 提出成本感知的PLES采集函数，仅用传统方法1/10算力即可估计LLM最优超参数缩放律
practical_value: '- 训练业务侧模型（召回/排序模型、Agent垂直LLM等）时，可复用PLES思路先做小尺度超参实验拟合缩放律，直接推断大尺度最优超参，大幅降低GPU成本

  - 多超参调优场景可复用PLES的多目标熵降加权思路，优先选择能同时降低多个超参不确定性的实验，减少调优轮次

  - HPO停止规则可借鉴PLES的目标尺度不确定度阈值法，无需消耗全部预算，达标即可终止，提升调优效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
最优超参数缩放律可直接推断生产级大尺度模型的最优配置，无需执行大尺度HPO，但传统网格搜索成本极高，过往工作仅拟合学习率、batch size的缩放律就消耗近百万H800 GPU小时；且模型架构迭代后缩放律即失效，需要高频重跑，成本压力极大。

### 方法关键点
- 基于多保真Bayesian Optimization，用GP作为损失曲面代理模型，通过Thompson采样估计不同尺度下的最优超参，再做贝叶斯线性回归拟合幂律形式的缩放律，输出系数的不确定度
- 提出PLES成本感知采集函数，每轮选择单位算力下能最大程度降低缩放律系数熵的候选实验，天然偏好低成本小尺度实验
- 支持多超参同时估计，可通过加权多个缩放律的熵降扩展采集函数，单目标优化也能顺带得到其他超参的准确缩放律
- 内置停止准则：当目标大尺度下的超参估计不确定度低于阈值时终止实验

### 关键实验
在合成基准、真实LLM训练数据拟合的代理模型、实际Llama-3预训练三个场景下，对比网格搜索、Ladder BO、Sobol采样三个基线，PLES仅用不到基线1/10的算力即可收敛到准确的缩放律，且94%以上的实验集中在成本不到目标尺度6%的小尺度上，额外计算开销可忽略。

### 核心结论
拟合超参缩放律本质是回归任务，相比在小尺度做密集调优，跨尺度分散做低成本实验的收益高得多。
