---
title: 'Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA
  Extraction and Biological Interpretation'
title_zh: 基于GraphRAG的自动化富集分析：多数据库ORA高效提取与生物学解读
authors:
- Guangcan Li
- Shuyuan Zheng
- Jiayao Liu
- Shigeto Seno
- Makoto Onizuka
affiliations:
- Graduate School of Information Science and Technology, The University of Osaka,
  Japan
- The First Affiliated Hospital of China Medical University, China
arxiv_id: '2610.30710'
url: https://arxiv.org/abs/2610.30710
pdf_url: https://arxiv.org/pdf/2610.30710
published: '2026-10-22'
collected: '2026-10-26'
category: RAG
direction: GraphRAG 跨源知识整合与生成解读优化
tags:
- GraphRAG
- Knowledge Graph
- Cross-Database Retrieval
- Faithfulness Evaluation
- LLM Generation
one_liner: 提出融合知识图谱的GBOR-RAG框架，实现跨数据库ORA的高效可溯源生物学解读
practical_value: '- 跨源异构数据统一建模可复用「知识图谱+关联实体连通」思路，替代分散查询降低延迟，适合多商品库/内容库的推荐召回场景

  - 子图检索后喂给LLM生成的范式，可迁移到电商商品关联解释、用户评价归因等生成式推荐场景，提升输出可信度

  - 声明级忠实度评估方法可复用，用来校验RAG生成的推荐理由、营销文案是否和底层召回的商品/用户数据一致，减少幻觉'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统ORA分析结果分散在多个基因集数据库，以扁平词表呈现，掩盖了相关富集信号间的基因级关联，查询效率低，生成解读的可追溯性差。
### 方法关键点
1. 将异构基因集数据库构建为统一的术语-基因知识图谱，用共享基因连通跨源相关术语；
2. 图基ORA打分后检索紧凑连通证据子图，保留跨源关联和基因级支撑信息；
3. 子图作为LLM输入生成生物学解读，新增声明级忠实度指标校验生成内容的证据匹配度。
### 关键结果
图基ORA和传统结果Pearson相关系数均值0.997，查询时间中位数降低37×（最高48×）；检索子图平均36.8节点，整合得分4.12；生成内容声明级忠实度达0.90，新增PubMed文献层后解读质量从4.17提升至4.75。
