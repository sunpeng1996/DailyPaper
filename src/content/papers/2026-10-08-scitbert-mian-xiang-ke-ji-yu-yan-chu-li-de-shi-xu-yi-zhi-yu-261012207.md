---
title: 'SciTBERT: A family of chronologically consistent language models for scientific
  and technological language processing'
title_zh: SciTBERT：面向科技语言处理的时序一致性语言模型系列
authors:
- Thomas Gebhart
- Russell J. Funk
affiliations:
- Carlson School of Management, University of Minnesota
arxiv_id: '2610.12207'
url: https://arxiv.org/abs/2610.12207
pdf_url: https://arxiv.org/pdf/2610.12207
published: '2026-10-08'
collected: '2026-10-11'
category: LLM
direction: 领域大模型 · 时序一致性预训练
tags:
- BERT
- Domain Pre-training
- Temporal Consistency
- Scientific NLP
- Benchmark
one_liner: 提出时序一致的科技领域BERT模型族与专利评测基准，解决预训练模型前瞻偏差与域适配问题
practical_value: '- 做时序敏感的内容/商品推荐预训练时，可参考时序切分训练集+无前瞻数据泄漏的训练逻辑，避免未来信息污染历史任务效果

  - 跨域（如电商商品+搜索Query+种草内容）预训练时，可借鉴按领域分布对齐的后训练策略，提升跨域表征一致性

  - 做行业特定大模型评测时，可参考PatRepEval的构建思路，聚焦业务核心的跨场景任务设计评测集'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有科技领域预训练模型未约束训练数据的时间与来源分布，存在前瞻偏差、域偏差，无法支撑时序依赖的科技/专利文本分析任务。
### 方法关键点
1. 按年度切分训练数据，训练2013-2025逐年截止的BERT衍生模型族SciTBERT，训练数据覆盖论文、专利、高质量教育网页文本，无未来数据泄漏
2. 基于论文、专利引用关系做时序一致的后训练，得到增强版SciTBERT-CI模型族
3. 构建跨科技-专利领域的PatRepEval评测基准，覆盖分类、回归、检索三类任务
### 关键结果
即使受早年训练数据量限制，SciTBERT效果仍优于过往领域专用编码器；时序一致的编码器效果匹配甚至超越无时间约束训练的同规模模型
