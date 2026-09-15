---
title: Measuring the Creativity of Frontier LLMs in Automated Research
title_zh: 前沿大模型在自动化科研场景下的创造力评估
authors:
- Yiheng Zhao
- Mengzhuo Chen
- Chengming Hu
- Pengyi Liao
- Yiran Pang
affiliations:
- Concordia University
- Independent Researcher
- McGill University
- Florida Atlantic University
arxiv_id: '2609.14057'
url: https://arxiv.org/abs/2609.14057
pdf_url: https://arxiv.org/pdf/2609.14057
published: '2026-09-12'
collected: '2026-09-15'
category: Eval
direction: LLM 自动化科研创造力评估
tags:
- LLM
- Creativity Evaluation
- Automated Research
- Novelty Metrics
- Valueness Assessment
one_liner: 提出覆盖价值度与三类新颖度的量化指标体系，评估自动化科研场景下大模型的创造力
practical_value: '- 做Agent生成idea的评估时，可直接复用「价值度+多维度新颖度」的评估框架，无需从零搭建指标体系

  - 做生成式推荐/广告文案创意评估时，可参考Exact-Match/变量级/知识偏离度三类新颖度的划分逻辑，适配业务场景做量化改造

  - 业务中需优先优化Agent的变量级新颖度，该维度和最终产出效果的相关性最高'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前前沿LLM已具备自动化科研能力，但针对该场景下的LLM创造力缺乏系统的量化评估体系，创造力的两个核心维度（新颖性、价值度）没有可落地的度量方法。

### 方法关键点
从价值度、新颖度两大核心维度构建评估体系：价值度判断生成idea的实用性；新颖度拆分3个子维度，分别为校验是否完全匹配现有工作的Exact-Match P-Novelty、校验是否探索未出现变量/变量组合的Variable-level P-Novelty、校验是否脱离检索外部知识生成的H-Novelty。

### 关键结果
不同前沿LLM在大部分创造力指标上得分接近，仅在Variable-level P-Novelty维度差异显著；相关性分析表明Variable-level P-Novelty是和科研产出效果相关性最高的创造力维度。
