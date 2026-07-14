---
title: Generative Chinese Statute Retrieval
title_zh: 生成式中文法条检索框架GCSR
authors:
- Yiteng Tu
- Zitao Su
- Weihang Su
- Xuanyi Chen
- Yueyue Wu
- Yiqun Liu
- Min Zhang
- Qingyao Ai
affiliations:
- Tsinghua University
- Quancheng Laboratory
- Renmin University of China
arxiv_id: '2607.11109'
url: https://arxiv.org/abs/2607.11109
pdf_url: https://arxiv.org/pdf/2607.11109
published: '2026-07-13'
collected: '2026-07-14'
category: Other
direction: 生成式检索 · 结构化DocID设计
tags:
- Generative Retrieval
- Structured DocID
- Legal IR
- Multi-task Training
- Sequence Generation
one_liner: 提出融合多粒度结构化DocID与多任务训练的生成式中文法条检索框架，性能优于各类基线
practical_value: '- 多粒度结构化DocID设计思路可复用在电商分层类目商品的生成式检索/推荐场景，将类目层级、属性语义嵌入ID编码，提升生成召回准确率

  - 把检索任务重构为序列生成问题的范式，可迁移到垂直领域垂搜（如商品规格检索、客服知识库检索）的端到端检索链路设计

  - 多任务训练融合领域结构知识的策略，可用于小样本垂直领域生成式检索模型的微调，降低领域标注数据依赖'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有法条检索方案难以弥合用户口语化法律查询与正式法条表述之间的语义鸿沟，传统稀疏、稠密检索方法对垂直领域结构化知识的适配性不足，无法满足法律RAG、法律咨询等下游任务的检索精度需求。
### 方法关键点
将法条检索重构为序列生成任务，提出GCSR生成式检索框架，把法条领域知识内化到生成模型中；设计融合法条层级结构信息与语义特征的多粒度结构化DocID，搭配多任务训练策略优化模型生成准确率。
### 关键结果
实验中GCSR全面优于稀疏检索、稠密检索、法律领域专用等多个强基线，验证了生成式检索在垂直领域检索场景的有效性，可直接支撑法律信息查询、司法推理等下游任务落地。
