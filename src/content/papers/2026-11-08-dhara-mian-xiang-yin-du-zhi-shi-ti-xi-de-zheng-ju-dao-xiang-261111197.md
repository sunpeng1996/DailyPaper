---
title: 'Dhara: Evidence-Oriented Retrieval for Indian Knowledge Systems'
title_zh: 《Dhara：面向印度知识体系的证据导向检索系统》
authors:
- Avinash Holenarasipur Nagendra
- Anand Kaniyaar Sriranga Prasad
- Rahul Vishwakarma
- Trupti Gavit
- Anish Amol Tipnis
- Yashaswini Mandayam Rangayyan
- Vinod Appajanna
- Kousik Sarathy Sridharan
- Mohan Raghavan
affiliations:
- Indian Institute of Technology Hyderabad
- HTSR Institute
- Central Sanskrit University
- Bheri Technology Foundation
- IBM (India)
arxiv_id: '2611.11197'
url: https://arxiv.org/abs/2611.11197
pdf_url: https://arxiv.org/pdf/2611.11197
published: '2026-11-08'
collected: '2026-11-10'
category: RAG
direction: 多分支RAG · 证据导向检索
tags:
- Hybrid Search
- Entity Notes
- Fuzzy Verse Retrieval
- Neural Reranking
- RAG
one_liner: 提出融合混合搜索、实体笔记、模糊检索和神经重排序的多分支检索引擎，在印度知识语料上优于基线检索效果
practical_value: '- 多分支检索架构可直接复用：直接检索+实体维度检索+特定文本片段模糊检索三个分支，用CombMAX融合结果且不扩大候选池规模，适合电商商品/评论/属性多模态检索、Agent知识库检索等场景

  - 实体笔记（EN）设计思路可迁移：预生成层级实体描述并关联原始内容，召回时先召回实体描述再映射到原始段落，可用于优化电商商品属性、商品百科类内容的召回优化

  - 模糊片段检索（FVR）可用于搜索场景：针对用户输入的不完整片段（如商品标题片段、口播内容片段）做模糊匹配召回，可用于搜索suggestion、片段式query召回等场景

  - 资源权衡方案可参考：BGE-M3单向量检索性能接近ColBERTv2，但延迟仅为1/9、存储仅为1/13，适合工业界资源受限的检索场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
印度知识体系（IKS）的证据分散在不同章节的段落、诗句、翻译、注释中，用户查询可能是概念问题、跨章节实体关联、半记忆的模糊片段，现有检索方法无法同时覆盖精准匹配、实体关联、模糊片段检索的需求，且效果与资源开销难以平衡。

### 方法关键点
- 多分支检索架构：分为直接检索分支、实体笔记（EN）分支、模糊诗句检索（FVR）分支，最终候选池规模与直接检索一致，不增加重排序开销
- 实体笔记（EN）：预生成章节级（CEN）和书籍级（BEN）实体描述，每条笔记关联原始源段落，召回时先召回实体笔记再映射到原始段落
- 模糊诗句检索（FVR）：从用户query中提取片段，生成拼写变体，通过子串和三元组匹配检索关联源段落，优先级高于其他结果
- 结果融合：两个分支分别重排序后用CombMAX融合结果，保留每个chunk取最高得分，最终结果规模与直接检索一致

### 关键实验
在Dhara Bench 325个标注查询、60121个源段落数据集上测试，对比BM25、ColBERTv2、Gemini：BGE-M3单向量检索nDCG@10、Recall@20、MRR@20全类别优于BM25，性能接近ColBERTv2，延迟0.108s vs ColBERTv2的0.962s，存储仅为后者1/13；加入实体笔记分支后nDCG@10在Qwen重排序下全12类均提升，BGE下10类提升；FVR使诗句类查询nDCG@10提升20个百分点；Qwen重排序效果全类别优于BGE，但耗时为BGE的6.72倍；加入EN和FVR的Qwen流水线在10类上Recall@20优于Gemini，多跳查询完整证据召回更强。

### 最值得记住的一句话
多分支异构召回+结果融合在不增加候选规模的前提下可显著提升检索效果，工业界可根据资源预算在效果和延迟间灵活选择组件。
