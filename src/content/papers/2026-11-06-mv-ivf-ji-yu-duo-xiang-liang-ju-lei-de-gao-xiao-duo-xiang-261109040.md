---
title: 'MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering'
title_zh: MV-IVF：基于多向量聚类的高效多向量检索索引
authors:
- Kishen N Gowda
- Laxman Dhulipala
- Lars Gottesbüren
- Rajesh Jayaram
affiliations:
- University of Maryland
- Google Research
arxiv_id: '2611.09040'
url: https://arxiv.org/abs/2611.09040
pdf_url: https://arxiv.org/pdf/2611.09040
published: '2026-11-06'
collected: '2026-11-09'
category: RAG
direction: 多向量检索 · 原生IVF索引优化
tags:
- Multi-Vector Retrieval
- IVF Index
- MaxSim
- Clustering
- ANN Search
- Quantization
one_liner: 提出原生适配多向量检索的IVF索引MV-IVF，大幅降低检索延迟提升吞吐
practical_value: '- 电商语义搜索/商品召回、RAG知识库检索等多向量检索场景，可直接替换现有单向量代理的检索流程，90% Recall-10@10下最高可获得8倍延迟降低、173倍QPS提升

  - 多向量聚类可直接复用MV-Lloyd设计：点云分配后中心更新退化为扁平化嵌入的加权s-means问题，无需开发复杂多向量聚类算法，直接复用现有成熟k-means优化库

  - 分层量化、查询压缩、批处理调度等系统优化trick可直接迁移：路由/粗筛/精排阶段分别用4bit/1bit/8bit量化，Ward法压缩query嵌入，按叶子分组调度批查询复用缓存，精度损失极小的前提下大幅降本提效

  - 高并发多query场景优先选择MV-IVF架构，相比图索引、单向量代理方案批处理性能优势显著，适配电商大促、实时搜索等高QPS场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多向量检索（如ColBERT的token级嵌入表示）通过细粒度的set-to-set交互（如MaxSim）实现远超单向量检索的精度，是当前语义搜索、RAG系统的核心技术。但现有工业界方案多通过单向量代理做候选召回，存在不可避免的精度损失；原生多向量索引多为图架构，批处理性能差、构建成本高，缺乏可大规模落地的高吞吐、低延迟原生多向量IVF索引方案。
### 方法关键点
- 提出MV-Lloyd聚类算法，适配多向量点云的Chamfer距离聚类目标，固定点云到簇的分配后，簇中心更新退化为扁平化嵌入的加权s-means问题，可直接复用现有成熟的单向量聚类优化能力
- 基于MV-Lloyd递归构建分层IVF树，内部节点存储点云形心，查询路由直接使用query与形心的MaxSim打分，无单向量代理转换带来的精度损失
- 配套系统优化：分层低bit量化（路由用4bit、粗筛用1bit、精排用8bit）、Ward法聚合冗余query嵌入实现查询压缩、按叶子分组调度批查询复用缓存，进一步降低计算和内存开销
### 关键实验
在BEIR、LoTTE共8个公开文本检索数据集上，对比SVH、MUVERA、MV-Vamana等主流多向量检索方案，90% Recall-10@10下，单query延迟最高降低8.03倍，批处理QPS最高提升173.5倍；相比FastPLAID、IGP等现有开源方案，吞吐量高1-2个数量级，同时构建时间、索引大小均处于工业界可接受的合理区间。
### 核心结论
原生多向量IVF索引完全可以替代现有单向量代理的多向量检索架构，在精度无损的前提下实现数量级的吞吐提升，是大规模多向量检索落地的首选方案
