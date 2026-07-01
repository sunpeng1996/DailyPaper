---
title: 'One Retrieval to Cover Them All: Co-occurrence-Aware Knowledge Base Reorganization
  for Session-Level RAG'
title_zh: 面向会话级RAG的共现感知知识库重组：一次检索覆盖全需求
authors:
- Shivam Ratnakar
- Yixuan Zhu
- Cecilia Cheng
- Chaya Vijayakumar
affiliations:
- University of Southern California
arxiv_id: '2606.31156'
url: https://arxiv.org/abs/2606.31156
pdf_url: https://arxiv.org/pdf/2606.31156
published: '2026-06-30'
collected: '2026-07-01'
category: RAG
direction: 会话级RAG · 知识库预重组优化
tags:
- RAG
- Session-level Retrieval
- Knowledge Base Organization
- Co-occurrence Clustering
- Hybrid Retrieval
one_liner: 通过离线共现感知聚类重组知识库，结合在线聚类扩展检索，提升会话级RAG的覆盖效率
practical_value: '- 电商客服、智能导购等会话式RAG场景，可复用离线共现聚类思路，用用户历史会话/浏览序列训练Word2Vec得到功能关联的文档/商品embedding，预分簇减少重复检索

  - RAG检索层可叠加轻量簇扩展逻辑：先召回top-kv语义匹配结果，再扩展其所属簇的所有候选重排，仅增加O(1)簇查表开销，即可大幅提升会话覆盖

  - 簇结构与语义编码器无关，一次离线聚类可兼容多个召回模型，适合多模态/多召回通路的业务RAG架构

  - 评估体系可直接借鉴：将session-level coverage、calls-to-τ-coverage加入RAG线上指标，更贴合用户全链路需求，替代单一query召回率指标'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统均针对单query语义匹配优化，而企业级用户的需求多以会话形式存在，相关文档可能分散在语义空间的不同区域，单query检索仅能覆盖41%的会话级需求，用户需要多次提问才能获取全部信息，大幅增加了交互成本与延迟。

### 方法关键点
- 离线阶段：构建三类共现序列（专家标注的相关文档组、语义邻域随机游走序列、QA驱动的模拟浏览序列），用Word2Vec CBOW训练得到文档的功能关联embedding，再通过层次聚类将知识库压缩为原大小的20%，簇内为用户常共同需要的语义异质文档
- 在线阶段：先召回top-kv语义匹配文档，再扩展所有召回文档所属簇的全部候选，对合并候选按语义相似度重排后返回top-k结果，保证原有单query精度损失可控

### 关键实验
在WixQA企业支持知识库（6221篇文档）、电商客服数据集上测试，对比Vanilla RAG、跨编码器重排基线：
1. 单query会话覆盖从41%提升至58%，绝对值+17%，跨4类语义编码器均稳定增益17%~21%
2. 达到70%会话覆盖所需的检索调用次数减少34%，跨6个功能域均有正向增益
3. 电商客服数据集上覆盖从32%提升至43%，绝对值+11%

### 核心结论
语义相似性和用户实际信息需求是两个正交信号，企业级RAG的核心评估指标应从单query召回率转向会话级覆盖。
