---
title: 'SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration'
title_zh: SearchOS-V1：面向高鲁棒性开放域信息查询的多智能体协作框架
authors:
- Yuyao Zhang
- Junjie Gao
- Zhengxian Wu
- Jiaming Fan
- Jin Zhang
- Shihan Ma
- Yao Yao
- Weiran Qi
- Chuyan Jin
- Guiyu Ma
affiliations:
- Renmin University of China
- Ant Group
arxiv_id: '2607.15257'
url: https://arxiv.org/abs/2607.15257
pdf_url: https://arxiv.org/pdf/2607.15257
published: '2026-07-15'
collected: '2026-07-17'
category: Agent
direction: 多Agent协作 · 开放域信息搜索
tags:
- Multi-Agent
- Information Retrieval
- State Management
- Pipeline Parallelism
- Tool Middleware
one_liner: 提出将隐式搜索进度显式持久化共享的多Agent搜索框架，大幅提升长周期信息查询鲁棒性与效率
practical_value: '- 可复用SOCM状态管理设计：将Frontier Task、Evidence Graph、Coverage Map、Failure
  Memory作为全局共享状态，应用在电商导购Agent、商品信息聚合Agent场景下，可避免重复搜索、减少无效调用，提升信息采集准确性与效率。

  - 可直接复用流水线并行调度策略：释放的Agent槽位立即分配新任务，相比批调度降低24.3%端到端耗时、提升41.7%槽位利用率，适合大流量下多Agent服务调度，比如大促期间智能客服、搜索Query理解的并行处理。

  - 搜索工具中间件的工程架构值得参考：将上下文注入、证据抽取、停滞检测、预算管控等逻辑从Agent Prompt中抽离为系统级能力，无需依赖LLM自身遵守规则，可适配不同基座，大幅降低Agent工程迭代成本。

  - 分层技能库设计可直接迁移：将通用搜索策略和场景/站点专属访问技能拆分，技能复用可降低36.6%搜索耗时、39.1%搜索调用量，适合电商垂直场景沉淀专属技能，比如不同平台商品信息抽取、规则校验技能可单独维护。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具增强LLM做长周期开放域信息查询时，搜索进度完全隐藏在交互历史中，Agent容易丢失任务上下文、重复搜索陷入死循环，多Agent并行场景还会出现重复劳动、资源闲置问题，搜索预算浪费严重，输出的信息完整性、准确性不稳定。

### 方法关键点
- 任务抽象：将开放域信息查询建模为带来源引用的关系型Schema补全任务，每个填充字段都绑定来源URL和原文锚定片段，进度可量化、结果可溯源。
- 搜索导向上下文管理（SOCM）：全局持久化共享4类核心状态：Frontier Task任务池、Evidence Graph证据图谱、Coverage Map覆盖度地图、Failure Memory失败记忆，不同角色Agent按需获取状态投影，避免上下文冗余与版本不一致。
- 流水线并行调度：无需等待批次任务全部完成，释放的Agent槽位立即分配新的未覆盖Schema补全任务，大幅提升资源利用率和吞吐量。
- Search Tool Middleware Harness：拦截Agent与工具的全部交互，自动注入上下文、抽取绑定证据、检测停滞循环、管控搜索预算，无需Agent主动触发防护逻辑，适配不同基座LLM。
- 分层搜索技能库：拆分为全局编排技能、通用搜索策略技能、站点专属访问技能，可跨任务复用，减少重复试错。

### 关键实验
在WideSearch和GISA两个公开信息查询基准上，对比ReAct、Plan-and-Solve、A-MapReduce等单/多Agent基线：WideSearch上Item F1达80.3，超最优基线4.3个点；GISA上Set F1达76.5，超最优基线13.4个点；流水线调度相比批调度降低24.3%端到端耗时，引入分层技能后搜索耗时降低36.6%、搜索调用量降低39.1%。

**最值得记住的一句话**：长周期搜索的状态应该由系统维护，而不是反复从交互历史中推断。
