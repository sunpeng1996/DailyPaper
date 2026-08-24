---
title: 'EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document
  Question Answering'
title_zh: EnSI-RAG：面向长文档问答的实体结构索引检索增强生成框架
authors:
- Xuanyu Meng
- Jiashuo Sun
- Jash Rajesh Parekh
- Jiawei Han
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2608.21252'
url: https://arxiv.org/abs/2608.21252
pdf_url: https://arxiv.org/pdf/2608.21252
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: 检索增强生成 · 长文档结构化索引
tags:
- RAG
- Long-document QA
- Entity Index
- Information Extraction
- Multi-hop Reasoning
one_liner: 提出基于实体结构索引的RAG框架，解决长文档问答chunk碎片化、多跳推理准确率低的问题
practical_value: '- 电商客服/导购Agent的知识库RAG可复用实体中心chunk逻辑，以SKU、订单、售后工单为核心语义单元构建passage，避免固定长度chunk拆分关联属性，提升多跳查询召回准确率

  - 电商商品、商家资质、平台规则类知识库可借鉴<实体, 类型, 属性/关系/维度, 内容>四元组索引结构，支持跨实体对比、多跳关联类查询的精准定位

  - 索引粒度自适应策略可直接复用：商品/营销域用粗粒度属性标签降低语义稀疏性，平台规则/法律合规类场景用细粒度标签避免歧义，平衡精度与召回率

  - 离线做 heavy 实体抽取与索引构建、在线仅做结构化匹配+小范围passage生成的架构，适合高并发电商场景，可在保证效果的同时控制在线 latency'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG普遍采用固定长度chunk索引，易拆分实体与关联证据、混合无关内容，在长文档多跳问答、跨文档信息聚合场景下召回准确率低；单纯扩大LLM上下文窗口则会面临“lost in the middle”效应、推理成本高的问题，亟需兼顾检索精准度和推理可靠性的长文档RAG方案。
### 方法关键点
- 离线预生成以实体为中心的语义passage替代固定长度chunk，每个passage围绕单个核心实体保留完整上下文，关联唯一psg_id支持原始文本溯源
- 从passage中抽取四元组结构化记录<实体e, 类型t, 语义分类c∈{property/relation/aspect}, 值v>，构建查询无关的实体结构索引，索引仅作为检索句柄，不替代原始文本参与推理
- 在线阶段先解析用户查询生成结构化检索计划，单跳/多跳匹配索引获取关联passage集合后直接喂给LLM合成答案，避免结构化抽取误差传导到推理环节
### 关键实验
在Loong（跨金融/法律/学术多文档推理）、Oolong（长文本信息聚合）两个长文档QA基准上测试，对比RAG、LongRAG、GraphRAG、SLIDERS等8个SOTA基线，EnSI-RAG平均准确率达78.24%，较基线最高值高出6.62个百分点；消融实验验证：金融域表行级passage比整表passage准确率高8.5个点，Top5检索深度比Top12高2个点，属性粒度按域自适应调整可提效1-3个点。
### 核心结论
长文档RAG优化的核心思路是解耦证据定位与答案合成，用结构化索引做精准召回、原始文本做推理依据，既避免结构化抽取的误差传导，又解决纯语义检索的碎片化问题。
