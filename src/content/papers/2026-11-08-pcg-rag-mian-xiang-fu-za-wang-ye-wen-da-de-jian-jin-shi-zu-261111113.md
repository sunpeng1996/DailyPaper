---
title: 'PCG-RAG: Progressive Compositional Grounding for Retrieval-Augmented Generation
  in Complex Web Question Answering'
title_zh: PCG-RAG：面向复杂网页问答的渐进式组合接地RAG框架
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Chongqi Qu
- Xiuquan Hou
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.11113'
url: https://arxiv.org/abs/2611.11113
pdf_url: https://arxiv.org/pdf/2611.11113
published: '2026-11-08'
collected: '2026-11-10'
category: RAG
direction: 检索增强生成 · 复杂网页问答优化
tags:
- RAG
- Web QA
- Progressive Reasoning
- Compositional Grounding
- Entity Identification
one_liner: 提出渐进式组合接地RAG框架，解决复杂Web问答中过早锁定实体导致检索偏离需求的问题
practical_value: '- 多步检索场景可复用「provisional实体候选+未满足约束召回」逻辑，避免电商多条件商品搜索、用户复杂咨询应答等场景下过早锁定候选导致结果偏离需求

  - 证据关联环节可借鉴「实体-关系跨页面溯源+证据链完整性校验」设计，提升RAG应答可解释性与准确率，适用于商品详情问答、售后咨询等对答案准确性要求高的场景

  - 上下文预算有限时，可复用「优先保留完整证据链而非独立高相关片段」的检索片段选择策略，在长上下文输入成本受限的场景下提升答案准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
复杂Web问答需要从多线索描述中识别目标实体、拼接跨网页分散的证据，现有多步RAG易过早锁定仅满足部分约束的实体候选，导致后续检索偏离用户原始信息需求，无法关联跨页面的实体识别证据与关系证据，最终应答准确率低、资源消耗高。
### 方法关键点
- 渐进式证据获取：将实体候选分为provisional/accepted两种状态，基于provisional候选结合未满足的约束生成检索query，不断补全证据迭代实体候选，直到所有约束满足后标记为accepted
- 组合推理：将复杂问题拆解为子问题构建语义依赖DAG，按拓扑顺序执行子问题，provisional候选用于缩小检索范围，应答时仍保留原始约束做校验，允许子问题在父问题未完全确认时提前完成
- 证据接地：构建每个子问题答案的跨页面证据链，最终生成时优先选择能完整覆盖证据链的片段填充上下文，避免孤立选取高相关片段导致证据关联断裂
### 关键实验
在BrowseComp-Plus、WebWalkerQA两个复杂Web QA数据集上，对比WebThinker、DeepHone、LQT等SOTA基线，准确率分别提升5.43、5.15个百分点；在多跳推理数据集MuSiQue上，完整证据召回率All@5比SOTA基线高4.4个百分点，同时token消耗比WebThinker降低82.98%，推理延迟降低62.31%。
### 核心洞见
多步RAG中不应急于将部分匹配的实体候选作为确定结论，应保留未满足的约束指导后续检索，并在最终生成时关联完整的跨页证据链，才能同时提升准确率与推理效率。
