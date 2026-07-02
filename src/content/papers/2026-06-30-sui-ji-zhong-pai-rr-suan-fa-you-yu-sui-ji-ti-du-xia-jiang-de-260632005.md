---
title: Random Reshuffling Dominates Stochastic Gradient Descent
title_zh: 随机重排（RR）算法优于随机梯度下降（SGD）的理论证明
authors:
- Zijian Liu
affiliations:
- Stern School of Business, New York University
arxiv_id: '2606.32005'
url: https://arxiv.org/abs/2606.32005
pdf_url: https://arxiv.org/pdf/2606.32005
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: 机器学习训练 · 优化算法理论
tags:
- SGD
- Random Reshuffling
- Convex Optimization
- Stochastic Optimization
- Training Optimization
one_liner: 首次证明光滑凸优化下任意合理步长、任意有限轮次后RR均优于SGD，解决长期开放问题
practical_value: '- 训练CTR/CVR等推荐排序模型时，默认优先选择每轮随机重排训练数据的Shuffling SGD，无需受原有理论的步长、epoch阈值限制，可直接获得比原生SGD更优的收敛效果

  - 分布式训练推荐模型时，每轮训练前做跨节点全局随机重排全量训练数据，比固定分片不洗牌的方式收敛性更优，可直接复用到现有训练流水线

  - 调优推荐模型训练步长时，无需受原RR理论要求步长≤1/n的限制，可根据业务数据集灵活调大步长，加快收敛速度同时保障训练效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
SGD是机器学习最核心的优化算法，工业界实际落地的Shuffling SGD中主流Random Reshuffling（RR）策略经验效果远好于原生SGD，但原有理论存在两个和实践完全矛盾的限制：一是RR收敛要求步长小于和样本量n成反比的阈值，二是epoch数小于和n成正比的阈值时RR理论收敛率劣于SGD，是存在十余年的开放理论问题。

### 方法关键点
针对光滑凸优化场景，提出全新的RR收敛性证明框架，突破原有理论的两个核心限制。

### 关键结果
首次严格证明在任意合理步长、任意有限训练轮次下，RR的收敛表现都严格优于原生SGD，完全匹配工业界长期实践观察，解决了该长期悬而未决的理论问题。
