---
title: 'Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents:
  A Precision-Oriented Alternative to Learned Abstraction Trees'
title_zh: 面向长叙事文档的结构感知层次检索：学习抽象树的精度导向替代方案
authors:
- Rohit Singh
- Nathaniel Weems
affiliations:
- Independent Research
arxiv_id: '2611.29966'
url: https://arxiv.org/abs/2611.29966
pdf_url: https://arxiv.org/pdf/2611.29966
published: '2026-11-23'
collected: '2026-11-24'
category: RAG
direction: RAG 长文档层级检索优化
tags:
- RAG
- Hierarchical Retrieval
- Long Document QA
- BM25
- Delta Ingestion
- RAPTOR
one_liner: 利用长文档原生层级结构做两级粗精检索，精度优于扁平RAG与RAPTOR，索引维护成本更低
practical_value: '- 针对电商场景下有原生结构的规则文档、商品手册、品牌介绍、结构化评价集合，可直接复用两级检索架构：先用BM25+dense混合匹配做章节/品类级粗筛，再在筛选范围内做细粒度检索，减少无关内容干扰，提升RAG回答准确率

  - 可直接复用section-aware expansion开关策略：下游任务对干扰敏感（如广告合规审核、活动规则问答）时关闭开关保障精度，需要上下文连贯（如商品教程问答、客服回复）时开启开关提升MRR

  - 基于content-hash的delta ingestion方案可直接落地到RAG索引维护，电商商品信息、规则迭代时仅重嵌修改部分，实测可复用94%+的已有embedding，大幅降低索引更新成本

  - 工程落地避坑：OpenSearch做带过滤的ANN检索时，必须用kNN原生filter参数而非post-filter，避免小k场景下检索结果为空的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长文档RAG的扁平检索忽略文档原生层级结构，主流的RAPTOR学习抽象树需要递归聚类、重生成摘要，索引更新成本高，且返回的摘要节点覆盖范围过广，定位精度差，无法满足需要精准定位的长文档问答需求。

### 方法关键点
- 两级粗精检索架构：第一级用BM25+dense混合匹配查询与章节摘要，选出3~7个候选章节；第二级在候选章节内做原生过滤式稠密检索，避免全局ANN后过滤的空结果问题；第三级可选section-aware扩展，将Top检索块扩展为连续上下文，支持精度/排序效果的tradeoff
- 基于SHA-256 content hash的delta ingestion：仅对修改的章节/块重嵌，大幅降低索引更新成本
- 设计上直接复用文档原生结构，无递归聚类和多层摘要生成步骤，全链路除章节摘要生成外完全可复现、确定性

### 关键结果
- QuALITY基准：层级检索准确率81.0%，显著优于扁平检索的70.4%，与全文档输入的79.3%无统计差异，仅用1/4的上下文token量就达到长上下文天花板
- 自研5本公开书113个查询集：关闭扩展时精度比扁平检索高3.3pp（p=0.014），开启扩展时MRR提升0.055（p=0.040）；与RAPTOR对比，定位精度显著更高（p<0.001），无统计显著的准确率差距
- NovelQA 200K+token小说基准：层级检索与扁平检索准确率相当（55.7% vs 56.8%），聚合类问题优于扁平检索，局部事实类问题弱于扁平检索，明确了方法适用边界

### 核心结论
针对有原生结构的长文档，直接复用已有层级的检索方案，在精度和维护成本上远优于从零构建学习抽象树的方案，二者是互补而非替代关系
