---
title: 'Search, Inspect, Fetch: Exploiting Boolean Retrieval for Deep-Research Agents'
title_zh: SIEVE：基于布尔检索的深度研究Agent搜索-检查-获取策略
authors:
- Shuai Wang
- Haodong Chen
- Yu Yin
- Shengyao Zhuang
- Bevan Koopman
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
arxiv_id: '2608.02751'
url: https://arxiv.org/abs/2608.02751
pdf_url: https://arxiv.org/pdf/2608.02751
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 检索工作流优化
tags:
- Boolean Retrieval
- Research Agent
- Context Efficiency
- Structured Document
- Retrieval Workflow
one_liner: 结合字段化布尔检索与分段读取，提升深度研究Agent准确率同时降低20.7%-50.6%的token消耗
practical_value: '- 电商商品/内容检索场景可复用字段化布尔检索逻辑：针对用户带属性的查询（如「2025年发布1T以上小米手机」），可让Agent自动生成带字段约束的过滤条件，先筛符合硬规则的候选再排序，既提升召回精准度，又降低后续排序算力消耗

  - Agent检索工具链可增加「结构预览-分段读取」流程：返回搜索结果时先给出标题、章节头、query相关短摘要，让Agent选择仅读取所需片段，大幅降低上下文token消耗，尤其适合长商品详情、攻略类内容的RAG场景

  - 布尔检索的fallback机制可直接复用：当带约束的查询返回空结果时，自动退化为仅用正关键词做全量召回，避免过严约束导致无结果，平衡精准性和召回率

  - 检索系统无需将文档打平处理：保留原生的标题、章节、属性等结构信息，不仅能提升检索效率，还能降低Agent读取无效内容的比例'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有深度研究Agent的Search-Visit工作流搜索后直接读取全页面，忽略网页/文档自带的标题、章节、元数据等结构化信息，既无法通过字段约束缩小召回范围，还会将大量无关内容带入上下文，导致准确率低、token消耗高的问题；同时专业领域常用的布尔检索过去人工编写门槛高，LLM Agent的出现让自动生成复杂布尔查询成为可能。

### 方法关键点
- 核心采用Search-Inspect-Fetch三步工作流：首先Agent自动生成带字段约束的布尔查询（BQL），先过滤出符合硬规则的候选集，再用可插拔排序器（支持BM25、稠密向量、融合排序）对候选排序
- Inspect阶段返回结构化结果卡：包含文档标题、章节列表、25个token的query相关摘要，支撑Agent快速判断有效章节
- Fetch阶段仅返回Agent指定的单个章节内容，而非全文档，大幅减少无效上下文引入
- 设计fallback机制：若布尔查询返回空结果，自动去掉约束用正关键词做全量排序召回，避免无结果问题

### 关键实验
在HotpotQA、MuSiQue、BCP-S三个QA数据集上测试，对比传统Search-Visit、Search-Fetch、DCI等基线，SIEVE默认BM25+稠密融合配置相比各数据集最优的Search-Visit基线，准确率提升0.7-3.1个百分点，同时token消耗降低20.7%-50.6%；该增益在9种排序器-数据集组合、3种不同Agent backbone、6种不同稠密编码器下均稳定存在。

### 核心结论
文档的结构化信息不是预处理的附属产物，将其贯穿检索、预览、读取全流程，能同时提升Agent检索的效果和效率。
