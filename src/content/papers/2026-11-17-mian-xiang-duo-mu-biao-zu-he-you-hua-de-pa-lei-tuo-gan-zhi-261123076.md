---
title: Pareto-Informed Smart "Predict, then Optimize" for Multi-Objective Combinatorial
  Problems
title_zh: 面向多目标组合优化的帕累托感知智能“先预测后优化”方法
authors:
- Aabhash Dhakal
- Tim Lachner
affiliations:
- University of Würzburg
arxiv_id: '2611.23076'
url: https://arxiv.org/abs/2611.23076
pdf_url: https://arxiv.org/pdf/2611.23076
published: '2026-11-17'
collected: '2026-11-18'
category: Other
direction: 多目标组合优化 · 决策聚焦学习
tags:
- Multi-Objective Optimization
- Decision-Focused Learning
- Pareto Frontier
- Combinatorial Optimization
- Predict-then-Optimize
one_liner: 将单目标SPO+扩展为帕累托感知版本，解决多目标组合优化下决策聚焦学习的标量化缺陷，效果优于现有基线
practical_value: '- 电商多目标推荐/广告排序场景（需平衡CTR、CVR、客单价等冲突目标），可替换现有标量化损失为本文帕累托感知损失，优化多目标
  tradeoff 效果

  - 广告预算分配、物流路径规划等组合优化场景，可复用该方法的后悔值最小化损失设计，替代传统MSE训练目标，降低决策次优率

  - 多目标决策Agent开发中，可借鉴「偏好采样+帕累托前沿对齐」思路，生成匹配动态业务偏好的最优决策'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
多目标组合优化广泛存在于物流、资源分配等真实场景，传统两阶段「先预测后优化」方案仅以MSE优化预测精度，易导致下游决策次优；现有多目标决策聚焦学习（DFL）依赖简单标量化，无法充分捕捉帕累托前沿的丰富 tradeoff 空间。
### 方法关键点
对单目标Smart "Predict, then Optimize"（SPO+）框架做帕累托感知扩展，损失函数基于真实帕累托前沿，结合采样的偏好向量生成对齐的目标决策，最小化与该目标的决策后悔值。
### 关键结果
在多目标最短路径、多目标背包问题上，性能显著优于传统两阶段MSE基线，也超过基于标量化的SPO+方法。
