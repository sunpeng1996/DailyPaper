---
title: 'DocPC: Document-Level Visual Retrieval via Representative Page Composition'
title_zh: DocPC：基于代表性页面拼接的文档级视觉检索框架
authors:
- Chengsong You
- Junwei Zhou
- Nan Du
affiliations:
- East China Normal University
- Matter Innovation Inc.
arxiv_id: '2608.25434'
url: https://arxiv.org/abs/2608.25434
pdf_url: https://arxiv.org/pdf/2608.25434
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: 文档级视觉检索 · RAG知识库索引优化
tags:
- Visual-Document-Retrieval
- VLM
- Contrastive-Learning
- Listwise-Ranking
- RAG
- Benchmark
one_liner: 通过拼接代表性页面为网格图实现高效文档级视觉检索，同时构建多正例基准DocViRe
practical_value: '- 电商场景下多页商品说明书、商家资质、合规文件的视觉检索，可直接复用前4页拼接2×2网格的索引方案，相比逐页索引降10.1倍存储、提效7.7倍，还能提升跨页语义匹配准确率

  - 存在多正样本的排序类任务，可借鉴多正例InfoNCE + 稀疏调度listwise损失的训练策略，每40步插入一次ApproxNDCG损失，平衡表示学习和排序优化效果，优于单用任意一种损失

  - 企业级知识库、电商服务助手的RAG检索模块，可迁移该框架替代逐页索引+MaxP聚合的现有方案，在教育、工业等跨页语义密集的场景增益尤为明显'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有视觉文档检索均为页级粒度，逐页索引的存储成本随页数线性增长，且分布在多页的关联语义无法被单页匹配捕捉；而企业搜索、法律审查、知识库RAG等大量场景都需要完整文档级的检索能力，当前既无成熟的高效框架，也缺乏对应的多正例标注基准数据集。
### 方法关键点
- 核心采用**代表性页面拼接（PC）**策略：从多页文档中选择K个代表性页面（默认取前4页），拼接为2×2网格的单张图片，仅需一次VLM编码即可得到文档级表示，索引成本从O(N)降至O(1)，无额外模型复杂度
- 适配文档级多正例特性的训练损失：组合多正例InfoNCE损失和稀疏调度的ApproxNDCG列表式损失，列表损失每40步执行一次，既避免把同批次其他相关文档误判为负样本，又针对性优化top-K排序效果
- 构建DocViRe文档级视觉检索基准：覆盖生物、教育、金融等7个领域，包含1.3w+查询、8k+文档，均带多正例相关性人工标注。
### 关键实验结果
在DocViRe数据集上，DocPC-ColQwen取得NDCG@5 44.09，比最强页级基线（38.91）高5.18个百分点；同时索引图片、向量、存储均降低10.1×，端到端索引时间降低7.7×；相同前4页的预算下，网格编码比逐页编码+MaxP分数聚合的方案高6.41个NDCG@5点。
### 最值得记住的一句话
跨多单元的语义匹配任务中，将多个关联单元拼接为统一输入让模型联合编码，比单独编码后再做分数聚合的效果和效率都更高。
