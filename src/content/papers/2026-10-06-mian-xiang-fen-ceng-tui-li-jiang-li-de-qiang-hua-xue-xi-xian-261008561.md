---
title: 'Reinforcement Learning for Hierarchical Reasoning Rewards: Minimax-Optimal
  Rates with Transformers'
title_zh: 面向分层推理奖励的强化学习：Transformer实现最小最大最优收敛率
authors:
- Naoki Nishikawa
- Taiji Suzuki
affiliations:
- The University of Tokyo
- RIKEN AIP
arxiv_id: '2610.08561'
url: https://arxiv.org/abs/2610.08561
pdf_url: https://arxiv.org/pdf/2610.08561
published: '2026-10-06'
collected: '2026-10-07'
category: Training
direction: 大模型RL后训练 · 最优收敛率理论分析
tags:
- Reinforcement_Learning
- Transformer
- Minimax_Optimality
- Hierarchical_Reward
- On-Policy_Training
one_liner: 证明基于Transformer的on-policy Actor-Critic在分层推理奖励下达到最小最大最优收敛率，量化on-policy采样收益
practical_value: '- 做电商多轮导购、复杂搜索query理解、广告文案逻辑校验这类分层推理任务的LLM Agent时，优先选择on-policy
  RL训练，避免固定分布离线采样的指数级样本效率损失

  - RL后训练时可复用深度课程+自适应查询策略：迭代逐步提升查询的推理深度，对当前策略置信度低于阈值的前缀提前停止查询，大幅降低奖励校验/标注成本

  - 分层任务的Actor-Critic训练中，Critic用Transformer实现过程奖励建模，配合PPO的信任域更新、梯度裁剪策略，可达到理论最优的样本效率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RL已成为LLM推理类任务后训练的标准工具，on-policy探索结合神经奖励模型的有效性缺乏理论支撑，分层多步推理场景下固定分布离线采样的样本效率瓶颈也未被量化。
### 方法关键点
- 提出分层嵌套奖励模型，模拟多步推理中只有完成前序步骤才能解锁后续奖励的特性，奖励由嵌套区域内的α-Hölder平滑分量逐层叠加组成，分量权重随深度按i^-γ衰减
- 设计基于Transformer的on-policy Actor-Critic算法：交替从KL正则化的Gibbs策略采样响应，拟合Transformer Critic作为过程奖励模型，用信任域掩码+梯度裁剪更新策略
- 采用深度课程+自适应查询策略：迭代逐步提升查询的推理深度，对当前策略分配质量低于阈值的前缀提前停止查询，节省采样成本
### 关键结果
- 固定prompt数量下，所提算法的收敛率达到minimax最优，仅差对数因子
- 弱正则化场景下，固定分布离线采样的regret仅能以对数速率下降，on-policy策略可达多项式速率n^(-(γ-1)/(2γ+1))
- 大预算场景下，on-policy策略regret达到ρ*(nρ^(2+1/γ)/M)^(-2α/(2α+d))，固定采样会额外引入exp(cρ^(-1/γ))的指数级成本
### 核心结论
分层多步推理任务中，on-policy RL训练的样本效率远高于固定分布的离线奖励建模，差异可达指数级
