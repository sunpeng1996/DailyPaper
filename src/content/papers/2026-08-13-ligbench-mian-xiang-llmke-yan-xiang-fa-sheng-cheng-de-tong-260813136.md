---
title: 'LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea
  Generation'
title_zh: LigBench：面向LLM科研想法生成的统一人类对齐基准
authors:
- Chenrun Wang
- Mingxuan Zhu
- Tiancheng Huang
- Wenjie Li
- Yujie Zhang
- Zichen Zhu
- Zhiying Zou
- Kai Yu
- Lu Chen
affiliations:
- Shanghai Jiao Tong University X-LANCE Lab
- Shanghai Innovation Institution
arxiv_id: '2608.13136'
url: https://arxiv.org/abs/2608.13136
pdf_url: https://arxiv.org/pdf/2608.13136
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 大模型生成任务评估 · 人类对齐
tags:
- Benchmark
- LLM Evaluation
- Pairwise Ranking
- Human Alignment
- Idea Generation
one_liner: 提出统一评估基准LigBench与配对数据集PAIR-IQ，提升科研想法生成评估与专家判断的对齐度
practical_value: '- 做营销文案、推荐理由等业务生成类任务评估时，可复用 pairwise 对比标注思路替代单样本直接打分，提升评估与业务目标的对齐度

  - 自研内部业务效果评估基准时，可参考LigBench的跨生成分布一致性设计思路，降低不同生成模型效果对比的偏差

  - 业务侧排序类评估任务可基于少量专家标注的配对样本微调小模型，替代大模型直接打分，降低评估成本同时提升鲁棒性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM科研想法生成的评估体系碎片化、缺乏客观标准，大多依赖LLM直接打分，无法在不同生成分布下提供统一可靠的评估结果，与人类专家判断对齐度低。

### 方法关键点
1. 推出LigBench自动化评估基准，支持跨不同生成分布的细粒度、可靠的AI科研想法评估
2. 开源PAIR-IQ配对标注数据集，专门用于训练配对想法判断模型，辅助更客观的对比评估

### 关键结果
- LigBench的评估结果稳定可解释，与专家判断的对齐度显著优于现有直接LLM打分方案
- 基于PAIR-IQ训练的想法排序模型，排序准确率与鲁棒性均有明显提升，为可扩展的客观想法评估建立了标准化范式
