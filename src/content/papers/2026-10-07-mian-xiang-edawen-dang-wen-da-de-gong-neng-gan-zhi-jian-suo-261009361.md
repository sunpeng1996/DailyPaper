---
title: 'From Chunks to Functional Evidence: Function-Aware Retrieval for EDA Documentation
  QA'
title_zh: 面向EDA文档问答的功能感知检索：基于功能单元的RAG优化
authors:
- Xiaotian Qiu
- Kairui Liu
- Shi Chenyi
- Jinyuan Deng
- Qi Sun
- Cheng Zhuo
affiliations:
- Zhejiang University
- Shanghai Innovation Institute
arxiv_id: '2610.09361'
url: https://arxiv.org/abs/2610.09361
pdf_url: https://arxiv.org/pdf/2610.09361
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG · 垂类专业文档检索优化
tags:
- RAG
- Document QA
- Hybrid Retrieval
- Hypergraph
- LoRA
- Technical Domain
one_liner: 将异构EDA文档构件组织为功能单元，结合混合检索大幅提升专业技术文档QA的RAG效果
practical_value: '- 垂类场景（电商规则/商品参数/帮助中心QA）RAG可复用功能单元组织逻辑：将同属一个功能/商品/活动的异构信息（参数表、文案、FAQ、规则）按实体锚点聚合成超边检索单元，解决碎片化信息召回不全问题

  - 混合检索架构可直接落地：并行检索聚合功能单元+原始chunk，再用双编码器加权重排，既能覆盖全量关联信息，又不丢失细粒度细节，论文实测可减少16.6%送入LLM的冗余token

  - 检索编码器训练可复用类型感知对比损失：构造硬负样本时加入语义相似但缺失所需信息类型的样本，让检索模型同时匹配语义和用户查询所需的信息类型，适配电商不同查询意图的召回优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG基于独立chunk检索，在专业技术文档（如EDA手册、电商商品/规则手册）场景下，支撑一个回答的信息常分散在不同类型的片段（代码、参数表、说明文案）中，语义相近但功能无关的chunk分数高度聚类，导致召回信息缺漏、相关性差，成为QA效果的核心瓶颈。

### 方法关键点
- 离线构建功能单元索引：解析文档结构抽取带类型的artifact（代码、表、文案、步骤等），以命令/实体为锚点，将同属一个功能的异构artifact聚合成超边形式的功能单元，保留所有原始chunk溯源路径，支持增量更新
- 训练功能感知编码器：基于Visualized-BGE-M3用LoRA微调，对比损失除InfoNCE外加入类型匹配排序损失，构造硬负样本（语义相似但缺失所需信息类型），让模型学会召回同时匹配语义和所需信息类型的功能单元
- 混合检索+重排：并行检索top-k功能单元（展开为原始chunk）和top-k原始chunk，去重后用双编码器（基础语义编码器+功能感知编码器）加权重排，选top-K作为生成上下文

### 关键实验
在自建EDADocEval-QA数据集（100条QA、33份OpenROAD文档）上，比Chunk RAG ROUGE-L提升37.1%、LLM-Score提升5.3分，比最强Graph RAG基线ROUGE-L提升55.6%；在公共ORD-MMBench基准上，比最强基线VISTA-RAG ROUGE-L提升30.0%、LLM-Score提升10分，检索Recall@5达0.917。检索延迟仅增加7ms，送入LLM的上下文token减少16.6%。

最值得记住的一句话：垂类RAG的核心瓶颈往往不是模型推理能力，而是检索单元的组织方式与用户查询所需信息结构的匹配度。
