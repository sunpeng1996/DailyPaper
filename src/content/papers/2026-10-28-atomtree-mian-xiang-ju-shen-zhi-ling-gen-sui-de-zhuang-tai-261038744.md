---
title: 'AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following
  with LLMs'
title_zh: AtomTree：面向具身指令跟随的状态感知层次化LLM规划框架
authors:
- Haotian Zhai
- Tianming Sha
- Junnan Li
affiliations:
- University of Minnesota
- Stony Brook University
- University of Wisconsin–Madison
arxiv_id: '2610.38744'
url: https://arxiv.org/abs/2610.38744
pdf_url: https://arxiv.org/pdf/2610.38744
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: 具身Agent · LLM层次化任务规划
tags:
- LLM Planning
- Embodied Agent
- Hierarchical Planning
- Zero-shot Learning
- Instruction Following
one_liner: 提出状态感知的层次化树状规划框架，零样本下在具身指令跟随任务上超越现有少/零样本基线
practical_value: '- 做电商全链路导购、售后工单处理等长周期任务Agent时，可复用「边执行边动态拆解子目标」的树状规划逻辑，替代一次性生成全链路计划的方案，大幅降低长任务错误累积概率

  - 可移植轻量化符号记忆模块设计，仅结构化存储历史执行结果、已观测实体/用户行为标签，不需要喂全量交互日志给LLM，既降低推理token成本，也能避免上下文遗忘问题

  - 做动态任务重规划时，可复用层次化回溯机制：子任务失败后回到父节点重新生成子树计划，而非仅在失败点局部重试，减少错误轨迹漂移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM驱动的具身指令跟随规划多采用一次性生成全量串行计划的方案，仅在执行失败后被动触发重规划，缺乏对实时环境状态的感知。对ALFRED基准的错误分析显示，长周期任务下规划错误占比随任务长度线性上升，当PDDL计划长度>7时，规划错误占比达68.7%，成为长horizon任务的核心性能瓶颈。

### 方法关键点
- 层次化树状规划范式：每步决策时LLM基于当前环境状态、当前子目标、历史记忆，选择要么将当前子目标拆解为有序的细粒度子任务列表，要么直接输出可执行的原子动作，逐步构建动态演进的子目标树；
- 轻量化符号记忆模块：仅存储历史原子动作的执行成败记录、已观测到的实体集合，序列化为短文本后作为prompt输入，既解决自然语言描述与环境实体的对齐问题，也避免上下文遗忘、重复执行问题，同时大幅降低LLM输入token量；
- 层次化回溯重规划：当子动作执行失败或超时时，直接回退到对应父节点，基于最新状态和记忆重新生成子树计划，而非仅在失败点局部重试，避免错误轨迹持续漂移。

### 关键实验
在ALFRED具身指令跟随基准的零样本设置下测试，仅用高等级目标指令（无分步引导）：比最优零样本基线Socratic Planner在Test Unseen拆分上SR（任务成功率）从13.47%提升到41.20%，同时超越少样本基线FLARE的32.57%，性能接近部分全监督训练方法；消融实验显示三个核心组件均带来稳定收益，其中记忆模块对性能提升贡献最大。

### 核心结论
长周期任务规划的核心不是一次性生成完美计划，而是基于实时状态动态拆解、调整目标结构，用结构化的分层决策替代线性的单轮推理。
