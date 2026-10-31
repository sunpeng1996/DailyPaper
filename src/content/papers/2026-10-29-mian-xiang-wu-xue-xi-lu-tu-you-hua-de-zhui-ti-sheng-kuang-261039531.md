---
title: Conic-Lifting for Learning-rate-free Convex Optimization
title_zh: 面向无学习率凸优化的锥提升框架
authors:
- Julien Grand-Clément
- Joon Kwon
- Francesco Orabona
affiliations:
- HEC Paris
- INRAE & Université Paris–Saclay
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2610.39531'
url: https://arxiv.org/abs/2610.39531
pdf_url: https://arxiv.org/pdf/2610.39531
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 无学习率凸优化 · 锥提升统一框架
tags:
- Online Convex Optimization
- Conic Lifting
- Parameter-free Optimization
- FTRL
- OMD
one_liner: 提出统一无学习率在线凸优化算法族，通过锥提升实现多类无参优化方法的分析与扩展
practical_value: '- 推荐/广告模型训练场景可尝试该框架下的无学习率优化器，省去学习率网格搜索调参成本，尤其适配小样本冷启动训练任务

  - 在线推荐的实时FTRL更新模块可集成该框架无梯度界要求的无参算法，降低在线流量梯度波动带来的更新不稳定问题

  - 多Agent策略优化场景可借鉴锥提升的正交约束思路，简化无参策略更新的regret分析与实现复杂度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
在线/随机优化算法的学习率超参调参成本极高，现有AdaGrad、Conic Blackwell、无参算法等不同流派的分析框架割裂，难以统一扩展到无界域场景。

### 方法关键点
提出锥提升框架，通过新增一维标量坐标将原凸域映射到锥空间，使提升后的子梯度与提升后的决策正交，消除regret分析中的比较器缩放约束；在锥空间上分别应用FTRL和OMD，统一推导得到有界希尔伯特空间的CBA/CBA+算法，并扩展到带强凸平方范数的有限维赋范空间。

### 关键结果
- 对任意非空闭凸域，已知梯度界即可获得无参regret保证
- 无约束希尔伯特空间下该框架可完全复现KT投币赌博算法
- 提出无需梯度界的无约束域无参优化算法
