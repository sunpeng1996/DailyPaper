---
title: 'Structure then Query: Enabling Precise Analytical Queries over Unstructured
  Documents'
title_zh: 先结构化再查询：实现非结构化文档的精准分析查询
authors:
- Teng Lin
- Yuyu Luo
- Nan Tang
affiliations:
- HKUST(GZ)
arxiv_id: '2608.13384'
url: https://arxiv.org/abs/2608.13384
pdf_url: https://arxiv.org/pdf/2608.13384
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: RAG优化 · 非结构化文档结构化检索
tags:
- RAG
- Structured Retrieval
- Schema Induction
- LLM Cost Optimization
- Document Analysis
one_liner: 提出AnnoIndex系统，通过离线分层标注索引+在线结构化查询引擎，实现低成本高精准的非结构化文档分析查询
practical_value: '- 电商场景海量非结构化商品评价、客服会话、商品详情页可复用SchemaLoop分层schema归纳思路，先离线按品类/维度做结构化标注索引，查询时先做结构化过滤再调用LLM，可降低商品问答、评论分析等RAG类应用的LLM成本70%以上

  - 可借鉴在线EXTRACT算子的梯度调用策略：优先用正则、轻量SLM处理简单语义条件，仅对极小部分过滤后候选集调用大模型，兼顾效果与成本，适合广告/推荐场景的用户Query理解、素材合规检查等场景

  - 可复用查询后属性回写索引的设计，高频查询的提取结果自动沉淀为正式schema字段，边际成本随调用量持续下降，适合电商高频客服问答、商品属性提取等迭代型业务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有非结构化文档分析方案存在两大核心痛点：一是向量相似度检索属于模糊匹配，无法满足属性级精准过滤需求，召回结果噪声高，后续LLM处理成本高且易受上下文误导出错；二是知识图谱类预提取方案 upfront 成本极高，且无法支持聚合、连接等结构化分析操作，复杂查询准确率低，无法满足企业级大规模非结构化数据的精准分析需求。

### 方法关键点
- 离线层：SchemaLoop模块自动生成三层分层标注schema（数据集层/表层/文档层），通过「生成-验证-优化」闭环迭代，兼顾属性可提取性与过滤效率，用轻量模型离线提取属性值，构建结构化标注索引，将提取成本一次性摊销到所有后续查询
- 在线层：结构化查询引擎将自然语言query转成类SQL执行计划，优先用结构化索引做精准过滤大幅缩小候选集，再按成本从低到高（正则→SLM→LLM）调用EXTRACT算子处理剩余语义条件，提取结果自动回写索引复用

### 关键实验
在LCR法律语料、WikiText百科、SWDE网页三个真实数据集上，对比VectorDB+RAG、GraphRAG、QUEST等SOTA方案，AnnoIndex性能模式平均F1达0.87，比次优QUEST高7个百分点，比直接调用GPT-4o高14个百分点；单query摊销LLM token仅18.3K，是直接LLM调用的1/11；查询量增长时，EXTRACT算子调用量最多可下降79%，边际成本持续降低。

### 核心结论
将非结构化数据的属性提取成本从在线查询阶段转移到一次性离线构建阶段，通过结构化索引+梯度执行的方式，是兼顾RAG类系统精度与成本的核心路径。
