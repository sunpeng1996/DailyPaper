---
title: 'Grid Cells as Spectral Successor Features: A Reusable Basis for Continual
  Reinforcement Learning'
title_zh: 网格细胞作为谱后继特征：持续强化学习的可复用特征基
authors:
- Élodie Côté-Gauthier
- Doina Precup
- Isabeau Prémont-Schwarz
affiliations:
- McGill University
- Mila – Quebec AI Institute
- Université Laval
arxiv_id: '2611.26504'
url: https://arxiv.org/abs/2611.26504
pdf_url: https://arxiv.org/pdf/2611.26504
published: '2026-11-19'
collected: '2026-11-21'
category: Agent
direction: Agent 持续强化学习表征优化
tags:
- Successor Representation
- Continual RL
- Grid Cell
- Spectral Method
- Reinforcement Learning
one_liner: 基于参考策略转移矩阵特征向量构建可复用特征基，无需额外网络与回放缓冲即可实现持续RL快速任务适配
practical_value: '- 电商多场景多任务推荐场景，可参考固定参考策略转移矩阵特征向量思路，预构建跨任务通用的用户/物品表征基，降低新任务适配成本

  - 推荐/广告策略持续迭代场景，可复用该方法线性回归适配逻辑，无需回放缓冲即可快速适配新业务目标，减少训练资源消耗

  - 端侧轻量Agent决策优化场景，可借鉴无额外后继特征网络的设计，降低端侧推理与更新的算力开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
持续强化学习要求Agent在任务切换时复用已有环境知识避免从头重训，现有后继特征（Successor Features）方法将环境动态与任务特定奖励解耦，但效果高度依赖基础特征选择，缺乏通用可复用的特征基构建方案。
### 方法关键点
1. 以内嗅皮层网格细胞对应后继表征特征向量为设计原则，从固定参考策略的转移矩阵特征向量构建通用特征基
2. 状态-动作对的后继特征可直接表示为同对基础特征的线性组合，系数有闭式解$θ_i=1/(1-γλ_i)$（$λ_i$为对应特征值）
3. 长期回报可直接通过与即时回报相同的特征预测，无需后继特征网络与回放缓冲，新任务适配仅需对回报做线性回归。
### 关键结果
双目标网格世界实验中，以均匀随机游走为参考策略时，该方法构建的Agent在每次目标切换时均维持接近最大回报，而SimpleSF、DQN每次切换后回报会出现大幅下降。
