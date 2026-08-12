---
title: Efficient Hypergradient Descent for Inverse Reinforcement Learning
title_zh: 面向逆强化学习的高效超梯度下降方法
authors:
- Nikita Sevriukov
- Anna Barabanova
- Uliana Gagarina
- Karina Ivanova
- Sofiia Kasaeva
- Ilya Levin
- Marina Sheshukova
affiliations:
- HSE University
arxiv_id: '2608.11052'
url: https://arxiv.org/abs/2608.11052
pdf_url: https://arxiv.org/pdf/2608.11052
published: '2026-08-11'
collected: '2026-08-12'
category: Training
direction: 逆强化学习 · 双层优化效率提升
tags:
- Inverse Reinforcement Learning
- Bilevel Optimization
- Hypergradient Descent
- Fisher Information Matrix
- Spectral Sketching
one_liner: 提出基于Fisher的结构化超梯度与流谱草图近似，降低逆强化学习双层优化计算开销
practical_value: '- 做基于IRL的用户行为模拟、推荐策略学习场景，可复用Fisher矩阵近似替代海森矩阵逆乘的trick，降低双层优化计算量

  - 需处理大规模高维参数的超梯度计算场景，可借鉴流谱草图方法，避免显式构造大矩阵，降低存储与计算开销

  - 电商推荐的奖励函数调优、排序策略反向学习场景，可参考该方法提升IRL落地的可行性与运行效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
逆强化学习（IRL）从专家演示恢复奖励函数通常建模为双层优化问题，外层更新需计算内层目标的逆海森向量乘积，计算开销极高，难以适配大规模落地场景。
### 方法关键点
1. 证明内层最优时，内层目标的海森与策略的Fisher信息矩阵成正比，推导出基于Fisher的结构化超梯度，与自然超梯度下降高度适配；
2. 采用流谱草图近似逆Fisher向量乘积，无需显式构造高维Fisher矩阵，解决扩展性瓶颈。
### 关键结果
在离散/连续控制环境上对比一阶随机双层基线，策略表现与奖励排序质量达可比水平；对比显式Fisher求解器，Fisher草图降低曲率存储复杂度，计算效率显著提升。
