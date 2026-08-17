---
title: 'MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce
  Recommendation'
title_zh: MACS：面向可靠对话式电商推荐的混合多智能体框架
authors:
- Juli Huang
- Hannah Clay
- Sajjad Beygi
- Thomas Sarda
- Negin Golrezaei
- Amin Saberi
affiliations:
- Stanford University
- University of Southern California
- Amazon
- Massachusetts Institute of Technology
- Google DeepMind
arxiv_id: '2608.14068'
url: https://arxiv.org/abs/2608.14068
pdf_url: https://arxiv.org/pdf/2608.14068
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 多Agent 对话式电商推荐优化
tags:
- Multi-Agent
- Conversational Recommendation
- LLM4Rec
- E-commerce
- Constraint Enforcement
one_liner: 拆分LLM交互与确定性约束执行的混合多Agent框架，解决固定目录对话推荐的约束漂移问题
practical_value: '- 架构设计可直接复用：将对话推荐系统拆分为LLM交互层和确定性规则执行层，LLM仅处理自然语言相关任务，商品检索、约束过滤完全通过结构化SQL/知识图谱执行，从架构层面避免LLM幻觉导致的违规推荐，无需依赖大量prompt工程约束LLM行为

  - 多轮会话状态管理可复用：用结构化的slot字典独立存储跨轮次用户约束，支持约束累加、更新、反转操作，完全不依赖LLM的上下文记忆能力，彻底解决多轮对话的约束漂移问题

  - 降级逻辑可直接落地：当检索结果不足时，按预设优先级放松非核心属性约束，价格、品牌等用户明确提出的硬约束永不放松，且必须在响应中明确告知用户放松的约束项，既避免空结果又保证用户知情权

  - 评估方法可复用：将推荐系统的评估拆分为确定性约束检查（SQL校验商品合规性）和响应质量LLM打分两部分，无需人工标注即可快速评估对话推荐系统的可靠性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
固定商品目录的对话式电商推荐要求所有推荐必须来自商家自有库存，不能出现幻觉商品或违反用户约束，现有纯LLM方案容易遗忘跨轮次的品牌排除、预算上限等硬约束，约束漂移、合规性差的问题严重影响落地。

### 方法关键点
- 双Agent架构拆分职责：Shopping Agent基于LLM完成意图路由、偏好提取、响应生成等语言类任务；Merchant Agent通过SQL过滤、知识图谱查询完成确定性的商品检索、硬约束执行，Shopping Agent无权直接访问商品库，从架构层面杜绝幻觉
- 会话持久化偏好层：用带类型的slot字典存储跨轮次用户约束，自动支持约束累加、预算覆盖、品牌排除反转等操作，不依赖LLM的历史记忆能力
- 渐进式约束降级：检索结果不足3个时，按优先级放松非核心属性约束，价格、品牌等硬约束永不放松，且显性告知用户放松的约束项，永不返回空结果

### 关键结果
基于笔记本类目的140条单轮查询、10个多轮场景基准测试，对比GPT+Catalog、Gemini+Catalog基线：单轮通过率87.1%（基线最高72.1%），品牌合规率100%；多轮Macro Pass@5达72%（基线56%/52%），约束漂移率为0，排除反转、约束累加场景Pass@5达100%（基线最高60%），响应质量与基线持平。

固定目录对话推荐场景下，架构层面拆分自然语言交互与确定性约束执行，可靠性远优于纯prompt优化的LLM方案。
