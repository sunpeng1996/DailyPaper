---
title: 'FlowState: Execution State as Memory for Long-Horizon LLM Agents'
title_zh: FlowState：面向长程LLM Agent的执行状态内存框架
authors:
- Minghao Li
- Bangyan Li
- Zifan Wang
- Yulong Li
- Hu Xu
- Gan Zhang
- Jingtong Wu
- Wenqiang Xu
affiliations:
- Ant International, Ant Group
arxiv_id: '2609.34565'
url: https://arxiv.org/abs/2609.34565
pdf_url: https://arxiv.org/pdf/2609.34565
published: '2026-10-07'
collected: '2026-10-21'
category: Agent
direction: 长程LLM Agent · 内存架构优化
tags:
- Long-Horizon Agent
- Agent Memory
- Execution State
- Token Efficiency
- Progressive Retrieval
one_liner: 将执行状态作为跨请求可复用内存，结合增量更新与渐进访问提升长程Agent性能并降低token消耗
practical_value: '- 电商多轮导购、售后客服等业务Agent可直接复用ISU增量状态更新机制，仅维护当前请求的用户偏好、订单信息、规则约束等状态节点，无需全量重构状态，大幅降低上下文长度

  - PSA按需关联拉取历史状态的设计可替代传统固定召回的RAG方案，通过状态节点的关系链回溯历史证据（如用户历史议价记录、关联的退款政策），避免关键信息遗漏同时减少无效token占用

  - 论文提出的5类状态语义分类（用户偏好、环境知识、实体属性、Agent判断、执行产物）可直接复用在业务Agent的状态设计中，明确不同信息的存储、更新、访问规则'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent任务（如多轮导购、跨会话旅行规划、复杂数理推导）需要持续复用历史交互信息，但全量保留历史会导致token成本飙升、上下文噪声干扰决策，压缩历史则容易丢失后续需要的关键细节，传统RAG类内存方案又常出现关键信息召回不及时的问题，亟需统一的内存架构平衡任务性能与推理成本。

### 方法关键点
- 持久化执行状态分三层设计：全量存储状态节点、关联关系、原始工具返回的持久化状态仓库，仅存ID与摘要的轻量历史索引，以及当前推理用的活跃状态，隔离持久化存储与按需访问
- Incremental State Update（ISU）：每次推理仅增量对当前请求的状态节点执行增/改/删操作，无需全量重构状态
- Progressive State Access（PSA）：推理过程中按需通过历史索引或已暴露状态的关联关系，拉取对应历史状态及原始证据，避免全量加载历史
- 执行循环中每次LLM输出同时包含状态增量、历史访问请求、执行决策，三者联动更新状态后再执行后续动作

### 关键实验
在MemoryArena（捆绑购物、团体旅行规划、数理推理）和τ3-Bench（航空服务、零售服务）两个长程任务基准上测试：与同基座DeepSeek-V4-Flash全上下文基线相比，MemoryArena平均成功率提升4.55pp，token消耗降低43.2%；τ3-Bench平均通过率提升13.95pp，token消耗降低40.6%；在DeepSeek-V4-Flash、GPT-5.6-terra、Qwen3.5-397B三种基座上均稳定获得性能提升，同时实现28.3%~56.3%的token节省。

**最值得记住的一句话**：长程Agent内存不能只依赖静态压缩或固定召回，将执行状态作为可追溯关联关系的内存单元、动态按需披露才能同时兼顾效果与成本。
