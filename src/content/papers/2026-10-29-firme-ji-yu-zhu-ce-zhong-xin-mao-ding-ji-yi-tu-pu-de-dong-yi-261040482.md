---
title: 'FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor
  Knowledge'
title_zh: FIRME：基于注册中心锚定记忆图谱的动态异构投资者知识管理
authors:
- Yunbai Zhang
- Yunyi Gao
- Han-Tai Shiao
affiliations:
- The Vanguard
arxiv_id: '2610.40482'
url: https://arxiv.org/abs/2610.40482
pdf_url: https://arxiv.org/pdf/2610.40482
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 记忆图谱构建 · 异构时序知识整合
tags:
- Knowledge Graph
- Entity Resolution
- Memory System
- Temporal Data
- Knowledge Fusion
one_liner: 提出注册中心锚定的记忆图谱框架FIRME，解决跨源时序异构知识的实体对齐与关系沉淀问题
practical_value: '- 可复用「标准身份库+持久别名映射」的实体对齐方案，解决电商场景下用户query、商品别名、品牌异名的归一化问题，减少匹配歧义

  - 关系的确定性时序更新规则（强化/失活/重新激活）可直接迁移到用户长短期兴趣建模，实现兴趣演变的可追溯、可解释管理

  - 跨源数据的规则融合+固定本体映射框架，可用于整合电商用户行为、客服会话、商品属性等异构数据构建业务知识图谱'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
金融AI复用投资者知识的场景需要跨源跨周期的持久记忆能力，现有知识图谱存在同实体多表层形式导致的关系历史碎片化、证据无法沉淀的问题。

### 方法关键点
FIRME为注册中心锚定的记忆图谱：1）周期内通过规则融合+固定产品-主题本体，关联投资者电话会议讨论与投资组合现金流信号；2）跨周期通过标准身份+持久别名机制将重复观测映射到同一关系历史，采用确定性更新策略实现关系的强化、失活与重新激活状态管理，全程保留数据来源、时间与上下文信息。

### 关键结果数字
对比无别名记忆的历史注册基线，固定评审协议下4组数据集/后端配置的最终周期正确匹配率提升7.8-12.1pp；人工盲审下正确匹配率提升9.0-16.5pp，重绑定召回提升22.5-29.0pp；投资者场景下300个周期内融合输出中293个具备有效证据路径
