---
title: Toward Continuous Assurance for the Democratization of AI Agent Creation in
  Industry
title_zh: 面向工业界平民化AI Agent开发的持续可靠性保障框架
authors:
- Natan Levy
- Harel Berger
affiliations:
- 希伯来大学
- 阿里尔大学
arxiv_id: '2607.21495'
url: https://arxiv.org/abs/2607.21495
pdf_url: https://arxiv.org/pdf/2607.21495
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 平民化开发可靠性保障
tags:
- AI Agent
- Continuous Assurance
- Agent Reliability
- Low-Code Agent
- Agent Governance
one_liner: 为非技术用户搭建的企业级AI Agent提供轻量化持续保障方案，覆盖依赖校验、契约管理与全生命周期治理
practical_value: '- 企业内部低代码Agent平台可直接复用9类故障分类与对应校验规则，覆盖模型、工具、RAG、权限、语义漂移等常见故障点

  - Agent上线流程可新增readiness契约环节，业务方仅需提供任务成功样例、依赖清单、所有者信息，平台自动转换为周期性巡检规则，无需业务方掌握运维知识

  - 电商场景下业务人员搭建的运营Agent、商品分析Agent、客服Agent，可按业务criticality分层设置巡检强度，低危Agent用轻量检查，交易/客户相关Agent加严校验并配置escalation路径

  - 可参考原型实现思路，基于LLM开发轻量Agent巡检工具，自动识别Agent依赖、分类故障、输出可直接执行的修复建议，大幅降低运维成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
企业非技术用户（运营、法务、财务等）通过低代码/无代码/对话式平台快速搭建Agent，催生了大量业务关键型Agent，但这类Agent依赖动态变化的模型、工具、RAG源、权限、外部API，极易出现无告警的静默降级。传统DevOps/MLOps/AgentOps要求工程背景，普通业务用户无法使用，导致大量Agent无人运维，存在严重可靠性风险。

### 方法关键点
- 提出平民化长期运行Agent的9类故障分类，覆盖模型依赖、工具调用、RAG、权限凭证、输出契约、工作流调度、语义降级、所有权、治理维度，每个维度匹配对应就绪校验规则
- 落地五要素持续保障框架：依赖映射自动识别Agent运行所需所有资源；就绪契约将业务方的任务级要求转换为可执行校验条件；调度检查在定时或依赖变更时自动执行校验；诊断模块按故障分类定级影响；生命周期治理明确所有者、上报路径、下线规则
- 实现原型巡检器，可基于Agent配置、任务样例、运行日志自动生成就绪契约、分类故障、输出修复建议，区分「确认发现/可复现风险/未知项」三类结论，避免过度断言无证据的状态

### 关键实验
基于6个真实企业Agent故障场景做评估，原型巡检器100%匹配预期故障分类，能准确区分确认故障/未知状态，全部输出可落地的修复建议，无过度断言未提供证据的配置项。

### 核心结论
平民化Agent的可靠性远不止模型准确率问题，80%以上的实际故障来自依赖变化、权限过期、所有权缺失等运营层面问题，持续保障的核心是把业务侧的任务要求自动转换为可执行的巡检规则，无需业务用户掌握运维知识
