---
title: 'MC-RAG System: A Structure-Driven RAG System for Multi-Constraint Queries'
title_zh: MC-RAG：面向多约束查询的结构驱动检索增强生成系统
authors:
- Xiao Zhang
- Yang Wan
- Yi Li
- Miao Xie
- Chunli Lv
affiliations:
- 中国农业大学
- 南洋理工大学
- 农业农村部农业信息化标准化重点实验室
arxiv_id: '2607.10151'
url: https://arxiv.org/abs/2607.10151
pdf_url: https://arxiv.org/pdf/2607.10151
published: '2026-07-11'
collected: '2026-07-14'
category: RAG
direction: 检索增强生成 · 多约束查询处理
tags:
- RAG
- Knowledge Graph
- Subgraph Matching
- Multi-constraint Query
- Indexing
one_liner: 将多约束查询场景下的RAG检索转化为知识图谱子图匹配问题，结合双嵌入索引实现高准确率可解释生成
practical_value: '- 电商多约束商品检索（如用户搜「高蛋白低卡含钙适合孕妇的零食」）可复用该框架，将query转化为商品属性KG的子图匹配，避免语义召回漏判约束

  - 双嵌入（语义标签嵌入+GNN结构嵌入）+R*-Tree索引的路径检索方案可直接复用，解决大规模KG下子图匹配效率问题，latency可控制在秒级

  - 智能导购Agent的多约束需求应答可借鉴约束校验逻辑，生成回答前先验证所有约束满足情况，大幅降低幻觉和错答率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统多依赖文本块语义相似度召回，处理多约束查询（如同时满足多个属性、关系要求的查询）时容易出现约束遗漏、事实幻觉，现有图RAG仅依赖局部结构相似度排序，无法保证所有约束精准满足，在电商导购、医疗咨询等强约束场景下落地性差。

### 方法关键点
- 离线层：从原始文档抽取实体和关系构建KG，对每条KG路径生成双嵌入：语义标签编码（LLM生成，捕捉节点语义）+结构主导嵌入（轻量GNN生成，捕捉路径结构模式），所有路径嵌入存入R*-Tree索引实现分层剪枝检索
- 在线层：先用LLM解析用户query的约束生成查询图，拆解为固定长度路径后通过R*-Tree做路径级语义+结构联合匹配，聚合匹配路径并校验约束，输出满足所有条件的子图作为证据喂给LLM生成答案，无精确匹配时自动退化为近似匹配或核心实体1跳邻居召回
- 支持全流程可视化，用户可查看query解析、子图匹配、约束校验的完整过程，可解释性强

### 关键实验
在覆盖20个领域、共20.6万条query、单条平均含4.6个约束的ERQA多约束数据集，以及Natural Questions单约束数据集上测试，对比NaiveRAG、GraphRAG、LightRAG、KAG以及GPT-5、Gemini-2.5等主流SOTA系统，Hit@1最高提升37.04个点，Recall最高提升42.45个点，F1最高提升0.40；端到端平均耗时10.8秒，其中子图匹配仅6-7秒，效率与KAG持平，离线索引构建总耗时11小时，可跨数据集复用。

### 核心结论
多约束查询场景下，结构匹配的优先级远高于语义相似度排序，可从根源上避免约束遗漏和幻觉。
