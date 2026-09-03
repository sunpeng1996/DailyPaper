---
title: Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
title_zh: 面向低成本检索模型选型的增量池化LLM评估方法
authors:
- Max Nelson
- Hanoz Bhathena
- Aviral Joshi
- Saket Sharma
affiliations:
- JPMorgan Chase
arxiv_id: '2609.02745'
url: https://arxiv.org/abs/2609.02745
pdf_url: https://arxiv.org/pdf/2609.02745
published: '2026-09-02'
collected: '2026-09-03'
category: Eval
direction: RAG检索评估 · LLM as Judge
tags:
- LLM-as-Judge
- RAG
- Retrieval Evaluation
- Cost Optimization
- Incremental Benchmark
one_liner: 提出增量池化LLM评估框架，复用标注大幅降低RAG检索模型选型成本
practical_value: '- 可直接复用增量池化评估流程做RAG检索组件选型：对多个候选检索模型的召回结果取并集做LLM标注，新增模型仅标注新增召回文档，最高可降4.9倍评估成本

  - LLM judge 可直接采用3档分级标注+结构化输出范式，温度设为0+固定模型版本，标注一致性可达93%+，系统排序与人工标注相关性达0.69~0.95，足以支撑选型决策

  - 检索模型选型时可优先测试BM25+embedding的hybrid配置：生产验证hybrid对低维度embedding的性能损失有补偿作用，同时对query改写的鲁棒性优于纯dense检索

  - 对存量已标注的query-文档对可建立统一评估池，后续新增检索组件、query改写策略的评估可直接复用，无需重复标注'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产RAG系统的检索模型选型依赖大规模相关性标注，传统人工标注成本高、迭代慢，独立用LLM标注每个候选模型又存在大量重复标注（不同模型召回结果重叠度高），无法支撑高频的检索模型迭代需求。

### 方法关键点
- 池化标注：对所有候选检索模型的Top-K召回结果取并集，仅对唯一的(query, document)对做LLM标注，复用标注计算所有模型的IR指标
- 增量扩展：新增候选模型时，仅标注其召回结果中不在现有池中的文档，原有标注100%复用，所有模型可在同一基准下公平比较
- 稳定性保障：P@k、DCG@k指标在池扩展时完全不变，Recall@k、AP、nDCG@k的单query pairwise排序保持不变，宏观排序仅在模型性能差距<0.001时可能出现无意义翻转
- LLM Judge设计：固定GPT-4.1版本+温度0输出，采用3档分级标注+短CoT结构化输出范式，保证标注一致性

### 关键实验
在4个公开检索基准（FiQA、TREC-COVID、NQ、FinRAG-V）+1个金融新闻QA生产场景测试，覆盖11个稀疏/稠密/混合检索配置：池化LLM排序与人工金标准的nDCG@10 Spearman相关系数达0.69~0.95，74%的排序分歧处于金标准本身的bootstrap采样噪声范围内，97%的pairwise排序关系和金标准一致；标注复用率达65%~80%，生产环境评估62个检索配置时成本降低4.9倍，总标注成本仅800美元。

### 核心结论
增量池化LLM评估是生产环境高频迭代检索组件的最优性价比方案，仅需对新增召回文档做标注即可实现跨模型的公平比较。
