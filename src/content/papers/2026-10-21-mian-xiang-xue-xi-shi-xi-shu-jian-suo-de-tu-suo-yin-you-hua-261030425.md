---
title: Getting a GRIP on Graph-Based Search for Learned Sparse Retrieval
title_zh: 面向学习式稀疏检索的图索引优化系统GRIP
authors:
- Vihan Lakshman
- Franco Maria Nardini
- Cosimo Rulli
- Rossano Venturini
affiliations:
- MIT CSAIL
- ISTI-CNR
- Linkup
- University of Pisa
arxiv_id: '2610.30425'
url: https://arxiv.org/abs/2610.30425
pdf_url: https://arxiv.org/pdf/2610.30425
published: '2026-10-21'
collected: '2026-10-23'
category: RecSys
direction: 稀疏检索 · 图ANN索引性能优化
tags:
- Learned Sparse Retrieval
- Graph ANN
- Inverted Index
- SPLADE
- Recall Optimization
one_liner: 融合倒排索引优势优化图ANN检索，在亿级稀疏检索场景下延迟超SOTA倒排2.5倍
practical_value: '- 电商/广告稀疏检索召回场景可直接复用term-based entry point seeding技巧，预存每个term权重Top-L的文档作为图搜索入口，实测可降低50%以上的图遍历无效计算，延迟提升2x左右

  - 可借鉴sparse sketching思路，检索路由阶段仅用向量Top-R个非零分量计算相似度，最终候选再用全向量重排，在召回损失<1%的前提下降低30%左右的距离计算开销

  - 大规模稀疏向量建图时可复用Sparse PiPNN思路，用倒排索引替代PiPNN的稠密矩阵乘计算分区内相似度，能把亿级语料的图构建时间从天级压缩到小时级，适配每日重索引的业务需求

  - 若业务已部署图索引做稠密向量召回，可参考GRIP架构复用现有图基建做稀疏检索，无需单独维护倒排索引链路，降低30%以上的检索系统维护复杂度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
业界普遍认为学习式稀疏检索（LSR）场景下图ANN索引性能远弱于定制化倒排索引，默认选择倒排作为LSR部署方案，但混合检索场景下需要同时维护图索引（稠密向量用）和倒排索引（稀疏用），架构复杂度高，且图索引的成熟生态无法复用，亟需优化图索引在LSR场景下的性能。

### 方法关键点
- term-based entry point seeding：离线预计算每个词汇对应权重Top-L的文档列表，查询时取query权重最高的T个term对应的文档作为图遍历入口，避免从固定入口遍历的无效计算
- 近似路由稀疏素描：离线为每个文档保留Top-R个最大权重分量作为素描向量，图遍历阶段仅用素描向量做相似度计算，最终候选再用全向量重排，因LSR权重非负，素描分数是精确分数下界，不会漏失有效结果
- 稀疏分区图构建（Sparse PiPNN）：修改PiPNN的稠密计算逻辑，用倒排索引计算分区内向量相似度替代原稠密矩阵乘，将图构建时间降低一个数量级，再加上一轮基于term种子的遍历优化边质量

### 关键实验
在MS MARCO v2（138M段落）SPLADE嵌入场景下，GRIP在95% recall@10下延迟比SOTA倒排索引Seismic低2.5倍，90%-98% recall@10区间延迟提升2.2-3.4倍；MS MARCO v1（8.8M段落）上比Seismic快1.4-1.7倍，SPARSEUP嵌入下92-95% recall@10快1.2倍；138M规模图构建时间7.3小时，满足日常重索引需求。

### 核心结论
图索引在LSR场景下并非天生弱于倒排，将倒排的结构优势融合进图索引设计，即可在大规模场景下获得比倒排更好的延迟性能，还可复用现有稠密检索的图基建。
