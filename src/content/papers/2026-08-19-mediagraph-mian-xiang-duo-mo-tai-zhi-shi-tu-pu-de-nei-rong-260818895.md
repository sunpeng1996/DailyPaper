---
title: 'MediaGraph: A Content-Aware Data Model and Query Framework for Multimodal
  Knowledge Graphs'
title_zh: MediaGraph：面向多模态知识图谱的内容感知数据模型与查询框架
authors:
- Florian Ruosch
- Luca Rossetto
affiliations:
- FPR Consulting, Switzerland
- Dublin City University, Ireland
arxiv_id: '2608.18895'
url: https://arxiv.org/abs/2608.18895
pdf_url: https://arxiv.org/pdf/2608.18895
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态知识图谱 · 存储查询框架
tags:
- Multimodal Knowledge Graph
- SPARQL
- Graph Database
- Multimedia Retrieval
- Content-aware Query
one_liner: 将多媒体内容作为多模态知识图谱原生节点，提出开源的内容感知存储与查询框架
practical_value: '- 搭建电商多模态商品知识图谱时，可复用将商品图片/视频/详情文本直接作为KG节点而非外部链接的设计，提升跨模态关联查询效率

  - 多模态召回场景可借鉴其原生特征相似度检索、动态内容分段的实现思路，降低多模态数据查询的工程复杂度

  - 构建电商多模态内容检索Agent时，可基于其扩展SPARQL的方案实现跨模态语义查询的统一接口'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态知识图谱将多媒体文件作为外部URI引用或不透明二进制块存储，内容感知能力完全缺失，无法支持跨模态复杂关系查询与深度分析，限制了多模态检索、分析类任务的上限。
### 方法关键点
1. 设计MediaGraph数据模型，将多媒体内容直接作为知识图谱的原生节点而非外部独立实体，实现媒体内容与图谱核心结构的深度融合
2. 开发开源实现MeGraS（MediaGraph Store），扩展SPARQL查询语言，原生支持特征相似度检索、动态内容分段、非物化关系推理等操作
### 关键结果
开源MeGraS框架填补了内容感知多模态知识图谱存储查询领域的空白，可直接支撑各类复杂跨模态检索与分析任务，无额外业务适配成本。
