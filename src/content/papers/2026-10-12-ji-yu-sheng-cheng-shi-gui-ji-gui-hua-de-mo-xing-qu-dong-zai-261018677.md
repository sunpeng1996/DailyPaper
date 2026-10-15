---
title: Model-Based Online Decision Making via Generative Trajectory Planning
title_zh: 基于生成式轨迹规划的模型驱动在线决策框架GTP
authors:
- Haldun Balim
- Yilun Du
- Na Li
affiliations:
- Harvard University
arxiv_id: '2610.18677'
url: https://arxiv.org/abs/2610.18677
pdf_url: https://arxiv.org/pdf/2610.18677
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: Agent 长时序在线决策优化
tags:
- Reinforcement Learning
- Diffusion Model
- Trajectory Planning
- Model-based RL
- Online Decision Making
one_liner: 以扩散模型为动作序列提议分布，结合模型基规划实现高效长时序在线决策
practical_value: '- 电商智能导购Agent、会话式推荐的多轮决策场景可复用GTP的beam search+扩散微调框架：用扩散模型生成多轮候选交互动作序列，结合用户价值模型、状态转移模型打分剪枝，避免单步决策的短视问题

  - 长序列优化任务（如广告多日预算分配、用户生命周期消费路径规划）可借鉴其基于集成模型的轨迹级不确定性估计策略，乐观探索+保守更新平衡探索利用，提升样本效率

  - 训练生成式序列模型时可复用Langevin增强精英样本的trick，避免扩散模型模式崩溃，提升序列生成的多样性与质量

  - 推荐系统召回/排序的序列候选生成场景，可替换传统随机采样为扩散先验采样，缩小候选搜索空间，提升长序列规划效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在线决策框架存在本质权衡：价值驱动RL依赖短horizon自举，长时序信息传播慢、误差累积严重；轨迹优化方法每步需解高维非凸优化问题，计算成本高、易陷入局部最优；现有扩散策略RL仅将扩散模型作为单步策略替换，未发挥其长序列建模优势，长时序在线决策性能受限。
### 方法关键点
- 提出GTP框架，将扩散模型作为动作序列的提议分布，替代传统随机采样，避免每步从零优化
- 规划采用迭代beam search流程：分支候选轨迹前缀、对未确定后缀做部分加噪/去噪微调、用集成动力学模型+奖励模型+价值模型打分剪枝，渐进生成高收益轨迹
- 训练阶段引入Langevin增强精英轨迹集，缓解扩散先验模式崩溃；基于集成动力学模型的分歧做轨迹级不确定性估计，采用乐观探索+保守更新策略平衡探索利用
- 价值学习采用多步轨迹返回逆方差加权，缓解长时序模型误差累积问题
### 关键结果
在MuJoCo连续控制、Fetch长时序操作、PushT视觉操作三类任务上对比SAC、TD3、DreamerV3、TD-MPC2等SOTA基线：
1. MuJoCo 5个环境中，H=4的GTP全面超越所有基线，Humanoid-v4任务得分较次优基线高26%，HalfCheetah-v4较次优高14%
2. 长时序操作任务中，GTP在FetchPush、FetchPick&Place、PushT视觉任务上成功率分别达100%、98%、99%，所有RL/扩散策略基线在PushT视觉任务上成功率为0

生成式模型更适合作为规划的结构化提议分布，而非直接替代策略，这是生成式建模与模型基决策结合的新范式
