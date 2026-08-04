---
title: 'CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation'
title_zh: CalibratedRubric：面向开放端大模型评估的任务自适应评分细则库
authors:
- Mengting Chen
- Yanshu Sun
- Wanting Liang
- Beidi Luan
- Rui Sun
- Dezhi Chen
- Jing Li
- Zuo Bai
affiliations:
- FinStep
- StepFun
arxiv_id: '2607.29252'
url: https://arxiv.org/abs/2607.29252
pdf_url: https://arxiv.org/pdf/2607.29252
published: '2026-07-31'
collected: '2026-08-04'
category: Eval
direction: 大模型开放输出评估 · 自适应评分细则构建
tags:
- LLM Evaluation
- Rubric Construction
- Bayesian Filtering
- Item Response Theory
- Open-ended Generation
one_liner: 提出结合贝叶斯过滤与IRT的自适应评分框架，提升开放端LLM评估的一致性与效率
practical_value: '- 对Agent生成的电商导购文案、RAG召回的问答回复做自动评估时，可复用贝叶斯可测性过滤方法筛选有效评分维度，提升和人工打分的一致性

  - 做多维度LLM输出质量评估时，可借鉴基于次模优化+IRT的评分细则压缩方法，用更少维度达到目标评估相关性，降低评估成本

  - 针对垂域大模型服务（如金融投研、法律合规）的效果验收场景，可直接复用该框架构建垂域专属评分细则库，减少专家标注成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
开放端LLM输出（如长报告、Agent交互回复）的可靠评估依赖细粒度评分细则，人工构建成本高难扩展，现有自动方案依赖严格评委一致性、二元方差过滤，无法区分可测和高信息价值的评分维度。

### 方法关键点
1. 采用分类别打分+贝叶斯细则可测性过滤，用Beta-Bernoulli一致性后验估计每个评分细则的可测度；
2. 结合Item Response Theory (IRT)，用次模信息覆盖目标构建覆盖观测能力范围的紧凑评分细则库。

### 关键结果数字
- 可测性过滤将JudgmentBench上和人工金标准的一致性从κ=0.604提升至0.743；
- IRT贪婪选择在所有6个响应块上的跨拟合排序保真度优于随机选择，在FinResearchBench决策支持任务上仅需49条细则（原131条）即可达到目标相关性。
