---
title: 'Similar but Not Redundant: Embedding-Gated Refinement for High-Granularity
  Topic Models'
title_zh: 相似但不冗余：高粒度主题模型的嵌入门控优化方法
authors:
- Daniel Denley
- Robert L. Nicol
- Mike J. Chantler
affiliations:
- Heriot-Watt University
- STMicroelectronics
arxiv_id: '2611.17030'
url: https://arxiv.org/abs/2611.17030
pdf_url: https://arxiv.org/pdf/2611.17030
published: '2026-11-12'
collected: '2026-11-13'
category: Other
direction: 高粒度主题建模 · 冗余话题过滤优化
tags:
- Topic Modeling
- Embedding
- LLM Judgement
- Redundancy Filtering
- Iterative Merging
one_liner: 提出嵌入门控迭代合并EGIM方法，精准区分高粒度主题的真冗余与相似差异化子话题
practical_value: '- 搜索Query细粒度意图聚类场景，可复用「embedding粗筛候选+LLM精判冗余」的两级架构，比纯LLM降本80%以上，比纯embedding准确率高

  - 电商商品/内容标签体系梳理场景，可直接套用EGIM迭代合并逻辑，既避免标签冗余，又能保留细分领域的差异化标签

  - 用户细粒度兴趣建模时，用该方法区分相似但不同的兴趣标签，减少推荐泛化错误，提升个性化推荐的区分度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
高粒度主题建模可提取上百个细分 niche 主题，但常被误归为「过聚类」故障；现有后处理方法（纯embedding阈值过滤、纯LLM引导合并）无法有效区分「语义相似但有实际价值的子话题」和「真冗余子话题」，无法满足高细分场景需求。
### 方法关键点
提出混合架构EGIM：1. 迭代生成富上下文的主题表示；2. 用embedding相似度全量召回候选合并对，缩小LLM判定范围；3. 调用LLM做最终判定，仅合并真冗余对，保留细分主题的差异化价值。
### 关键结果数字
在2个专利语料、1个法律语料上测试，embedding召回的候选对中83%被LLM判定为非冗余无需合并；相比纯LLM迭代基线，EGIM合并后主题的区分度提升25~55%，同时更好保留原始主题分布。
