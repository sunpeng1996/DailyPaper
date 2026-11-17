---
title: 'Living Context Graphs: Continual Semantic Learning for Enterprise Data Reasoning'
title_zh: 动态上下文图：面向企业数据推理的持续语义学习
authors:
- Varun Agrawal
- Ayush Srivastava
- Eshan Gujar
- Kaushal Kumar
- Ayush Gupta
affiliations:
- Genloop
arxiv_id: '2611.20976'
url: https://arxiv.org/abs/2611.20976
pdf_url: https://arxiv.org/pdf/2611.20976
published: '2026-11-16'
collected: '2026-11-17'
category: Reasoning
direction: 持续语义学习 · 企业数据推理
tags:
- Continual Learning
- Semantic Graph
- Text-to-SQL
- Enterprise AI
- Context Retrieval
one_liner: 提出无需修改底层数仓的动态上下文图LCG，提升企业文本转SQL准确率同时降低检索开销
practical_value: '- 电商/广告数仓的智能查询场景可复用LCG无侵入架构，无需修改原有数仓，直接从历史查询沉淀业务指标定义、类目关联等语义规则，大幅降低数仓改造成本

  - 落地数据类Agent的text-to-SQL/工具调用模块时，可借鉴LCG的增量学习机制，从用户验证通过的正确结果沉淀可复用语义映射，降低few-shot调用的token开销

  - 搜索推荐的query理解模块可复用LCG的动态淘汰逻辑，业务语义变更（如新类目上线、老指标调整）时自动淘汰过时映射，避免检索/推荐结果出错'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
企业AI落地的核心瓶颈并非模型能力，而是业务语义、指标定义、关联关系散落在非文档系统和员工经验中，底层数仓无内置语义信息，导致数据推理类任务准确率低、业务适配成本高。
### 方法关键点
提出独立的持续学习上下文层Living Context Graph（LCG），无需拷贝或修改底层数仓，核心设计包括：1. 从原始数据自动冷启动基础语义与关联关系；2. 服务查询时动态构建概念图索引业务上下文；3. 从验证通过的结果沉淀长期语义知识；4. 新结果与旧知识矛盾时自动淘汰过时语义。
### 关键结果
在BIRD数据集3个库共499条text-to-SQL样本上评估：冷启动阶段准确率提升4.6pp；仅用历史数据学习时，零接触跨域测试集准确率提升22.6pp，比同历史的5-shot检索高12.3pp；增量学习在所有库上都能在误差范围内达到one-shot效果；去掉图结构后准确率基本不变，但单查询成本升高2.3~3.3倍，中位数latency升高1.8~3.4倍。
