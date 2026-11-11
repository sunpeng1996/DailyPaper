---
title: 'Semantic Chains: From Reachable Facts to Justified Answers'
title_zh: 语义链：从可触达事实到可解释答案
authors:
- Misha Andreev
arxiv_id: '2611.14252'
url: https://arxiv.org/abs/2611.14252
pdf_url: https://arxiv.org/pdf/2611.14252
published: '2026-11-10'
collected: '2026-11-11'
category: Reasoning
direction: 大模型事实推理 · 可解释性
tags:
- Reasoning
- Fact_Checking
- Interpretability
- LLM_Evaluation
- Semantic_Chain
one_liner: 提出语义链数学模型，证明上下文事实到问题答案的可解释推导链必然存在
practical_value: '- 电商RAG客服/商品咨询场景可复用语义链构建逻辑，从召回的上下文文档中提取从用户Query到答案的事实推导路径，提升回答可信度与可解释性

  - 可基于文中的公共lexical key匹配、事实关联规则开发LLM答案自动化事实校验工具，避免商品参数、活动规则、售后政策等关键信息回答错误

  - 搜索摘要生成场景可复用文中的文本剪裁规则，生成保留核心事实逻辑的短摘要，提升用户搜索信息获取效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM生成答案的事实错误、可解释性不足是落地核心痛点，尤其是RAG、电商客服等依赖给定上下文回答的场景，长期缺乏答案与问题间事实关联的形式化定义，也无法验证合法答案是否必然存在可解释推导路径，导致答案校验、可解释性优化无理论依据支撑。
### 方法关键点
1. 定义上下文契约（Contract）基础结构：包含逻辑事实、对象指代规则、内容保留变换规则，明确事实间嵌套、引用、公共父事实三类合法关联关系
2. 明确语义链构建约束：链上每个节点为独立逻辑事实，相邻节点需同时满足结构关联、共享同一对象的可验证指代（lexical key）两个条件，整条链的事实集合可推导出完整答案
3. 形式化证明两个核心结论：合法完整答案必然与问题共享至少一个公共lexical key；只要上下文存在合法答案，就必然存在至少一条可解释的语义链连接问题与答案
### 关键结果
本研究为纯理论推导，无实验验证环节，所有核心结论均通过形式化逻辑证明成立。
### 核心结论
只要给定上下文存在问题的合法答案，就一定可以构造出由连续关联事实组成、可验证、可解释的推导链，无需依赖黑盒生成逻辑。
