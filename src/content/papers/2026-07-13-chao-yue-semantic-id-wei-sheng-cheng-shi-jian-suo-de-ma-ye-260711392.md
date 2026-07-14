---
title: 'Beyond Semantic IDs: Encoding Business-Value Ranking into Document Identifiers
  for Generative Retrieval'
title_zh: 超越Semantic ID：为生成式检索的DocID编码业务价值排序
authors:
- Gui Ling
- Zhihong Chen
- Yu Li
- Tong Xiong
- Kunhai Lin
- Kaixuan Zhang
- Yuliang Yan
- Dan Ou
- Haihong Tang
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.11392'
url: https://arxiv.org/abs/2607.11392
pdf_url: https://arxiv.org/pdf/2607.11392
published: '2026-07-13'
collected: '2026-07-14'
category: GenRec
direction: 生成式检索 · 业务价值编码DocID设计
tags:
- Generative Retrieval
- Semantic ID
- CRID
- DocID
- E-commerce Search
one_liner: 提出解耦语义聚类与业务价值排序的CRID DocID方案，淘宝3亿商品库落地提1.06% GMV
practical_value: '- 分层DocID设计可直接复用：前N层用语义聚类保证召回相关性，最后一层替换为业务价值（点击率/转化率/GMV等）排序，天然无碰撞且无需全量重训codebook

  - 增量更新技巧可迁移：新增商品仅需分配到最近语义簇，每日按最新业务指标全簇重排即可，适配电商高频上新场景

  - 语义簇大小调优框架可复用：通过分解个性化偏好与统计先验贡献，平衡top-K和深K召回效果，直接指导生产环境codebook配置

  - 推理优化技巧：分阶段动态调整beam size，早期语义聚类阶段用小beam，后期业务排序阶段用大beam，在保证召回率的同时降低推理延迟'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索的Semantic ID仅基于语义嵌入构建，存在两大核心痛点：一是大规模语料下ID碰撞严重，二是编码目标（语义重建）与业务优化目标（转化、GMV）存在天然 mismatch，成为生成式检索落地工业场景的核心瓶颈。

### 方法关键点
- 提出CRID（Cluster-Ranked Identifier），将DocID解耦为两部分：前N层为语义聚类前缀，通过查询-商品对对比学习得到的嵌入做RQ-KMeans量化生成，保证语义相关性
- 最后一层为业务价值排序token：每个语义簇内的商品按转化/点击等业务指标排序，将排序结果作为最后一层ID，天然实现ID无碰撞
- 增量更新机制：新增商品仅需匹配最近语义簇，每日全簇按最新业务指标重排即可，无需全量重训codebook
- 提出增益分解框架：将检索收益拆分为个性化偏好泛化和统计先验泛化，语义簇大小可调控两者的平衡，直接指导codebook配置

### 关键实验
实验基于淘宝3亿商品电商语料，backbone采用Qwen2.5-0.5B，对比包括RQ-KMeans、OPQ、Tiger、FORGE等主流DocID方案，以及工业界最强的EBR基线。核心结果：比最强DocID基线HR@20提升3.72pp、HR@1000提升9.10pp；比EBR基线in-search HR@20提升13.26%，out-of-search HR@20提升8.00%；全流量线上A/B测试GMV提升1.06%。

> 最值得记住的结论：生成式检索的DocID设计不需要盲目追求语义精度，将业务价值作为最后一层的排序信号，成本远低于复杂量化技术，收益反而更高
