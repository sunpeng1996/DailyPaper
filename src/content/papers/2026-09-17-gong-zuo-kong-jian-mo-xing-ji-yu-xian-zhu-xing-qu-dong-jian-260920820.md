---
title: 'Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision'
title_zh: 工作空间模型：基于显著性驱动监督的轻量机器人记忆方法
authors:
- Nitish Dashora
- Douglas Chen
- Idan Shenfeld
- John Marangola
- Pulkit Agrawal
- Max Simchowitz
affiliations:
- Massachusetts Institute of Technology
- Carnegie Mellon University
arxiv_id: '2609.20820'
url: https://arxiv.org/abs/2609.20820
pdf_url: https://arxiv.org/pdf/2609.20820
published: '2026-09-17'
collected: '2026-09-19'
category: Agent
direction: Agent 长时记忆蒸馏与部署优化
tags:
- AgentMemory
- KnowledgeDistillation
- VLM
- LatentRepresentation
- DeploymentEfficiency
one_liner: 训练阶段用VLM蒸馏轻量工作空间Token，部署无需在线VLM即可完成长记忆任务
practical_value: '- 长时记忆任务可采用「训练阶段大模型离线提取显著性信息蒸馏到轻量Token，部署直接用Token推理」的架构，大幅降低在线算力开销

  - 蒸馏损失可参考集合重构损失，保证轻量表示保留所有任务关键信息，避免冗余信息引入的伪相关问题

  - 生成式推荐/Agent对话的用户长序列建模可复用该思路，用离线LLM提取用户历史关键特征蒸馏到Semantic ID，降低在线推理延迟'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
长时决策任务依赖历史信息，直接输入全量历史容易引入伪相关降低模型性能，现有方案在线调用VLM处理历史显著性信息算力开销高、部署延迟大，无法满足低时延场景需求。
### 方法关键点
1. 训练阶段离线调用VLM识别任务所需的当前+历史关键信息，通过集合重构解码损失将关键信息蒸馏为轻量的工作空间Token（Workspace Token）；
2. 部署阶段直接用工作空间Token替代原始观测输入下游策略，无需在线调用VLM做推理。
### 关键结果数字
仿真与硬件实验中，该方案任务成功率达91.5%，远高于在线VLM方案的66.8%、朴素历史输入方案的53.8%，同时推理延迟更低、算力开销更小。
