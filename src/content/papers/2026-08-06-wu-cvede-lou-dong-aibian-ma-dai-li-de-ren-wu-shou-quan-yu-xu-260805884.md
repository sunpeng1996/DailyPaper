---
title: 'The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and
  Authority in AI Coding Agents'
title_zh: 《无CVE的漏洞：AI编码代理的任务授权与权限持续缺口管理》
authors:
- Shayell Aharon Salomon Amir Shaked Matan Noga
affiliations:
- Bluebear Security
arxiv_id: '2608.05884'
url: https://arxiv.org/abs/2608.05884
pdf_url: https://arxiv.org/pdf/2608.05884
published: '2026-08-06'
collected: '2026-08-08'
category: Agent
direction: AI Agent 安全风险管控体系建设
tags:
- Agent Security
- Vulnerability Management
- Authorization
- Least Privilege
- Runtime Governance
one_liner: 提出Agent姿态漏洞(APV)抽象，可系统化管理AI代理权限与控制的持续安全风险
practical_value: '- 部署业务侧Agent（如电商选品、文案生成、客服Agent、推荐系统调度Agent）时可复用APV抽象，统一管理跨组件的权限过大、授权边界模糊等长期安全风险，无需等CVE披露再响应

  - 可直接复用6种APV常见模式、漏洞生命周期和关闭矩阵，搭建业务Agent的权限管控基线，降低越权操作、数据泄露等风险

  - 做Agent运行时治理时，可参考APV的任务关联逻辑，为不同任务场景动态分配最小权限，避免单一固定权限带来的持续安全隐患'
score: 5
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Agent安全框架仅覆盖单次事件的权限、授权风险，无法管理跨组件、长期存在的部署态Agent持续安全缺口，且这类风险不属于传统CVE覆盖的产品缺陷范畴，缺乏统一管理抽象。
### 方法关键点
Agentic Posture Vulnerability（APV）作为任务条件下的漏洞管理抽象，将不同任务下的运行时风险表现关联到不变的安全姿态，明确了APV的定义、6种常见模式、全生命周期、最小记录字段、管控关闭矩阵，同时划清与CVE、OWASP过度权限等现有概念的边界。
### 关键结果
提供可落地的APV治理工具设计方向和可验证研究议程，可直接补充现有Agent安全管控体系，填补非产品缺陷类Agent安全风险的管理空白。
