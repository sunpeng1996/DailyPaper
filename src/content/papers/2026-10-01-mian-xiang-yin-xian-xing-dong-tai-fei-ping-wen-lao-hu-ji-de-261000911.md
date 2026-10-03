---
title: Block Optimism for Nonstationary Bandits with Latent Linear Dynamics
title_zh: 面向隐线性动态非平稳老虎机的块乐观优化算法
authors:
- Taehyun Hwang
- Hyunjun Choi
- Heesang Ann
- Min-hwan Oh
affiliations:
- Seoul National University
arxiv_id: '2610.00911'
url: https://arxiv.org/abs/2610.00911
pdf_url: https://arxiv.org/pdf/2610.00911
published: '2026-10-01'
collected: '2026-10-03'
category: RecSys
direction: 非平稳在线学习 · 老虎机算法优化
tags:
- Nonstationary Bandit
- UCB
- Online Learning
- Regret Bound
- Latent Dynamics
one_liner: 提出自适应块乐观UCB算法，将隐线性动态非平稳老虎机 regret 降至Õ(√T)
practical_value: '- 电商/广告冷启动、非平稳用户偏好场景可复用自适应块乐观UCB框架，相比传统explore-then-commit策略 regret
  更低，长期收益更优

  - 长序列用户隐状态建模可借鉴块级截断近似思路，降低无限历史记忆的存储与计算开销，适配在线推理时延要求

  - 在线实验流量分配、动态推荐策略迭代时，可参考有限记忆块代理的优化思路，平衡探索效率与长期用户价值'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有针对内生非平稳隐线性动态老虎机的explore-then-commit方案仅能实现Õ(T^(2/3)) regret，无法适配推荐/广告等用户隐偏好随推荐动作动态变化、需要长序列规划的业务场景，传统外生非平稳建模方法也无法覆盖动作影响未来环境状态的情况。
### 方法关键点
1. 提出循环近似思路：稳定动态下可截断无限记忆奖励过程，通过有限记忆块级代理近似开环基准；
2. 基于UCB构建块级乐观算法，维护截断动态参数的置信集，乐观选择最优动作块。
### 关键结果
首次为双线性奖励观测、开环动作序列基准的隐线性动态老虎机取得Õ(√T)的regret上界，相较原有Õ(T^(2/3))的保证有显著提升。
