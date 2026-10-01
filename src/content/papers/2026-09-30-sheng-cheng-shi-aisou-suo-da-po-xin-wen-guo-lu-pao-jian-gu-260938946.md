---
title: 'Breaking News Out of the Filter Bubble: Generative AI Search Diversifies Collective
  Attention and Raises Shared Information Consumption'
title_zh: 生成式AI搜索打破新闻过滤泡：兼顾共享信息增长与注意力多样化
authors:
- Heeseung Andrew Lee
- Dokyun Lee
- Gwanhoo Lee
- Dongwon Lee
affiliations:
- University of Texas at Dallas
- Boston University
- American University
- Hong Kong University of Science and Technology
arxiv_id: '2609.38946'
url: https://arxiv.org/abs/2609.38946
pdf_url: https://arxiv.org/pdf/2609.38946
published: '2026-09-30'
collected: '2026-10-01'
category: RAG
direction: RAG搜索 · 内容消费影响实证评估
tags:
- RAG
- Generative Search
- Field Experiment
- Filter Bubble
- Information Diversity
- User Behavior
one_liner: 通过华盛顿邮报3.7万用户随机对照实验，验证RAG搜索可同时提升信息共享度与内容消费多样性
practical_value: '- 内容/电商平台上线带AI摘要+引文的RAG搜索可同时提升用户信息共识与内容消费多样性，打破过滤泡担忧，适配内容搜索、商品导购等场景

  - 可复用该实验的三维评估指标：共享信息消费、话题集中度、话题流行度，分层衡量搜索/推荐系统对用户注意力分布的影响，补充单一点击率/时长指标的不足

  - 电商导购场景可参考：搜索结果顶部增加多商品对比AI摘要+对应商品入口，既提升用户决策效率，也能为尾部商品带来更多曝光，平衡头部马太效应'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长期以来算法推荐与传统搜索被诟病会形成过滤泡，窄化用户信息视野、降低群体信息共识；生成式AI搜索普及后，业界普遍担忧这一问题会进一步加剧，但此前缺乏大规模实地实验验证其真实影响，该研究针对性填补了这一空白。

### 方法关键点
- 联合华盛顿邮报开展38天随机对照实地实验，覆盖37561名读者，对照组仅展示传统语义搜索结果，实验组在结果顶部额外展示AI生成答案及最多5篇引用来源文章，两组共享同一内容库
- 用BERTopic对37万+篇文章做主题建模，从三个核心维度评估效果：共享信息消费、话题集中度、话题流行度，同时区分仅计文章点击的消费、含AI答案的总消费两类统计口径

### 关键结果
实验组用户共享信息消费提升69%，用户间内容相似度显著上升；总消费的Gini系数在个体层面降0.013、聚合层面降0.034，有效话题数分别提升21%、4.6%；Top10热门话题消费占比个体层面降4个百分点、聚合层面降4.4个百分点；用户搜索次数提升29%，每分钟信息消费效率提升62%。

### 核心结论
带AI摘要和引文的RAG搜索不仅不会加剧过滤泡，反而能在提升群体信息共识的同时拓宽用户的内容消费边界，打破“多样性提升必然伴随共识下降”的固有认知。
