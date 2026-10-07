---
title: Linear Bandits under Exact Sliding-Window Constraints
title_zh: 精确滑动窗口约束下的线性老虎机算法研究
authors:
- Seyed Mohammad Hadi Hosseini
- Yasin Abbasi-Yadkori
- Sattar Vakili
affiliations:
- University College London (UCL)
arxiv_id: '2610.08745'
url: https://arxiv.org/abs/2610.08745
pdf_url: https://arxiv.org/pdf/2610.08745
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 在线学习 · 带约束线性老虎机优化
tags:
- Linear Bandit
- Sliding Window Constraint
- Online Learning
- Regret Bound
- Sequential Decision Making
one_liner: 提出满足精确滑动窗口约束的线性老虎机算法，给出次线性 regret 保证，策略更新次数大幅降低
practical_value: '- 电商推荐/广告的时序合规场景（如连续w次曝光不重复同品类、用户频控）可直接复用精确滑动窗口约束建模框架，天然满足业务规则

  - 罕见切换的策略更新逻辑可大幅降低在线推荐服务的调度开销，适合大流量低延迟的生产环境

  - 滑动窗口约束下的 regret 界推导思路可用于优化冷启动探索策略，平衡探索收益与业务约束的冲突'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有线性老虎机方法大多仅支持单步动作约束或长期全局约束，无法适配连续多步动作的时序合规需求（如广告频控、推荐品类打散、滚动资源分配等场景），缺少带精确滑动窗口约束的理论保证与低开销落地算法。
### 方法关键点
1. 离线场景下证明当可行集满足凸性+循环移位不变性时，平稳解为最优解，窗口长度w无法整除总步长T时仅存在O(w)的附加收益gap；
2. 在线场景引入转移直径τ量化可行动作的可达性，提出罕见切换OFUL算法；移除循环不变性后引入历史状态直径D，结合乐观剩余horizon规划与稀疏策略更新实现低开销优化。
### 关键结果
两种场景下的 regret 界分别为$	ilde{O}(d\sqrt{T}+τd+w)$和$	ilde{O}(d\sqrt{T}+dD+w)$；真实与合成基准测试中，算法保持100%约束可行性的同时，收益与regret表现与无约束基线相当，策略更新次数远低于对比方法。
