---
title: Bag of concepts can enhance other text representations for medical systematic
  review screening
title_zh: 概念袋特征可增强医学系统综述筛选场景的文本表示性能
authors:
- Radosław Pytlak
- Paweł Cichosz
- Bartłomiej Fajdek
- Bogdan Jastrzębski
affiliations:
- Warsaw University of Technology
arxiv_id: '2611.15798'
url: https://arxiv.org/abs/2611.15798
pdf_url: https://arxiv.org/pdf/2611.15798
published: '2026-11-11'
collected: '2026-11-14'
category: Other
direction: 文本表示增强 · 特征融合
tags:
- Text Representation
- Feature Fusion
- Active Learning
- Bag of Concepts
- Medical NLP
one_liner: 验证概念袋特征与主流文本表示融合可提升医学文献主动学习筛选效率
practical_value: '- 可复用「领域概念袋(BoC)+通用语义向量」的特征融合思路，在电商类目/商品属性匹配、广告定向场景补充结构化领域知识，提升语义表示的领域适配性

  - 多向量融合的效果验证方法可迁移至推荐召回排序的特征组合优化，用 workload savings 类的业务效率指标替代纯精度指标做效果评估

  - 领域本体/词典生成BoC特征的方案可用于RAG检索的query增强，解决垂类场景通用LLM语义向量对领域术语理解偏差的问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
主动学习驱动的半自动化医学系统综述筛选场景下，概念袋（BoC）表示的价值长期被忽略，单一通用文本表示存在领域结构化信息缺失问题。
### 方法关键点
对比BoW、BoC、PubMedBERT、Jina、Gemma、Qwen3等单表示，以及BoC与各表示的融合方案，覆盖医学文献分类、聚类初始化、不确定性采样三类任务，同时评估不同领域本体对BoC特征效果的影响，采用工作量节省率、性能曲线作为核心评估指标。
### 关键结果
BoC增强后的表示在DERP数据集上的平均工作量节省率均优于对应基础表示，Qwen3+BoC组合取得最优平均性能，不同本体选择对分类效果存在显著影响。
