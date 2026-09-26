---
title: 'Anchored Extra-Proximal Methods: Optimal Higher-Order Methods for Monotone
  Inclusion Problems'
title_zh: 锚定额外近端方法：面向单调包含问题的最优高阶算法
authors:
- Ruichen Jiang
- TaeHo Yoon
affiliations:
- Google Research
- Johns Hopkins University
arxiv_id: '2609.30212'
url: https://arxiv.org/abs/2609.30212
pdf_url: https://arxiv.org/pdf/2609.30212
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 凸优化 · 单调包含问题高阶求解
tags:
- Optimization
- Monotone Inclusion
- Higher-order Method
- Proximal Method
- Complexity Analysis
one_liner: 提出锚定额外近端框架，实现p阶单调包含问题的最优求解复杂度，匹配理论下界
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
单调包含问题可建模min-max优化、变分不等式等多种核心优化任务，现有p阶求解算法的复杂度上界未达理论最优，存在性能提升空间。
### 方法关键点
1. 提出Anchored Extra-Proximal (AEP)框架，融合锚定外推步与满足相对误差约束的非精确锚定近端更新；
2. 一阶场景下可兼容现有复合快速额外梯度法，p≥2时通过外推点泰勒近似替换隐式更新算子，结合二分线搜索实现高阶扩展。
### 关键结果
p≥2时，求解切线残差≤ε的p阶方法oracle调用复杂度为$	ilde{O}(rac{1}{rac{2}{	au_{3p-1}}})$，优于此前最优$	ilde{O}(rac{1}{	au_{p}})$上界；同时证明该复杂度匹配$	ilde{rac{1}{	au_{3p-1}}}$的最坏情况下界，仅差对数因子，达到最优。
