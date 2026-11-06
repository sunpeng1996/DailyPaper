---
title: 'Persistent Retrieval for Conversational Agents: A Study of Retrieval Efficiency'
title_zh: 对话智能体的持久化检索效率对比研究
authors:
- Karthik Ravula
- Sathwik Kowtha
- Rishabh Verma
- Kala Mehak Jain
- Gunjit Mittal
affiliations:
- ServiceNow
arxiv_id: '2611.07899'
url: https://arxiv.org/abs/2611.07899
pdf_url: https://arxiv.org/pdf/2611.07899
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 检索子模块效率优化
tags:
- ConversationalAgent
- RetrievalEfficiency
- Subagent
- MultiTurnConversation
- CostOptimization
one_liner: 提出跨轮保留检索历史的持久化检索子Agent，多轮对话场景下效率显著优于两种主流检索设计
practical_value: '- 多轮对话类业务（电商售前咨询、订单查询、客服导购）可拆分独立持久化检索子Agent，检索历史跨轮复用，大幅降低主Agent的上下文膨胀压力

  - 检索子Agent直接返回原始证据而非合成结果摘要，单轮可节省12~13秒生成耗时，对响应延迟要求高的实时交互场景收益显著

  - 成本与延迟权衡参考：多轮依赖强的场景优先选持久化检索方案，比主Agent内置检索降本45%、提速9.1%；单轮短对话场景非持久化子Agent成本更低

  - 可复用`handoff_after_this`标记机制，检索完成后直接返回结果跳过不必要的LLM调用，进一步降本提效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前对话Agent的检索架构存在两个普遍问题：主Agent内置检索时，检索结果随轮次累积会导致上下文严重膨胀，token成本和延迟持续上升；采用非持久化检索子Agent时，每轮重启会话历史，会重复执行相同检索任务，多轮交互下效率极低，企业级多轮对话场景急需平衡准确率、延迟、API成本的检索方案。

### 方法关键点
- 拆分独立的持久化检索子Agent，跨轮保留所有检索历史（查询语句、工具调用结果、元数据），新请求优先复用已有结果，避免重复检索
- 检索子Agent完成任务后直接返回原始证据+检索逻辑说明，跳过中间结果合成步骤，由主Orchestrator直接基于证据生成最终回答
- 支持纠错机制：主Agent判断证据不全时可下发修正指令，检索子Agent复用已有上下文继续检索，无需重启会话
- 引入`handoff_after_this`布尔标记，工具调用无错误时直接返回结果，省略多余的子Agent LLM调用

### 关键实验
基于IT服务管理（57题）、HR服务（48题）、带跨轮依赖的ITSM Complex（69题）3个企业级数据集，对比主Agent内置检索（Skill）、非持久化检索子Agent两个基线：
- 多轮场景下对比Skill基线：总token减少43.3%，API成本降低45.0%，平均响应时间快9.1%，准确率基本持平
- 对比非持久化子Agent：每轮响应快15.6秒，仅通用多轮场景下token高65.1%、成本高29.1%；强依赖多轮ITSM Complex场景下成本低于两个基线
- 消融实验显示：直接返回证据的效率增益（提速17.7秒）远大于持久化历史的增益（提速4.3秒）

**最值得记住的一句话**：对话Agent检索模块拆分时，优先做「直接返回原始证据」的优化，再做跨轮历史持久化，能在准确率损失可忽略的前提下获得最大效率提升
