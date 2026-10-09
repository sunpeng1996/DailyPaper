---
title: Empowering Users in Graph Rule Mining via Large Language Models
title_zh: 基于大语言模型的图规则挖掘用户赋能方案
authors:
- Francesco Cambria
- Francesco Invernici
- Andrea Colombo
- Anna Bernasconi
affiliations:
- Politecnico di Milano, Italy
arxiv_id: '2610.09842'
url: https://arxiv.org/abs/2610.09842
pdf_url: https://arxiv.org/pdf/2610.09842
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: LLM 图规则挖掘交互优化
tags:
- Large Language Model
- Graph Mining
- Association Rules
- Prompt Engineering
- Graph Database
one_liner: 通过prompt引导LLM生成、优化、解释图规则查询，降低图挖掘的专业技能门槛
practical_value: '- 电商用户行为/商品关联图挖掘场景，可复用prompt引导LLM自动生成图规则查询逻辑，降低图查询编写的专业门槛

  - 推荐系统关联规则挖掘环节，可借鉴LLM生成+校验图规则的流程，快速挖掘用户-商品跨场景关联模式

  - 涉及图谱查询的Agent模块，可对接该LLM转图查询的能力，降低自然语言到图查询的转换开发成本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
属性图是建模互联数据的主流方案，可直观表达用户行为、商品关联、社交关系等复杂结构，但传统图关联规则挖掘依赖用户同时掌握图论知识与专业查询语法，非技术背景的业务人员无法直接使用图挖掘能力。
### 方法关键点
通过分层prompt范式引导LLM完成全链路图规则挖掘交互：支持将自然语言需求直接转换为标准MINE GRAPH RULE查询；自动对生成的查询做语法校验、规则优化，降低错误率；可将挖掘得到的图关联规则结果转换为自然语言解释，方便业务人员直接理解。
### 关键结果
已完成核心流程的可行性验证，可覆盖绝大多数常见的图关联规则挖掘需求，全流程无需用户具备图技术相关专业背景。
