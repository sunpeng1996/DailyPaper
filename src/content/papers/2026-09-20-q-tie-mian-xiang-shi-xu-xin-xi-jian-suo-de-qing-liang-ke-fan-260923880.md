---
title: 'Q-TIE: A Lightweight and Generalizable Re-ranking Framework for Temporal Information
  Retrieval'
title_zh: Q-TIE：面向时序信息检索的轻量可泛化重排序框架
authors:
- Soyeon Kim
- Hyunjin Kim
- JinYeong Bak
- Steven Euijong Whang
affiliations:
- Korea Advanced Institute of Science and Technology
- Sungkyunkwan University
arxiv_id: '2609.23880'
url: https://arxiv.org/abs/2609.23880
pdf_url: https://arxiv.org/pdf/2609.23880
published: '2026-09-20'
collected: '2026-09-23'
category: RAG
direction: RAG 时序检索重排序优化
tags:
- TIR
- RAG
- Re-ranking
- Temporal Intent
- Lightweight
one_liner: 提出基于可学习时序意图提取的轻量TIR重排序框架Q-TIE，兼顾显式时序约束与泛化性可直接接入RAG链路
practical_value: '- 电商搜索、商品问答RAG场景可直接复用TIE模块提取用户查询的时序约束（如「2024款笔记本」「去年的社保政策」的时间区间），作为重排序独立特征过滤过时商品/内容，提升结果准确性

  - 无需重构现有检索链路，Q-TIE可作为轻量插件接入召回后重排序阶段，工程上线成本极低

  - 可参考「可学习时序区间表示+独立信号融合」的设计思路，替换现有业务中规则型时序筛选逻辑，提升跨品类、跨查询类型的泛化效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
RAG落地中时序不匹配的召回证据会导致LLM生成过时、错误内容，现有两类时序信息检索（TIR）方案存在明显trade-off：时序检索器基于表示学习实现灵活Query理解，但缺乏显式时序约束管控；时序重排序器可显式执行时序约束，但依赖预定义规则，跨查询类型泛化性差。

### 方法关键点
提出Q-TIE轻量重排序框架，核心为可学习的Temporal Intent Extraction（TIE）模块，可将Query中隐含的时序约束映射为统一的<t_start, t_end>区间表示，既通过模型学习突破规则的泛化性瓶颈，又将时序约束作为独立信号显式建模，同时覆盖两类范式的优势，可作为插件直接接入现有检索链路。

### 关键结果
在多类时序查询测试集上效果一致优于现有SOTA TIR方法，作为轻量组件可无缝集成到时序感知RAG pipeline中，代码已开源。
