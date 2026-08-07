---
title: Mapping Similarity Spaces across Embedding Models with Synthetic Query Probing
title_zh: 基于合成查询探测的多嵌入模型相似度空间对齐方法
authors:
- Marcin Rozmus
- Peter van der Putten
affiliations:
- Pegasystems
- Leiden University
arxiv_id: '2608.05857'
url: https://arxiv.org/abs/2608.05857
pdf_url: https://arxiv.org/pdf/2608.05857
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: RAG 嵌入相似度校准与阈值迁移
tags:
- Embedding Calibration
- Synthetic Query
- RAG Optimization
- Similarity Mapping
- Threshold Transfer
one_liner: 无标注合成查询探测框架，支持跨嵌入模型相似度分数映射与检索阈值迁移
practical_value: '- 跨嵌入模型迁移时，可直接复用Synthetic Query Probing（SQP）流程，用LLM生成3级相关性的查询-文档对，无需人工标注即可快速校准相似度阈值，节省RAG系统换模型的适配成本

  - 同模型家族不同维度的嵌入转换优先用线性映射即可，跨不同厂商模型（如OpenAI ada到Titan）的转换优先选保序回归，比线性映射平均R²提升10%以上，MAE降低30%左右

  - 电商/企业知识库的检索阈值不能跨语料直接复用，异构内容的跨模型校准误差比同构科学语料高15%以上，必须基于业务语料单独做校准

  - 做RAG召回过滤时，若使用压缩分数空间的嵌入模型（如ada-002），需注意其无关/相关分数重叠度更高，优先选宽分数空间的模型（如Titan系列）可获得更优的精确率-召回率trade-off'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG系统中不同嵌入模型的相似度分数因几何结构、训练目标差异无法直接可比，原有校准阈值无法跨模型/语料迁移，导致更换嵌入模型时需要重新标注数据调参，大幅提升运维成本，现有研究多关注嵌入下游效果，未解决阈值跨模型迁移问题。

### 方法关键点
- Synthetic Query Probing（SQP）无标注框架：对目标语料的文档chunk，用LLM生成三类查询：可直接从chunk回答的PARAPHRASE、主题相关但需额外信息的RELEVANT、完全无关的IRRELEVANT，构造带伪标注的查询-文档对
- 直接建模相似度分数的映射关系而非嵌入空间对齐，对比线性回归、保序回归（isotonic regression）、分位数映射三种转换函数的效果

### 关键实验
- 测试数据集：公开SciFact科学语料、Pegasystems内部11万+企业文档语料，对比4种嵌入配置：Titan V2 256/512/1024维、OpenAI ada-002
- 核心结果：同模型家族跨维度转换R²最高达0.996，MAE低至0.01；跨模型转换中保序回归效果最优，Titan转ada的R²最高达0.945，MAE仅0.014；跨语料阈值差异可达6倍，直接复用阈值会导致精确率明显下降

### 核心结论
跨嵌入模型的相似度阈值首先是语料依赖的，同构语料的校准效果远优于异构内容，保序回归是跨模型分数映射的首选方案。
