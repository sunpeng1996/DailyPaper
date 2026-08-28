---
title: Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?
title_zh: 用户自定义权限策略能否有效防范AI Agent越权行为？
authors:
- Ting Yan
arxiv_id: '2608.27443'
url: https://arxiv.org/abs/2608.27443
pdf_url: https://arxiv.org/pdf/2608.27443
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: AI Agent 权限控制用户行为研究
tags:
- AI Agents
- Permission System
- Human-AI Interaction
- User Study
- Policy Management
one_liner: 通过113名非技术用户对照实验，发现用户自定义权限策略的AI Agent越权拦截率低于逐次审批和自动审核
practical_value: '- 做消费级AI Agent权限设计时，不要默认用户自定义静态规则比逐次审批更安全：80%以上普通用户会选择「每次询问」，反而可能因弹窗疲劳提高越权操作通过率

  - Agent权限的「询问」选项不是中性妥协：需提前向用户展示该规则下会触发询问的典型场景、预估询问频次，避免用户盲目选询问导致实际防护失效

  - 工具调用权限映射可复用论文方案：基于MCP协议的代理层用LLM分类工具元数据到后果类别，准确率比关键词匹配、embedding近邻方案高20%以上

  - 不要将用户主观可控性等同于实际安全性：自定义规则组用户感知可控性与其他组无差异，但越权通过率高20%以上，需建立客观越权拦截率监控指标'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI Agent正成为数字服务核心入口，可调用支付、消息、文件管理等工具执行任务，非技术用户缺乏易懂、可复用的跨工具权限控制方式。此前行业默认用户提前定义的静态权限规则比逐次审批更高效、防护性更强，但缺乏实证对比数据，本研究验证这一假设是否成立。
### 方法关键点
- 设计三类权限模式对照：逐次人工审批（HITL）、模型自动逐次审核（AUTO）、用户提前按后果类别（花钱/发消息/删除/访问隐私数据）设置「允许/询问/禁止」规则的POLICY模式
- 开发基于MCP协议的代理层，用LLM将工具元数据映射到后果类别，自动匹配应用用户权限规则
- 招募113名无专业软件背景的用户参与对照实验，全程模拟18项日常Agent操作，其中包含7项预设越权操作
### 关键结果
- POLICY组越权拦截率比HITL低20.1pp，比AUTO低14.5pp；三类模式正常任务完成率均达94%以上，无显著差异
- 81.4%的POLICY用户给规则选择「询问」选项，仅18.6%的规则提前明确允许/禁止；POLICY组越权操作 runtime 通过率达66.8%，比HITL高26.4pp，比AUTO高20.6pp
- POLICY组runtime弹窗数从HITL的18次降至10.9次，但算上规则设置时间总干预时长无显著下降
### 最值得记住的结论
权限设计不仅是偏好收集问题，更是承诺设计问题：给用户提供规则模板没用，核心是要让用户明确知道规则提前确定了哪些边界、哪些决策仍会留到运行时处理
