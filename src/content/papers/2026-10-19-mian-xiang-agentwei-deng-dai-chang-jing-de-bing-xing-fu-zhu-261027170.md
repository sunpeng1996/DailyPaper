---
title: 'Too Long to Watch, Too Short to Leave: Designing for Agent Micro-Waits'
title_zh: 面向Agent微等待场景的并行辅助交互界面Sidecar设计
authors:
- Kevin Pu
- Anh Truong
- Michael Terry
- Carrie J. Cai
- Michael Xieyang Liu
- Savvas Petridis
affiliations:
- University of Toronto
- Google DeepMind
arxiv_id: '2610.27170'
url: https://arxiv.org/abs/2610.27170
pdf_url: https://arxiv.org/pdf/2610.27170
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 交互优化 · 微等待场景辅助
tags:
- Agent Interaction
- Micro-Wait
- Human-AI Collaboration
- Parallel Assistant
- User Experience
one_liner: 提出同屏并行辅助界面Sidecar，解决Agent微等待时用户注意力分散、效率低下的问题
practical_value: '- 电商导购Agent、多步生成式推荐场景（如生成定制化穿搭、旅游方案的分钟级等待）可复用同屏侧边辅助栏设计，无需用户切页，利用等待时间展示相关选项，降低用户跳失率

  - 等待期内容设计要和主任务强绑定：可同步展示主Agent隐含决策（如推荐商品时选的价位段）、可探索需求方向（如是否需要加防晒属性），既提升用户参与感又能提前收集补充需求，减少后续返工

  - 严格遵循非侵入式设计原则：所有等待期建议静默展示在侧边栏，不弹出强制交互内容，支持一键最小化，用户主动触发才展示详情，避免引起反感

  - 复用上下文共享机制：侧边辅助自动同步主Agent的对话、推理Trace、生成中内容，无需用户重复输入上下文，降低使用门槛'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Agent执行复杂多步任务时普遍存在10秒到数分钟的微等待区间，既长到用户不愿干等，又短到无法投入其他深度任务。现有场景下用户要么切换页面导致注意力碎片化、错过Agent运行反馈，要么干等浪费时间，亟需适配该场景的交互方案。
### 方法关键点
- 设计同屏侧边辅助界面Sidecar，与主Agent共享全量上下文（对话历史、推理Trace、生成中产物），用户可在不切页、不中断主Agent运行的前提下和Sidecar交互、脑暴、预存后续指令
- 实时从主Agent运行数据中提取两类卡片：Decision卡片展示Agent自主做出的用户未明确指定的决策，Explore卡片推荐和主任务相关的可探索方向，内容随运行进度动态更新、逐步精准
- 非侵入式设计：所有建议静默展示在侧边栏底部，不弹出强制交互内容，根据等待时长、任务进度动态调整建议数量，用户输入时暂停推送新建议避免打扰
### 关键结果
16人组内对照实验，基线为无Sidecar的原生Agent界面：等待期用户切页时间占比从35%降至13%，感知注意力碎片化评分从6.0降至3.0（7分制越低越好），感知等待期任务进度评分从2.0升至5.0，仅认知负荷从2.5升至5.0。
### 核心启示
Agent微等待场景的辅助设计核心是将用户空闲时间转化为对主任务的前置思考、需求补充，而非填充无关内容，同时要完全把交互主动权交给用户。
