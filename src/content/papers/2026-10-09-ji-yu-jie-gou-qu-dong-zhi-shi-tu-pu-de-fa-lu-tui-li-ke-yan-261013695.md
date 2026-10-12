---
title: Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge
  Graph
title_zh: 基于结构驱动知识图谱的法律推理可验证检索方法
authors:
- Ibrahim Siddig
- Sviatoslav Tugeev
- Munir Georges
affiliations:
- Technische Hochschule Ingolstadt
arxiv_id: '2610.13695'
url: https://arxiv.org/abs/2610.13695
pdf_url: https://arxiv.org/pdf/2610.13695
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: Graph-RAG 可验证检索优化
tags:
- Graph-RAG
- Knowledge-Graph
- Chunking-Strategy
- Retrieval-Efficiency
- Legal-Reasoning
one_liner: 构建德国联邦法律结构KG，对比多组KG感知分块与检索策略，提升法律RAG的检索精度和token效率
practical_value: '- 结构化内容（电商商品属性、平台规则、售后政策等层级文档）可效仿结构驱动KG构建方法，按天然层级做分块，比固定长度naive分块token效率高3倍，适合规则类、条款类内容的RAG场景

  - 检索评价可参考ToER（token效率召回率）指标，平衡召回效果和token消耗，避免盲目增大chunk size或上下文长度带来的冗余成本，尤其适配大流量RAG服务的成本优化

  - 1-hop检索扩展策略中，仅扩展引用关联的节点性价比最高，父节点扩展会带来大量token冗余，电商场景下做关联商品、关联规则召回时可优先选择跨节点引用的轻量扩展，避免冗余内容占用上下文'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
高可靠场景（法律、医疗、电商合规/售后/规则问答）下的RAG要求检索结果可溯源、可验证，现有朴素RAG在大语料规模下容易遗漏关键上下文，且固定长度分块策略容易出现token冗余或粒度不匹配问题，检索结果的精度和资源消耗难以平衡；尤其法律场景下法条引用错误会带来严重后果，亟需兼顾检索准确率、可验证性和token效率的方案。

### 方法关键点
- 构建德国联邦法律结构KG：包含58部法典、16.8万节点、24万条边，覆盖8层层级结构，内置法条内部跨引用边，每个节点绑定对应文本片段
- 对比5种KG层级分块策略（从粗到细：§/Absatz/Satz/Nummer/Buchstabe），与100词固定长度的naive分块基线做对比
- 测试3种1-hop检索扩展策略：仅扩展父节点、仅扩展引用节点、混合扩展，提出ToER（每千词token效率召回率）指标，消除chunk大小对召回评估的偏见
- 采用深度分层前缀匹配规则评估召回结果，适配不同粒度的引用验证需求

### 关键结果
在12037份德国联邦法院判例数据集上测试：
- 最优分块策略（Nummer/Satz层级）的ToER比naive分块高3倍，Code层级ToER达14.23（基线4.19），§层级达3.25（基线1.10）
- 仅扩展引用节点的1-hop策略可稳定提升ToER约5%，父节点扩展计入token成本后ToER反而下降70%以上
- 分块粒度是影响检索效率的核心因素，不合适的粗粒度分块（如§层级）性能甚至低于naive基线

对天然具备层级结构的文档，基于结构KG的粒度适配分块+轻量引用关联扩展，是兼顾检索准确率和token效率的最优方案
