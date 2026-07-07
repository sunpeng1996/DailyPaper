---
title: 'Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System
  Design and Empirical Analysis'
title_zh: 面向候选约束场景的检索增强生成系统设计与实证分析
authors:
- Yingdong Yang
- Haijian Wu
arxiv_id: '2607.04008'
url: https://arxiv.org/abs/2607.04008
pdf_url: https://arxiv.org/pdf/2607.04008
published: '2026-07-04'
collected: '2026-07-07'
category: RAG
direction: 检索增强生成 · 候选约束RAG优化
tags:
- RAG
- Retrieval
- Reranking
- LongEval-RAG
- MiniLM
one_liner: 提出候选约束场景下最优RAG pipeline，融合规则切块与后期MiniLM句子重排，多指标领先
practical_value: '- 电商/广告候选池约束RAG场景（如商品问答、营销文案生成、合规客服应答）可直接复用「规则固定切块+后期MiniLM句子重排」架构，比语义切块落地成本低，检索精度和信息覆盖度更优

  - 多召回结果融合优先采用RRF，搭配确定性查询扩展、伪相关反馈PRF，无需复杂语义召回即可在固定候选池内拿到可观的召回收益

  - RAG评估不能仅依赖LLM-as-judge，需结合检索精度、事实信息覆盖率、引用合规性等多维度指标，避免被流畅但事实性不足的生成结果误导

  - 可复用论文的确定性来源追踪方案，给每句生成内容绑定候选资源ID，满足电商内容合规、可溯源的业务要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LongEval-RAG场景要求所有检索证据、生成引用必须严格限定在给定候选文档集内，现有RAG方案要么过度依赖上游语义/主题切块引入误差传播，要么召回效率低、引用溯源能力弱，缺乏针对候选约束场景的端到端优化方案和系统性实证对比。

### 方法关键点
- 全链路候选约束：加载阶段仅读取查询关联的候选文档，所有检索、重排、生成、引用环节均不超出候选集范围，内置确定性来源追踪机制，每句生成内容可溯源至对应候选文档
- 召回层：融合确定性查询扩展、伪相关反馈PRF、多排序结果RRF融合，以BM25为基础排序，新增文档级引用先验、时间信号做轻量微调
- 证据选择：采用规则生成的140词、重叠1句的固定长度切块，后期仅对候选句子用MiniLM交叉编码器做重排，筛选Top10句子作为生成证据，避免上游切块误差传播

### 关键结果数字
基于CLEF 2026 LongEval-RAG的47条查询（每条对应10个候选文档），对比10种pipeline变体，最优rule-minilm方案拿下BERTScore 0.168、检索精度0.975、nugget覆盖率0.367、平均得分2.929，均为所有提交方案最高，比官方naive baseline检索精度提升726%。

### 核心结论
候选约束RAG场景下，最大性能收益并非来自上游复杂语义切块，而是稳定的规则切块搭配后期轻量句子级神经重排
