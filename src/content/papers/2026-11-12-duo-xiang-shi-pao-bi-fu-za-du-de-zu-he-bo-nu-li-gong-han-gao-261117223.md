---
title: Combinatorial Bernoulli Factories with Polynomially Many Coins
title_zh: 多项式抛币复杂度的组合伯努利工厂高效实现
authors:
- Renato Paes Leme
- Rad Niazadeh
affiliations:
- Google Research
- Chicago Booth
arxiv_id: '2611.17223'
url: https://arxiv.org/abs/2611.17223
pdf_url: https://arxiv.org/pdf/2611.17223
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 组合优化 · 精确随机采样算法
tags:
- Exact Sampling
- Combinatorial Optimization
- Bernoulli Factory
- Polytope Rounding
- Randomized Algorithm
one_liner: 提出组合伯努利工厂高效算法，抛币次数与运行时间达维度和1/δ*的多项式级
practical_value: '- 电商广告拍卖机制设计中，可复用其仅用未知偏置硬币输出精确期望分布的方法，保障激励相容性

  - 推荐系统召回/排序链路的概率采样场景，可借鉴其无偏随机顶点采样思路，避免近似采样的偏差累积

  - 业务涉及蒙特卡洛精确模拟的链路，可参考其多项式复杂度方案替代旧指数级方案，提升运行效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统组合伯努利工厂采样复杂度极高，完美匹配场景下STOC2021旧方案期望抛币次数达$n^{2n-1}$的指数级；近似采样存在固有偏差，无法满足机制设计、蒙特卡洛模拟等场景对采样精确性的严格要求。
### 方法关键点
针对所有可构造伯努利工厂的立方体仿射切片多胞体，设计统一采样算法：无需预先输入$\delta_*$（$\delta_*=\min_i\{x_i,1-x_i\}$），仅通过未知偏置硬币的抛币结果，输出期望严格等于输入偏置向量$x$的多胞体随机顶点。
### 关键结果
- 算法期望抛币次数与运行时间在维度和$1/\delta_*$上为多项式级
- 完美匹配场景下仅需$O(n^8\delta_*^{-2}\log(n/\delta_*))$次抛币，较旧方案指数级降低复杂度
- 支持多胞体内部点的精确rounding，仅要求$x$远离多胞体边界
