---
title: 'Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation'
title_zh: LLM Agent程序性记忆的管控、适配与迁移评估
authors:
- Julia Belikova
- Rauf Parchiev
- Evgeny Egorov
- Grigorii Davydenko
- Gleb Gusev
- Andrey Savchenko
- Maksim Makarenko
arxiv_id: '2606.23127'
url: https://arxiv.org/abs/2606.23127
pdf_url: https://arxiv.org/pdf/2606.23127
published: '2026-06-21'
collected: '2026-07-01'
category: Agent
direction: Agent 程序性记忆优化与评估
tags:
- Procedural Memory
- LLM Agent
- Benchmark
- Skill Transfer
- Agent Evaluation
one_liner: 推出企业级LLM Agent程序性记忆迁移评估基准AFTER，验证多模型轨迹生成技能的跨场景泛化优势
practical_value: '- 构建业务Agent的程序性技能库时，优先聚合多模型执行轨迹提炼通用技能，可大幅提升跨模型泛化能力，相比单模型轨迹最高提效13.7个百分点

  - 针对不同业务角色（如电商运营、投放优化师、客服）定制专属技能，避免跨角色迁移带来的性能下降，实测跨角色迁移会带来4.8-7.5个点的准确率损失

  - 技能迭代时只需单轮LLM引导的优化即可带来3.7-6.7个点的性能提升，同时可降低16%-62%的token消耗，平衡效果与推理成本

  - 评估业务Agent的技能复用性时，可参考AFTER的分层评估范式，分别测试同场景增益、跨任务/角色/模型迁移能力，避免技能过拟合到特定上下文'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent在工业场景处理重复任务时，常用程序性记忆沉淀可复用技能以降低推理成本、提升效果，但现有基准无法区分技能的本地效果与跨场景迁移能力，窄经验提炼的技能易过拟合到源上下文，无法适配任务、角色、模型的变化，缺乏标准化的评估框架指导工业级程序性记忆系统搭建。

### 方法关键点
- 推出AFTER基准，包含382个真实企业任务，覆盖6个职业角色、22项程序性技能，支持单/多技能流程测试，设置跨任务、跨角色、跨模型三类迁移拆分维度，隔离技能质量与检索质量的影响
- 配套EVOLUTION评估框架，标准化轨迹收集、技能版本管理、更新执行、迁移度量流程，支持基于执行反馈的技能迭代优化
- 定义特异性（源场景性能增益）、泛化性（分布偏移下的迁移效果）两类核心指标，M1衡量任务部分完成率，M2衡量全任务成功率

### 关键结果
- 静态技能平均提升全任务成功率2.8个百分点，单轮LLM引导的技能优化可额外提升3.7-6.7个点，小模型从技能中获得的增益高于大模型
- 基于多模型混合轨迹进化的技能跨模型测试准确率达73.1%，比最优单模型轨迹来源高13.7个点
- 同角色内进化的技能可带来6.2-11.7个点的增益，跨角色迁移时反而带来4.8-7.5个点的性能损失
- 进化后的技能可降低16%-62%的token消耗，大幅压缩推理成本

**最值得记住的一句话**：程序性记忆的核心挑战不是存储更多经验，而是提取能在源环境外仍然有效的过程性结构。
