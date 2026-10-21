---
title: 'MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems'
title_zh: MAS-Guard：单智能体到多智能体LLM系统的统一安全护栏框架
authors:
- Mohammad Kachuee
- Phu Mon Htut
- Sheng Li
- Nikolaos Pappas
- Miguel Ballesteros Martinez
- Yassine Benajiba
- Sujith Ravi
- Dan Roth
affiliations:
- Oracle AI
arxiv_id: '2610.28397'
url: https://arxiv.org/abs/2610.28397
pdf_url: https://arxiv.org/pdf/2610.28397
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: 多智能体系统统一安全防护
tags:
- Multi-Agent-Safety
- LLM-Guardrail
- Agent-Security
- Prompt-Injection-Defense
- Runtime-Enforcement
one_liner: 提出跨单/多智能体的分层安全护栏框架，攻击成功率降71.5%-86.3%且保留良性任务效用
practical_value: '- 可直接复用分层防护架构：在电商导购/推荐Agent的用户输入、工具调用、结果返回环节插入A-Guard专项检测，比如拦截诱导跳转第三方、泄露用户隐私的恶意内容

  - 系统层可复用Agent Charter+Control Plane设计：给多Agent电商系统（选品Agent、内容生成Agent、客服Agent等）分别定义角色权限、通信路由、能力边界，用确定性检查直接拦截非法跨Agent调用（比如内容生成Agent直接调用用户支付工具）

  - 可复用4级干预机制：根据风险等级做柔性处理，低风险违规内容让Agent自行修正，高风险操作（比如下单、支付）触发用户确认，平衡安全防护与用户体验

  - 第三方黑盒Agent无需侵入改造：仅在通信边界做系统层防护即可覆盖基础安全要求，降低多Agent系统的接入成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent及多智能体系统（MAS）应用范围持续扩大，可支持电商导购、智能客服、任务调度等复杂场景，但同时暴露了大量安全风险：prompt注入、信息泄露、恶意工具调用、攻击跨Agent传播等，且当系统同时包含自研可埋点Agent和第三方黑盒Agent时，现有碎片化防护方案仅覆盖单风险点或单Agent，无法形成统一安全管控，还容易影响正常业务的执行效率。

### 方法关键点
- 分层防护架构：本地A-Guard层对接可埋点Agent的执行钩子，根据事件类型（用户输入、工具调用、工具返回、跨Agent消息等）匹配专项检测专家，避免不必要的模型调用开销
- 系统层全局管控：通过Agent Charter定义每个Agent的预设角色、输入输出边界、允许的能力范围；Control Plane层先做路由、格式、权限的确定性检查，再叠加消息内容语义合规校验，同时支持黑盒Agent的边界防护
- 统一干预机制：所有防护层共用4级干预策略（ALLOW/REFLECT/CONFIRM/BLOCK），多防护结果冲突时取最严格策略，无需额外模型决策层

### 关键结果
在6个覆盖单/多智能体场景的基准数据集上，对比8种现有防护方案和无防护基线，测试GPT-5.6-Terra、Muse-Glimmer-30B、Grok-4.3三款不同厂商的Agent LLM，MAS-Guard相对无防护基线降低整体攻击成功率71.5%-86.3%，同时良性任务效用满足参考标准，无明显下降。

### 核心结论
多智能体系统的安全防护不能仅依赖单Agent内部的安全能力，必须结合本地执行层检测与系统级角色、路由、权限管控，才能平衡安全防护效果与业务体验。
