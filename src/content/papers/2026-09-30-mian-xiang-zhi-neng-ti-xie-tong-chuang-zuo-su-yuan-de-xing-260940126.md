---
title: Who Asked for This? Inline Annotations as Authoring Transactions for Provenance
  in Agentic Authoring
title_zh: 面向智能体协同创作溯源的行内注释创作事务机制
authors:
- Chang Xiao
affiliations:
- Boston University
arxiv_id: '2609.40126'
url: https://arxiv.org/abs/2609.40126
pdf_url: https://arxiv.org/pdf/2609.40126
published: '2026-09-30'
collected: '2026-10-03'
category: Agent
direction: 智能体协同创作 · 操作溯源
tags:
- Agentic_Authoring
- Provenance
- Transaction_Protocol
- Inline_Annotation
- Lineage_Tracking
one_liner: 提出带验证事务协议的Reactant交互范式，实现AI智能体协同写作的词级别修改溯源
practical_value: '- 电商文案生成Agent可复用这套可验证事务协议，记录每一次用户指令、调用技能和修改对应关系，方便后续回溯bad case优化生成效果

  - 推荐系统Prompt迭代、Agent调用链路可借鉴词级别lineage追踪方法，快速定位效果劣化的来源环节

  - 可复用事务留痕机制从用户重复请求中挖掘可固化的通用技能，降低Agent重复调用成本，提升任务执行效率'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
AI 智能体协同写作场景下，终稿无法追溯每处修改对应的用户请求、调用的 Agent 技能，修改链路不透明，难以沉淀可复用能力。
### 方法关键点
1. 提出 Reactant 交互范式，支持用户在原始文档中插入带类型的行内注释触发 Agent 操作；
2. 设计可验证事务协议，全链路记录每条请求、调用技能 ID、增删改操作的对应关系；
3. 内核通过校验记录状态与操作凭证，生成词粒度的全生命周期修改溯源链路。
### 关键结果
经本论文修订历史验证方案可行性，3名用户4个月自主使用数据显示，该事务记录可支撑修改历史对话查询、从重复请求中提取可复用技能两大核心场景，成为智能体创作的可扩展底层支撑。
