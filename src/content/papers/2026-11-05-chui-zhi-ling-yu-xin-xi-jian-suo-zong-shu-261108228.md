---
title: Domain-specific information retrieval
title_zh: 《垂直领域信息检索综述》
authors:
- Suzan Verberne
- Florina Piroi
- Allan Hanbury
affiliations:
- Leiden University
- TU Wien
- Complexity Science Hub
arxiv_id: '2611.08228'
url: https://arxiv.org/abs/2611.08228
pdf_url: https://arxiv.org/pdf/2611.08228
published: '2026-11-05'
collected: '2026-11-06'
category: Other
direction: 垂直领域检索 · 技术综述
tags:
- Domain-specific-IR
- Long-document-retrieval
- Query-processing
- Cross-domain-transfer
- Vertical-search
one_liner: 系统梳理垂直领域信息检索的任务、挑战与技术方案，验证领域方法可跨域乃至向开放域迁移
practical_value: '- 电商垂直商品搜索场景可复用文中长文档/长Query处理方法，适配商品详情页、用户复杂搜索词的检索需求，提升召回准确率

  - 跨域迁移方法可直接用于多品类电商检索系统的冷启动，大幅降低单领域标注数据的采集成本

  - 领域专属encoder的两阶段检索架构，可优化RAG+推荐/Agent的垂直知识召回效果，同时降低推理算力开销'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
通用网页检索方案难以适配法律、医疗、学术、专利等垂直场景的工作类检索需求，垂直领域普遍存在长文档、长Query、用户需求高度定制化、检索会话链路长等特有问题，缺乏系统性的技术梳理框架。
### 方法关键点
系统梳理4类核心垂直IR场景的任务范式、公开基准数据集，总结6项核心挑战（长文档长Query处理、复杂用户需求建模、会话式探索检索、可复现性、偏差与公平性、领域专属评估体系），覆盖两阶段检索、领域专属encoder、Query优化、跨域迁移、低算力优化、会话检索等9类技术方案。
### 关键结果
验证垂直领域IR的技术方法可迁移到其他垂直领域甚至开放域网页检索场景，给出明确的可落地未来研究方向。
