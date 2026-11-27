---
title: 'On the Impact of Extra Information in Bandit Learning: More is Not Always
  Merrier'
title_zh: 多臂老虎机学习中额外信息的影响：数据更多未必效果更好
authors:
- Ramakrishnan Krishnamurthy
affiliations:
- Courant Institute of Mathematical Sciences, New York University
arxiv_id: '2611.33479'
url: https://arxiv.org/abs/2611.33479
pdf_url: https://arxiv.org/pdf/2611.33479
published: '2026-11-24'
collected: '2026-11-27'
category: RecSys
direction: 多臂老虎机 · 探索利用策略优化
tags:
- Multi-armed Bandit
- UCB
- Thompson Sampling
- Regret Minimization
- Sequential Decision Making
one_liner: 证明随机老虎机场景额外信息未必提升UCB性能，提出保障性能不退化的通用元算法
practical_value: '- 冷启动召回/广告探索场景不要盲目给UCB类算法喂额外离线样本，可能反而拉高探索阶段累积regret

  - 线上现有UCB策略可直接叠加论文提出的元算法wrapper，无需重构核心逻辑即可避免额外信息带来的性能下降

  - 新业务探索策略选型优先考虑Thompson Sampling，对额外信息兼容性更好，无天然性能退化风险'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统监督学习中更多无偏样本可单调提升模型效果，但在多臂老虎机这类需权衡探索利用的序列决策场景（如推荐冷启动、广告动态选型）中，免费无偏的额外信息是否总能降低regret尚未被验证，工业界常用的UCB类算法直接引入额外信息可能存在性能隐患。
### 方法关键点
1. 形式化定义「额外信息下性能不退化」标准，构造反例证明UCB算法存在引入无偏额外回报样本后regret反而升高的问题；
2. 对比验证Thompson Sampling、Explore-Then-Commit两类算法可稳定从同类额外信息中获益；
3. 提出通用元算法wrapper，可适配绝大多数老虎机基础算法，理论上可证明引入额外信息后性能不会低于无额外信息的基线。
### 关键结果
仿真实验验证元算法可100%避免额外信息带来的性能退化，同时保留80%以上的额外信息潜在收益，针对UCB的改造可完全抵消额外信息引入的非预期regret升高。
