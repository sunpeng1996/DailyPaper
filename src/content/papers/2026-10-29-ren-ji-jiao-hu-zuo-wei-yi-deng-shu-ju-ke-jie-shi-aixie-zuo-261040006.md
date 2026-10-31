---
title: 'Human--AI Interactions as First-Class Data: A Formal Interaction Model and
  Runtime for Explainable AI Collaboration'
title_zh: 《人机交互作为一等数据：可解释AI协作的形式化模型与运行时》
authors:
- Michela Taufer
- Kin Ng
- Ian Lumsden
- Aashish Pandey
- Rajasi Gore
- Angelina Ju
- Sukanya Moudgalya
- Ewa Deelman
- Sai Swaminathan
affiliations:
- University of Tennessee
- University of Southern California
arxiv_id: '2610.40006'
url: https://arxiv.org/abs/2610.40006
pdf_url: https://arxiv.org/pdf/2610.40006
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: 人机协同Agent 交互数据结构化建模
tags:
- Human-AI-Interaction
- HAIDL
- Agent-Middleware
- Structured-Interaction-Data
- LLM-Assistant
one_liner: 推出人机交互描述语言HAIDL及配套中间件，实现全链路交互的结构化存储查询与分析
practical_value: '- 可复用HAIDL的结构化建模框架，把电商导购Agent、推荐系统和用户的全链路交互（query、上下文、推荐结果、用户反馈等）存储为可查询结构化对象，解决现有交互日志零散不可追溯的问题

  - 可参考HAIDL-X中间件架构设计，在大模型推荐/导购Agent业务系统中新增交互数据采集层，统一对接不同LLM服务商，同时沉淀全量交互数据用于后续用户行为分析、模型迭代

  - 可借鉴交互数据映射用户行为指标的思路，基于结构化交互数据自动计算用户engagement、求助行为、满意度等指标，替代传统零散埋点统计'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前嵌入各类工具的AI助手多将人机交互视为临时prompt-响应交换，未作为持久数据产品留存，阻碍交互的可复现性、可解释性、回溯分析及AI自适应优化。

### 方法关键点
1. 形式化人机交互描述语言HAIDL参考Backus-Naur Form设计语法，将每次交互编码为结构化对象，覆盖计算上下文、用户请求、prompt payload、AI响应、用户反馈、问题上下文、provenance、模型元数据等全维度字段；
2. JupyterLab适配中间件HAIDL-X实现用户-机器人状态捕获、上下文prompt构建、多AI服务商对接、反馈收集、结构化交互数据持久化全链路能力；
3. 上层学习层基于交互对象与notebook执行轨迹，量化用户engagement、表现、求助行为、错误导向使用、用户persona等可复现行为指标。

### 关键结果
HAIDL-X实现了人机协同交互数据的结构化、可查询、可重放、可分析，为可解释AI协作提供标准化底层支撑。
