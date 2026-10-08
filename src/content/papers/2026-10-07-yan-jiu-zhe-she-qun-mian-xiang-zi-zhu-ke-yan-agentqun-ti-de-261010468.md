---
title: 'A Society of Researchers: Designing Institutions for Populations of Autonomous
  Research Agents'
title_zh: 研究者社群：面向自主科研Agent群体的制度设计
authors:
- Ali Asaria
- Deep Gandhi
- Tony Salomone
affiliations:
- Transformer Lab, Canada
arxiv_id: '2610.10468'
url: https://arxiv.org/abs/2610.10468
pdf_url: https://arxiv.org/pdf/2610.10468
published: '2026-10-07'
collected: '2026-10-08'
category: MultiAgent
direction: 多智体 · Agent集群治理与制度设计
tags:
- Multi-Agent
- Agent Society
- Institutional Design
- Autonomous Research Agent
- Resource Allocation
one_liner: 提出基于科研社群制度的万级Agent集群组织框架，通过竞争式算力分配实现自主科研
practical_value: '- 大规模Agent集群可借鉴「给目的而非明确目标+制度约束而非指令」的设计，避免LLM Agent目标博弈与重复劳动，适配广告文案、内容生成等创意类多Agent协同场景

  - 可复用竞争式资源分配机制：通过RFP（需求征集）+独立评审+算力授信的方式分配集群资源，比中心式调度更适配分散的探索类任务，如推荐新场景探索、算法优化方向试错

  - 针对LLM Agent同质化问题，可参考角色分层设计（开拓者/追随者/校验者）+异步信息同步机制，既保留探索多样性，又避免过早收敛到局部最优'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前科研Agent部署已走向万级集群规模，但现有架构（单项目流水线、中心式规划、无约束Swarm）要么无法跨项目扩展，要么容易自发形成不可控的隐式组织、出现95%以上的重复劳动，必须主动设计显性制度来规范大规模Agent集群的协作，对齐顶层目标。

### 方法关键点
1. 六大设计原则：给Agent目的而非具体目标、建制度而非写指令、通过资源分配而非任务指派治理、保留群体多样性、设立独立校验制度、持久化身份与记忆
2. 三层组织架构：底层为项目执行Agent组，中层为带稳定身份、角色、风险偏好的PI（首席研究员）Agent，上层人类管理者仅通过发布需求、分配算力池、设定评审规则4个杠杆调控，不指派具体任务
3. 算力分配闭环：发布需求公告→PI自主申报提案→独立评审团从方法可行性、投入产出比、创新性3个维度独立打分→择优发放算力授信→成果存入公共知识库，负向结果也计入贡献

### 关键实验
部署包含10000个Agent的Research City，仅给定「优化大模型预训练效率」的方向，无具体任务指派；最终集群自发产出的预训练方案实现同等质量下降低30%算力消耗，同时完整产出负向结果、争议结论等科研产出，全程无人类干预任务分配。

### 最值得记住的一句话
大规模Agent集群一定会自发形成组织，与其等它长出不可控的隐式规则，不如主动设计明确的制度来对齐目标。
