---
title: 'DeepTrans Studio: Turning Expert Interventions into Shared Team Knowledge
  in Agentic Translation Workflows'
title_zh: DeepTrans Studio：将智能体翻译工作流的专家干预转化为团队共享知识
authors:
- Ziyang Lian
- Qingya Zhang
- Hao Wang
- Huiwen Xiong
- Qi Yang
- Lingyi Meng
- Xiaoyi Gu
- Rui Wang
affiliations:
- 上海大学
- 华东师范大学
- 上海交通大学
arxiv_id: '2606.29727'
url: https://arxiv.org/abs/2606.29727
pdf_url: https://arxiv.org/pdf/2606.29727
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent 人机协作工作流优化
tags:
- Agentic Workflow
- Human-AI Collaboration
- Team Memory
- Workflow Interception
- Collaborative System
one_liner: 搭建带节点拦截、共享团队记忆的协作翻译Agent工作流，实现专家修正的跨成员复用
practical_value: '- Agent工作流可引入高风险节点拦截机制，在广告文案生成、合规审核等高风险场景暂停流供人工干预，避免错误下发

  - 可复用共享团队记忆设计，将专家审核结果（如合规禁用词、商品类目标准）沉淀为可检索先例，减少重复审核、跨团队标准不一致问题

  - 可借鉴问责溯源链路设计，对内容生成、推荐排序的全链路决策留痕，满足电商/广告的合规审计需求'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
高风险领域专业翻译为强团队协作场景，现有LLM翻译工具多为单用户端到端设计，专家单次修正仅留存于本地会话，无法跨成员跨项目复用，导致团队重复解决同类术语冲突、法律歧义问题，既增加重复劳动，也存在术语漂移、责任追溯缺失的风险。

### 方法关键点
- 设计节点拦截层：Agent工作流在术语冲突、法律模态歧义等高风险节点自动暂停，暴露中间输出给专家审核修正，避免错误向下游传播
- 共享团队记忆模块：将专家审核通过的干预决策（含修正结果、决策 rationale）同步到「活词典」作为先例，后续同场景下主动检索推送，对齐全团队决策标准
- 问责追溯链路：全链路记录模型建议、人工修正、先例复用的来源，支持跨角色审核决策链，满足高合规要求
- 状态同步协作 workspace：多角色共享文档状态（拦截、已签收等），无需从本地聊天记录重构决策上下文

### 关键结果
针对12位专业翻译的形成性走查显示，所有参与者均认可节点拦截原因查看、修正依据记录、修正结果跨队友可见的价值，资深翻译反馈个人干预可作为全团队的一致性锚点，将个人经验转化为团队共享知识资产。

### 核心洞见
AI辅助工作的核心价值不是替代专家，而是把专家的单次干预转化为可复用的团队知识资产，实现1份投入N份复用。
