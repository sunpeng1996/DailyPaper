---
title: 'Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents'
title_zh: Jev-Mem：基于双系统认知的高效AI Agent记忆架构
authors:
- Dongming Jiang
- Yi Li
- Bingzhe Li
affiliations:
- The University of Texas at Dallas
arxiv_id: '2609.23986'
url: https://arxiv.org/abs/2609.23986
pdf_url: https://arxiv.org/pdf/2609.23986
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: Agent 智能体长时记忆优化
tags:
- Agentic Memory
- Dual Process
- LLM Agent
- Memory System
- Efficient Inference
one_liner: 提出双系统分层Agent记忆架构，用轻量System One控制记忆全流程，同时提升效果与运行效率
practical_value: '- 可复用双系统分层思路做Agent记忆管控：高频结构化决策（如用户偏好打标、历史行为关联、检索终止判断）用小模型/轻量分类器实现，仅将复杂推理、回答生成交给大模型，大幅降低长时记忆系统的调用成本与延迟

  - 多关系记忆存储设计可直接迁移到用户行为建模：给用户记忆节点附加语义、时间、因果、实体四类关联边，检索时按需路由到对应关系视图，比纯语义向量召回更适配跨会话因果推理类场景（如用户退货原因溯源、复购需求预判）

  - 自适应检索终止机制可优化现有召回链路：不用固定top-k召回阈值，通过轻量模型判断当前已召回信息是否足够支撑后续推理，满足条件即停止检索，降低实时推荐、客服Agent场景的响应延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent长时记忆系统要么依赖固定规则，灵活性不足难以适配复杂查询；要么全流程调用autoregressive LLM做记忆管控，高频决策开销大，成为长时交互场景的性能瓶颈，无法同时兼顾记忆效果与运行效率。
### 方法关键点
- 采用双系统三层架构：轻量System One控制平面负责全生命周期记忆管控，多关系记忆平面存储共享节点+语义/时间/因果/实体四类关联边+向量/词法双索引，System Two推理平面仅负责复杂证据合成与回答生成
- 写路径：System One完成记忆分类、冗余过滤、关联边构建，保留原始观测不做不可逆删除，避免信息损失
- 读路径：System One实现查询路由、检索预算动态分配、图遍历、候选打分、自适应停止，证据足够即终止检索，减少无效计算
### 关键实验
在LoCoMo长时对话基准上对比A-MEM、Nemori、MAGMA等SOTA记忆系统，LLM-as-a-Judge整体得分0.777，较最强基线相对提升11.0%；记忆构建时间仅158s，较最快基线提速6.6倍；平均查询 latency 0.93s，较最快基线降低36.7%。
### 最值得记住的一句话
高频结构化记忆管控无需依赖大模型生成，将计算任务按复杂度分层拆分，可同时实现效果提升与效率优化。
