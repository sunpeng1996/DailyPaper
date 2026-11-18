---
title: Regularized Score Centering
title_zh: 正则化分数对齐（RSC）：稳定离策略强化学习的智能体训练方法
authors:
- Hao Bai
- Chenlu Ye
- Xuanchang Zhang
- Aviral Kumar
- Tong Zhang
affiliations:
- UIUC
- CMU
arxiv_id: '2611.21791'
url: https://arxiv.org/abs/2611.21791
pdf_url: https://arxiv.org/pdf/2611.21791
published: '2026-11-15'
collected: '2026-11-18'
category: Agent
direction: 智能体训练 · 离策略强化学习优化
tags:
- Reinforcement-Learning
- Off-Policy-Learning
- Score-Centering
- KL-Regularization
- Agent-Training
one_liner: 在Score Centering基础上引入反向KL正则，解决离策略漂移问题，实现多类智能体任务性能最优
practical_value: '- 电商导购Agent、搜索推荐RL调优场景：使用旧策略生成的离策略用户行为日志训练时，可在现有对齐损失上加token级反向KL正则，限制当前策略与行为策略的漂移，缓解训练不稳定问题

  - 分布式异步RL训练场景：可搭配截断重要性采样（TIS）+ RSC，既降低梯度方差，又避免策略漂移导致的reward高估，相同采样量下提升样本效率

  - 原有Score Centering落地场景：可将top-k估计中心的方式替换为蒙特卡洛采样行为策略的辅助token计算条件均值，无偏估计直接提升训练效果，无额外环境交互成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
异步强化学习可大幅提升训练吞吐量，但离策略数据来自过时策略、训练推理数值不一致等问题会导致学习不稳定；原有Score Centering（SC）方法能消除奖励基线对更新的影响，但当学习策略与生成数据的行为策略差异过大时仍会失效，在动作会改变后续状态和奖励的智能体交互任务下失效问题更突出。

### 方法关键点
- 提出Regularized Score Centering（RSC），在SC基础上增加token级反向KL（KL(πθ∥µ)）惩罚，约束学习策略的下一词分布与行为策略尽可能接近，限制策略漂移
- 兼容无重要性采样、截断重要性采样（TIS）两种模式，TIS模式下截断token重要性权重，进一步降低梯度方差
- 优化SC的中心估计方式，用蒙特卡洛从行为策略采样辅助token计算条件均值，替代原有top-k近似估计，无偏且不需要额外环境交互

### 关键结果
在数学推理、6类智能体任务（在线购物WebShop、工具使用AppWorld、导航BabyAI、游戏Crafter等）、全异步软件工程任务上验证，对比IS-PPOClip、SC、SC+TIS等SOTA基线：6类智能体任务全部取得最优性能，AppWorld比SC+TIS提升14.3%，BabyAI达到最强基线IS-PPOClip的9.9倍得分，Crafter比IS-PPOClip提升52%；高学习率异步训练场景下比SC+TIS提升51%，更耐受策略过时问题。

最值得记住的一句话：离策略RL训练中，光做梯度修正不够，限制学习策略和行为策略的分布差异，才能从根源上避免基于行为数据的优化无法迁移到学习策略真实交互效果的问题。
