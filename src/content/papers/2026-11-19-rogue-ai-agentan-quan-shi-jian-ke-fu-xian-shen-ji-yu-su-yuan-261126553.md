---
title: 'Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)'
title_zh: ROGUE-AI：Agent安全事件可复现审计与溯源框架
authors:
- Mengxiao Wang
- Mahbub Alam
- Kalyan Nakka
- Nitesh Saxena
affiliations:
- Texas A&M University
arxiv_id: '2611.26553'
url: https://arxiv.org/abs/2611.26553
pdf_url: https://arxiv.org/pdf/2611.26553
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent安全 · 事件复现与审计框架
tags:
- LLM Agent
- Security Audit
- Multi-Agent
- Incident Replication
- Root Cause Analysis
one_liner: 多Agent框架复现真实LLM Agent安全事件 带对照组验证根因 复现成功率达89%
practical_value: '- 电商导购、智能运营等高权限LLM Agent上线前，可复用该框架的对照组测试方法，复现历史同场景风险事件做回归校验，避免生产事故

  - Agent风险防御可直接复用论文验证有效的方案：每次工具调用返回后，附带当前操作的风险点+明确后果警告，该方案将Claude Sonnet 4.6有害操作率降至2%，效果远优于单纯重述规则

  - 多Agent流水线的分工+跨厂商模型交叉校验机制可复用：比如电商内容审核、商品上架校验等场景，用不同模型分工处理、交叉校验，可降低单一模型的偏差漏判

  - 做Agent权限设计时优先防控非对抗性风险：数据显示普通场景的权限过大、目标识别错误等风险造成的危害远高于prompt injection，优先做细粒度权限管控、高风险操作二次确认'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent已支持执行删改文件、发起支付等高权限操作，但公开安全事件报告仅描述故障结果，既不验证事件真实性也不定位根因；现有事件目录、基准测试均不开展带对照组的可复现验证，无法支撑风险修复和模型版本迭代的安全校验。
### 方法关键点
- 搭建多角色specialist Agent流水线：由不同厂商的LLM Agent分工完成事件收集、源文件校验、根因标注、复现环境搭建、交叉审核，所有判断均有独立校验，最终由代码自动识别有害操作，避免人工误差
- 每个事件构建两组对称环境：事件环境保留报告提及的风险点，对照环境仅移除该风险点，其他配置完全一致，通过两组有害操作率的差异验证根因的因果性
- 支持多模型快速审计：仅需适配模型API即可完成新版本模型的全量安全事件回归测试，单模型审计成本仅为0.54~47美元
### 关键结果
- 基于2025-2026年253份公开安全事件报告，构建108个可复现测试用例，覆盖96个真实事件、38类风险场景，事件复现成功率达89%
- 测试5款主流LLM（GPT-5.6系列、Claude Sonnet 4.6、Gemini 3.5 Flash、DeepSeek-V4-Flash），事件环境下有害操作率为18%~33%，对照环境下仅为0%~1%
- 86%的真实生产危害事件无攻击者介入，非对抗性普通风险（权限未管控、目标识别错误等）造成的危害远高于prompt injection；工具返回后附带风险+后果警告可将Claude Sonnet 4.6的有害操作率降至2%，效果远优于等长的规则重述提示
> 最值得记住的结论：LLM Agent的绝大多数安全风险来自普通场景的非对抗性疏忽，而非热门的prompt injection，细粒度权限管控和操作前明确风险警告的投入性价比远高于对抗攻击防御
