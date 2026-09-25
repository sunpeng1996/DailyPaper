---
title: Search-Aware Reinforcement Learning for Multi-Component Query Understanding
  in Roblox Game Search
title_zh: 面向Roblox游戏搜索多组件Query理解的搜索感知RL框架
authors:
- Nayoung Choi
- Shengjian Chen
- Xiaokai Wei
- Wenzheng Zhang
- Daiyao Yi
- Rachit Pareek
- Vincent Su
- Michelle Gong
- Jinho D. Choi
affiliations:
- Emory University
- Roblox Corporation
arxiv_id: '2609.30177'
url: https://arxiv.org/abs/2609.30177
pdf_url: https://arxiv.org/pdf/2609.30177
published: '2026-09-24'
collected: '2026-09-25'
category: QueryRec
direction: Query理解 · 搜索感知RL优化
tags:
- QueryUnderstanding
- ReinforcementLearning
- RLAIF
- KnowledgeDistillation
- GR-DPO
one_liner: 通过蒸馏+分组件搜索感知RL优化多任务Query理解小模型，大幅提升搜索效果且满足线上时延要求
practical_value: '- 多组件Query理解等结构化生成任务不要仅用单一端到端奖励，需针对每个组件的业务角色设计专属奖励，解决多任务场景下的credit分配问题，可直接迁移到电商/内容搜索的query理解场景

  - 采用「大模型SFT蒸馏小模型+搜索感知RL精调」的两阶段范式，既保证输出格式合规、满足线上低时延要求，又能通过下游引擎反馈优化实际搜索效果，适合工业级落地

  - 多奖励RL训练优先选择GR-DPO等离线组偏好优化方法，相比on-policy的GRPO更稳定，可避免模型为规避低分项奖励故意不输出特定组件的投机行为

  - 奖励计算可复用RLAIF范式，用LLM judge+真实业务引擎返回结果替代人工标注，大幅降低标注成本，适配标注难度高的业务场景'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有生成式Query理解多基于静态标注做监督训练，无法感知输出与下游搜索pipeline的交互影响，实际搜索效果优化空间大；单端到端RL奖励存在多任务credit分配不足的问题，同时大模型推理时延过高，无法适配生产级搜索的吞吐和时延要求。
### 方法关键点
- 两阶段训练范式：第一阶段通过SFT将大模型教师的多组件Query理解能力蒸馏到Qwen3.5 2B/4B小模型，保证输出格式合规、满足基础能力要求；
- 分组件复合奖励设计：无需人工标注，基于真实生产搜索引擎的返回结果，通过RLAIF范式由LLM judge为每个QU组件（意图分类、query归一化、扩query、属性抽取、否定词等）计算专属奖励，加权聚合得到总奖励；
- 稳定RL优化：采用GR-DPO离线组偏好优化方法，相比单对DPO和on-policy RL训练更稳定，避免模型出现为规避惩罚故意不输出扩query、错误归类无意图等投机行为。
### 关键结果
基于Roblox 1.6万条真实+合成搜索query验证：4B模型经RL优化后，NDCG@20比SFT基线高8.9个百分点，比单端到端RL基线高3.5个百分点；p50推理时延比大模型教师低5.8倍，吞吐量提升6倍，满足线上部署要求。
> 最值得记住的结论：生产环境的多组件结构化生成任务，仅优化端到端目标的效果远不如针对每个组件的业务角色设计专属搜索感知奖励
