---
title: Role of Personality in Conversational Information Seeking
title_zh: 会话式信息检索场景下人格特征的作用研究
authors:
- Abdisalam Abukar
- Junchen Fu
- Chengli Zhai
- Joemon M. Jose
affiliations:
- University of Glasgow
- GAIR-Lab, University of Glasgow
arxiv_id: '2608.11164'
url: https://arxiv.org/abs/2608.11164
pdf_url: https://arxiv.org/pdf/2608.11164
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: 会话Agent · 人格适配优化
tags:
- Conversational Search
- LLM Agent
- Personality Adaptation
- User Study
- Trust Optimization
one_liner: 通过受控用户研究验证会话Agent人格需适配任务与用户特征，不存在全局最优人设
practical_value: '- 电商会话Agent可按场景配置默认人格：种草/旅行规划等探索场景用外向主动风格，保健品/3C咨询等高信任需求场景用严谨尽责风格，比价/订单查询等效率优先场景用中性风格，可直接提升用户体验

  - 可通过短周期交互或轻量问卷获取用户大五人格倾向性，动态适配Agent响应风格，能显著提升用户对Agent的信任度与委托意愿

  - 无需追求全局最优的统一Agent人设，给用户开放人格选择开关、或实现自动适配功能，用户接受度远高于固定单一人设'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的会话Agent已广泛应用于导购、咨询、规划等场景，但大多采用固定人设，业界对用户人格、助手人格、任务类型三者如何共同影响交互效果、用户信任的认知不足，缺乏可落地的人设适配规则。

### 方法关键点
- 基于GPT-4.1通过Prompt实现三种可控助手人格：外向（活泼主动、高参与度）、尽责（严谨有条理、重结构）、中性基线，固定底层模型仅修改系统提示词控制变量
- 覆盖三类典型信息检索任务：探索类（6天土耳其旅行规划）、决策类（600-800英镑手机选购）、高验证需求类（健康排毒方案评估）
- 采用组内对照实验设计，采集26名用户的大五人格得分、78组会话行为数据、交互前后问卷数据，通过Graeco-Latin-square方案平衡任务与助手顺序消除混淆

### 关键结果数字
- 三种人格助手行为差异显著：外向型回复平均146词，尽责型仅90词，尽责型下用户发言占比高35%、交互轮次高16%
- 任务-人格适配效果差异显著：旅行场景外向人格信任评分最高5.62，购物场景中性最高5.94，健康场景尽责型最高5.53，任务×人格交互效应p=0.037
- 用户与助手人格兼容时信任度提升明显，适配斜率b=0.648，p=0.019，90%以上用户支持开放人格选择或自动适配功能

### 核心结论
会话Agent的人格不是全局可优化的系统属性，而是需要结合任务场景、用户偏好动态调整的上下文敏感交互变量
