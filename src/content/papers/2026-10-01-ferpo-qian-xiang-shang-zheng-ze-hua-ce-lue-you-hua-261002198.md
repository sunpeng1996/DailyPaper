---
title: 'FERPO: Forward Entropy-Regularized Policy Optimization'
title_zh: FERPO：前向熵正则化策略优化
authors:
- Sebastian Sanokowski
- Alireza Sarmadi
- Majid Khadiv
affiliations:
- Applied and Theoretical Aspects of Robot Intelligence (ATARI) Lab
- Munich Institute of Robotics and Machine Intelligence (MIRMI)
- Technical University of Munich
arxiv_id: '2610.02198'
url: https://arxiv.org/abs/2610.02198
pdf_url: https://arxiv.org/pdf/2610.02198
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 强化学习 · 策略优化训练算法
tags:
- Reinforcement Learning
- Policy Optimization
- On-policy RL
- Continuous Control
- KL Divergence
one_liner: 提出无需对critic求动作梯度的前向熵正则化RL策略优化算法，提升样本效率与更新速度
practical_value: '- 基于RL的推荐排序/Agent决策场景可复用无需对critic求动作梯度的设计，规避critic梯度不准导致的策略更新不稳定问题

  - 多目标推荐/多模式探索场景可用forward-KL替代reverse-KL作为优化目标，鼓励覆盖更多高价值模式，提升探索效率

  - 在线RL类任务的策略更新可复用self-normalized importance sampling + KL正则的设计，控制重要性权重方差，提升训练稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有连续控制在线RL方法依赖学习到的critic的动作梯度更新策略，但critic精准预测回报不代表动作导数准确，易导致策略更新不可靠。
### 方法关键点
1. 提出FERPO这一on-policy最大熵RL算法，无需对critic求动作梯度即可完成策略提升
2. 从带熵和KL散度正则的策略提升目标中推导最优目标动作分布，采用forward-KL目标拟合actor，用rollout策略生成的动作做self-normalized importance sampling（SNIS）估计
3. KL正则限制目标分布与rollout策略的偏差，保证重要性权重稳定；forward-KL相比reverse-KL更鼓励覆盖多高价值模式，提升探索性
### 关键结果
在MuJoCo Playground、ManiSkill基准上性能具备竞争力，实现样本效率提升；计算基准测试显示actor更新速度快于REPPO算法。
