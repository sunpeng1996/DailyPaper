---
title: 'When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls'
title_zh: 当“不要”不等于拒绝：CLAUDE.md安全规则与内置控制的差异研究
authors:
- Ting Yan
arxiv_id: '2608.23550'
url: https://arxiv.org/abs/2608.23550
pdf_url: https://arxiv.org/pdf/2608.23550
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent指令安全 规则落地有效性评估
tags:
- Agent Security
- Prompt Guardrail
- Instruction Control
- Usable Security
- LLM Safety
one_liner: 实测481份公开CLAUDE.md中仅4%-16%的自然语言安全规则有对应内置强制控制
practical_value: '- 自研Agent系统时不要仅依赖自然语言prompt写安全规则，必须配套内置硬控制（如权限、沙箱）兜底，避免规则失效

  - 可借鉴论文的规则-控制匹配校验方法，为Agent开发者做规则有效性的实时反馈工具，降低安全风险

  - 对电商导购、广告生成类Agent，敏感规则（如不得夸大宣传、不得泄露用户隐私）必须同时做内置拦截和prompt约束双重校验'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
大量缺乏安全经验的开发者用自然语言给Agent编写规则，CLAUDE.md这类纯文本指令通道为写-only模式，没有落地反馈，开发者无法确认规则是否真的被系统强制执行，存在严重安全隐患。
### 方法关键点
1. 采集481份公开CLAUDE.md文件，提取其中安全规则候选集
2. 用LLM将提取的规则与Claude Code官方公开的内置控制做匹配，同时由2名安全专家独立盲标注样本做校验
3. 分不同匹配严格度统计规则的内置控制覆盖率
### 关键结果
- 不同匹配宽松度下，仅4%-16%的成功提取的安全规则有对应内置控制，最严格标准下覆盖率仅4.4%（95%置信区间2.6%-6.7%）
- 本次规则提取方法的召回率为66.3%，上述覆盖率结果仅适用于成功提取的规则
