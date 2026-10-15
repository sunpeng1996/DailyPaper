---
title: 'Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents'
title_zh: CarryOn：面向长程Agent的面向对象上下文运行时框架
authors:
- Yuchen Lu
- Julian McAuley
- Lei Zhang
affiliations:
- University of California San Diego
arxiv_id: '2610.18784'
url: https://arxiv.org/abs/2610.18784
pdf_url: https://arxiv.org/pdf/2610.18784
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 长程Agent · 上下文压缩与管理
tags:
- Long-Horizon Agent
- Context Management
- Object-Oriented
- LLM Agent
- Token Efficiency
one_liner: 提出面向对象的长程Agent上下文组织范式，提升任务效果的同时大幅降低token消耗
practical_value: '- 可复用上下文三分法架构：将历史拆分为已完成可复用对象、待执行上下文、近期交互尾段，适配电商导购Agent、搜索多轮问答Agent的长会话场景，避免重复处理已确认的用户需求、已展示的商品历史

  - 针对信息检索类长任务（如电商商品调研、竞品分析Agent），可借鉴fold机制，定期将已验证的检索结果、分析结论封装为可复用的信息载体，减少重复计算已消化的历史信息，降低token成本

  - 可复用环境校验逻辑：对外部存储的实体（如用户收藏夹、购物车、已生成的文案）绑定状态校验规则，无需保留生成这些实体的全量交互历史，仅保留引用和校验条件即可'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长程Agent执行任务时，已完成的任务进展（如生成的文档、检索到的有效结论）已沉淀在环境或输出中，但现有上下文管理方法仍依赖全量交互历史的压缩、检索或摘要，既产生大量冗余token消耗，还容易因摘要偏差导致与实际状态漂移，难以支撑超100轮以上的长任务执行。

### 方法关键点
- 采用三分式上下文视图：① 延续载体：封装可复用的任务对象，分为外部对象（如文件、文档）、信息产物（如检索结论）、环境状态三类，绑定复用条件和版本；② 执行上下文：保留未被载体覆盖的待执行目标、约束、未解决问题；③ 实时交互尾段：保留最近一次fold之后的全量交互
- 设计fold流水线：定期触发上下文折叠，依次完成候选载体识别、证据绑定与环境校验、载体与执行上下文联合更新、验证提交四个步骤，用折叠后的上下文替换覆盖的历史交互，无需重构过往进展

### 关键实验
在OSWorld 2.0长程桌面任务基准上，对比Claude Opus 4.7基线，partial得分从43.9%提升到49.7%（+5.8%），总token消耗降低51.9%，单任务成本降低35.9%；在BrowseComp-Plus长程检索基准上，准确率从49%提升到56%（+7%），总token消耗降低22.9%，任务越长成本优势越明显，500轮时成本比基线低34.1%。

最值得记住的一句话：长程上下文管理的核心不是压缩历史，而是围绕可复用的进展组织上下文，用已沉淀的状态替代产生状态的交互历史。
