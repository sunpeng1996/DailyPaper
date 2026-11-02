---
title: 'Peeling the Matryoshka: Extracting Ontological Structure from Retrieval Embeddings'
title_zh: 拆解套娃：从检索嵌入中提取本体结构
authors:
- Eunchan Kim
- Inwhee Joe
affiliations:
- Hanyang University
arxiv_id: '2610.41785'
url: https://arxiv.org/abs/2610.41785
pdf_url: https://arxiv.org/pdf/2610.41785
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 本体构建 · Matryoshka嵌入应用
tags:
- MRL
- Ontology Construction
- Retrieval Embedding
- Taxonomy Induction
- Unsupervised Learning
one_liner: 发现MRL嵌入前缀长度与分类粒度对齐，提出仅需概念词汇的无监督本体结构提取方法PEEL
practical_value: '- 电商类目体系构建可复用MRL嵌入的粒度对齐特性，用短前缀做粗分类、长前缀做细分类，降低类目人工标注成本

  - 召回侧多粒度检索可直接复用MRL前缀特性，无需单独训练多粒度向量，减少向量存储与计算开销

  - 无监督类目关系挖掘可参考PEEL的order-embedding+最小生成树方案，仅需概念词汇就能生成is-a层级关系'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有分类体系（如电商类目、知识图谱层级）构建成本高：聚类类方法需逐语料调优、生成层级不稳定；LLM类方案依赖昂贵的领域特定训练，跨域迁移性差。
### 方法关键点
1. 实证发现MRL嵌入的前缀长度与金标准分类的粗-细粒度天然对齐，该规律在3种不同架构的MRL模型上均成立
2. 提出PEEL方法：基于冻结的MRL嵌入训练轻量探针，以顺序嵌入目标将层级关系表示为向量包含关系，再通过最小生成树解码出分类DAG，仅需概念词汇无需文档输入
### 关键结果
在2个OLLM基准上实现高结构保真度，无需目标边监督即可直接跨域迁移，效果优于传统无监督分类构建方案。
