---
title: 'PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant
  LLM Agents'
title_zh: PolicyGuide：面向合规LLM Agent的全流程引导框架
authors:
- Seongjae Kang
- Taehyung Yu
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2608.19861'
url: https://arxiv.org/abs/2608.19861
pdf_url: https://arxiv.org/pdf/2608.19861
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent 合规引导 工作流管控
tags:
- LLM Agent
- Policy Compliance
- Workflow Graph
- Runtime Safeguard
- Customer Service
one_liner: 将领域政策编译为工作流图，在用户轮次边界主动校验，跨模型提升Agent流程合规性与任务完成率
practical_value: '- 电商售后、订单修改类客服Agent可直接复用「离线政策转可校验工作流图+用户轮次边界主动校验」架构，替代原有仅拦截最终工具调用的方案，减少身份核验、用户确认等前置步骤遗漏导致的合规风险

  - 可复用跨模型兼容设计，仅维护一套工作流规则即可适配不同基座Agent，无需针对每个基座做微调或流程重写，降低多模型部署的运维成本

  - 应对恶意用户诱导（比如套取优惠、违规改单）场景可借鉴「仅工具返回的实据满足工作流节点要求才放行操作」的逻辑，比纯语义判断的校验准确率更高，红队攻击下拦截率提升超50%

  - 流程规则越多、步骤越固定的业务场景落地收益越高，实验中强流程的电信域合规通过率提升超2倍'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有客服类LLM Agent的合规管控存在两类缺陷：单动作拦截类方案仅校验最终工具调用，无法前置发现身份核验遗漏、步骤错序等流程类违规；内置工作流的Agent将流程逻辑与模型耦合，无法跨基座复用，也不具备强安全拦截能力，极易产生违规操作导致业务损失，亟需一套外置、跨模型的全流程合规引导方案。

### 方法关键点
- 离线流程编译：将领域政策文本+工具注册表自动编译为带校验规则的工作流图，经过覆盖率、可达性校验后冻结，全场景复用
- 在线主动校验：在每次用户轮次结束后、Agent响应前主动触发校验，持久化每个用户请求在工作流中的执行进度，遍历到第一个未满足的节点即返回对应修复指引，仅所有前置节点校验通过才放行可变操作的工具调用
- 全外置架构：工作流、校验逻辑完全独立于Agent基座，与模型解耦，支持任意LLM Agent无缝接入

### 关键结果
基于τ2-bench航空、零售、电信三个客服域数据集测试，对比ReAct无防护、PolicyGuard单动作拦截等基线：平均Pass4从0.42提升至0.62，强流程的电信域Pass4从0.19暴涨至0.61；CRAFT红队攻击下攻击成功率仅0.087，较无防护方案降低56%；同一套工作流可直接迁移到Claude Sonnet 4.6、Gemini 2.5 Pro，均获得稳定合规增益。

> 最值得记住的结论：合规管控的核心单元应该是完整业务流程而非孤立动作，外置工作流追踪方案兼顾了跨模型兼容性与安全可控性
