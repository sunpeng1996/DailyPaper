---
title: 'Agent Against Agent: An Agentic System for Automatic Prompt Injection Red
  Teaming'
title_zh: 基于智能体对抗的自动化提示注入红队测试系统
authors:
- Yanting Wang
- Chenlong Yin
- Runpeng Geng
- Jinyuan Jia
affiliations:
- The Pennsylvania State University
arxiv_id: '2608.05108'
url: https://arxiv.org/abs/2608.05108
pdf_url: https://arxiv.org/pdf/2608.05108
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: LLM安全 · 智能体红队测试
tags:
- Prompt Injection
- Red Teaming
- Hierarchical Memory
- Agent
- LLM Security
one_liner: 提出带分层记忆的PIMiner智能体，无需针对新目标训练即可达到RL级提示注入攻击效果
practical_value: '- 分层记忆架构可直接复用在业务Agent设计中：长期通用策略库+同场景短期经验池+单会话历史记忆的三层结构，既能沉淀跨场景通用知识，又能适配当前场景特性，同时降低上下文冗余

  - 策略路由机制可迁移到RAG/知识库类系统：用轻量路由模块仅加载Top-K相关知识片段，可降低30%+的输入token量，同时不损失效果，大幅降低推理成本

  - 动态策略库更新逻辑可用于业务知识沉淀：自动从成功/失败案例中提炼通用策略、更新适用范围与失效条件，无需人工标注即可持续迭代系统能力，适合电商客服、推荐Agent等高频迭代场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent已广泛应用于各类业务场景，但提示注入攻击会严重影响系统安全，现有自动化红队测试方法存在明显缺陷：RL类方法需针对每个目标LLM做大量交互训练，泛化性差、成本极高；搜索类方法无需训练但效果远低于RL类，且无法积累复用历史攻击经验，亟需兼顾效果、泛化性与成本的方案。
### 方法关键点
- 三层分层记忆机制：长期跨数据集策略库存储可复用攻击策略、适用范围、正反案例；intra-dataset记忆存储当前数据集-模型对的攻击经验；intra-sample记忆存储当前样本的攻击历史反馈，三类记忆互补提升效果
- 策略路由模块：仅将Top-K相关策略加载到攻击Agent上下文，可减少43%~61%的输入token量，降低推理成本且不损失攻击效果
- 经验消化模块：自动从攻击结果中提炼新策略、更新现有策略的适用范围与失效条件，策略库可随使用持续迭代，无需针对新目标LLM做额外训练
### 关键结果
在IPIArena、AgentDojo两个基准数据集上测试，效果与SOTA RL类方法相当：IPIArena上对Gemini-2.5-Pro攻击成功率（ASR@10）达76.2%，对GPT-5.1达61.9%；AgentDojo上对Gemini-2.5-Pro ASR@10达86.7%，且测试时每个样本仅需最多10次查询即可完成攻击
### 核心结论
带分层可积累记忆的搜索类智能体，可达到RL级的任务效果，同时避免RL训练成本高、泛化性差的缺陷
