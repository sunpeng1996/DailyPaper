---
title: 'ABRA: Agent-Bound UI for Human-Agent Communication beyond Chat with Reusable
  Views'
title_zh: ABRA：支持可复用视图的Agent绑定UI 实现超越聊天的人机交互
authors:
- Seon Gyeom Kim
- Hannah Kim
affiliations:
- Megagon Labs
arxiv_id: '2610.30780'
url: https://arxiv.org/abs/2610.30780
pdf_url: https://arxiv.org/pdf/2610.30780
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 人机交互与多智体协作优化
tags:
- Human-Agent Interaction
- Multi-Agent Collaboration
- UI Framework
- Generative UI
- LLM Agent
one_liner: 提出解耦可复用交互结构与任务语义的Agent-Bound UI模型，支撑人机/多Agent高效协作
practical_value: '- 电商导购Agent可复用这套交互范式：将通用组件（商品卡片、对比表、选购决策树）与任务语义绑定，用户直接点击/编辑组件即可传递意图，替代纯chat输入降低交互门槛

  - 多Agent协作场景可复用语义绑定发布机制：不同角色Agent（召回Agent、排序Agent、权益Agent）创建的画布内容通过统一referent绑定同步，避免信息重复与语义歧义

  - 推荐系统用户反馈采集可借鉴交互分层设计：本地操作（勾选、排序、筛选）直接前端生效，涉及个性化调整的操作（偏好修改、候选扩充）提交给Agent处理，兼顾响应速度与个性化效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前人机Agent交互以纯聊天为核心，存在输出端多模态结构化、输入端仅支持自然语言的不对称问题，用户难以高效表达与可视化内容绑定的模糊意图；现有生成UI要么生成即固定难以复用，要么绑定特定任务无法跨场景适配，无法支撑多Agent共享交互语义的协作需求。

### 方法关键点
- 核心架构分三层：可复用交互视图（预设graph/table/text/display四类通用视图，明确定义元素、本地操作与需Agent处理的操作边界）、语义绑定机制（Agent为视图元素绑定任务专属语义，本地操作前端直接执行，需推理的操作提交给画布所属Agent解析）、语义发布机制（绑定规则作为共享画布状态公开，所有参与者均可读取语义规则并执行对应操作）
- 实现ABRA原型，通过结构化tool call封装画布创建、读取、更新、操作、关闭全生命周期接口，不绑定特定Agent框架，兼容多SDK开发的Agent接入

### 关键实验
测试4款LLM-backed Agent（Claude Opus 4.8/Haiku 4.5、GPT-5.4/GPT-5.4-mini）在三类任务的表现：画布创建通过率最高97.8%（GPT-5.4），结果解析通过率最高100%（Haiku 4.5、GPT-5.4），跨Agent调用通过率最高100%（Claude Opus 4.8）；小模型存在明显短板，GPT-5.4-mini跨Agent调用通过率仅66.7%，多因操作类型选择错误导致。

最值得记住的一句话：将交互结构与任务语义解耦并公开语义绑定规则，是让可视化交互成为人机、多Agent间通用协作语言的核心前提。
