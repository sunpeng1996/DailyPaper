---
title: 'Workflow as Knowledge: Semantic Persistence for LLM-Mediated Workflows'
title_zh: 工作流即知识：面向LLM驱动工作流的语义持久化框架
authors:
- Emanuele Quinto
- Carlo Andrea Rozzi
- Francesco Zanitti
affiliations:
- UNHCR
- CNR—Istituto Nanoscienze
- ZeLe & F ApS
arxiv_id: '2607.08740'
url: https://arxiv.org/abs/2607.08740
pdf_url: https://arxiv.org/pdf/2607.08740
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: Agent 工作流语义持久化架构
tags:
- Agent Workflow
- Semantic Persistence
- LLM Orchestration
- Knowledge Representation
- DSL
one_liner: 提出将LLM工作流全链路元素作为第一类语义对象持久化的概念模型，明确derive与infer的语义边界
practical_value: '- 可复用`derive`/`infer`二分法设计Agent工作流：把特征计算、规则匹配等确定性逻辑归为`derive`，LLM语义理解、打分等需要推理的步骤归为`infer`，既方便调试也可单独做结果溯源

  - 做电商Agent导购、广告审核这类强合规需求的工作流时，可参考核心语义对象schema，把审批记录、上下文快照、LLM推理结果都作为可查询的持久化对象存储，满足审计要求

  - 复用工作流实例持久化的思路做长周期Agent任务（如大促活动策划、用户全生命周期运营）的断点续跑，避免中断后重新执行全流程的资源浪费

  - 做Agent可观测性时，可参考该模型的依赖链接设计，明确每个决策的前置依赖（如用户输入、RAG召回结果、LLM推理结果），降低问题排查成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent工作流系统普遍将工作流定义、运行实例、中间结果分离存储，仅保留执行层面的 checkpoint 与日志，缺乏统一语义建模，导致历史工作流不可查询、决策溯源困难、中断恢复依赖特定执行环境，无法满足合规审计、知识复用、长周期任务运行的需求。

### 方法关键点
- 提出三层架构：底层运行时服务层提供模型适配、工具调用、存储能力；中间控制层为DSL执行器，负责上下文组装、结果校验、状态流转；上层语义层将所有工作流相关元素作为统一语义对象存储
- 明确`derive`与`infer`的语义边界：`derive`为确定性状态计算，可复现、可测试；`infer`为受控的LLM推理，必须声明上下文、预期返回类型、权限策略，且推理结果与上下文快照会被持久化
- 定义核心语义对象schema：包含工作流定义、工作流实例、推理记录、上下文快照、审批记录、依赖链接等10+类标准化对象，所有对象存储于共享知识基座，具备全局唯一ID与可查询的关联关系
- 参考Lisp符号式表达设计DSL，工作流定义本身为可解析的数据对象而非黑盒代码，支持跨执行环境的解析与复用

### 关键结果
本文为纯概念模型论文，暂未提供实证验证结果，仅通过77份工作流语料的扫描验证了核心词汇的覆盖度，证明设计的原语可覆盖绝大多数实际工作流的语义表达需求。

### 核心结论
不要只把工作流当成可执行的控制结构，要把它的定义、运行实例、产生的推理决策记录都当成可被检索、复用、审计的知识资产本身。
