---
title: 'SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking'
title_zh: SHELF：面向多任务书目基准测试的合成评估框架
authors:
- Michael J. Bommarito
arxiv_id: '2609.03047'
url: https://arxiv.org/abs/2609.03047
pdf_url: https://arxiv.org/pdf/2609.03047
published: '2026-09-02'
collected: '2026-09-06'
category: Eval
direction: LLM 多任务基准评估框架构建
tags:
- Benchmark
- LLM Evaluation
- Synthetic Data Generation
- Information Retrieval
- Text Classification
one_liner: 基于国会图书馆词汇生成6万+可控基准文档，构建覆盖多任务的书目场景LLM评估框架
practical_value: '- 可复用SHELF的合成基准生成逻辑，基于业务类目、文案规范生成电商商品、广告文案等垂域可控评测数据集，规避真实数据泄露、分布偏移问题

  - 可参考其多任务分层评估范式，为搜推广场景的召回、分类、匹配任务构建统一的模型选型评测管线，同时对齐效果、耗时两个核心指标

  - 验证了稀疏方法（TF-IDF、BM25）在简单分类任务上仍有竞争力，业务中低复杂度任务无需强行上大模型Encoder，可大幅降本提效'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
图书馆/档案机构缺乏适配书目场景的系统化评测基准，无法在有限算力、人力预算下完成多任务处理模型选型，通用基准的效果排名也难以迁移到垂域场景。
### 方法关键点
1. 开发Python框架SHELF，输入标注类目、写作规范、生成预算即可自动生成可控评测数据与对应任务；
2. 基于美国国会图书馆词汇生成62899篇合成文档，覆盖分类、聚类、检索、配对分类、指令检索5类任务；
3. 支持独立控制书目特征维度，可生成模型训练 cutoff 时间点后未见过的全新验证文档。
### 关键结果
主题分类任务最优准确率达0.8887，体裁分类仅0.2605，部分配对/聚类任务效果接近随机；稀疏检索方法在分类任务上效果仍具竞争力，TF-IDF是主题分类任务中速度最快的方案；合成基准的模型相对排名可迁移到真实场景，但绝对得分无法直接对应生产精度。
