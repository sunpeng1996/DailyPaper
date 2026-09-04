---
title: Dutch Books for Language Models
title_zh: 面向大语言模型的荷兰赌概率一致性评估方法
authors:
- Isaiah Andrews
- Suproteem Sarkar
affiliations:
- MIT
- NBER
- University of Chicago
arxiv_id: '2609.02797'
url: https://arxiv.org/abs/2609.02797
pdf_url: https://arxiv.org/pdf/2609.02797
published: '2026-09-02'
collected: '2026-09-04'
category: Eval
direction: LLM概率预测一致性评估
tags:
- Probabilistic Forecasting
- Dutch Book
- LLM Evaluation
- Coherence Measurement
- Unsupervised Assessment
one_liner: 提出无需结果标签的荷兰赌评估框架，量化LLM概率预测不一致性并验证关键影响因素
practical_value: '- 电商销量预测、广告转化预估类Agent可引入荷兰赌一致性检查，过滤自相矛盾的LLM概率输出，降低预测错误率

  - 给LLM输入预测类prompt时主动剔除无关上下文，可直接降低概率预测不一致性一个数量级，投入小收益高

  - 多事件联合预测场景（如大促多品类销量联动、用户多行为路径概率预测）需额外加一致性校验，抵消逻辑复杂度升高带来的偏差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM已被广泛用于各类决策场景的概率预测，用户默认其输出的概率符合逻辑自洽的世界模型，但现有评估方法大多依赖事件结果标签，无法对未发生、未观测的事件做一致性校验。

### 方法关键点
基于de Finetti定理设计无标注的荷兰赌评估框架：首先从股票收益数据生成预测事件集，采集LLM对各事件的概率输出，再通过线性规划计算套利者与模型对赌可获得的最大无风险利润（即荷兰赌利润），以此作为概率不一致性的量化指标，全程无需事件结果标签。

### 关键结果
1. LLM的概率预测存在显著的逻辑不一致性；
2. 事件间逻辑关联越复杂，不一致性越高；
3. 输入中加入无关上下文细节，可使不一致性升高1个数量级。
