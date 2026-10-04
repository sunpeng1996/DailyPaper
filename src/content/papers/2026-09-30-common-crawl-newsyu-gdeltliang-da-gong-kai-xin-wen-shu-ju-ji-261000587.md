---
title: Comparison of Common Crawl News & GDELT
title_zh: Common Crawl News与GDELT两大公开新闻数据集对比研究
authors:
- Ameir El Ouadi
- David Beskow
affiliations:
- United States Military Academy, West Point
- Department of Systems Engineering, United States Military Academy
arxiv_id: '2610.00587'
url: https://arxiv.org/abs/2610.00587
pdf_url: https://arxiv.org/pdf/2610.00587
published: '2026-09-30'
collected: '2026-10-04'
category: Other
direction: 公开新闻语料 · 数据集对比评估
tags:
- NewsDataset
- GDELT
- CommonCrawl
- CorpusEvaluation
- LLM
one_liner: 对比GDELT与Common Crawl News的内容覆盖与优劣势，为新闻语料选型提供参考
practical_value: '- 做热点关联的电商选品、商品推荐、广告素材生成时，可按需选择语料：GDELT多源长周期特性适合长周期舆情分析，Common Crawl
  News更适配互联网热点挖掘

  - 构建LLM领域微调语料、RAG事实性外部知识库时，可参考两者的数据源差异做互补融合，降低数据偏差

  - 开发依赖实时新闻事实的决策Agent时，可组合两个数据集的内容做交叉验证，提升事实准确性'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
全球新闻语料是LLM训练、知识图谱构建、舆情分析、事件驱动推荐等任务的核心基础资源，当前主流的GDELT、Common Crawl News两大公开数据集的覆盖特性、优劣势缺乏系统性对比，易导致语料选型偏差。
### 方法关键点
从数据源类型、时间覆盖、内容分布三个维度对两个数据集做横向对比，拆解两者的采集逻辑、数据结构、适用场景差异。
### 关键结果
1. GDELT覆盖1979年至今的全球广播、印刷、网页多源新闻，支持100+语言，自带CAMEO事件编码，适合长周期、跨媒介的全球事件分析；
2. Common Crawl News仅收录网页爬虫获取的全球新闻站点内容，互联网新闻覆盖密度更高；
3. 两个数据集的新闻来源分布存在显著差异，不存在完全的替代关系。
