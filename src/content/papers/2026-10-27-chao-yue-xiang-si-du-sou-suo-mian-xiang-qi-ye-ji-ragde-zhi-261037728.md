---
title: 'Beyond Similarity Search: Knowledge Graph Metadata Enrichment for Enterprise
  Retrieval-Augmented Generation'
title_zh: 《超越相似度搜索：面向企业级RAG的知识图谱元数据增强方法》
authors:
- Fakabbir Amin
arxiv_id: '2610.37728'
url: https://arxiv.org/abs/2610.37728
pdf_url: https://arxiv.org/pdf/2610.37728
published: '2026-10-27'
collected: '2026-10-30'
category: RAG
direction: 企业级RAG · 知识图谱增强
tags:
- RAG
- GraphRAG
- Knowledge Graph
- Enterprise Search
- Entity Disambiguation
one_liner: 在SEC EDGAR金融数据集上对比三类RAG架构，验证GraphRAG在多跳问答场景的准确率与安全性优势
practical_value: '- 电商跨多源数据（用户/订单/商品/合规）问答场景，可复用「实体ID先解析+确定性关系遍历+精准文本召回」的两段式GraphRAG架构，避免纯向量搜索的实体混淆问题，比如用户查询「我买过的XX品牌手机的售后政策」，先解析用户ID、商品ID再遍历关联关系，召回准确率远高于纯向量搜索

  - 对幻觉容忍度极低的合规问答、商品资质查询场景，可借鉴「所有关系边绑定唯一溯源ID（如商品ID、合规文件编号、订单ID）」的设计，从结构上消除同名实体混淆导致的幻觉，且所有回答可溯源

  - RAG架构选型可参考本文适用边界：纯结构化聚合查询优先用Text-to-SQL性价比最高，单文档语义查询可采用「向量搜索+实体元数据过滤」的混合方案，跨源多跳问答再上GraphRAG，避免盲目全量部署GraphRAG导致token成本过高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业级RAG常需处理跨多源异构文档的多跳问答需求，传统向量相似度搜索无法编码「属于某实体」这类结构化属性，大规模下易召回同主题但非目标实体的内容；Text-to-SQL虽然处理结构化聚合查询高效，但多跳场景易出现Join逻辑错误、同名实体混淆问题，且动态元数据频繁重嵌入成本极高，亟需更适配企业场景的RAG架构。

### 方法关键点
- 数据集：抽取SEC EDGAR 12个月财报数据，包含16.7万份 filings、50.8万条风险因子文本chunk、43万节点/56万条边的知识图谱，所有边绑定来源文件唯一accession number实现全链路溯源
- 三类对比架构：① Text-to-SQL：提供全量表结构Prompt，LLM生成SQL执行后基于结果生成答案；② 向量RAG：all-MiniLM-L6-v2编码文本chunk，HNSW cosine召回Top8后生成答案；③ 两段式GraphRAG：LLM先生成Cypher查询解析核心实体ID，系统确定性遍历实体关联关系，按主键精准拉取对应文本片段后生成答案
- 评估规则：20道题分4类（单文档语义、结构化聚合、多跳关系+文本、跨文档实体消歧），每道题重复3次，采用确定性规则打分，无LLM评委避免评估幻觉

### 关键结果
- GraphRAG 20道题中16道三次尝试全对，总通过率50/60，无任何幻觉；Text-to-SQL 10道全对，总通过率36/60，出现6次同名实体混淆导致的幻觉；向量RAG仅3道全对，总通过率9/60
- 向量RAG在预期占优的单文档语义场景仅3/15通过，核心原因是大规模下向量无法编码实体归属属性，召回内容多为同主题但非目标公司的文本
- 多跳场景下GraphRAG通过率14/15，远高于两个基线的0/15；结构化聚合场景Text-to-SQL通过率15/15，GraphRAG仅6/15，token成本为Text-to-SQL的12.2倍

如果问题需要的多个事实从来没有共同出现在任何一个文本块里，再精准的排序算法也召回不到不存在的证据，此时必须引入结构化的知识关联能力
