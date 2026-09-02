---
title: 'PEARL: Front-Loading Relational Chains for Multi-Hop Table Retrieval'
title_zh: PEARL：前置加载关系链的多跳表格检索框架
authors:
- Subeen Ho
- Hyeongu Kang
- SeongKu Kang
- Susik Yoon
affiliations:
- Korea University, Seoul, Korea
- Computer Science and Engineering, Korea University
arxiv_id: '2608.30291'
url: https://arxiv.org/abs/2608.30291
pdf_url: https://arxiv.org/pdf/2608.30291
published: '2026-08-31'
collected: '2026-09-02'
category: RAG
direction: RAG · 结构化多跳表格检索优化
tags:
- Table Retrieval
- Multi-hop Retrieval
- RAG
- Training-Free
- Offline Preprocessing
one_liner: 无需训练的多跳表格检索框架，离线预构关系链与分块语料，查询时无LLM推理即可提效
practical_value: '- 结构化知识库RAG场景可复用离线预生成多跳关联路径的思路，把跨表join关系提前编码到检索语料，降低查询时推理延迟

  - 垂直分块子表编码方案可迁移到电商商品库、订单库等多表关联检索场景，避免整表编码忽略跨表语义的问题

  - 训练免框架无需微调LLM，可快速落地到现有RAG系统，尤其适合算力紧张、迭代快的业务场景'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
LLM具备优异的表格推理能力，但真实场景下表格数据碎片化、存在跨表关联依赖，现有基于整表表征的检索方法忽略join关系带来的跨表语义，多跳检索效果差，且多数方案查询时需调用LLM推理，延迟高难以落地。

### 方法关键点
1. 采用无训练范式，切换为基于垂直分块的子表编码思路，无需微调LLM即可实现效果提升
2. 离线阶段基于预识别的表间join路径生成多跳查询，将关联列重组织为垂直分块的语料单元，提前把跨表语义编码进检索库
3. 查询阶段无需调用LLM推理，直接基于预构建的分块语料完成多表检索，延迟极低

### 关键结果
在多跳表格检索任务上效果全面优于现有方案，3跳查询的R@2指标最高提升30.05%
