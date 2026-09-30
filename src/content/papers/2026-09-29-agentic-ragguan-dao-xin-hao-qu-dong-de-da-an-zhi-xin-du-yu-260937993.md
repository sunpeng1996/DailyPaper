---
title: 'BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from Agentic RAG Pipeline
  Signals'
title_zh: Agentic RAG管道信号驱动的答案置信度预测（NTCIR参赛方案）
authors:
- Julien Knafou
- Luc Mottin
- Alexandre Flament
- Paul van Rijen
- Esteban Gaillac
- Patrick Ruch
affiliations:
- HES-SO Geneva, Switzerland
- SIB Swiss Institute of Bioinformatics, Geneva, Switzerland
arxiv_id: '2609.37993'
url: https://arxiv.org/abs/2609.37993
pdf_url: https://arxiv.org/pdf/2609.37993
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agentic RAG · 置信度校准
tags:
- Agentic RAG
- Confidence Calibration
- Retrieval Augmented Generation
- Orchestrator
- Hybrid Retrieval
one_liner: 基于Agentic RAG管道原生信号与轻量规则实现高准确率的答案置信度校准
practical_value: '- 电商智能客服、商品问答类Agent可复用这套不依赖LLM自评估的置信度计算逻辑，基于检索、证据校验的原生管道信号输出置信度，避免LLM过度自信的幻觉问题

  - 多跳检索类场景（比如复杂商品属性查询、跨文档信息聚合）可参考多次去重检索的ensemble策略，多轮检索去重已召回内容能提升nDCG@20约0.07，多跳场景增益更显著

  - 业务系统的置信度校准不需要额外训练模型，仅基于管道已有的推理步数、证据一致性、多轮结果重合度等信号写简单规则，就能大幅提升校准效果，本案例中HMR从0.49提升到0.70

  - 可以借鉴提出的accHMR指标替代单纯的置信度校准指标，避免为了校准牺牲回答准确率，更符合业务中既要答得对也要敢拒答的需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG置信度校准方案多依赖LLM自评估、logits分析或标注训练，易受LLM幻觉干扰，且额外增加pipeline复杂度；同时现有评测指标常将准确率与置信度校准度分开评估，易出现为了校准牺牲回答准确率的问题，亟需一套无需额外训练、复用管道原生信号的置信度计算方案。

### 方法关键点
- 采用LLM与外置orchestrator解耦架构：LLM负责检索、阅读、记录证据，orchestrator负责证据校验（引号匹配+双模型entailment级联校验）、流程管控、置信度计算，全程不需要LLM自评估置信度
- 混合检索架构：sparse检索（Elasticsearch）+ dense检索（nomic-embed-text-v1.5）+ RRF结果融合 + cross-encoder重排，预标注实体补全文档内指代问题
- 多轮ensemble策略：每个query执行3-4轮检索，每轮排除之前轮次已召回的段落，提升召回多样性；置信度基于多轮结果一致性、证据数量、推理步数等管道原生信号计算，无额外模型调用
- 提出accHMR指标：准确率 × HMR（校准度harmonic mean），同时衡量回答准确率和置信度校准度，避免单纯优化校准度导致准确率过低

### 关键结果
在NTCIR-19 R2C2赛道64个评测query上：检索任务中多轮ensemble相比单轮检索nDCG@20提升0.0709，多跳、后处理密集场景分别提升0.0998、0.1824，位列该类场景赛道Top1；回答任务中原生pipeline准确率0.9219（赛道第6），叠加简单规则后准确率提升至0.9375（赛道第5），HMR从0.4915提升到0.6985，accHMR达0.6549（赛道第5）。

### 核心结论
Agentic RAG管道的原生运行信号已经包含足够的置信度相关信息，无需额外训练模型或要求LLM自评估，仅用简单规则即可实现兼顾高准确率和置信度校准的效果。
