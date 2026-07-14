---
title: Deep Gaussian Processes on Directed Acyclic Graphs
title_zh: 有向无环图上的深度高斯过程
authors:
- Federico L. Perlino
- Oliver Hamelijnck
- Adam M. Johansen
- Theodoros Damoulas
affiliations:
- University of Warwick
- Unilink Software Ltd
arxiv_id: '2607.09645'
url: https://arxiv.org/abs/2607.09645
pdf_url: https://arxiv.org/pdf/2607.09645
published: '2026-07-10'
collected: '2026-07-14'
category: Other
direction: 概率图建模 · 深度高斯过程推断
tags:
- DAG
- Gaussian Process
- Variational Inference
- Causal Modelling
- Uncertainty Estimation
one_liner: 提出DAG上的深度高斯过程框架，配套理论分析与变分推断方法，多任务达SOTA且具备可解释性
practical_value: '- 若业务涉及因果用户行为建模（如多触点归因、转化路径分析），可参考DAG上的函数先验建模思路，引入不确定性估计能力

  - 多保真度仿真优化场景（如广告多渠道投放效果仿真），可复用其结构化变分近似的图依赖保留方法

  - 核心为概率建模理论贡献，纯排序召回类推荐业务直接迁移价值有限'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现实中大量过程可表示为有向无环图（DAG）上的函数组合，广泛覆盖因果建模、工程多保真仿真、生物调控网络等场景，但普遍存在观测不全、带噪声、采样异构的问题，给模型重建、不确定性传播、推断带来重大挑战。
### 方法关键点
1. 对DAG上的节点函数引入先验，提出DAG上的深度高斯过程框架；
2. 理论分析先验坍塌行为，推导得到输入区分度保留深度的几乎确定渐近下界，验证了适用的宽核类别，证明了输入连接的作用结论；
3. 设计结构化变分近似方法，可保留图依赖关系、组合不确定性，同时捕捉对撞机的解释消除行为。
### 关键结果
在潜对撞机DAG建模、蛋白质信号网络、多保真重离子碰撞仿真3类任务上达到SOTA性能，可还原低保真贡献，同时提供仿真层级的可解释性。
