---
title: What Makes a Good Semantic ID for Generative Recommendation? A Reproducibility
  Study
title_zh: 生成式推荐中优质Semantic ID的设计规律：可复现性研究
authors:
- Yufei Chen
- Junchen Fu
- Jujia Zhao
- Yukun Zhao
- Zhaochun Ren
affiliations:
- Shandong University
- University of Glasgow
- Leiden University
arxiv_id: '2609.24430'
url: https://arxiv.org/abs/2609.24430
pdf_url: https://arxiv.org/pdf/2609.24430
published: '2026-09-21'
collected: '2026-09-23'
category: GenRec
direction: 生成式推荐 · Semantic ID设计评估
tags:
- Semantic ID
- Generative Recommendation
- Reproducibility
- RQ-VAE
- OPQ
- T5
one_liner: 在统一实验框架下系统评测Semantic ID设计对生成式推荐的影响，给出落地选型指导
practical_value: '- 选型基线：优先选用RPG作为生成式推荐的初始基线，同时保留SASRec作为传统方法对比基准，避免盲目上线复杂生成式方案

  - 调优经验：不要盲目追求高codebook利用率、更长的Semantic ID、更大的T5底座，以上三者与效果无单调正相关，需根据业务数据集联合调优；RQ类ID优先选长度3，OPQ类ID优先选长度6作为初始值

  - 场景适配：若业务需要召回语义相似的item集合（如猜你喜欢、相似推荐场景）选用OPQ类Semantic ID；若需要保留top相似邻居的排序（如相关推荐、搭配推荐场景）选用RQ-Kmeans类Semantic
  ID

  - 诊断方法：codebook利用率仅适合用来检测ID坍缩/不平衡问题，不要作为ID质量的优化目标，避免过度正则化反而降低推荐效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐领域Semantic ID设计策略差异大，不同研究的数据集、模型底座、训练流程不统一，无法明确不同ID设计对推荐效果的真实影响，导致工业界选型缺乏可复现的指导依据。
### 方法关键点
- 搭建统一实验框架，固定70:13:17的全局时间拆分、多目标评估协议，在TIGER基准底座下仅替换Semantic ID实现，隔离ID设计的单一变量影响
- 从4维度系统评估：不同ID方案的相对推荐效果、codebook利用率与效果的关联、ID长度/底座大小的缩放规律、ID对局部item语义的保留能力
- 覆盖RQ-VAE、OPQ、RQ-Kmeans、树结构ID、metadata-based ID等主流构造方案，对比含/不含CF正则的多种实现
### 关键结果
在Amazon Video Games、Microlens-50K/100K、Yelp 4个公开数据集上，对比11种生成式推荐方案+SASRec传统基线：
1. 无全局最优ID方案，RPG在3个数据集上排名前2，平均NDCG@10领先基线TIGER约10.7%
2. codebook利用率与NDCG@10的Pearson相关系数仅为-0.02，无显著正相关
3. 语义保留方面OPQ的Jaccard@20比RQ-Kmeans高0.04左右，RQ-Kmeans的RBO@20比OPQ高0.01左右
### 核心结论
生成式推荐的Semantic ID设计没有万能方案，需结合业务场景的语义需求、数据集特性联合选择ID构造策略、长度和底座大小，不要盲目迷信单一设计的增益。
