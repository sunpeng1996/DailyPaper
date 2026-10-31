---
title: Satisficing Regret Minimization in Bandits with Knapsacks
title_zh: 带背包多臂老虎机的满意后悔最小化研究
authors:
- Qing Feng
- Tianyi Ma
- Ruihao Zhu
affiliations:
- Cornell University School of Operations Research and Information Engineering
- Cornell University SC Johnson College of Business
arxiv_id: '2610.39321'
url: https://arxiv.org/abs/2610.39321
pdf_url: https://arxiv.org/pdf/2610.39321
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 在线学习 · 带背包多臂老虎机优化
tags:
- Bandits-with-Knapsacks
- Online-Learning
- Regret-Minimization
- Dynamic-Pricing
- Sequential-Decision-Making
one_liner: 提出带背包多臂老虎机通用框架SELECTwK，存在满意策略时可达常数级满意后悔
practical_value: '- 电商有限库存动态定价场景可直接复用SELECTwK框架，在满足库存约束的前提下最小化低于收益阈值的累计损失，比传统BwK算法更贴合业务保底收益要求

  - 预算约束下的广告投放/流量分发场景，可将预设ROI/消耗阈值作为满意阈值，用SELECTwK替换现有bandit策略，避免早期资源耗尽、收益不达标的问题

  - 有资源约束的在线决策场景（如推荐位预算控量），可复用论文的LP对偶regret分析方法做理论上界推导，快速验证策略可行性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
带背包多臂老虎机（BwK）是资源约束下在线决策的通用框架，传统标准regret指标无法满足业务对保底收益的要求，且存在两个核心瓶颈：即使标准regret很小，低于收益阈值的累计缺口仍可能达到线性量级；期望可行的策略可能因随机消耗导致资源提前耗尽。

### 方法关键点
提出通用算法模板SELECTwK，基于具备次线性标准regret上界的BwK oracle，搜索并验证满足「平均收益高于预设阈值、周期内资源消耗期望可行」的候选满意策略，采用LP对偶理论完成regret上界分析。

### 关键结果
存在满意策略时，SELECTwK可达到常数级期望满意regret；引入单步正向收益缺口约束时，可获得更紧的常数界+时间维度次线性界；若阈值不可达，仍保留原oracle的次线性标准regret上界；有限库存动态定价实验验证了算法的实际性能。
