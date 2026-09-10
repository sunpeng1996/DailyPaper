---
title: 'LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation'
title_zh: LiteRAG：基于图结构的低成本检索增强生成方法
authors:
- Daniel Alejandro Coll Tejeda
- Pedro García López
- Daniel Barcelona-Pons
affiliations:
- Universitat Rovira i Virgili
arxiv_id: '2609.10239'
url: https://arxiv.org/abs/2609.10239
pdf_url: https://arxiv.org/pdf/2609.10239
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: RAG · 图检索效率优化
tags:
- RAG
- GraphRAG
- Multi-hop Reasoning
- Token Efficiency
- Context Construction
one_liner: 提出无查询时LLM介入的图RAG方案，成本降99%、延迟降低超100倍
practical_value: '- 图检索场景可复用社区感知的hub惩罚机制，降低高热度通用节点导致的检索漂移，比如电商类目知识图谱检索时过滤跨类目的通用关联节点

  - 上下文构造阶段可将检索到的子图转成推理链形式，大幅压缩token占用，适合电商客服Agent、商品咨询问答等token预算敏感的场景

  - 锚点选择阶段可叠加语义+lexical+社区三重打分，提升多跳查询的初始锚点准确率，适配多条件商品搜索、跨属性关联的用户问题解答场景

  - 查询自适应阈值策略可根据初始锚点质量动态调整遍历范围，在知识库规模扩容时保持检索latency稳定，适合大体积商品知识库、电商内容库的RAG落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于图的RAG（如微软GraphRAG）依赖查询时LLM控制图遍历、社区摘要，导致latency高、成本高，返回的上下文冗余度高，多跳问答场景下token利用效率极低，无法适配大规模知识库落地需求。

### 方法关键点
- 锚点选择：融合语义相似度、lexical匹配、社区相关性三重信号筛选初始检索锚点，避免纯语义检索漏过精准领域实体/专有名词
- 子图扩展：采用查询自适应动态阈值+社区感知hub惩罚的纯算法遍历，完全移除查询时LLM介入，高热度跨社区节点会被加权过滤，减少检索漂移
- 上下文构造：将检索到的子图转成结构化推理链（实体-关系-实体描述），仅保留TopN高相关实体的关联关系，大幅降低上下文token量

### 关键实验
在DistComp（分布式系统论文多跳问答基准，最大1280篇文档）和UltraDomain（多领域公开基准）上对比GraphRAG全系列、LightRAG、HiRAG、LinearRAG等基线：DistComp上整体质量达0.798（全场最高），相对GraphRAG Global延迟降超100×、成本降超99%；UltraDomain上质量与LinearRAG持平，token用量降14×、成本降92%；固定2000token预算下其他基线质量下降2.1%~16.1%，LiteRAG无质量损失。

**最值得记住的一句话**：GraphRAG优化的核心不仅是找对相关证据，更要把证据以最高信息密度的形式喂给LLM。
