---
title: 'Distilling Lexical Product Associations into Deep Transformers: An Extreme
  Multi-Label Approach for Natural Language E-Commerce Search'
title_zh: 面向电商自然语言搜索的词汇商品关联蒸馏极端多标签方法
authors:
- Sunnidhya Roy
- Samarpita Bhaumik
affiliations:
- International Institute of Information Technology Bangalore
arxiv_id: '2609.26921'
url: https://arxiv.org/abs/2609.26921
pdf_url: https://arxiv.org/pdf/2609.26921
published: '2026-09-22'
collected: '2026-09-24'
category: RecSys
direction: 电商搜索 · 知识蒸馏 极端多标签分类
tags:
- Knowledge Distillation
- Extreme Multi-label Classification
- E-commerce Search
- DistilBERT
- TF-IDF
one_liner: 通过伪标签蒸馏将TF-IDF商品关联注入DistilBERT，解决电商会话式搜索词汇不匹配问题
practical_value: '- 伪标签构造trick：可复用现有成熟词法匹配算法（TF-IDF/BM25）生成无监督商品关联伪标签，蒸馏到Transformer，大幅降低语义检索模型的标注成本，适配新类目/新站点冷启动场景

  - 评测校准方案：做商品检索评测时必须加严格自排除规则（mask掉query对应的商品自身），同时修正相似度矩阵与分类标签的索引对齐问题，避免基线指标虚高/虚低，保证评测可信度

  - 架构选型参考：中小规模商品库（<10万SKU）可直接用极端多标签分类架构做端到端检索；超过10万SKU建议转双塔向量检索，用蒸馏得到的Transformer初始化双塔，平衡效果与推理性能

  - 降级机制设计：蒸馏模型输出的sigmoid置信度校准性好，低于阈值的抽象query可触发词法检索/人工规则fallback，降低bad case率'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统电商搜索依赖词法匹配（BM25、TF-IDF），面对会话式、转述型、意图型用户query时存在严重的词汇不匹配问题，召回效果极差；同时标注大量对话式搜索的query-商品关联数据成本极高，新场景冷启动困难。

### 方法关键点
- 任务重构：将会话式商品检索转化为极端多标签分类（XMLC）任务，直接输出对应商品ID的分类结果
- 伪标签蒸馏框架：用无监督TF-IDF计算商品文本元数据的余弦相似度，取Top50近邻作为伪标签，作为teacher的知识信号，无需人工标注
- 学生模型：基于DistilBERT加极端多标签分类头，用多标签BCE loss训练，训练和评测阶段严格mask掉商品自身的标签，避免指标虚高
- 基线bug修复：修正了过往工作中TF-IDF相似度索引与分类标签索引不对齐的问题，保证teacher基线的upper bound可信

### 关键实验
实验基于Amazon Reviews '23数据集，包含5.4万件商品、27个均衡类目，采用85:15分层拆分。对比TF-IDF teacher基线：DistilBERT学生模型P@1=93.15%（达到teacher效果的94.95%），NDCG@10=0.8845（达到teacher效果的93.91%）；10类典型会话式query评测中，词法模型完全失效的场景下，学生模型可正确理解用户意图召回相关商品。

### 核心结论
低成本的无监督词法知识蒸馏可以快速让Transformer获得优于词法匹配的语义检索能力，是电商搜索冷启动阶段的高性价比方案。
