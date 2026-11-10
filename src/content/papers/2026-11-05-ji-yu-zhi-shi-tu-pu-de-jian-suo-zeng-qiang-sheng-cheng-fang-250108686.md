---
title: Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching
title_zh: 基于知识图谱的检索增强生成方法实现高效模式匹配
authors:
- Chuangtao Ma
- Sriom Chakrabarti
- Arijit Khan
- Bálint Molnár
affiliations:
- Aalborg University
- Bowling Green State University
- Eötvös Loránd University
arxiv_id: '2501.08686'
url: https://arxiv.org/abs/2501.08686
pdf_url: https://arxiv.org/pdf/2501.08686
published: '2026-11-05'
collected: '2026-11-10'
category: RAG
direction: 检索增强生成 · KG驱动模式匹配优化
tags:
- RAG
- Knowledge Graph
- Schema Matching
- Hallucination Mitigation
- LLM
one_liner: 提出融合多策略KG检索的RAG框架，解决LLM模式匹配的语义歧义与幻觉问题
practical_value: '- 多检索融合的KG-RAG框架可直接复用：向量检索+图遍历+重排序的子图召回流程，可迁移到电商场景下的商品属性对齐、异构商家类目匹配、语义检索query理解任务，无需重新训练LLM，冷启动成本低

  - 低相关上下文过滤trick可落地：给LLM添加few-shot指令要求对检索到的KG子图打0-10分，仅保留≥7分的上下文注入prompt，可应用于所有RAG系统减少无关信息干扰，降低幻觉

  - 向量检索选型结论可复用：语义对齐类任务中，RoBERTa生成嵌入、余弦相似度做距离度量、HNSW做索引的组合性能最优，可直接复用该配置搭建属性/类目匹配的向量检索模块'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统基于相似度的模式匹配方法无法解决复杂领域的语义歧义，纯LLM做模式匹配缺乏背景知识容易幻觉，现有RAG仅能检索非结构化文本，无法利用外部大规模KG的结构化语义知识解决跨表、跨领域的属性对齐问题。

### 方法关键点
- 采用KG-RAG4SM框架，支持4种子图检索策略：LLM直接检索子图、向量检索KG三元组、向量召回实体+BFS遍历3跳子图、LLM召回实体+BFS遍历，可适配通用/领域KG
- 设计双层重排序机制：先基于召回路径的高频相关关系打分，再归一化路径长度，优先选短且相关性高的子图减少上下文冗余
- 加入低相关子图过滤模块：通过few-shot指令让LLM给检索到的子图打相关性分，仅保留≥7分的知识注入prompt，降低上下文污染

### 关键结果
在医疗（MIMIC、Synthea等）、金融、影视共6个数据集上验证，对比SOTA LLM方法Jellyfish-8B，MIMIC数据集precision提升39.79%、F1提升30.56%；对比SOTA PLM方法SMAT，Synthea数据集precision提升69.20%、F1提升21.99%，无需微调LLM即可获得显著收益。

### 核心结论
外部大规模结构化KG的检索增强，是解决LLM在语义对齐类任务中幻觉问题的低成本高效方案，效果显著优于纯文本RAG。
