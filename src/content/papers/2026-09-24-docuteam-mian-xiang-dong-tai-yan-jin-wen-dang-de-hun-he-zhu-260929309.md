---
title: 'DocuTeam: Mixed-Initiative Multi-Agent Discussions around Evolving Documents'
title_zh: 《DocuTeam：面向动态演进文档的混合主动式多Agent讨论系统》
authors:
- Heechan Lee
- Juhyeon Choi
- Tae Soo Kim
- Juho Kim
- Joseph Seering
affiliations:
- KAIST
- Seoul National University
- SkillBench
arxiv_id: '2609.29309'
url: https://arxiv.org/abs/2609.29309
pdf_url: https://arxiv.org/pdf/2609.29309
published: '2026-09-24'
collected: '2026-09-27'
category: MultiAgent
direction: 多Agent人机协作 · 混合主动交互
tags:
- MultiAgent
- Human-AI Collaboration
- Mixed-Initiative Interaction
- Document Collaboration
- Proactive Agent
one_liner: 提出锚定动态文档区域的混合主动多Agent讨论系统，降低用户编排负担同时提升开放任务产出质量
practical_value: '- 可借鉴Agent主动触发逻辑：在电商文案编辑、推荐策略评审等场景，配置Agent监控业务内容变更，自动触发合规校验、卖点优化、效果预估等多Agent讨论，无需运营/算法同学主动发起，降低操作门槛

  - 复用「讨论锚定业务对象」的设计：将多Agent讨论直接绑定到商品、搜索词、推荐策略等具体业务单元，而非全局会话，方便从业者快速定位上下文，避免讨论与业务实际脱节

  - 落地混合主动分级干预机制：支持用户不同粒度的讨论控制，从直接发消息介入、调整Agent角色权重到完全放权自主讨论，适配不同业务场景的可控性要求

  - 参考讨论结论一键落地的设计：支持将Agent讨论产出的优化点一键/拖拽应用到对应业务内容（如商品详情、活动规则、推荐话术），减少上下文切换成本，提升工作效率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有多Agent讨论系统存在两类局限：要么仅支持单Agent主动反馈，无Agent间自主讨论能力；要么多Agent讨论完全依赖用户主动发起、逐轮编排，且与用户正在编辑的工作文档割裂，用户需手动桥接会话与工作内容，交互负担重，无法充分发挥多Agent协作的价值。

### 方法关键点
- 设计3种任务导向的讨论模式：Idea（创意发散）、Discussion（方案权衡）、Evaluation（效果校验），匹配开放任务不同阶段的需求
- 实现双触发机制：支持用户拖拽Agent到文档指定区域发起讨论；同时Agent自动监控文档变更，通过2s防抖过滤无效修改后，多Agent独立为三类讨论模式评分，对应模式平均分超0.75阈值则自动启动讨论
- 讨论引擎由Moderator Agent统一调度：自动推断讨论目标、指派下一个发言Agent、判断是否需询问用户补充信息、是否达成讨论目标；每个Agent携带独立角色Profile与长时记忆，发言遵循Issue/Claim/Support/Rebut/Question五类动作规范
- 交互层面所有讨论锚定对应文档区域，提供分级摘要，支持拖拽讨论结论直接插入文档，用户可通过发消息、增减Agent等方式灵活调整讨论方向

### 关键实验
采用N=20的被试内研究，对比基线为无Agent主动触发、无文档锚定的常规多Agent讨论系统，任务为开放型活动策划。核心结果：产出方案的新颖度提升19.4%、相关性提升18.7%、特异性提升42.5%，均达统计显著性；用户发送的讨论控制消息减少46%，文档修改次数提升39%，整体认知负荷与基线无显著差异。

### 核心结论
将多Agent讨论与用户正在操作的业务资产（文档/商品/策略）深度绑定，让主动交互、自主讨论、结论落地形成闭环，是大幅降低多Agent使用门槛、同时提升业务价值的核心路径。
