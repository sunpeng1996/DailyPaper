---
title: 'Semantic Bundling: Interactive Node and Edge Bundling to Simplify Knowledge
  Graphs using Large Language Models'
title_zh: 基于大语言模型的语义捆绑：交互式节点边聚合简化知识图谱
authors:
- Adam Coscia
- Zeyu Hua
- Eric Krokos
- Timothy Lin
- Alex Endert
affiliations:
- Georgia Institute of Technology
- DOD
arxiv_id: '2608.04002'
url: https://arxiv.org/abs/2608.04002
pdf_url: https://arxiv.org/pdf/2608.04002
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: 知识图谱简化 · LLM驱动交互式分析
tags:
- Knowledge Graph
- LLM
- Graph Summarization
- Visual Analytics
- Sensemaking
one_liner: 提出LLM驱动的语义捆绑技术，通过超节点、超边聚合简化知识图谱并保留证据溯源能力
practical_value: '- 电商商品关联、用户行为KG可复用超节点/超边聚合逻辑，解决大规模KG「毛团」问题，支撑运营快速洞察商品关联模式、用户群体共性，降低人工分析成本

  - 可直接复用摘要-三元组-源文档的全链路溯源方案，约束LLM仅基于现有KG三元组生成聚合内容，大幅降低幻觉率，适配电商风控、合规审计等高可靠性要求的场景

  - 超边多跳路径聚合能力可迁移到推荐召回链路的隐性关联挖掘，比如挖掘用户与商品的多跳语义关联，补充召回特征，提升冷启动场景下的推荐准确率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有知识图谱（KG）随着实体和关系规模增长，极易形成难以解读的「毛团」结构，传统图简化技术仅优化可视化结构，丢失了语义信息，且无法关联原始证据；同时LLM直接生成的KG摘要易出现幻觉，缺乏溯源能力，无法支撑高可靠性的业务分析场景。
### 方法关键点
- 核心设计两类语义捆绑操作：超节点聚合用户选定的子图区域，生成语义标签与自然语言摘要，同时保留子图的结构特征；超边聚合两个节点间的多条直接边或多跳路径，生成高层级关联关系
- 全链路溯源机制：约束LLM仅基于选定范围内的三元组生成内容，将摘要的每句话与支撑的三元组关联，三元组进一步关联原始源文档，所有生成结果均可追溯到原始证据，大幅降低幻觉
- 落地为开源系统AgentK，支持从原始文本自动抽取三元组构建KG、交互式点选/框选触发捆绑操作、自定义聚合粒度（按主题、指定分组数、自动聚类），适配不同分析需求
### 关键实验
在IMDb《星际穿越》影评数据集、KRONOS情报分析数据集上做场景化验证：800篇文档规模的KRONOS数据集下，分析人员可在10分钟内完成核心实体定位、绑架案关联线索挖掘，效率较人工逐篇阅读提升90%以上；影评数据集上可快速聚合出电影评价核心主题、演员与导演的隐性关联，无需人工梳理数千条三元组。
### 核心结论
LLM驱动的知识图谱简化必须把语义保留和全链路溯源放在第一位，不能为了可视化简洁牺牲结果的可靠性
