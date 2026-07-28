---
title: 'SINT-Flow: Schema Integration using Large Language Model Workflows'
title_zh: SINT-Flow：基于大语言模型工作流的Schema集成框架
authors:
- Keti Korini
- Christian Bizer
affiliations:
- University of Mannheim
arxiv_id: '2607.24492'
url: https://arxiv.org/abs/2607.24492
pdf_url: https://arxiv.org/pdf/2607.24492
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: LLM工作流 · 多源Schema自动集成
tags:
- Schema Integration
- LLM Workflow
- Self-Consistency
- Review Loop
- Benchmark
one_liner: 推出含5个LLM算子的端到端自动化Schema集成框架SINT-Flow及配套基准SINT-Bench
practical_value: '- 电商/广告场景多渠道异构数据（商品表、用户行为表）汇聚时，可复用5算子拆分的工作流架构，自动拆解含多实体的非规范化表，降低数据预处理人力成本

  - Schema匹配环节无需微调模型，直接叠加自一致性策略+review回环即可提升准确率，轻量易落地，可直接复用到商品属性对齐、跨站点类目Schema合并场景

  - 做Schema集成相关的业务效果验证时，可复用SINT-Bench的任务设计和评估指标，降低自建测试基准的成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统Schema集成方法无法处理包含多实体类型的非规范化源表，人工对齐异构数据源Schema成本极高，无法满足电商、广告等场景多渠道数据快速汇聚的需求。
### 方法关键点
1. SINT-Flow由5个可组合LLM算子构成工作流，支持端到端全自动化Schema集成
2. 可自动将包含多实体属性的非规范化源表，分解为单实体专属关系表
3. Schema匹配算子引入自一致性策略+review回环，无需微调即可提升效果
### 关键结果
在自建SINT-Bench（含10个集成任务、共93张关系表）测试：
- 以GPT-5.2或Qwen-3.6-27B为底座，实体类型检测F1≥96%，属性检测F1≥85%，Schema映射F1≥83%
- 消融实验验证自一致性、review回环均对效果有显著正向作用
