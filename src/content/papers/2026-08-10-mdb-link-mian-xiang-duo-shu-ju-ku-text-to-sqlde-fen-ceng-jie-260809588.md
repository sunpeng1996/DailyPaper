---
title: 'MDB-Link: Hierarchical Schema Linking for Multi-Database Text-to-SQL'
title_zh: MDB-Link：面向多数据库Text-to-SQL的分层Schema链接框架
authors:
- Beiyu Xu
- Zhenyu Wu
- Jiaoyan Chen
- Riza theresa Batista-navarro
affiliations:
- University of Manchester
- Faculty of Science and Engineering
- Department of Computer Science
arxiv_id: '2608.09588'
url: https://arxiv.org/abs/2608.09588
pdf_url: https://arxiv.org/pdf/2608.09588
published: '2026-08-10'
collected: '2026-08-11'
category: Other
direction: 多数据库Text-to-SQL · 分层Schema匹配
tags:
- Text-to-SQL
- Schema Linking
- LLM
- Reranking
- Information Retrieval
one_liner: 提出分层schema链接框架MDB-Link，大幅提升多库Text-to-SQL的匹配精度与推理速度
practical_value: '- 电商多异构数仓的Text-to-SQL自助查数场景可复用分层筛选架构：先通过全局列级索引初筛匹配库，再用LLM完成库、表、列的精筛，大幅降低LLM输入token成本。

  - 预算感知的LLM调用设计可复用：通过前置召回缩小下游任务输入范围，既提升生成准确率，又降低推理延迟，适合企业级高并发查询场景。

  - 列级全局索引+证据聚合的分层定位思路可迁移到跨域推荐场景：先通过全局语义索引定位目标业务域，再做细粒度item匹配，降低跨域推荐的计算开销。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统Text-to-SQL研究默认已知目标数据库，无法适配企业大规模异构数仓场景下需先定位目标库、再生成SQL的真实需求，多库场景下schema链接决策分层依赖，库选择错误会直接导致下游SQL生成失效。
### 方法关键点
提出MDB-Link分层schema链接框架：1）构建全局列级语义索引，召回与query相关的列，聚合检索证据初筛候选数据库；2）引入预算感知LLM，依次完成数据库重排序、表选择、列grounding，输出紧凑的SQL相关schema子集。
### 关键结果
基于Qwen2.5-14B实现，在MMQA、Spider2-Snow、BIRD-dev数据集上Exact Match分别较基线LinkAlign提升至51.41、9.17、38.01，推理速度优于LinkAlign与AutoLink，生成的schema子集大小接近金标准。
