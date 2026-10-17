---
title: 'HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration'
title_zh: HTN-Orchestrate：面向多智能体编排的分层任务网络框架
authors:
- Yanchen Deng
- Jianguo Huang
- Yao Long Teng
- Yixuan Li
- Handuo Zhang
- Ning Wang
- Liangcai Su
- Xinyu Wang
- Bo An
affiliations:
- Nanyang Technological University, Singapore
- Apodex
arxiv_id: '2610.22195'
url: https://arxiv.org/abs/2610.22195
pdf_url: https://arxiv.org/pdf/2610.22195
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智能体 · 分层任务网络编排
tags:
- Multi-Agent
- Hierarchical Task Network
- Task Orchestration
- Task Decomposition
- Agent Planning
one_liner: 提出两层解耦的分层任务网络多智能体编排框架，兼顾全局规划结构与局部执行自适应
practical_value: '- 复杂多Agent业务任务可复用两层架构设计：上层用HTN维护子任务层级与依赖，仅当前置结果返回后再分解后续任务，适配电商用户复杂咨询、大促活动全链路调度等动态场景

  - 子任务执行层可参考单叶子任务专属Orchestrator设计，每个独立子任务分别调度信息收集、结果验证、内容生成等角色worker，配合AND语义向上汇总结果，降低多Agent调度复杂度

  - 长流程任务失败时可复用证据留存重规划机制：保留已验证的有效结论重构任务网络，避免重复执行已完成子任务，提升客服应答、商品调研等长周期任务的执行效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多智能体编排方案存在明显tradeoff：预定义工作流模式全局结构清晰，但任务分解在执行前就已固化，无法适配执行过程中产生的新信息；动态调度模式支持实时分配子任务，但不显性建模子任务层级和依赖关系，难以同时保障全局规划的结构性和局部执行的灵活性，复杂长周期任务的效果和效率都受限。
### 方法关键点
- 两层解耦架构：上层Planner维护分层任务网络（HTN），显性记录子任务层级、兄弟节点前置依赖，仅当前置子任务结果返回后再分解后续依赖任务，避免前期盲目规划；下层每个可执行叶子子任务分配专属Orchestrator，独立调度多worker完成本地执行，支持并行调度、结果验证和动态跟进
- AND语义结果汇总：所有子节点执行完成后才合成父节点结果，逐层向上传递直至根节点输出最终答案
- 证据留存式重规划：当前任务网络无法解决问题时，保留已验证的有效结论重构新的任务网络，避免重复执行已完成的子任务
### 关键实验
在BrowseComp（网页检索）、SUPERChem（化学推理）等5个跨领域基准上，以DeepSeek-V4.1-Flash为基座，对比ReAct、Agent Team、DeepSeek Harness基线：BrowseComp准确率达89.73%，超Agent Team 2.45个百分点；SUPERChem准确率73.44%，超Agent Team 4.69个百分点，效果接近GPT-5.6 Sol等前沿闭源模型。
### 核心结论
多智能体系统的性能上限不仅取决于基座模型能力，分层解耦的编排架构可以用更小的开放基座模型实现媲美大参数闭源模型的效果
