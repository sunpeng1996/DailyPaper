---
title: 'Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents'
title_zh: 面向长周期Agent的主动式记忆干预代理架构
authors:
- Yifan Wu
- Lizhu Zhang
- Yuhang Zhou
- Mingyi Wang
- Bo Peng
- Serena Li
- Xiangjun Fan
- Zhuokai Zhao
affiliations:
- Meta AI
arxiv_id: '2607.08716'
url: https://arxiv.org/abs/2607.08716
pdf_url: https://arxiv.org/pdf/2607.08716
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 长周期Agent · 主动记忆干预
tags:
- Memory Agent
- Long-Horizon Agent
- Proactive Intervention
- LLM Agent
- Memory Policy
one_liner: 提出独立双阶段主动记忆代理，解决长周期Agent的行为状态衰减问题
practical_value: '- 电商导购/服务类长会话Agent可直接复用该解耦架构，无需修改现有业务Agent逻辑，即可减少重复提问、规则遗忘等问题，提升会话转化率

  - 记忆库拆分知识、过程、私有状态三类的设计，比普通无结构RAG召回更适配业务场景，可显著提升记忆精准度

  - 选择性干预而非全量注入记忆的设计，既降低不必要的token消耗，又减少无关记忆对当前决策的干扰，适配推理成本敏感的线上场景

  - 中小厂可参考SFT+GRPO蒸馏小参数模型的思路，用业务会话数据微调小模型做记忆干预，平衡效果和成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期Agent任务（如多轮客服、复杂工具调用）中，关键决策信息（任务要求、环境事实、历史失败尝试等）易被淹没在长上下文中，哪怕在context window内也无法有效影响决策，即**行为状态衰减**问题；现有记忆方案多聚焦存储和召回，未解决「何时注入记忆」的干预问题，注入过多会增加token成本、干扰决策，注入过少则无法解决状态衰减。

### 方法关键点
- 解耦架构：独立记忆代理与业务动作Agent并行，即插即用无需修改原有Agent逻辑，按固定间隔触发执行
- 双阶段设计：第一阶段维护结构化记忆库，分私有状态（记忆代理自用进度跟踪，不暴露给动作Agent）、知识记忆（稳定事实如规则、用户信息）、过程记忆（尝试结果如失败案例、解决方案）三类，通过预定义工具调用实现记忆增删改
- 选择性干预：第二阶段仅在记忆可能影响当前决策时，输出精准提醒注入动作Agent上下文，其余时候选择不干预，禁止输出泛化战略指导
- 训练方案：先SFT蒸馏大模型的记忆操作和干预逻辑，再用GRPO强化学习校准干预时机

### 关键实验
在Terminal-Bench 2.0（命令行长周期任务）和τ2-Bench（多轮工具交互，含航空、零售、电信域）测试：
- Claude Opus 4.6作为记忆代理，弱动作Agent Sonnet 4.5在Terminal-Bench pass@1提升+8.3pp，τ2-Bench加权平均提升+6.8pp；强动作Agent Opus 4.6也分别提升+2.4pp、+2.5pp
- 消融实验显示双阶段架构比全量记忆暴露、强制每轮注入、无记忆库顾问模式、Mem0通用记忆层的跨域效果更均衡
- SETA训练的Qwen3.5-27B开源记忆代理，迁移到Terminal-Bench时pass@1提升+3.5pp

Agent记忆的核心不是存储和召回，而是在正确的时机将正确的信息注入决策流，避免不必要的干扰。
