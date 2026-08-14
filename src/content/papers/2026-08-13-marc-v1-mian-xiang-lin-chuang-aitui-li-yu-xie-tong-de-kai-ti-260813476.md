---
title: 'MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and
  Coordination'
title_zh: MARC v1：面向临床AI推理与协同的开源多智能体框架
authors:
- Saisha Shetty
- Satvik Tripathi
- Austin Lin
- Colin Zhao
- Theodore Kim
- Don Enwerem
- Jacinta Arnold
- Shahriar Faghani
- Tessa S Cook
affiliations:
- University of California, Davis
- University of Pennsylvania
- Drexel University
arxiv_id: '2608.13476'
url: https://arxiv.org/abs/2608.13476
pdf_url: https://arxiv.org/pdf/2608.13476
published: '2026-08-13'
collected: '2026-08-14'
category: MultiAgent
direction: 多智能体编排 · 开源通用推理框架
tags:
- Multi-Agent
- Orchestration
- Prompt Automation
- Model-Agnostic
- Open Source
one_liner: 推出支持自动生成Agent提示、无代码配置的开源多智能体推理协调框架
practical_value: '- 可复用多智能体编排思路，将推荐/广告全链路拆分为抽取、推理、生成、评估等角色专属Agent，便于分模块排障优化

  - 可借鉴Decomposer模块设计，基于业务自然语言描述自动生成各Agent专属prompt，大幅降低非技术人员prompt工程成本

  - 可参考YAML全配置、无代码修改的部署设计，同时支持API调用与本地CPU部署的架构，适配不同业务资源场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有单体LLM提示模式在复杂领域推理场景下存在可解释性差、故障难以定位的问题，同时定制化prompt工程门槛高，无编程经验的领域人员难以快速落地。
### 方法关键点
1. 采用确定性多智能体编排替代单体LLM推理，拆分出信息抽取、逻辑推理、答案生成、效果评估四类角色专属Agent，显式传递上下文、中间输出全链路可追溯，支持分阶段故障归因
2. 内置Decomposer模块，仅需输入自然语言形式的任务描述，即可自动生成各Agent的任务专属prompt，无需人工做prompt工程
3. 模型无关，同时支持API形式调用大模型与本地CPU兼容部署，全流程通过YAML配置即可调整，无需修改代码
### 关键结果
框架已完全开源，适配无编程经验的领域专家快速使用，可直接迁移至电商、广告等各类垂直领域的复杂推理任务落地
