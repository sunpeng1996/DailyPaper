---
title: Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication
  Topology Design
title_zh: 面向高效多智能体通信拓扑设计的奖励引导自回归图生成方法
authors:
- Poomphob Suwannapichat
- Boonyarit Changaival
- Caesar Wu
- Pascal Bouvry
affiliations:
- University of Luxembourg
- King Mongkut’s University of Technology Thonburi
arxiv_id: '2608.20099'
url: https://arxiv.org/abs/2608.20099
pdf_url: https://arxiv.org/pdf/2608.20099
published: '2026-08-20'
collected: '2026-08-21'
category: MultiAgent
direction: 多智能体 · 通信拓扑效率优化
tags:
- Multi-Agent System
- RLHF
- Graph Generation
- Token Efficiency
- Topology Optimization
one_liner: 引入RLHF式奖励引导优化多智能体拓扑生成，不降准确率下平均减20.5%token消耗
practical_value: '- 业务多智能体系统（如智能客服、商品决策Agent组）可复用奖励模型设计思路：优先加权任务完成率，再分别给智能体数量、通信边数量加惩罚权重，保证效果不跌的前提下降低推理成本

  - 拓扑生成的Best-of-N采样策略可直接复用：生成少量候选拓扑用轻量GNN reward模型选最优，额外开销远低于LLM推理开销，性价比极高

  - 奖励模型支持跨任务复用，新增Agent角色无需重新训练拓扑生成器，适合业务侧多场景多角色的多智能体架构快速迭代'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM驱动的多智能体系统在复杂推理、代码生成等任务上表现优于单LLM，但多轮交互带来极高的token消耗；此前的自回归拓扑生成方法ARG-Designer仅基于最大似然训练，无显式激励生成稀疏结构，存在大量冗余开销。
### 方法关键点
- 借鉴RLHF范式设计三阶段pipeline：复用预训练的自回归图生成器，采样候选拓扑执行后生成偏好对数据集，训练融合任务正确性与结构紧凑度的GNN奖励模型，最后用GRPO策略微调生成器，加KL约束避免偏离预训练分布。
- 奖励函数加权优先级明确：任务完成率权重0.6，智能体数量权重0.3，通信边数量权重0.1，严格保证正确性优先，不会为降低开销牺牲效果；偏好对过滤仅保留至少一个任务成功、奖励差大于0.05的样本，降低无效训练信号。
- 推理侧采用Best-of-N（N=5）策略，生成少量候选拓扑后用轻量GNN奖励模型选最优，额外开销可忽略。
### 关键实验结果
在GSM8K、AQuA、HumanEval等6个推理/代码基准上对比单LLM、AgentPrune、ARG-Designer等5个基线，准确率与基线无统计显著差异的前提下，比ARG-Designer平均降低20.5%的token消耗，5个基准优化效果统计显著，仅模板化程度高、无结构冗余的MultiArith数据集无明显优化。
### 核心结论
对于结果可验证的多智能体任务，用奖励引导替代单纯的最大似然训练，是在不损失效果的前提下降低推理成本的高性价比方案。
