---
title: Comment-level Topic Drift Analysis in the Reddit Corpus
title_zh: Reddit语料库的评论级话题漂移分析
authors:
- Steven Morse
- Daniel Runfola
- Trenton W. Ford
affiliations:
- William & Mary
arxiv_id: '2608.19133'
url: https://arxiv.org/abs/2608.19133
pdf_url: https://arxiv.org/pdf/2608.19133
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 短文本语义分析 · 大规模话题漂移检测
tags:
- Topic Drift
- Dynamic Topic Modeling
- Embedding Clustering
- Unsupervised Learning
- Short Text Analysis
one_liner: 提出基于嵌入的大规模动态话题建模方法，量化短文本评论级话题漂移，通过空模型过滤虚假动态
practical_value: '- 可复用该方案的空模型对比逻辑，过滤电商用户评论、搜索Query的语义漂移假阳性信号，提升用户兴趣建模准确性

  - 大规模短文本分窗聚类+跨时间簇对齐的工程方案，可直接迁移到电商评论话题演化、营销热点追踪场景，适配十亿级语料

  - 不同领域话题漂移程度的结论可复用：社会/争议类话题语义漂移速度远高于文娱体育类，做相关内容推荐时需更高频更新语义向量库'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有嵌入驱动的话题建模多为静态描述，无法量化话题在嵌入空间的真实动态漂移，也无法区分真实漂移与随机波动，难以支撑十亿级短文本的话语演化分析。
**方法关键点**：1. 基于预训练LM生成短文本上下文语义嵌入，在月度时间窗内做无监督聚类，跨时间对齐相似簇得到话题演化路径；2. 提出空模型对比检验过滤虚假漂移信号，同时优化原有方法适配大规模语料处理。
**关键结果**：覆盖2006-2022年共127亿条Reddit评论验证，政治、社会争议类话题的嵌入空间存在显著定向漂移，跨话题距离的系统变化超出空模型可解释范围，音乐、体育类话题语义相对稳定。
