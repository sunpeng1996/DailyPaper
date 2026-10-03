---
title: 'JoinGR: Learning to Traverse Join Graphs for Table Retrieval'
title_zh: JoinGR：基于连接图遍历的表格检索方法
authors:
- Sandipan De
- Abhijit Chakraborty
- Sambaran Bandyopadhyay
- Vivek Gupta
affiliations:
- Arizona State University
- Adobe Research, India
arxiv_id: '2610.01064'
url: https://arxiv.org/abs/2610.01064
pdf_url: https://arxiv.org/pdf/2610.01064
published: '2026-10-01'
collected: '2026-10-03'
category: RAG
direction: 检索增强 · 多跳关联表格检索
tags:
- Table Retrieval
- Join Graph
- Text-to-SQL
- Graph Traversal
- Lightweight MLP
one_liner: 提出感知表间连接关系的JoinGR表格检索方法，大幅提升多跳场景下的检索召回
practical_value: '- 电商跨类目关联推荐、商家后台多表查询场景可复用连接图遍历思路，补充召回query未直接提及的关联商品/数据表

  - 冻结预训练embedding仅训练轻量MLP打分器的架构，低资源场景可快速落地，无需重训大模型

  - 跨域可迁移的打分器设计可用于多业务线共享检索模块，降低不同业务重复训练的成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有Text-to-SQL前置的密集表格检索方案独立对schema元素打分，完全忽略表间连接关系，无法召回query未提及、仅能通过关联关系定位的必要表格，在企业级多跳检索场景存在明显性能瓶颈。
### 方法关键点
1. 以数据库连接图为检索空间，列作为图节点，表内关联、外键关联作为带类型边；
2. 先召回与query语义匹配的锚点表，再用query条件化的轻量MLP打分器遍历连接边，聚合边得分得到全表排序分数；
3. 打分器基于冻结的query、节点、边预训练embedding训练，采用成对margin loss优化。
### 关键结果
在BIRD、Spider公开数据集上性能比肩SOTA检索基线；在多跳企业级基准BEAVER上，召回率显著优于密集检索、重排序基线；跨域实验证明打分器可跨基准迁移，具备通用连接图遍历能力。
