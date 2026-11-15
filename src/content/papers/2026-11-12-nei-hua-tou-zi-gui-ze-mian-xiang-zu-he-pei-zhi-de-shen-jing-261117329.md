---
title: 'Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio
  Allocation'
title_zh: 内化投资规则：面向组合配置的神经符号强化学习方法
authors:
- Zeynep Yıldız
- Satchit Chatterji
- Ercan Atam
- Erman Acar
affiliations:
- Boğaziçi University
- Finesse Lab, University of Amsterdam
arxiv_id: '2611.17329'
url: https://arxiv.org/abs/2611.17329
pdf_url: https://arxiv.org/pdf/2611.17329
published: '2026-11-12'
collected: '2026-11-15'
category: Agent
direction: 神经符号RL · 智能体约束合规学习
tags:
- Reinforcement Learning
- Neurosymbolic AI
- Constrained RL
- Continuous Action Space
- Safe RL
one_liner: 提出适配连续动作空间的神经符号RL方法，使智能体自主学习满足约束无需推理后修正
practical_value: '- 做推荐/广告Agent的约束合规（如营销预算约束、商品合规规则）时，可参考将约束满足概率加入训练目标，避免推理时后处理带来的效果折损

  - 连续动作空间的约束学习场景（如动态出价、流量分配比例优化），可复用重参数化蒙特卡洛采样估计约束满足概率的方法

  - 原使用奖励惩罚法做约束的业务场景，可替换为该神经符号监督方法，大幅降低约束违反率的同时保留优化效果'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
深度RL可优化收益但无法保证符合业务规则约束，现有神经符号约束RL方法仅支持离散有限动作空间，无法适配投资组合分配、流量调控等连续动作场景，推理时后处理修正又会影响优化效果。
### 方法关键点
受PLPG启发的连续动作空间神经符号RL方案：1) 用重参数化蒙特卡洛采样估计智能体执行动作满足符号规则的概率；2) 将该概率项加入训练目标，无需额外推理时后处理步骤，让智能体自主学习内化规则约束。
### 关键结果数字
针对6条随市场状态变化的规则约束，无约束RL违反率为96%~98%，奖励惩罚基线违反率为33.4%，该方法将违反率降至4.8%，同时无需推理时动作修正
