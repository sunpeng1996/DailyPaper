---
title: 'MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward
  Reinforcement Learning'
title_zh: MAGIC：基于稠密奖励强化学习的混合粒度智能体图增量构建框架
authors:
- Kairui Yang
- Ziheng Yi
- Xunkai Li
- Minghao An
- Zhanke Liu
- Zekai Chen
- Rong-Hua Li
arxiv_id: '2609.26667'
url: https://arxiv.org/abs/2609.26667
pdf_url: https://arxiv.org/pdf/2609.26667
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多智体协作拓扑自适应优化
tags:
- MultiAgent
- ReinforcementLearning
- RewardShaping
- GraphConstruction
- LLMCollaboration
one_liner: 提出混合粒度多智能体拓扑生成框架，用稠密奖励RL优化，效果与推理效率均超现有SOTA
practical_value: '- 多智能体业务场景可复用混合粒度设计思路：复杂任务（如大促活动方案生成、用户投诉智能处理）用预定义协作组，简单子任务（如单一商品属性校验、query改写）用单原子Agent，平衡效果与推理成本

  - 可迁移潜在基奖励塑造技巧：多智能体任务训练时除终端结果奖励外，可加入中间步骤的效用增益、结构复杂度惩罚、角色重复惩罚等稠密信号，无需全链路跑完即可给出反馈，大幅降低训练所需API成本

  - 电商/推荐场景的多智能体动态拓扑构建可借鉴增量式决策模式：根据当前任务（如用户个性化内容生成、售后问题路由）动态选择所需角色、粒度、依赖关系，比固定拓扑多智能体链路平均节省15%左右token成本

  - RL训练多智能体拓扑时可直接用当前策略采样的轨迹更新，无需提前收集成功轨迹的示范数据集，冷启动成本更低，小样本场景下也能快速迭代'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM多智能体系统的协作拓扑生成采用固定粒度设计：要么全用单原子Agent，构建序列长、无复用先验；要么全用预定义组，缺乏细粒度控制，简单子任务也会产生不必要的多智能体开销，且训练仅用终端结果奖励，反馈稀疏学习效率低，无法适配同个任务下不同子任务的协作需求。

### 方法关键点
- 定义混合粒度智能体组织空间：每个功能角色可根据子任务需求选择实例化为单原子Agent或预定义可复用协作组，全单/全组拓扑均为该空间的特例
- 增量式拓扑构建流程：每步依次选择功能角色、对应粒度、与现有单元的连接关系，直到触发停止动作，所有决策均由任务条件策略输出
- 稠密奖励RL优化：采用基于潜在函数的奖励塑造，结合探针效用增益、结构复杂度惩罚、角色重复惩罚构造中间反馈，不改变最终任务奖励总和，仅将信号分配到中间步骤，训练直接用当前策略采样的轨迹更新，无需预收集成功示范数据集

### 关键结果
在8个覆盖推理、代码、表格理解的基准数据集上对比17个SOTA基线，所有数据集性能均排第一：MMLU-Pro准确率从73.6%提升至83.2%，LiveCodeBench pass@1从26.86%提升至36.57%；同等API训练预算下效果比Search-then-SFT路线高2-8个百分点，推理阶段在3个数据集上token消耗最低，处于性能-成本帕累托最优前沿。

最值得记住的结论：多智能体拓扑无需固定粒度，混合粒度选择+稠密中间反馈可以在更低成本下实现比固定拓扑更好的任务效果。
