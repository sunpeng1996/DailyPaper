---
title: 'BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and
  Agent-Based Answer Generation'
title_zh: BIT.UA团队BioASQ 14B参赛方案：模块化检索与Agent式答案生成
authors:
- André Ribeiro
- Rúben Garrido
- Alexander Christiansen
- Richard A. A. Jonker
- Sérgio Matos
affiliations:
- University of Aveiro, Portugal
- Aalborg University, Denmark
arxiv_id: '2609.04999'
url: https://arxiv.org/abs/2609.04999
pdf_url: https://arxiv.org/pdf/2609.04999
published: '2026-09-04'
collected: '2026-09-08'
category: MultiAgent
direction: 多智体问答 · RAG检索优化
tags:
- Multi-Agent
- RAG
- BM25
- Dense Retrieval
- Query Expansion
one_liner: 提出pg_textsearch+Qdrant模块化检索与多Agent共识生成方案，在BioASQ 14B取得有竞争力成绩
practical_value: '- 检索层可复用pg_textsearch实现BM25检索+Qdrant稠密检索的混合架构，替代传统PyTerrier等框架，兼顾存储效率与GPU加速查询性能，适配电商商品/内容检索场景

  - 多Agent共识生成机制可迁移到电商智能客服、商品卖点文案生成场景，通过不同prompt的Agent辩论收敛输出，有效降低LLM生成幻觉，提升内容准确率

  - 检索阶段采用HyDE做query扩展+稠密检索负采样训练重排器的方案，可直接复用到搜索召回/重排管线，提升长尾query的检索匹配效果'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生物医学文献规模爆发式增长，现有问答系统存在检索效率低、生成答案幻觉高的问题，需重构全管线提升BioASQ生物医学问答任务表现。
### 方法关键点
1. 检索模块重构：用PostgreSQL pg_textsearch替代PyTerrier PISA做BM25检索，引入Qdrant做稠密向量索引支持GPU加速查询，搭配HyDE query扩展与Context-1检索策略；重排器训练引入稠密检索做负采样，提升排序精度。
2. 生成模块优化：引入LLM-as-a-judge框架，提出多Agent共识机制：不同prompt的多Agent迭代辩论，结合自适应文档留存策略收敛得到共识答案，首次参与片段生成子任务。
### 关键结果
所有批次取得有竞争力的成绩，Phase A文档检索在Batch 1、3的MAP排名第5，全量代码开源。
