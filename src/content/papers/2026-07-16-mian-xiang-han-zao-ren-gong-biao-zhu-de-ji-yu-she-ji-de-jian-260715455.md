---
title: Design-Based Supervised Learning with Noisy Human Labels
title_zh: 面向含噪人工标注的基于设计的监督学习方法
authors:
- Robert Chew
- Matthew R. Williams
affiliations:
- RTI International
- U.S. Bureau of Labor Statistics
arxiv_id: '2607.15455'
url: https://arxiv.org/abs/2607.15455
pdf_url: https://arxiv.org/pdf/2607.15455
published: '2026-07-16'
collected: '2026-07-20'
category: Training
direction: 监督学习 · 噪声标注校正
tags:
- Noisy Label Learning
- Label Correction
- Supervised Learning
- Audit Debiasing
- Downstream Analysis
one_liner: 提出PA-DSL方法，利用部分专家裁定样本校正含噪人工标注，消除自动标注下游分析偏差
practical_value: '- 清洗UGC内容标注、用户反馈标签时，可引入少量专家裁定样本校正众包/运营标注噪声，替代全量专家标注降低标注成本

  - 推荐/广告场景的自动标签（如LLM生成的item标签、用户意图标签）校正，可复用PA-DSL双阶段校正逻辑，先修正人工标注噪声再校正自动标注偏差

  - 当标注噪声存在可恢复信号时，优先用该方法替代纯小批量专家数据训练，可降低RMSE10%以上同时保证置信区间覆盖度'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有自动标注校正方法默认审计环节的人工标注完全准确，但实际场景中人工审计标注普遍存在噪声，且仅少部分审计样本能获得高置信度的专家裁定标注，缺乏适配该场景的校正方案。
### 方法关键点
提出PA-DSL双阶段校正框架：第一阶段用已知抽样概率的专家裁定样本校正含噪人工审计标签；第二阶段用校正后的审计信息对全量自动标注的下游分析做去偏，该估计器适配绝大多数下游任务，仅要求审计、裁定的抽样概率已知。
### 关键结果
合成数据+Wikipedia Detox半合成实验显示，当含噪人工标注存在可恢复信号时，相比仅使用专家裁定标注的方案，PA-DSL在保持标称置信区间覆盖度的同时，RMSE降低10%-17%。
