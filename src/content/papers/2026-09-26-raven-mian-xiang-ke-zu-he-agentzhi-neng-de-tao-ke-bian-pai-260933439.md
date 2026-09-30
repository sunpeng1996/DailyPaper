---
title: 'Raven: The Harness of Harnesses for Composable Agentic Intelligence'
title_zh: Raven：面向可组合Agent智能的套壳编排框架
authors:
- EverMind AI
affiliations:
- EverMind AI
arxiv_id: '2609.33439'
url: https://arxiv.org/abs/2609.33439
pdf_url: https://arxiv.org/pdf/2609.33439
published: '2026-09-26'
collected: '2026-09-30'
category: MultiAgent
direction: 多Agent · 跨域任务编排与套壳自演化
tags:
- Multi-Agent Orchestration
- Agent Harness
- Composable Intelligence
- Task Decomposition
- Skill Reuse
one_liner: 开源多Agent生态系统，自动构建演化模块化Agent套壳，跨域长流程任务性能显著优于SOTA
practical_value: '- 可复用多Agent编排架构：将电商场景下选品、文案生成、投放优化等不同领域Agent封装为模型+套壳的可组合单元，用DAG明确任务依赖，降低跨模块协作的对齐成本

  - 套壳自演化机制可迁移到业务Agent迭代：基于失败诊断自动优化Agent的工具调用逻辑、prompt模板、错误恢复策略，无需手动频繁调优业务Agent的执行逻辑

  - 跨任务经验复用设计：可落地到推荐系统的用户意图理解、多轮推荐流程中，将历史任务沉淀的Skill、上下文记忆复用给新任务，降低重复推理成本

  - 成本优化思路：同基座下比SOTA成本降低62.5%，可参考其任务拆分、资源匹配逻辑，优化大模型调用的单位成本，适合电商大促等大流量场景的Agent部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM驱动的Agent逐渐从孤立单领域任务转向长周期跨域工作流，但传统Agent套壳（含工具接口、上下文管理、执行策略等）手动开发难扩展，且单套壳和特定领域强耦合，无法支持跨域多Agent协作的能力复用。

### 方法关键点
- 架构层面：将每个模型+套壳的组合作为可独立调用的智能单元，支持内置专业Agent（研究、代码、设计、运维）和第三方Agent通过统一适配器接入生态
- 编排层：Host Agent负责目标拆分、子任务与专业Agent匹配、执行依赖建模为DAG，运行时前置校验依赖、调度就绪节点、处理执行异常、整合结果
- 自演化层：Skill Forge沉淀可复用的执行流程，Harness基因库支持套壳的重组优化，基于失败诊断自动迭代套壳策略，共享记忆库实现跨任务经验复用
- 理论层面：证明了在资源预算约束下，满足互补能力、兼容交接、有限误差三个条件时，组合系统的任务覆盖范围可超过单个Agent的能力上限

### 关键结果
对比同基座下各领域SOTA Agent系统，覆盖5类场景：多Agent编排任务Exact Match比最优基线高10.4~10.5pp；运维场景成功率提升17.6pp，单案例成本降低62.5%；代码任务SWE-bench Pro解决率提升2pp；设计任务ArtifactsBench得分最高提升2.8分。

最值得记住的一句话：多Agent协作的收益核心不是简单堆Agent数量，而是要通过明确的依赖契约、可演化的模块化套壳、低成本的经验复用，在可控的资源预算下拓展任务能力边界。
