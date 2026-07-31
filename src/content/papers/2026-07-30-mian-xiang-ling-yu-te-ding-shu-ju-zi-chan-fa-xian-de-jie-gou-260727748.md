---
title: A Structured Knowledge Infrastructure for Domain-Specific Data Asset Discovery
title_zh: 面向领域特定数据资产发现的结构化知识基础设施
authors:
- Mengdi Chen
- Yuanxin Huang
- Yulin Jiang
- Wei Sun
affiliations:
- Xiaohongshu
arxiv_id: '2607.27748'
url: https://arxiv.org/abs/2607.27748
pdf_url: https://arxiv.org/pdf/2607.27748
published: '2026-07-30'
collected: '2026-07-31'
category: RAG
direction: 企业级RAG · 知识图谱检索优化
tags:
- RAG
- Knowledge Graph
- Enterprise Agent
- Data Asset Retrieval
- Scenario Annotation
one_liner: 小红书广告数仓落地的图谱引导检索+场景感知排序RAG架构，大幅提升企业数据资产检索效果
practical_value: '- 企业内部垂直领域RAG可复用三层知识库设计：高频资源O(1)路由+8节结构化分节标注文档+知识图谱社区聚类，通过意图切片可降低71.6×token消耗，平衡检索速度与准确率。

  - 检索排序可直接复用正负向场景标注方案：新增「不适用场景」负向抑制特征，单特征可带来25pp的Hit@10提升，效果远优于纯正向匹配。

  - 知识库更新可借鉴轻量闭环方案：采用LLM生成补丁+专家yes/no审批+30s热重载的流程，以极低人力成本解决schema漂移问题，适配更新频率不高的内部知识库场景。

  - 检索架构优先选择「图谱门控粗召回缩小候选集→细粒度排序」的两级串联方案，比并行融合噪声更低，可大幅减少后续排序与LLM的计算量。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业数据分析Agent面临两大核心问题：一是通用RAG检索数据资产准确率极低（Hit@10仅19.1%），二是返回结果缺少使用知识导致指标解读错误，根因包括高频词噪声、实体歧义、schema漂移、资产使用知识缺失四类，通用RAG、GraphRAG方案无法适配垂直领域数仓的高准确率要求。

### 方法关键点
- 三层双用途知识库：Tier1为高频资源O(1)关键词路由；Tier2为179份带8节结构化标注的文档，可按需返回480token的意图切片；Tier3为2859节点的知识图谱，划分474个Louvain社区支持候选集快速缩小。配套闭环更新管道，LLM生成补丁经专家审批后30s内热重载，解决schema漂移问题。
- 图谱引导检索器（GGR）：图遍历+7类意图路由双路径并行，先把候选集缩小到3-15个，大幅降低后续计算量。
- 场景感知排序器（SAR）：19类规则实体匹配+适用/不适用场景标注加权，负向不适用场景直接打-8分抑制误召回，最终返回按意图过滤的知识切片。

### 关键实验
基于小红书广告数仓5300+ Hive表、1200+ BI数据集（覆盖14个业务域），用两套各100题的生产查询benchmark对比无图谱无实体特征的BM25全库检索基线：Hit@10从19.1%提升至96.6%（+77.5pp），知识覆盖率从56%提升至77%（+21pp），端到端延迟4.84-5.33s满足SLA要求。

### 核心结论
在垂直专业领域，显式注入领域知识（图谱结构、意图路由、场景标注）的效果远优于通用嵌入方案。
