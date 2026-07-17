---
title: Does generative AI supersede supervised XMLC? A Benchmark Study on Automated
  Subject Indexing with German Scientific Literature
title_zh: 生成式AI是否优于监督XMLC？德语文献自动标引基准研究
authors:
- Maximilian Kähler
- Katja Konermann
- Lisa Kluge
- Markus Schumacher
affiliations:
- Deutsche Nationalbibliothek
arxiv_id: '2607.14882'
url: https://arxiv.org/abs/2607.14882
pdf_url: https://arxiv.org/pdf/2607.14882
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: 极多标签分类 · 生成式与监督方法基准评估
tags:
- XMLC
- Extreme Multi-label Classification
- Generative AI
- Benchmark
- Long-tail Performance
- LLM
one_liner: 极多标签分类场景基准测试证明生成式LLM在长尾标签与分级相关度上优于传统监督XMLC
practical_value: '- 多标签分类/标签打标场景可采用混合架构：头部标签用传统监督XMLC保证整体指标，长尾标签用生成式LLM提升覆盖度与相关度

  - 算法选型评估不要仅依赖二元匹配指标，需结合业务核心关注的分级相关度（如点击/转化权重）设计评估体系，避免选型偏差

  - 电商SPU打标、广告关键词关联等超大标签集任务，长尾部分可直接复用LLM的零/少样本能力，降低标注与训练成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
图书馆自动主题标引属于极多标签分类（XMLC）场景，标签集规模可达百万级、分布极度不均衡，传统监督XMLC与生成式LLM的选型缺乏系统基准对比。
### 方法关键点
基于德国国家图书馆140万规模的受控权威词表GND，对比三类方案：传统词法匹配基线、多套基于Transformer稠密特征的监督XMLC方法、3款自研生成式LLM方法；评估维度同时覆盖历史标注二元匹配度、专业馆员人工分级相关度打分、长尾标签性能三个维度。
### 关键结果
监督XMLC方案在整体二元相关度指标上表现最优；生成式LLM在分级相关度、长尾标签召回两个核心维度效果更突出，更适合生产落地。
