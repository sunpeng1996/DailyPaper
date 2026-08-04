---
title: 'LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks'
title_zh: LongHorizon-Harness：面向真实场景的长周期Agent执行框架
authors:
- Ziyu Ma
- Hailang Huang
- Shun Zou
- Yong Wang
- Shidong Yang
- Yiming Hu
- Fei Wei
- XiangXiang Chu
affiliations:
- Alibaba Group DreamX Team
arxiv_id: '2608.01964'
url: https://arxiv.org/abs/2608.01964
pdf_url: https://arxiv.org/pdf/2608.01964
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: 长周期Agent执行框架优化
tags:
- Long-Horizon Agent
- Agent Harness
- Task State Management
- Manage-Execute-Audit
- LLM Agent
one_liner: 通过管理-执行-审计三角色循环显式维护经审计的任务状态，大幅提升长周期Agent跨场景任务成功率
practical_value: '- 电商长流程Agent任务（如用户全生命周期运营、跨部门需求落地）可复用MEA三角色拆分架构，将任务状态和执行解耦，避免错误累积与目标漂移

  - Agent执行链路引入只读审计角色，仅将经过环境验证的事实更新到任务状态，解决现有Agent自我评估不准、虚假完成的问题

  - 采用AgentAdapter兼容现有Agent原生执行逻辑，业务侧可低成本接入已有Agent能力，无需重构原有执行链路

  - 长周期任务可采用每轮执行重置上下文的设计，避免context rot问题，同时降低单轮上下文长度压力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期Agent框架将执行、状态维护、完成评估绑定在持续增长的上下文中，普遍面临错误累积、目标漂移、context rot、任务状态丢失三大核心问题，导致长流程任务成功率低，难以落地真实场景。

### 方法关键点
- 将长周期执行重构为任务状态管理问题，显式在执行链路外维护任务状态，仅将经环境独立验证的事实更新到状态
- 采用Manage-Execute-Audit（MEA）循环：Manager负责维护任务状态、拆分当前子任务并定义验收标准；Executor在全新上下文中仅执行当前子任务，执行历史每轮清空；只读Auditor独立验证环境状态变更，输出审计报告作为唯一跨轮记忆
- 轻量AgentAdapter支持兼容不同LLM后端、现有Agent原生执行循环，无需修改原有逻辑

### 关键实验
在WeaveBench、OSWorld 2.0、Terminal-Bench 2.1三个长周期Agent基准上测试，同模型（Qwen 3.7-Plus）对比基线：WeaveBench PassRate从51.8%提升到80.7%，Terminal-Bench 2.1成功率从69.7%提升到77.2%，OSWorld 2.0任务完成率从2.8%提升到8.3%，在Claude Opus 4.7上也获得一致增益。

**最值得记住的一句话**：长周期Agent的能力是模型与框架的共同系统属性，框架可以在不增加模型原生能力的前提下，大幅提升固定模型的端到端任务完成表现。
