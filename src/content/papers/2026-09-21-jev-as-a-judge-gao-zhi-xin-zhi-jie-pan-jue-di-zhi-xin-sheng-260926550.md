---
title: 'JEV-as-a-Judge: Accept When Confident, Escalate When Unsure'
title_zh: JEV-as-a-Judge：高置信直接判决、低置信升级的低成本评估框架
authors:
- Yubo Li
- Yidi Miao
- Ramayya Krishnan
- Rema Padman
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.26550'
url: https://arxiv.org/abs/2609.26550
pdf_url: https://arxiv.org/pdf/2609.26550
published: '2026-09-21'
collected: '2026-09-23'
category: Eval
direction: LLM评估 · 低成本级联评判方案
tags:
- LLM-as-a-Judge
- Evaluation
- Cost Optimization
- Confidence Calibration
- Cascaded System
one_liner: 提出轻量决策型JEV评估器搭配级联升级策略，以0.36%成本实现SOTA LLM评判99%准确率
practical_value: '- 电商/广告文案、推荐理由的批量效果评估可复用级联策略：先用低成本轻量模型做初筛，高置信结果直接落盘，低置信结果再调用大模型/人工审核，可大幅降低评估成本

  - LLM生成结果的置信度校准逻辑可直接迁移：将模型输出的标签概率作为置信度阈值，优先放行高置信判决，仅对歧义样本升级校验，可同时兼顾准确率和成本控制

  - 商品评价、客服话术的批量质检场景可直接套用该架构：初筛用小模型标注，低置信样本触发人工复核，可在几乎无损准确率的前提下压减99%以上的审核成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM-as-a-Judge已成为开放生成任务的主流评估方案，但大规模落地时存在推理成本过高、置信度可靠性不足的痛点，无法支撑电商/广告等场景海量生成内容的评估需求。
### 方法关键点
提出仅输出决策结果的轻量JEV评估器作为首道评估节点，对比测试16种生成式、奖励模型类评判方案，基于JEV输出的标签概率定义置信度，搭建「高置信判决直接接受、低置信判决升级到SOTA LLM评判」的冻结级联架构。
### 关键结果
普通偏好评估、证据支撑的事实性评估场景下，JEV准确率仅比SOTA LLM评判低3个百分点，成本仅为后者的0.36%；级联架构可保留SOTA评判99%的准确率，仅在需要校验推导逻辑、对抗精心构造的错误答案场景下存在明显精度gap。
