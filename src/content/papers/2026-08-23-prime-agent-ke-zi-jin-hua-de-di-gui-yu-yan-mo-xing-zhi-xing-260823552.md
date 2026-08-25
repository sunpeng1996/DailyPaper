---
title: 'Prime Agent: A Self-Improving RLM Harness'
title_zh: Prime Agent：可自进化的递归语言模型执行框架
authors:
- Seth Karten
- Alex L. Zhang
- Kevin Thomas
- Sebastian Müller
- Elie Bakouch
- Daniel Auras
- Mika Senghaas
- Fares Obeid
- Konstantin Dunas
- Johannes Hagemann
affiliations:
- Princeton University
- Prime Intellect
- MIT
arxiv_id: '2608.23552'
url: https://arxiv.org/abs/2608.23552
pdf_url: https://arxiv.org/pdf/2608.23552
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: Agent框架 · 长周期任务执行优化
tags:
- AgentFramework
- RLM
- MultiAgent
- LongHorizonTask
- SelfImproving
- CodeAgent
one_liner: 开源长周期Agent执行框架，支持持久状态、递归子代理与自进化，大幅提升复杂任务性能
practical_value: '- 可复用其四级状态分层（L0权重/L1上下文/L2 REPL与子代理/L3持久存储）设计，优化电商导购Agent的长会话状态管理，避免上下文溢出和状态丢失

  - 递归子代理+异步通信机制可迁移到多角色推荐Agent协作场景，比如用户意图理解、召回、文案生成子代理并行执行，降低推理 latency

  - Continual Harness的版本化技能/记忆迭代机制可沉淀电商场景通用处理逻辑（如促销规则计算、退换货流程解答），无需重复生成

  - 其标准化长周期评估核算方法可复用，解决Agent类推荐系统的效果追踪、资源消耗统计问题，区分框架故障与模型能力不足'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent执行框架普遍存在状态管理能力弱、工作流固定、长周期任务易因框架故障终止、无法准确衡量模型真实能力的问题，限制了大模型在长周期复杂任务上的潜力释放。

### 方法关键点
- 设计四级状态分层架构：L0模型权重、L1活跃上下文、L2持久IPython REPL与递归子代理、L3磁盘持久化历史/记忆/技能/子代理配置，各层通过显式操作流转数据
- 实现RLM递归调用原语，支持异步创建子代理，子代理独立持有上下文、执行环境和状态，通过守护进程管理的消息队列实现点对点通信
- 内置Continual Harness机制，支持版本化迭代更新提示、记忆、可执行技能和子代理配置，在模型权重固定的情况下实现自进化
- 提供标准化的长周期执行控制、资源核算、故障恢复机制，隔离框架故障和模型能力不足，支持人类实时干预会话

### 关键结果
- ARC-AGI-3基准上，将Opus 5的RHAE Best@1从原生框架的30%提升到95.5%，超过人类基线95.4%
- 长上下文任务上，相比Pi、Claude Code、Codex等原生框架，在OOLONG、LongBench Pro等多数任务上性能持平或更优，EmulatorBench的Game Boy Color仿真构建成功率达99.8%
- 支持连续85.5小时的nanoGPT自主优化任务，Factorio游戏7天运行中完成24项技术研究，累计创建633个子代理

### 核心结论
Agent框架的表达性和状态管理能力是决定大模型长周期任务上限的核心因素，固定模型下通过测试时计算和状态迭代可获得远超过原生能力的性能提升
