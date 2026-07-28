---
title: Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents
title_zh: 面向LLM Agent污点约束的智能权限策略代数框架APPA
authors:
- Arseny Kravchenko
- Vadim Liventsev
- Innokentii Konstantinov
- Ildar Iskhakov
- Matvey Kukuy
affiliations:
- Archestra AI
arxiv_id: '2607.24625'
url: https://arxiv.org/abs/2607.24625
pdf_url: https://arxiv.org/pdf/2607.24625
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 安全权限管控与污点约束
tags:
- LLM Agent
- Information Flow Control
- Taint Tracking
- Prompt Injection
- Security Policy
one_liner: 提出APPA框架，通过上下文分支与前置权限校验，将LLM Agent数据泄露攻击成功率从31%-50%降至0%-7%
practical_value: '- 电商/广告Agent（智能客服、投放规划Agent等）处理敏感数据（用户隐私、投放预算、订单信息）时，可借鉴APPA的上下文分支机制，敏感计算在子分支执行，避免主上下文被污点污染导致后续正常工具调用被限制，平衡安全与业务可用性。

  - 工具调用逻辑可复用前置校验方案：执行工具调用前先做权限标签预判，不满足条件时生成结构化补救方案（人工授权、数据脱敏、调用重调度），替代零散硬编码guardrail，降低多工具Agent的维护成本。

  - 分支场景下KV cache优化可直接复用：子分支继承父分支上下文快照，直接复用父分支预计算的KV cache，避免分支场景下prompt重复推理，降低多轮对话Agent的推理延迟与token消耗。

  - 跨分支全局append-only事件日志机制可迁移到电商合规场景，全链路记录Agent操作、权限变更、授权记录，满足金融、电商等高合规要求场景的操作追溯需求。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent处理混合密级数据时，两种主流防御方案均存在明显缺陷：零散的prompt guardrail易被prompt注入绕过，且无法防范模型幻觉导致的误操作；静态权限限制/传统信息流控制（IFC）的污点跟踪会永久抬高上下文密级，导致后续正常工具调用被禁止，严重降低多轮工具链场景下的Agent可用性。

### 方法关键点
- **前置获取校验**：工具调用执行前先评估标签变化与权限要求，不满足条件时不静默失败，而是生成结构化可执行补救方案（授权、接受权限收窄、调用重调度），所有操作留痕可审计。
- **引擎托管上下文分支**：处理敏感/不可信数据时自动生成子分支，子分支继承父分支的安全标签与上下文快照，子分支的标签变化、污点扩散完全隔离，仅允许经过校验的脱敏结果合并回父分支，避免主上下文被污染。
- **双半群形式化模型**：基于安全标签和共享事件日志构建二元半群模型，形式化证明父分支标签保留与合并约束，提供可验证的安全保障。

### 关键结果
基于自研的多轮工具链基准bench-corp测试，跨4个主流LLM对比无防护基线、Fides、无分支APPA、APPA四个方案：
1. 攻击成功率（ASR）从无防护基线的31%~50%大幅降至0%~7%，几乎完全阻断数据泄露风险。
2. 开启分支机制后，3个模型的业务效用显著提升：GPT-5.6 Luna从69%升至95%，Gemini 3.5 Flash-Lite从28%升至44%，Qwen 3.6 35B从54%升至72%，仅GPT-4o因调度 overhead 效用无明显变化。

> 最值得记住的话：引擎层面的上下文分支隔离而非prompt层的临时防护，是平衡LLM Agent安全与业务效用的核心路径。
