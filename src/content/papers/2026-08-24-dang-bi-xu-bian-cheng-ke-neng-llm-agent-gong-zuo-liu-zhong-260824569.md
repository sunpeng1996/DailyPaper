---
title: 'When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows'
title_zh: 当“必须”变成“可能”：LLM Agent 工作流中的约束弱化问题研究
authors:
- Yiheng Sun
- Huifei Wang
- Yancheng Zhu
- Zhenyu Li
- Zebin Zhao
- Yifan Yuan
affiliations:
- Shenzhen University
arxiv_id: '2608.24569'
url: https://arxiv.org/abs/2608.24569
pdf_url: https://arxiv.org/pdf/2608.24569
published: '2026-08-24'
collected: '2026-08-27'
category: Agent
direction: Agent 工作流约束留存优化
tags:
- LLM Agent
- Multi-agent Workflow
- Constraint Preservation
- AI Safety
- Agent Handoff
one_liner: 发现LLM Agent工作流语义留存不保证操作约束留存，给出可落地的修复与防控方案
practical_value: '- 搭建电商多Agent工单/营销审批流时，强制要求上下游传递的约束必须完整携带「状态标记、前置条件、负责角色、兜底方案」四个字段，避免合规风险，如营销预算审批、商品上架审核的约束不能被摘要压缩弱化

  - Agent工作流的信息压缩环节不能仅校验语义保真度，需额外增加约束属性校验模块，只要四个核心字段缺失任意一个就触发告警或自动补全

  - 存量Agent系统无法修改上游传递逻辑时，可直接在下游执行节点加硬校验（权限查询、合规规则校验、人工审批卡点），无需修复上游Artifact也能100%避免违规操作'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent多角色/多阶段工作流依赖摘要、工单、交接笔记等中间文本传递状态，过往研究仅关注文本语义保真度，未意识到绑定执行的约束（如「必须经审批才能执行」）可能在传递中从强制要求退化为非绑定参考信息，即使语义内容完整留存，也可能引发违规操作，这一漏洞对企业级Agent、电商营销审批、商品合规审核等高风险场景的可靠性影响极大。
### 方法关键点
- 将绑定执行的工作流状态抽象为4个核心字段：停止状态（是否必须暂停执行）、未解决前置条件、负责解决的权威角色、合法兜底方案
- 采用分阶段隔离实验：上游先基于完整上下文正确识别约束，再经过压缩、计划同化、共识趋同、权限下放、先例替换5类常见传递变换，下游仅基于变换后的中间Artifact执行，单独测量约束留存率与违规率
- 对比两类干预方案：直接修复Artifact补全缺失字段、不修改Artifact仅在下游执行节点加校验
### 关键结果
- 对照组直接传递原始约束，约束留存率100%，违规率0%；普通压缩场景下约束100%失效，违规率54.2%；多跳压缩约束失效97.2%，违规率31.9%；权限下放场景约束失效76.7%，违规率60.8%
- 给受损Artifact补全全部4个核心字段，约束留存率恢复至100%，违规率降至0%
- 仅在下游执行节点加硬校验（权限查询、人工审批），无需修改上游Artifact，违规率也可降至0%，此时Artifact的约束留存率仍仅为4.7%
### 最值得记住的结论
Semantic availability does not guarantee operational preservation.（语义可用不代表操作约束仍然生效）
