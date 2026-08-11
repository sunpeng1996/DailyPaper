---
title: 'VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for
  Unified Reasoning over Hierarchical Enterprise Knowledge'
title_zh: VDGR-RAG：融合向量、目录、图与反思的层级企业知识推理框架
authors:
- Wenqi Chen
- Haofei Yang
- Rui Yang
- Fangming Li
affiliations:
- Huawei Technologies
arxiv_id: '2608.07994'
url: https://arxiv.org/abs/2608.07994
pdf_url: https://arxiv.org/pdf/2608.07994
published: '2026-08-08'
collected: '2026-08-11'
category: RAG
direction: 企业级RAG · Agentic GraphRAG优化
tags:
- RAG
- GraphRAG
- Agentic RAG
- Enterprise QA
- Hierarchical Knowledge
one_liner: 提出融合多检索范式的Agentic GraphRAG框架，大幅提升企业知识QA的召回与准确率
practical_value: '- 搭建业务内部知识库RAG时，可复用H2KG构建逻辑：同时保留文档目录层级、内容块、领域实体三类节点，打通结构与语义关联

  - 检索链路可直接套用多路由并行设计：向量+BM25混合检索做底，搭配TOC结构引导的范围检索、实体关联的PPR图检索，互补提升召回率

  - 针对多业务线（如不同品类/类目）知识库场景，可复用目录增强的路由机制，先将query匹配到对应业务域知识库，减少跨域噪声

  - 低资源场景下可按优先级拆解模块：先上向量检索+TOC路由的基础版，再逐步叠加图检索、反思、目录回溯模块，平衡效果与成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG方案针对层级结构复杂、术语重叠度高的企业级知识库（如电信产品文档、电商运营/商品类目知识库），普遍存在域路由不准、层级结构利用不足、检索范式单一的问题，导致召回率低、幻觉严重，无法支撑复杂知识推理需求。

### 方法关键点
- 离线构建Hierarchical Heterogeneous Knowledge Graph (H2KG)：包含目录节点、内容块节点、领域实体节点三类，边分为层级包含、实体存在、实体共现三种，自底向上生成各目录节点语义摘要
- 上线4类可组合Agent检索工具：1）目录增强路由工具：用域TOC树匹配query，路由到对应域H2KG，剪枝无关域；2）多路由检索工具：并行执行向量+BM25混合检索、TOC引导的结构化检索、实体PPR图检索三类路径，合并结果；3）目录回溯工具：召回不足时向上回溯父目录、检索同级节点补充上下文；4）动态反思工具：评估召回内容充分性，不足时生成优化query重查

### 关键实验
在华为电信4个领域（节能、故障管理、体验保障、通用数据集）共700个测试query上测试，对比LinearRAG、BookRAG等5个SOTA基线，VDGR-RAG在ES数据集上Retrieval Recall达98.5%、Answer Accuracy达97.6%，相对最优基线分别提升13.7%、22.7%，同时单query LLM调用量降低42.7%。

### 核心结论
向量、目录、图、反思四类能力分别解决不同的RAG失败场景，互补融合而非单一优化才能最大化企业级RAG的效果与效率。
