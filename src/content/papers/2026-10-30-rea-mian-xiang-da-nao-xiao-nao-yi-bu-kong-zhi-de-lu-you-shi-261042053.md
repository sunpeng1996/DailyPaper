---
title: 'REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control'
title_zh: REA：面向大脑-小脑异步控制的路由式具身Agent运行时
authors:
- Pengfei Zhou
- Yixing Ma
- Zhengfeiyang Zhang
- Haoyuan Chen
- Zhenglin Wan
- Hexin Wang
- Wangbo Zhao
- Yang You
affiliations:
- National University of Singapore
- InfRec, Cardinal AI Lab
- University of California, Berkeley
- The University of Tokyo
- Hong Kong University of Science and Technology
arxiv_id: '2610.42053'
url: https://arxiv.org/abs/2610.42053
pdf_url: https://arxiv.org/pdf/2610.42053
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 具身Agent 双系统异步协调架构
tags:
- Embodied Agent
- LLM
- Runtime
- Dual-System
- Routing
- Asynchronous Control
one_liner: 提出三级异步路由运行时，协调慢LLM大脑与快执行策略，无阻塞提升具身任务表现
practical_value: '- 可复用三级异步架构做LLM+业务系统协同：将LLM（System2）放在离线策略生成/边界校验环节，快规则/模型（System0）负责实时执行，中间加路由层（System1）完全避免LLM阻塞线上链路，适合搜索推荐实时排序、广告文案生成等低延迟场景

  - 路由层Route Memory设计可直接复用：离线预统计不同策略（如不同召回源、不同文案生成模型）的历史成功率/耗时，线上查表选最优策略，比在线调用LLM选策略延迟更低、效果相当

  - 边界触发校验门可迁移到业务容错场景：仅在单段策略执行完成后调用LLM做结果校验，失败则按预设升级阶梯切换策略，既覆盖静默失败，又控制LLM调用成本，适合电商链路校验、推荐内容合规检测等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型高层推理能力强但延迟高、成本高，无法支撑细粒度实时控制；VLA、规则等快执行策略响应速度快但泛化性差，现有双系统架构要么快执行链路阻塞等待大模型决策，要么仅在策略报错时触发大模型，漏过大量无报错的静默失败，且不同类型策略缺乏统一运行时难以横向对比优化。

### 方法关键点
- 三级分层架构：System2（大脑）为大模型，仅负责离线生成候选策略、在线做结果校验；System1（路由层）负责策略调度、异步协调，完全不阻塞执行链路；System0（小脑）为各类快执行策略（代码、VLA、控制器），按原生速率独立运行
- 三个核心设计：① Route Memory：离线预统计各策略的任务成功率、耗时，线上查表选最优策略，无需在线调用大模型；② 边界触发校验门：仅在单策略执行完成后调用System2校验结果，识别静默失败，避免反复触发大模型；③ 共享预算升级阶梯：失败后从当前状态执行下一级策略，全局共享步骤/时间预算，避免无限重试
- 统一运行时接口，支持代码、VLA等不同类型策略接入，跨模拟器和真实机器人通用

### 关键结果
在60个LIBERO-Pro任务共3000个测试episode上，成功率达95.9%，超过最优单策略基线（94.7%），控制步数减少25%，控制时间减少17%；在RoboTwin 2.0共100个episode测试中，VLA策略下成功率84%，VLA+代码混合策略下达86%，超过最优单VLA基线MEDex的80%；在BEHAVIOR-1K、真实Unitree G1人形机器人、AlohaMini2机械臂上均取得最优效果。

**最值得记住的结论：大模型最好的位置是离线生成策略、或在策略执行边界做校验，永远不要让它出现在实时执行的关键路径上**
