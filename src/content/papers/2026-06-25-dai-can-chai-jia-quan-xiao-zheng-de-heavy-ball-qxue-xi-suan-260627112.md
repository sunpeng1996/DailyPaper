---
title: Heavy-Ball Q-Learning with Residual Weighting Correction
title_zh: 带残差加权校正的Heavy-Ball Q学习算法
authors:
- Donghwan Lee
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
arxiv_id: '2606.27112'
url: https://arxiv.org/abs/2606.27112
pdf_url: https://arxiv.org/pdf/2606.27112
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 强化学习 Q学习收敛加速优化
tags:
- Q-Learning
- Reinforcement Learning
- Heavy-Ball Momentum
- Convergence Analysis
- Switched Linear System
one_liner: 提出带残差加权校正的动量Q学习，证明其收敛性且理论收敛速度优于标准Q学习，可扩展至线性函数近似场景
practical_value: '- 电商/广告场景多步决策Agent训练时，可引入本文残差校正Heavy-Ball Q学习结构，提升Q值迭代收敛速度，降低训练算力开销

  - 基于线性函数近似的在线RL排序策略训练，可直接复用本文扩展版校正Q学习框架，保证收敛性的同时加快策略迭代效率

  - RL算法收敛性分析可参考Switched Linear System + Joint Spectral Radius框架，降低动态策略切换场景下的收敛证明难度'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
标准Q-learning当折扣因子接近1时，Bellman最优算子收缩性弱，收敛速度慢；现有动量类Q-learning改进普遍缺乏动态策略切换场景下的收敛加速理论保证。
### 方法关键点
1. 对基础Heavy-Ball Q-learning递归公式增加残差加权校正，使得关联均值映射共享公共特征向量，从结构上保障收敛性
2. 采用Switched Linear System（SLS）表示与Joint Spectral Radius（JSR）作为分析工具，推导得到算法收敛速度优于标准Q-learning的充分条件
3. 将校正方法扩展至带线性函数近似的Q-learning场景，同步给出收敛性与加速性理论证明
### 关键结果
理论证明在满足推导的充分条件时，带残差校正的Heavy-Ball Q-learning收敛速度显著优于标准Q-learning，线性函数近似版本也具备一致的收敛加速特性
