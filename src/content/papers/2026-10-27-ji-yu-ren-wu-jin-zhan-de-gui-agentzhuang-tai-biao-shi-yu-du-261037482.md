---
title: 'From Interaction to Capability: Task Advancement as State and Supervision
  for GUI Agents'
title_zh: 基于任务进展的GUI Agent状态表示与监督记忆框架
authors:
- Ziyang Chen
- Qian Li
- Chengwei Qin
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Shandong University
arxiv_id: '2610.37482'
url: https://arxiv.org/abs/2610.37482
pdf_url: https://arxiv.org/pdf/2610.37482
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: GUI Agent 长流程任务记忆优化
tags:
- GUI Agent
- Memory System
- Task State
- Skill Learning
- Long-horizon Task
one_liner: 提出任务进展记忆TAM，大幅提升GUI Agent长流程任务成功率并降低推理成本
practical_value: '- 做电商导购、订单处理等任务型Agent时，可借鉴任务进展状态设计：将已验证完成的子任务、已获取的用户/商品信息显式绑定到剩余任务的依赖上，避免跨应用/页面跳转时信息丢失、重复询问用户，提升交互体验

  - Agent技能沉淀可复用局部成功经验：无需等全流程任务成功才沉淀操作，只要局部子任务（如下单、改地址、查物流）验证通过，就抽象为包含输入、预期结果、验证条件的可复用算子，大幅提升技能积累效率

  - 大流量Agent业务可借鉴上下文精简逻辑：仅将已验证的进展、剩余任务依赖作为上下文输入，无需携带全量历史交互日志，实测可降低近40%的单任务token消耗，显著降低推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有GUI Agent记忆方案大多存储全量交互日志，或仅沉淀全流程成功的操作轨迹，在长流程跨应用任务中易丢失已获取的有效信息，失败任务中的有效子操作也无法复用，导致任务成功率低、推理token消耗高，难以落地到实际业务场景。

### 方法关键点
- 核心框架为Task Advancement Memory (TAM)，分为执行层和学习层双模块：执行层先将初始任务拆解为带依赖关系的需求图，每完成一个可验证的子需求（如获取到信息、操作成功返回确认）就更新任务进展状态，将已获取信息绑定到剩余子任务的依赖上，自动精简剩余任务范围
- 学习层采用进展监督机制：无论整体任务是否成功，只要局部子任务验证通过，就将对应的交互片段抽象为可复用算子，算子包含输入要求、预期结果、验证条件，和具体GUI操作路径解耦，适配界面迭代变化
- 配套证据缓存机制，存储子任务完成的可视化证据，避免上下文过长丢失关键信息，算子复用时优先匹配输入输出语义，再适配当前界面的操作路径

### 关键实验
在MobileWorld GUI-only跨应用任务集、SPA-Bench英文Level3单应用高难度任务集上测试，对比AWM、StructAgent、GUI-explorer、MemGUI-Agent等SOTA基线：MobileWorld上TAM成功率达34.2%，比最强基线高5.1pp，单成功任务生命周期token降低38.7%；SPA-Bench上成功率达57.0%，超过之前SOTA的53.7%。消融实验显示仅任务进展状态模块就能把基础Agent成功率从12.0%提升到28.2%。

**最值得记住的一句话：GUI Agent记忆不需要存储全量交互，围绕已验证的任务进展设计，既能提升长流程执行成功率，还能从失败任务里沉淀可复用技能，同时降低推理成本**
