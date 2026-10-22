---
title: 'Scriptorium: System Design and Implementation of a Multi-Human, Multi-AI Collaborative
  Digital Library Search Platform'
title_zh: Scriptorium：多人多AI协作数字图书馆搜索平台系统设计与实现
authors:
- Abbas Pirmoradi
- Milad Momeni
- Anna Chu
- Orland Hoeber
affiliations:
- University of Regina, Canada
arxiv_id: '2610.28929'
url: https://arxiv.org/abs/2610.28929
pdf_url: https://arxiv.org/pdf/2610.28929
published: '2026-10-20'
collected: '2026-10-22'
category: MultiAgent
direction: 多智体协作 · 协同搜索系统设计
tags:
- MultiAgent
- CollaborativeSearch
- SystemDesign
- WAG
- ExploratorySearch
one_liner: 开源带7个角色专业化Agent的多人多AI协作数字图书馆搜索平台，公开完整实现细节
practical_value: '- 多Agent分工设计可直接复用：做电商多人运营的选品/素材协作系统时，给Agent划分明确角色（query建议、竞品分析、合规校验、缺口提醒等），每个Agent仅输入最小必要上下文，既降低幻觉又提升可控性

  - 确定性前置校验trick可直接落地：调用LLM前先做规则化输入校验，不符合条件直接返回明确提示，不浪费token也避免无意义的模型调用，适配所有Agent类应用

  - Workspace Augmented Generation（WAG）思路可迁移到电商协作场景：仅把用户主动保存/丢弃的物料输入Agent，比通用RAG更贴合团队实际意图，减少无关信息干扰

  - 小流量场景可复用短轮询替代WebSocket的实现方案：原型验证/内部系统阶段无需复杂的长连接开发，3秒轮询足够支撑低并发需求，大幅降低开发成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有协同搜索系统要么仅支持多人协作能力，要么仅提供单人生成式AI辅助，未将全透明的多人协作状态与分角色多Agent辅助结合，无法支撑团队探索性搜索时的跨成员思路碰撞，也难以解决通用AI助手的幻觉、可信度低问题。

### 方法关键点
- 基于MERN栈实现，搜索层对接现有数字图书馆检索API，上层做多人协作层，所有用户操作（搜索、保存、删除、查看）全透明记录，采用软删除保留丢弃资源，作为Agent的负向反馈输入
- 多Agent采用Manager-Worker架构，7个Agent划分明确角色（查询建议、跨成员思路桥接、摘要、方法提取、引文格式化、证据批判、反方视角），每个Agent仅获取最小必要上下文，通过代码强制范围而非靠prompt约束
- 调用前加确定性前置校验，不满足输入条件直接返回提示，不调用LLM；路由支持显式@指定Agent或LLM自动路由，置信度低于0.7直接返回澄清提示，不盲猜
- 属于Workspace Augmented Generation（WAG）而非RAG，所有Agent输入仅来自团队主动操作产生的工作区数据，无外部检索结果干扰

### 关键实验
当前为技术报告，无上线实验数据，计划开展受控用户研究，对比有无协作 timeline、有无分角色Agent的两组用户的跨成员信息感知效率、AI信任度、搜索任务完成率。

### 核心结论
给AI分角色、限输入、加前置规则校验，比试图让单个通用大模型做所有事，可控性、可信度、实用性都高得多。
