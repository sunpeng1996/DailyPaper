---
title: Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift
title_zh: 召回还是重学？面向周期性概念漂移的上下文内专家混合方法
authors:
- Zhangkai Wu
- Xu Zhang
- Zhihong Cui
- Yiqi Wang
- Yi Zhang
affiliations:
- University of Sydney
- Macquarie University
- University of Oslo
- University of Southern Queensland
- University of Technology Sydney
arxiv_id: '2610.36585'
url: https://arxiv.org/abs/2610.36585
pdf_url: https://arxiv.org/pdf/2610.36585
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: 大模型流式适配 · 周期性概念漂移处理
tags:
- concept drift
- in-context learning
- tabular foundation model
- data stream
- mixture of experts
one_liner: 提出免训练MICE框架，解决表格大模型流式场景周期性概念漂移的召回重学决策问题
practical_value: '- 电商推荐流式场景（如大促前后用户行为漂移）可复用MICE的分段存储+历史上下文召回逻辑，避免概念回归时重训浪费算力

  - 可借鉴双层级加权融合机制：快速层用最近批次loss加权历史上下文，慢速层用最新FIFO窗口兜底，平衡召回收益和实时性

  - 上下文存储容量有限时，可复用MICE的误差容忍度合并策略，减少存储的专家数量同时保证效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
表格基础模型（TFM）在Web数据流场景下依赖更新上下文标注行实现免重训适配，但过往概念消失后再次回归时，面临召回历史上下文还是重新学习的决策难题，现有漂移后重置上下文的方案会浪费过往学习成果，准确率损失大。

### 方法关键点
提出免训练的MICE框架：
1. 检测到概念漂移时切分流数据为片段，满足误差容忍度和存储容量限制的闭合片段会被合并为上下文专家存储
2. 快速层基于最近标注批次的预测log-loss，对存储的上下文专家和FIFO窗口加权输出预测
3. 慢速层融合快速层输出与最新标注行FIFO窗口的预测，保证后悔界有理论保障

### 关键结果
网格流实验中MICE准确率显著高于漂移后重置上下文的方案，存储的专家数量比全量存储所有片段的方案更少；真实数据流实验中MICE的平均准确率为所有对比策略最高
