---
title: Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction
title_zh: 大语言模型能否生成可靠评分规则？面向实验复现的元评估
authors:
- Hanhua Hong
- Yizhi Li
- Jiaoyan Chen
- Luu Gia Huy
- Sophia Ananiadou
- Jung-jae Kim
- Chenghua Lin
arxiv_id: '2607.12835'
url: https://arxiv.org/abs/2607.12835
pdf_url: https://arxiv.org/pdf/2607.12835
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM 自动评估 · 元评估方法
tags:
- LLM Evaluation
- Meta-Evaluation
- Rubric Generation
- Experiment Reproduction
- Open-ended Output Assessment
one_liner: 首次针对论文复现场景系统性元评估LLM生成的评分规则，验证增强设定性能逼近人类基线
practical_value: '- 生成式推荐/Agent开放输出评估场景可复用checklist格式rubric自动生成框架，大幅降低专家标注成本

  - LLM生成评估规则时优先采用注入领域知识、Few-shot示例的增强设定，可显著提升评分与人工标注的对齐度

  - 业务落地时需额外补充过细条目过滤、评分偏置校准模块，规避LLM生成rubric的高评分偏置、领域适配差问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
基于rubric的评估是LLM研究Agent开放输出（尤其是论文复现场景）的高潜力方案，但定制化rubric构建依赖大量专家人力，限制了PaperBench等基准的可扩展性，当前缺乏对LLM自动生成rubric效果的系统性验证。
### 方法关键点
首次开展LLM生成论文复现rubric的系统性元评估，将rubric重构为checklist格式，在2个骨干LLM上对比4种生成设定，从内在（语义相似度）、外在（与ground-truth rubric的评分对齐度）两个维度完成评估，同步开展缺陷归因分析。
### 关键结果
增强生成设定可大幅提升下游评估对齐度，最优设定性能接近人类基线，而内在指标提升幅度较小；进一步分析发现LLM生成的rubric普遍存在粒度过细、高评分偏置、领域适配性差三类缺陷。
