---
title: Imitation Bootstrapped Multi-Agent Reinforcement Learning
title_zh: 模仿引导的多智能体强化学习（IBMARL）
authors:
- Tony H. Zhang
- Connor Mattson
- Daniel S. Brown
affiliations:
- University of Utah
arxiv_id: '2611.18543'
url: https://arxiv.org/abs/2611.18543
pdf_url: https://arxiv.org/pdf/2611.18543
published: '2026-11-13'
collected: '2026-11-16'
category: MultiAgent
direction: 多智能体强化学习 · 模仿学习引导
tags:
- MARL
- Imitation Learning
- RL
- Behavior Cloning
- Multi-Agent
one_liner: 提出仅需单人单智能体演示的多智能体强化学习框架，可快速超越演示性能上限
practical_value: '- 多Agent协同推荐/广告投放场景冷启动时，可采用R2BC轮询克隆方案，仅需单个运营人员轮流控制单Agent策略，即可低成本生成全团队初始IL策略，避免联合专家演示的高成本问题

  - 训练多Agent策略时，可给每个Agent保留IL、RL双动作候选，用中心化critic ensemble动态选择每个Agent的执行动作，搭配Q值门控的模仿损失，仅在critic判定IL动作更优时对齐，既解决稀疏奖励探索难问题，又不受演示性能上限约束

  - 训练完成后可直接部署各Agent的RL策略，无需保留中心化critic或IL策略，完全去中心化执行，满足电商/广告系统低延迟、高可用的部署要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统单智能体RL利用演示可大幅提升稀疏奖励下的训练效率，但扩展到多智能体场景存在两大痛点：一是难以获取所有智能体的联合专家演示，单人无法同时操作多个智能体；二是现有模仿引导RL方法部署时依赖中心化critic，无法支持去中心化执行，难以落地低延迟业务场景。

### 方法关键点
- 基于R2BC轮询行为克隆生成初始IL策略：演示者轮流控制单个智能体，其余智能体执行当前最优策略，仅需单人操作即可生成多智能体协同IL策略，无需联合演示
- 训练阶段每个智能体同时输出IL、RL两个动作候选，中心化critic ensemble对2^N种联合动作组合打分，选择最优组合执行
- 新增门控模仿损失：仅当critic判定IL动作价值高于RL动作时，才约束RL策略向IL对齐，训练完成后可直接部署各Agent的RL策略，无需任何中心化组件

### 关键结果
- 在4个VMAS多智能体基准任务上，超越初始IL策略的速度比现有基于演示的baseline快2.6~4.2倍，是唯一能在Balance、Transport两个高难度稀疏奖励任务上超过IL策略的方法
- 在Buzzwire、Balance任务上性能超过演示专家本身；真实人类演示的Buzzwire任务中，超越IL策略的速度是最优baseline的2倍以上

### 核心结论
对于多智能体系统，模仿策略直接参与训练过程提供动作候选，比仅作为离线数据填充回放缓冲区的价值高得多
