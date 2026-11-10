---
title: 'Approximate Recall, Approximate Forecasts: Recall as a Diagnostic for LLM
  Forecasting Errors'
title_zh: 近似召回对应近似预测：将召回作为LLM预测误差的诊断指标
authors:
- Prashanth Bhaskara
- Shubhaankar Gupta
- Seojoon Yeon
affiliations:
- University of Chicago
arxiv_id: '2611.10891'
url: https://arxiv.org/abs/2611.10891
pdf_url: https://arxiv.org/pdf/2611.10891
published: '2026-11-07'
collected: '2026-11-10'
category: LLM
direction: LLM 预测误差诊断与评估
tags:
- LLM
- Forecasting
- Recall Fidelity
- Error Diagnostic
- Evaluation
one_liner: 提出Recall Fidelity Score量化LLM历史召回保真度，可有效诊断预测误差来源
practical_value: '- 做LLM驱动的电商销量预测、爆款预判、大促效果预估时，可引入RFS指标先校验模型对同领域历史相似事件的召回保真度，提前筛除高置信错误记忆导致的预测偏差

  - 搭建预测类Agent的RAG模块时，优先补全/修正模型存在「自信错误召回」的历史事件知识，ROI远高于盲目扩充知识覆盖度，自信错误对预测的负面影响是无召回的3倍

  - 在商品卖点生成、query改写等需要事实准确性的生成场景，可复用RFS两级校验逻辑：先匹配结果正确性，再校验推理过程的事实一致性，降低幻觉输出率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM预测能力评估多采用Brier分数等指标，无法区分校准误差与底层知识召回错误导致的预测偏差，过往研究也未量化LLM历史事件召回保真度损失如何传导到未来事件预测效果，无法定位预测误差的核心来源。

### 方法关键点
- 提出Recall Fidelity Score（RFS）三级打分机制：0分（召回结果错误）、0.5分（结果正确但推理存在事实错误）、1分（结果与推理均事实一致），区分无召回、部分正确、自信错误等不同召回状态
- 设计Local Recall Metric：对每个待预测事件，通过TF-IDF+余弦相似度匹配Top k个历史相似事件，计算模型在这些事件上的平均RFS，关联预测效果
- 数据集覆盖9个领域，从Polymarket收集2650个二元预测市场数据，拆分1300个2023-2025年已结事件为召回集，1350个2026-2030年未结事件为预测集，评测4款前沿大模型

### 关键结果
- RFS从0.4提升到0.87时，召回任务Brier分数降低0.1，相当于参测模型最优与最差的性能差距
- 相似历史事件平均RFS每提升1单位，预测任务与市场共识的平方偏差降低0.065，仅同领域相似事件具备预测性，跨领域/随机采样事件无相关关系
- 自信错误召回是预测误差核心来源：相似事件中自信错误占比每提升1单位，预测损失提升0.2，是无召回带来损失（0.066）的3倍

### 核心结论
优化LLM预测能力时，优先减少错误记忆的危害远大于扩充知识覆盖度，「知道自己不知道」的模型表现远好于「自信记错」的模型
