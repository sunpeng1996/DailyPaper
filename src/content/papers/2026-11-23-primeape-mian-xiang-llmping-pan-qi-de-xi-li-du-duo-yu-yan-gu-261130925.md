---
title: 'PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge
  Models'
title_zh: PRIMEAPE：面向LLM评判器的细粒度多语言元评估基准
authors:
- Vladislav Mikhailov
- Sarfraz Ahmad
- Momina Ahsan
- Zoia Butenko
- Vladimir Dobrovolskii
- Preslav Nakov
- Erik Velldal
- Lilja Øvrelid
- Ekaterina Artemova
affiliations:
- University of Oslo
- MBZUAI
- Nebius AI
- Toloka AI
arxiv_id: '2611.30925'
url: https://arxiv.org/abs/2611.30925
pdf_url: https://arxiv.org/pdf/2611.30925
published: '2026-11-23'
collected: '2026-11-24'
category: Eval
direction: LLM评判器 · 多语言元评估
tags:
- LLM-as-Judge
- Multilingual
- Benchmark
- Meta-Evaluation
- Human Preference
one_liner: 发布覆盖7种语言的PRIMEAPE基准，可同时评测LLM评判器的判决一致性与人偏好对齐度
practical_value: '- 用LLM-as-Judge评估生成式推荐文案、Agent回复时，不能仅验证判决与生成理由的自洽性，必须抽样校验与人类偏好的对齐度，避免评估结果失真

  - 跨境多语言电商场景的LLM评判，需针对不同语言、不同评估维度（相关性/真实性/安全性）单独优化Prompt，不要使用统一通用评判Prompt

  - LLM评判存在首位偏好、长回复偏好，做推荐/广告文案A/B测试时，需随机打乱候选顺序、控制候选长度阈值，降低系统偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-as-Judge范式已广泛用于模型排序、偏好数据标注等场景，但现有评判器评估方案大多仅覆盖英文，且无法区分「判决与自身理由自洽」和「判决与人类偏好对齐」两个核心指标，易高估评判器可靠性。
### 方法关键点
构建PRIMEAPE多语言元评估基准，覆盖英、法、西、印地语等7种语言，包含2205组响应对、243条指令、11k条人类标注，覆盖相关性、自然度、真实性、安全性、整体质量5类评估维度，可同时评测评判器的判决-理由自洽性、人类偏好对齐度两类核心能力。
### 关键结果
对12款开源/闭源评判器的测试显示：聚合性能指标会掩盖不同语言、不同评估维度的表现差异；要求评判器输出理由无法稳定提升其与人类偏好的对齐度；评判器普遍存在首位偏好、长回复偏好、同源模型偏好，偏差幅度随语言、评估维度变化；甚至可在判决完全不符合人类偏好时，仍保持判决与自身生成理由的自洽性。
