---
title: 'Beyond Single-Model Injection: A Threat Model and Defense Architecture for
  Prompt Injection in Multi-Agent Systems'
title_zh: 多智能体系统Prompt注入威胁模型及分层防御架构
authors:
- Rudrendu Kumar Paul
- Sourav Nandy
affiliations:
- Boston University
- University of Texas at Austin
arxiv_id: '2609.22949'
url: https://arxiv.org/abs/2609.22949
pdf_url: https://arxiv.org/pdf/2609.22949
published: '2026-09-19'
collected: '2026-09-22'
category: Agent
direction: 多智能体系统 · Prompt注入安全防御
tags:
- Multi-Agent
- Prompt Injection
- Threat Modeling
- Defense Architecture
- LLM Security
one_liner: 枚举14种多智能体专属Prompt注入向量，提出4种架构防御将攻击成功率从31.2%降至4.2%
practical_value: '- 搭建多Agent电商导购/推荐系统时，放弃仅依赖system prompt做安全管控的思路，所有Agent边界加输入输出sanitization，轻量指令分类器仅加12ms延迟，可降低78%工具侧间接注入风险

  - 给不同角色Agent（导购Agent、订单处理Agent、合规Agent等）配置基础设施层的权限隔离，严格限制每个Agent可调用的工具/数据库范围，可100%消除权限提升攻击

  - 内部Agent通信链路加签名溯源机制，仅3ms/消息的开销就能降低91%的跨Agent注入攻击成功率

  - 异步部署Agent通信图的异常检测模块，不增加主路径延迟即可拦截84%的级联注入攻击，适配大流量电商Agent场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Prompt注入研究仅覆盖单LLM场景，多Agent系统特有的跨Agent消息传递、共享工具权限、信任传导特性会大幅放大注入风险，且现有单模型防御完全无法覆盖这些新增攻击面，当前多数生产级多Agent系统普遍仅依赖system prompt做防护，漏洞率极高。

### 方法关键点
- 梳理4大类共14种多Agent专属Prompt注入威胁向量：用户侧直接注入3种、工具输出侧间接注入4种、跨Agent消息注入4种、orchestrator级联注入3种
- 提出4种架构级（非prompt层）防御机制：跨Agent消息签名+溯源、Agent边界输入输出sanitization、按角色限定工具访问权限、Agent通信模式异常检测
- 测试采用生产级6Agent系统（编排器、检索、代码、分析、合规、输出Agent），覆盖金融分析类典型工作流，适配GPT-4o、Claude 3.5 Sonnet、Llama 3 70B三个主流LLM后端

### 关键实验结果
- 基线为仅加system prompt防护的6Agent系统，攻击总成功率31.2%，其中工具侧间接注入成功率达43%，67%的Agent存在至少一种可利用漏洞
- 4种防御叠加后总攻击成功率降至4.2%，其中跨Agent注入成功率降91%、间接注入降78%、权限提升攻击完全消除、级联攻击拦截率84%
- 总延迟开销仅4.7%，6Agent 15次消息交互仅新增225ms延迟，满足生产性能要求

**最值得记住的一句话：** Prompt层的防护永远不可靠，多Agent系统的安全必须在架构层做底层约束，而不是靠LLM自身的Guardrail。
