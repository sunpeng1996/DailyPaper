---
title: 'Trallie: from Free-Form Text to Structured Data with LLMs'
title_zh: Trallie：基于LLM的自由文本到结构化数据转换框架
authors:
- Vijayasri Iyer
- Cristiano De Nobili
- Mubashir Hussain Shah
- Sébastien Bratières
affiliations:
- Pi School
- Translated
- Critiqality
arxiv_id: '2611.30773'
url: https://arxiv.org/abs/2611.30773
pdf_url: https://arxiv.org/pdf/2611.30773
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM信息抽取 · 非结构化数据结构化
tags:
- Information-Extraction
- Zero-Shot
- Few-Shot
- Schema-Induction
- Unstructured-Data
- Open-Source
one_liner: 开源零/少样本LLM信息抽取框架，支持多格式解析、自动Schema归纳、无需大量标注
practical_value: '- 电商场景可直接复用该框架做商品评价、客服会话、商品详情页非结构化文本的零/少样本结构化抽取，无需大量标注即可快速搭建IE pipeline，大幅降低新场景冷启动成本

  - 可借鉴其自动Schema归纳的设计，在新类目上架、新业务线拓展时自动从现有文档中提炼需要抽取的属性字段，减少运营、产品侧人工定义Schema的工作量

  - 多格式兼容能力可直接复用在电商多源数据（HTML商品页、PDF资质文件、TXT运营文档）的统一结构化处理环节，无需为不同格式单独开发解析模块'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统信息抽取依赖大量标注数据与定制化开发流程，跨域适配成本极高，大量散落在各场景的非结构化文本无法转化为可查询的结构化数据，制约数据驱动业务落地。
### 方法关键点
1. 基于LLM零/少样本prompt能力实现信息抽取，无需域内标注训练即可适配新场景；
2. 原生兼容HTML、PDF、TXT、JSON多格式文档解析，无需额外开发格式适配模块；
3. 支持两种工作模式：给定目标属性的定向抽取、无用户引导时自动从文档集合归纳Schema再完成抽取，降低非技术用户使用门槛。
### 关键结果
在FDA 510(k)医疗文档、SWDE数据集的电影/高校网页场景测试，给定目标属性时性能优于过往SOTA系统，自动Schema归纳场景下性能与现有系统持平，框架已完全开源。
