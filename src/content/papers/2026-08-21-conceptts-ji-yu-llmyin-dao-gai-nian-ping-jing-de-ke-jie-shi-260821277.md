---
title: 'ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series
  Forecasting'
title_zh: ConceptTS：基于LLM引导概念瓶颈的可解释多变量时序预测
authors:
- Yichen Jiang
- Yueqiao Chen
- Dongyu Liu
affiliations:
- Stanford University
- University of California, Davis
arxiv_id: '2608.21277'
url: https://arxiv.org/abs/2608.21277
pdf_url: https://arxiv.org/pdf/2608.21277
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM驱动可解释多变量时序预测
tags:
- Time-Series Forecasting
- Concept Bottleneck
- Interpretable AI
- LLM
- Multivariate Time Series
one_liner: 提出LLM引导的概念瓶颈时序预测框架，精度媲美黑盒基线同时具备强可解释性
practical_value: '- 电商大促流量预测、库存时序预测场景可复用概念瓶颈架构，用LLM生成业务可理解的预测归因规则，替代人工标注概念

  - 做推荐系统可解释性优化时，可借鉴多概念瓶颈分层设计（历史/局部/全预测窗口），提升归因的可干预性

  - 时序预测任务中无需牺牲太多精度即可获得可解释性，适合监管要求高的广告投放效果预判场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前多变量时序预测黑盒模型精度高但解释性差，无法满足需明确预测归因的业务场景需求，人工标注可解释概念成本极高。

### 方法关键点
ConceptTS首先调用LLM生成任务相关的人类可读概念及可执行标注规则，无需人工标注即可获得概念监督信号；构建三层互补概念瓶颈，分别对应历史上下文、局部预测区间、全预测窗口三类概念；共享decoder基于三类概念的激活表示输出最终预测结果，决策过程完全透明且支持概念级干预。

### 关键结果
在北京多站点空气质量数据集上，预测精度与SOTA黑盒基线持平，同时输出语义可解释的概念激活结果。
