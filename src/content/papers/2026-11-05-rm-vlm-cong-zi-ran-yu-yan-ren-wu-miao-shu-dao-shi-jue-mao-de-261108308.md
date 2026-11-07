---
title: 'RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward
  Machines'
title_zh: RM-VLM：从自然语言任务描述到视觉锚定的奖励机器
authors:
- Roko Parac
- Christos Ziakas
- Leo Ardon
- Alessandra Russo
affiliations:
- Imperial College London
arxiv_id: '2611.08308'
url: https://arxiv.org/abs/2611.08308
pdf_url: https://arxiv.org/pdf/2611.08308
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: Agent 强化学习奖励机制优化
tags:
- Reinforcement Learning
- Reward Machine
- VLM
- LLM
- Task Grounding
one_liner: 结合LLM生成奖励机与VLM视觉锚定能力，实现无需人工标注的非马尔可夫RL任务奖励建模
practical_value: '- 做电商导购Agent、智能交互Agent的时序任务时，可复用「LLM生成结构化任务流程+多模态模型做任务节点锚定」的架构，替代人工硬编码任务规则，降低适配成本

  - 对推荐系统长周期用户行为链路奖励建模（如加购→复购→分享的多步转化），可参考RM的自动机结构，把非马尔可夫长期奖励拆解为可分步校验的节点，提升信用分配准确性

  - 多模态场景下的任务进度评估，可复用VLM做价值函数估计的思路，生成稠密过程奖励信号，避免仅靠最终成败的稀疏奖励导致的训练效率低下'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Reward Machines（RM）是强化学习中处理非马尔可夫任务的成熟方案，可通过自动机结构表达时序任务规则，但依赖人工为每个环境定制命题锚定的标注函数，落地成本极高，应用范围受限。
### 方法关键点
1. 调用LLM直接从自然语言任务描述生成RM自动机结构，无需人工设计任务逻辑；
2. 用VLM充当标注函数，在图像观测中实时锚定RM的命题条件，适配视觉输入场景；
3. 引入VLM驱动的价值函数估计器，评估Agent向RM各状态转移的进度，生成稠密过程奖励信号，解决稀疏奖励训练难问题。
### 关键结果
在非马尔可夫网格世界导航、机器人操控、3D物体收集三类测试域上，任务成功率全面优于现有所有VLM-based奖励方案。
