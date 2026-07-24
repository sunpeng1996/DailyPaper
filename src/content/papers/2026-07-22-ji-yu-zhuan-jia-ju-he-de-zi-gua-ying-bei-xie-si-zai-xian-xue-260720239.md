---
title: Adaptive Bayesian Online Learning via Expert Aggregation
title_zh: 基于专家聚合的自适应贝叶斯在线学习方法
authors:
- Jungbin Jun
- Ilsang Ohn
affiliations:
- Inha University
arxiv_id: '2607.20239'
url: https://arxiv.org/abs/2607.20239
pdf_url: https://arxiv.org/pdf/2607.20239
published: '2026-07-22'
collected: '2026-07-24'
category: Training
direction: 贝叶斯在线学习 · 专家聚合优化
tags:
- Bayesian Online Learning
- Expert Aggregation
- Conformal Inference
- Gaussian Process
- Online Prediction
one_liner: 将不同配置的贝叶斯更新规则作为专家按序损失聚合，实现流式场景自适应不确定性感知预测
practical_value: '- 可借鉴专家聚合思路解决推荐/广告系统在线更新的超参选择问题，将不同学习率、先验的贝叶斯更新规则作为专家动态选优，避免提前固定超参的性能损失

  - 可复用在线共形推理的落地方法，给电商实时推荐、广告预估的预测结果添加置信区间，支撑不确定性感知的流量调控策略

  - 流式数据场景下可直接套用该框架，无需提前选定最优贝叶斯更新配置，框架自动追踪最优专家性能，降低在线模型调优成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
贝叶斯在线学习支持流式数据的不确定性感知预测，但需提前固定学习率、先验分布、变分族等推理配置，超参选择成本高，模型适配性差，在分布变化的流式场景下性能易受损。
### 方法关键点
将不同超参配置的贝叶斯更新规则定义为独立专家，基于每轮预测的序列损失动态加权聚合专家输出，理论证明聚合模型性能可追平事后最优的单专家，聚合代价由每轮专家性能的评估规则决定。
### 关键结果
1. 在线共形推理场景落地得到平滑自适应贝叶斯变体，实现长期随机覆盖率保证；
2. 高斯过程回归场景下，累积预测KL风险满足oracle不等式，可自适应未知Hölder光滑性，仅产生对数级性能损失；
3. 实验验证框架无需先验选定最优专家，即可自动追踪表现最优的专家性能
