---
title: 'How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces
  to Enforcement'
title_zh: 《AI Agent用户权限系统研究：从交互界面到运行时执行》
authors:
- Alexandra E. Michael
- Franziska Roesner
affiliations:
- University of Washington
arxiv_id: '2607.13718'
url: https://arxiv.org/abs/2607.13718
pdf_url: https://arxiv.org/pdf/2607.13718
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent安全 · 用户权限体系设计
tags:
- Agent Security
- User Permission
- Policy Enforcement
- LLM Agent
- Taxonomy
one_liner: 调研21个学术方案+5款商用Agent，构建Agent用户权限全链路分类体系，识别核心落地缺口
practical_value: '- 落地电商导购/运营自动化Agent时，优先选择「结构化约束+确定性执行」的权限组合，避免完全依赖LLM guardrail做权限判断，降低资金操作、隐私泄露风险

  - 权限交互设计可复用「固定选项+自然语言补全」双模式，同时记录用户实时授权决策迭代权限策略，降低用户隐私疲劳

  - 权限系统必须明确告知用户LLM自动审核的使用场景，保留用户开关权限，避免黑盒授权引发的合规问题

  - 多Agent协作场景（如客服+下单+物流Agent联动）可参考信息流控制的权限标签方案，实现跨Agent细粒度权限隔离'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
AI Agent落地过程中，prompt injection、幻觉易引发越权执行敏感操作（如转账、泄露隐私），现有权限系统多为产品级全局策略，无法适配不同用户的隐私、操作偏好，且缺乏对用户级权限全链路设计的统一梳理。

### 方法关键点
- 调研2024-2026年的21个支持用户级权限的Agent学术方案，通过递归引文检索筛选符合要求的研究
- 构建覆盖威胁模型、UI层权限定义、内部策略表示、用户输入到内部策略推导、运行时执行5个维度的分类体系
- 对5款主流商用Agent（Claude全系列、ChatGPT全系列、Codex）做黑盒走查，对比学术方案与工业落地的差异

### 关键结果
- 21个学术方案普遍聚焦低用户开销、形式化规格、确定性执行3个目标，但无一个方案同时实现三个目标
- 商用Agent仅40%支持结构化权限配置，80%默认采用高开销的用户在环授权，普遍存在LLM自动审核不透明、权限无法灵活撤销的问题
- 仅不到30%的学术方案支持权限动态更新，远低于商用系统的覆盖度

### 核心结论
Agent权限系统必须在低用户开销、策略确定性、用户可控性三者间做平衡，完全依赖LLM guardrail或高频用户弹窗都会最终导致权限失效。
