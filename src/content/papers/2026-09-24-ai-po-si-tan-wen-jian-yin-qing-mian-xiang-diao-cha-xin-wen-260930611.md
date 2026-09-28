---
title: 'Epstein Files Engine: Agentic Search for Investigative Journalism'
title_zh: 爱泼斯坦文件引擎：面向调查新闻的智能体搜索系统
authors:
- Duy K. Nguyen
- Teresa Mondría Terol
- Dylan Freedman
- Zach Seward
affiliations:
- The New York Times
- National Public Radio
arxiv_id: '2609.30611'
url: https://arxiv.org/abs/2609.30611
pdf_url: https://arxiv.org/pdf/2609.30611
published: '2026-09-24'
collected: '2026-09-28'
category: Agent
direction: Agent 专业场景文档检索
tags:
- Agentic Search
- Text-to-SQL
- Multimodal Deduplication
- Information Retrieval
- RAG
one_liner: 纽约时报部署的多模态文档检索智能体，配合去重方法支撑记者调查产出20余篇报道
practical_value: '- 多模态去重方案可直接复用：拼接语义文本embedding+感知图像哈希+偏置项的无训练复合向量方案，可迁移到电商商品、广告素材的去重场景，可解释性强易调优，不需要额外训练融合模型

  - 智能体架构可借鉴：优先做Text-to-SQL跨库查询规划而非直接生成答案，所有结果附原始来源引用，既降低幻觉，又符合内容审核、业务校验要求，可复用在企业内部知识库、工单智能检索场景

  - 业务阈值调优思路可复用：面向漏召回损失远大于误召回损失的场景（如线索挖掘、风险巡检），可主动放宽阈值追求高召回，误召回的结果还可挖掘结构相似性价值（如同模板商品聚类、同类型售后工单分组）'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
2026年美国司法部公开约300万页多模态爱泼斯坦相关文件，传统关键词检索无法支撑记者快速从海量材料中挖掘独家线索，同时需要交叉验证内容是否已被自家或其他媒体报道，解决记者从模糊猜想转化为可核实线索的「首英里」和线索交叉校验的「最后一英里」痛点。

### 方法关键点
- 架构：基于LibreChat部署智能体，核心用LLM做Text-to-SQL查询规划，跨三个库检索：爱泼斯坦公开文件库、纽约时报历史报道库、外部媒体相关头条库，返回带原始引用的结果而非直接生成答案
- 多模态去重Diff方法：每页生成449维复合向量，含384维文本语义embedding、64维页面图像差分哈希、1维偏置项，L2归一化后用余弦相似度做近邻搜索判断重复
- 交互设计：明确告知用户输出不可直接信任，所有结论需核实原始材料，从规则层面避免幻觉导致的专业事故

### 关键结果
数据集为268万页PDF文档，分层抽样400对样本做人工标注，部署阈值设为0.92时，去重精度0.28、召回0.86，优先保证高召回避免漏过独家内容；上线后100+记者使用，累计查询4500次，支撑至少20篇见报报道。

### 最值得记住的结论
面向专业场景的智能体最大价值是作为机构知识库和原始材料的交互接口，而非自主内容生成工具，要把最终判断权交给专业用户。
