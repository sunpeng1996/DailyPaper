---
title: 'TS-RAG: Retrieval Augmented Generation for Time Series Forecasting'
title_zh: TS-RAG：面向时间序列预测的检索增强生成方法
authors:
- Yixiong Xiao
- Congxi Xiao
- Jingbo Zhou
affiliations:
- Baidu, Inc.
arxiv_id: '2608.06223'
url: https://arxiv.org/abs/2608.06223
pdf_url: https://arxiv.org/pdf/2608.06223
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: 时序预测 · RAG框架优化
tags:
- RAG
- Time Series Forecasting
- Reference Token
- Transformer
- SOTA
one_liner: 设计带专属参考token的TS-RAG框架，将RAG引入时序预测，在多个基准达SOTA
practical_value: '- 电商销量、流量、库存等时序预测场景可直接复用TS-RAG框架，引入相似历史序列参考提升预测精度

  - 借鉴参考token设计思路，解决多源序列信息融合时直接拼接prompt效果差的问题，适配小参数模型的RAG落地

  - 可迁移到时序相关的用户行为序列建模、长周期兴趣召回等推荐场景，增强序列信息利用率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Transformer时序预测模型受训练数据规模有限、参数量小、生成能力偏弱限制，泛化能力不足；直接照搬NLP领域RAG的prompt拼接方案适配性差，RAG在时序预测领域的落地尚缺乏成熟方案。时序预测是电商销量预估、流量调度、库存规划等业务的核心基础模块，对精度提升需求迫切。
### 方法关键点
TS-RAG框架先召回与输入序列相似的历史时序序列作为参考，引入专门设计的参考token实现输入序列与召回参考序列的信息融合，避免直接拼接带来的噪声干扰，支持模型自主学习不同来源序列的权重分配，更鲁棒地捕捉复杂时序动态。
### 关键结果
在多个真实世界时序预测基准数据集上，TS-RAG性能持续领先现有方案，达到SOTA水平，通用性较强。
