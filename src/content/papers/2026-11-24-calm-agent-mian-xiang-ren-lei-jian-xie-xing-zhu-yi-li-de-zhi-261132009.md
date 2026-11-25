---
title: 'Calm Agent: Reframing Agent Interaction around Intermittent Human Attention'
title_zh: Calm Agent：面向人类间歇性注意力的智能体交互框架
authors:
- Dian Jin
- Zixun Fu
- Guan Wang
- Yancheng Yuan
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.32009'
url: https://arxiv.org/abs/2611.32009
pdf_url: https://arxiv.org/pdf/2611.32009
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent交互优化 · 间歇性注意力适配
tags:
- AI Agent
- Human-Agent Interaction
- Calm Technology
- Generative UI
- Attention Optimization
one_liner: 提出适配人类间歇性注意力的Calm Agent框架及Orvlet原型，降低智能体交互的注意力占用
practical_value: '- 电商智能导购、客服Agent可复用Delegate/Adjust/Check三交互模式设计：用户用自然语言委托比价、降价监控等需求后，可通过固定控件快速调整参数、通过边缘胶囊轻量化查看状态，无需打断浏览/下单主流程，降低交互成本

  - 持久化任务表示+后台独立执行的架构可直接迁移到电商自动化任务场景：用户授权的补货提醒、订单物流监控等任务可在后台持续运行，无需用户保留对应页面，仅用轻量UI同步状态

  - 可借鉴注意力分级请求策略：将Agent干预按紧急度分为静默提示、弱提醒、强弹出三个等级，仅高优先级任务（如库存不足待确认）触发强提醒，避免过度打扰用户，降低负向反馈率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI Agent已可独立完成多步辅助任务，但用户与Agent交互时需要切换上下文、重读历史会话、重新表述需求，会大量占用主任务注意力，频繁切换还会增加额外认知负担。现有Agent交互设计未针对用户间歇性低注意力投入的场景做优化，无法平衡后台任务持续执行和低干扰交互的需求。

### 方法关键点
- 提出3条核心设计原则：交互间隙持久化任务状态与执行上下文、支持短路径针对性交互、用户回归时直接展示可理解状态与可操作控件
- 定义3种按需交互模式：Delegate（自然语言下发/修改任务目标）、Adjust（直接操作预制控件调整参数）、Check（轻量化查看任务状态），三种模式共享同一套持久化任务表示⟨目标G,约束C,状态S,动作A,历史H⟩
- 配套实现桌面原型Orvlet：后台独立执行任务，边缘用悬浮胶囊展示任务状态，hover时展开卡片提供控件，非活跃状态自动半透明降低视觉干扰，支持多任务并行管理

### 关键结果
通过音乐控制、多时区时钟、GitHub星数监控、股价对比4个典型场景验证框架可行性，相比传统会话式Agent，用户查看任务状态、调整参数的操作路径缩短80%以上，无需重读历史会话即可直接完成操作。

### 最值得记住的一句话
面向辅助类任务的Agent设计核心是保护用户主任务注意力，让技术在注意力中心和边缘之间按需切换，而非强制用户适配Agent的交互逻辑。
