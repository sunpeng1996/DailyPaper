---
title: The Greedy Advantage in Finite-Horizon Bandits
title_zh: 有限时域多臂老虎机的贪心策略优势
authors:
- Kai Zhou
- Michael Lingzhi Li
- Kai Wang
affiliations:
- Tsinghua University
- Harvard Business School
arxiv_id: '2607.29375'
url: https://arxiv.org/abs/2607.29375
pdf_url: https://arxiv.org/pdf/2607.29375
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 多臂老虎机 · 有限时域决策优化
tags:
- multi-armed-bandit
- finite-horizon
- regularized-greedy
- regret-bound
- sequential-experimentation
one_liner: 提出有限时域伯努利多臂老虎机的正则化贪心算法，给出首个有限时域regret边界，效果匹配或超现有SOTA
practical_value: '- 电商大促、短期活动等固定时长流量分配/AB测试场景，可直接替换原有UCB/Thompson采样为正则化贪心算法，降低短期决策regret

  - 参考论文给出的正则化参数校准规则，根据业务的时域长度快速调参，无需大量离线预实验

  - 冷启动Item探索场景（如新品上架7天测试期），可直接复用有限时域regret分解逻辑平衡探索成本与收敛速度'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有多臂老虎机算法多基于渐进 regret 保证，而电商大促、短期活动、新药试验等大量实际场景均为固定有限时域，原有算法在短周期下决策 regret 偏高，无法适配业务需求。
### 方法关键点
针对有限时域伯努利多臂老虎机场景提出一类正则化贪心算法，首次推导正则化贪心算法的有限时域 regret 边界，证明 regret 可分解为瞬时探索成本和次优收敛项，后者随正则化强度呈指数级衰减，同时给出可落地的正则化参数校准规则。
### 关键结果
大量数值实验验证，经过校准的正则化贪心策略表现始终匹配或优于现有SOTA算法，作为极限情况的经典贪心策略也获得了更紧的 regret 保证。
