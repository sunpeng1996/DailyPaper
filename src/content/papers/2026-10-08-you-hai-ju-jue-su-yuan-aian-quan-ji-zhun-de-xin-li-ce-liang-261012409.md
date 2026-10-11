---
title: 'Searching for "Harmful Refusal": A Psychometric Audit of an AI Safety Benchmark'
title_zh: “有害拒绝”溯源：AI安全基准的心理测量学审计
authors:
- Christopher M. Stewart
- Preston Botter
- Natalie Sarabosing
- Muye Zhang
- Rachel Phinnemore
- Shalini Ghosh
- Hong Shen
- Hoda Heidari
affiliations:
- Carnegie Mellon University
- Indiana University
- Google
arxiv_id: '2610.12409'
url: https://arxiv.org/abs/2610.12409
pdf_url: https://arxiv.org/pdf/2610.12409
published: '2026-10-08'
collected: '2026-10-11'
category: Eval
direction: LLM安全基准评估 · 心理测量学审计
tags:
- LLM Safety
- Benchmark Audit
- Psychometrics
- Harmful Refusal
- HELM Safety
one_liner: 通过心理测量学审计证明主流AI安全基准无法单维度衡量模型有害拒绝能力
practical_value: '- 业务侧LLM/Agent安全评估不要仅依赖第三方基准的单一总评分，需拆分虚假宣传、隐私泄露、违规内容等细分风险域做多维度评估，避免总分掩盖实际业务风险

  - 自研安全评估体系时，可复用构念效度验证、多维项目反应理论建模的方法，确保自定义评估指标确实对应要测量的安全属性，避免无效评估

  - 跨厂商LLM选型做安全能力对比时，需先对齐测试场景范围，消除不同厂商模型在特定安全域的优化差异带来的评分偏差'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI安全基准普遍输出单一总评分，易掩盖模型在不同安全维度的表现差异，甚至无法保证单数据集的评分对应单一可测量的安全属性；而有害拒绝（即拒绝响应危险/违规prompt的能力）是大模型落地业务的核心安全指标，需明确现有基准是否能有效衡量该能力。
### 方法关键点
基于构念效度框架，先筛查HELM Safety中4个疑似针对有害拒绝的数据集，发现3个存在评分饱和问题；仅对剩余的HarmBench展开两类心理测量学审计：用多维项目反应理论建模检验单属性一致性，用差异化项目功能分析检验跨厂商模型的评分公平性。
### 关键结果
1. HarmBench无法有效测量单维度的有害拒绝属性，安全能力相当的不同厂商模型，在特定测试项上得分差异显著，差异仅在对齐测试场景范围后消失；
2. 所有采用跨数据集/测试项平均的单一安全总评分，普遍存在特征混淆、评分饱和问题，不可直接用于跨模型的安全能力对比。
