---
title: 'Predicting Custom-Feed Returns for New Bluesky Posts: A Prospective Study'
title_zh: Bluesky新帖冷启动自定义Feed路由预测前瞻性研究
authors:
- Yipeng Wang
- Mohit Singhal
affiliations:
- Northeastern University
arxiv_id: '2608.13874'
url: https://arxiv.org/abs/2608.13874
pdf_url: https://arxiv.org/pdf/2608.13874
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 去中心化社交 · 内容冷启动排序
tags:
- Cold-Start Recommendation
- Learning to Rank
- Decentralized Social Media
- Reranking
- Benchmark Dataset
one_liner: 提出去中心化社交平台新帖冷启动Feed路由任务，构建基准数据集并验证LambdaRank排序效果最优
practical_value: '- 新内容冷启动路由场景可复用「多通道召回+轻量语义特征+树模型排序」的低成本架构，无需端到端大模型即可取得不错效果

  - 冷启动标签缺失场景可参考「先收集内容再后续打标」的前瞻性数据集构建方法，从根源避免时序泄露问题

  - 性能瓶颈诊断可采用候选集天花板计算方法，明确损耗来源是召回还是排序，指导迭代优先级

  - 排序优化时固定语义embedding（如MiniLM）接入LambdaRank的方案性价比极高，低算力消耗下即可显著提升NDCG、Recall指标'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统冷启动推荐仅解决新用户/新物品问题，而Bluesky这类去中心化社交平台存在全新场景：新发布内容为冷启动对象，独立运营的自定义Feed为候选集，需要预测新帖会被哪些Feed收录返回，该冷启动路由任务是Feed生态内容分发的核心基础，过往研究未覆盖该预测目标。

### 方法关键点
- 数据集构建采用「先收集公共帖、后续24小时内逐小时轮询Feed Top50结果打标」的前瞻性范式，避免时序泄露，覆盖5000个自定义Feed、1780.4万条公开帖、186.5万条帖-Feed返回记录
- 召回阶段采用6路并行通道：作者-Feed历史匹配记录、词级别TF-IDF相似度、字符级TF-IDF相似度、MiniLM语义相似度、话题标签相似度、历史返回量，合并得到最多370个候选Feed
- 排序阶段构造27维交叉特征（含4维MiniLM语义embedding特征），对比多类基线：单特征基线、点wise HGB分类模型、语义增强HGB、LambdaRank排序模型

### 关键结果
测试集共666.17万条帖，其中9.04%有至少一个正样本标签，采用两个24小时时序分折验证：LambdaRank效果最优，平均capped Recall@10 0.7361、NDCG@10 0.6127、Hit@10 0.7749，比语义增强HGB高0.0051 cR@10、0.0155 NDCG@10，比纯统计特征HGB高0.0313 cR@10；候选集天花板capped Recall@10为0.8448，说明当前性能瓶颈主要来自召回阶段（占性能损耗的58.8%）。

**最值得记住的一句话**：冷启动内容路由场景下，多通道召回+轻量语义特征接入树排序模型的低成本方案，性能远超过单特征基线，且召回优化的优先级高于排序优化。
