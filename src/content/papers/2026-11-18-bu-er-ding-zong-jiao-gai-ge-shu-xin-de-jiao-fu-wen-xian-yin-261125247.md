---
title: Retrieving Patristic References and Modelling Topics in Bullinger's Reformation
  Correspondence
title_zh: 布尔丁宗教改革书信的教父文献引用检索与主题建模
authors:
- Lena Pickartz
- Philipp Schaer
- Phillip B. Ströbel
affiliations:
- TH Köln–University of Applied Sciences, Cologne, Germany
- Department of History, University Zurich, Switzerland
arxiv_id: '2611.25247'
url: https://arxiv.org/abs/2611.25247
pdf_url: https://arxiv.org/pdf/2611.25247
published: '2026-11-18'
collected: '2026-11-22'
category: Other
direction: 历史文档检索 · 主题建模
tags:
- hybrid retrieval
- BM25
- bi-encoder
- topic modeling
- intertextuality detection
one_liner: 对比多种检索方案实现宗教改革书信的教父引用检测，优化主题建模适配历史文本分析
practical_value: '- 稀疏+稠密检索融合思路可复用：当BM25与bi-encoder召回结果重叠度低时，融合召回可在不增加推理成本的前提下提升长尾query、弱语义物品的召回率，适配电商小众商品、隐含需求搜索场景

  - 跨域迁移dense encoder时，优先选择和目标域语义分布最接近的预训练微调模型，可降低小样本业务场景的微调成本

  - 实时性要求高的搜索/推荐场景，可优先测试混合检索方案，性能接近cross-encoder重排但推理成本更低'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
宗教改革家布尔丁的书信中大量引用教父文献作为权威来源，现有研究缺乏自动化检测这类引用的技术方案，同时需要挖掘书信隐含主题支撑历史研究。

### 方法关键点
1. 对比BM25、bi-encoder稠密检索、混合检索三类方案，检测显式/隐式教父引用；
2. 为FASTopic加入种子引导损失函数和编辑摘要嵌入，优化主题建模效果；
3. 引入LLM-based概念归纳方法LLooM作为可解释主题挖掘备选。

### 关键结果数字
- BM25在显式引用检测上Recall@20达94%，优于bi-encoder最优值82%；
- 稀疏+稠密混合检索将隐式引用Recall@20提升至22%，接近cross-encoder重排的26%，无额外推理成本；
- 优化后的主题模型 coherence 增益有限，权重接近均匀分布，无法支撑检索任务。
