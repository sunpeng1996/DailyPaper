---
title: 'PILAR: A Page-Grounded Unified Evidence Representation via an Entity-Linked
  Assertion Graph for Open-Domain QA Agents over Multimodal Document Corpora'
title_zh: PILAR：面向多模态文档QA Agent的统一证据表示框架
authors:
- Joongmin Shin
- Gyuho Shim
- Jung-hun Lee
- Jaehyung Seo
affiliations:
- Korea University
- Korea Maritime and Ocean University
- Konkuk University
arxiv_id: '2609.32895'
url: https://arxiv.org/abs/2609.32895
pdf_url: https://arxiv.org/pdf/2609.32895
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: Agent 多模态QA证据表示优化
tags:
- QA Agent
- Multimodal RAG
- Knowledge Graph
- Entity Linking
- Cross-document Reasoning
one_liner: 提出基于实体链接断言图的多模态证据统一表示，提升跨文档跨模态QA性能
practical_value: '- 电商导购/客服Agent场景可复用统一SPO断言空间设计，将商品详情页的文本、规格表、展示图信息转化为实体关联的结构化断言，解决跨页跨模态信息孤立问题，提升回答准确率

  - 多跳推理场景可复用「页面为接地单元+实体关联图为链接单元」的分层设计，既保留证据溯源能力避免LLM幻觉，又能跨订单、物流、售后政策等多文档关联证据，降低多跳查询错误率

  - 企业知识库RAG优化可复用「粗粒度页面检索+受控图扩展」的流程，既避免纯图检索的漂移问题，又能补全粗粒度检索遗漏的关联证据，跨文档查询场景EM比flat RAG提升1.6以上

  - 多模态信息抽取需搭配本地性过滤策略，VLM抽取的表格/图片断言优先保留同页/相邻页/同章节的关联结果，可大幅降低VLM幻觉带来的噪声影响'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
开放域多模态文档QA需要关联分散在文本、表格、图片中的跨页跨文档证据，现有方案存在三类缺陷：chunk/页面检索仅保留孤立片段，无法做全局关联；纯文本KG不包含表格、图片等多模态信息；VLM生成的多模态描述未做实体链接，无法跨文档遍历，导致多跳、跨文档、多模态查询效果差。
### 方法关键点
- 离线构建统一断言空间：将文本、表格、图片提取的事实统一映射为SPO结构化断言，关联到标准实体，同时保留每个断言的文档ID、页码、位置、来源等溯源信息，构建四层实体链接断言图（实体层/断言层/支撑层/溯源层）
- 检索阶段分层设计：先用0.4*BM25 + 0.6*dense的混合检索做粗粒度页面召回，再基于断言图做受控扩展，包含邻页关联、实体别名扩展、实体-断言-支撑链路扩展三类信号，加相关性门控避免图漂移
- 输出标准化页面接地证据包：将关联的跨模态证据按页面聚合，保留原始上下文，在固定token预算内输出给下游QA Agent，兼容单轮/多轮Agent调用接口
### 关键结果
在M3DocVQA、Frames两个多模态QA benchmark上，对比14种检索后端、4种Agent框架（Naive RAG/ReAct/PlanRAG/AutoGen），整体EM比flat检索高1.6，组合式查询高2.9，3跳查询高5.9；消融实验显示文本断言单独带来1.2的EM提升，多模态断言搭配本地性过滤可额外带来0.4的EM提升。
### 核心结论
页面是接地单元，实体关联图是链接单元，两者结合才能在保留证据可溯源性的同时实现跨模态跨文档的证据关联。
