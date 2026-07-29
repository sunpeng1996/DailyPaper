---
title: Two-Timescale Hierarchical Reinforcement Learning for Resilient Operations
title_zh: 面向韧性运营的双时间尺度分层强化学习框架
authors:
- Young Hyun Cho
- Franz Stoll
- Will Wei Sun
- Guang Lin
- Stephan Biller
affiliations:
- Harvard University
- Purdue University
- Dauch Center for the Management of Manufacturing Enterprises
arxiv_id: '2607.23434'
url: https://arxiv.org/abs/2607.23434
pdf_url: https://arxiv.org/pdf/2607.23434
published: '2026-07-26'
collected: '2026-07-29'
category: Other
direction: 分层强化学习 · 多时间尺度决策优化
tags:
- Hierarchical RL
- Multi-timescale Decision
- Operational Resilience
- Reinforcement Learning
- Supply Chain Optimization
one_liner: 提出带收敛保证的双时间尺度分层RL框架，联合优化长短期决策提升冲击下运营韧性
practical_value: '- 电商备货、动态定价等分层决策场景可直接复用双时间尺度范式：长周期决策（如补货、大促资源预留）执行慢更新，短周期决策（如实时调价、流量调控）执行快更新，提升突发冲击下的业务韧性

  - 分层RL长短期策略耦合更新可参考论文的同步机制，自带收敛性保证可避免策略震荡，无需改动现有分层运营架构即可落地

  - 当业务负反馈信号清晰时，可复用论文的收敛加速方案，将策略后悔界从$O(T^{-1/2})$优化到$O(\log T/T)$，快速适配场景突变'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
全球运营场景频繁出现突发供需冲击，现有决策体系多分离长短期策略，无法协同适配动态变化，抗风险韧性不足，且分层多时间尺度RL缺乏耦合更新的收敛性理论支撑。
### 方法关键点
提出双时间尺度分层RL框架，长周期决策（如库存补货）、短周期决策（如动态定价）分别在对应时间尺度独立更新，设计耦合同步机制保障策略协同，首次证明双时间尺度耦合学习的收敛性：策略与最优解的平均后悔界为$O(T^{-1/2})$，当决策损失信号清晰时可优化至$O(\log T / T)$。
### 关键结果
二手车运营场景测试中，对比最优部分自适应基准：供需联合冲击下平均利润提升9.2%，长期冲击场景下利润提升11.8%，利润波动显著更低；仅短周期自适应无法应对供需双冲击，必须结合长周期策略协同优化。
