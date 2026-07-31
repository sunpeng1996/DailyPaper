---
title: 'GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation'
title_zh: GLM-RAG：基于图语言模型的图结构检索增强生成框架
authors:
- Maya Arseven
- Anette Frank
- Beni Egressy
- Johann Higl
- Moritz Plenz
affiliations:
- Heidelberg University
- Aleph Alpha Research
arxiv_id: '2607.28397'
url: https://arxiv.org/abs/2607.28397
pdf_url: https://arxiv.org/pdf/2607.28397
published: '2026-07-30'
collected: '2026-07-31'
category: RAG
direction: 图检索增强生成 · 多跳跨域推理优化
tags:
- GLM
- GraphRAG
- Multi-hop Reasoning
- Retriever
- OOD Generalization
one_liner: 用图语言模型替代GNN作为图RAG检索器，跨域多跳推理性能显著优于现有方案
practical_value: '- 垂直领域（电商商品知识图谱、售后知识库）多跳RAG场景可尝试用GLM替代GNN检索器，跨新类目/新场景零泛化能力提升明显，多跳查询召回比传统GNN高20%+。

  - 业务选型参考：单跳查询（商品属性查询、常见FAQ）直接用普通向量RAG即可，性能最优；需要跨实体推理的复杂查询（多条件组合商品检索、售后问题定位）才需要上Graph
  RAG。

  - GNN检索器低成本优化方案：给所有节点初始化静态句嵌入而非仅给种子节点赋值，域内多跳场景下效果可接近GLM-RAG，计算成本仅为GLM的1/10左右。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Graph RAG多依赖GNN检索器，仅能利用图结构+浅层语义嵌入，无法深度融合图节点/关系的文本语义，跨域泛化能力弱，复杂多跳查询召回率低；同时行业缺少不同检索器（向量/ GNN/ GLM）的适用场景清晰对比，业务选型无明确依据。

### 方法关键点
- 替换GFM-RAG的GNN检索器为端到端可训练的GLM检索器，保留预训练LM的语义理解能力，同时通过结构感知相对位置编码建模图拓扑，同时利用文本语义和图结构信息。
- 检索流程：提取查询种子实体周围子图，将三元组转成结构感知的token序列输入GLM编码，聚合节点token embedding得到节点表示，和查询向量匹配打分排序。
- 对比基线覆盖普通向量RAG、原生GFM-RAG、加入节点语义嵌入的GFM-RAG+，测试场景包含单跳/多跳、域内/跨域全维度。

### 关键实验
在3个维基百科多跳QA数据集域内训练，在11个跨域数据集测试：域内多跳场景下GLM-RAG和GFM-RAG+效果相当，Recall@2最高达79.6%；跨域单跳场景下普通向量RAG最优，比所有Graph RAG方法高5~15个百分点；跨域多跳场景下GLM-RAG显著优于所有基线，MultihopRAG数据集Recall@2达60%，比GFM-RAG高25.9%，比向量RAG高27.5%，G-Bench医疗/计算机科学数据集取得SOTA。消融实验显示GLM-RAG性能随模型参数增大持续提升，而GNN检索器会出现性能瓶颈。

### 核心结论
单跳查询用普通RAG足够，域内多跳可选用低成本的带节点语义的GNN RAG，跨域多跳复杂查询优先选GLM-RAG。
