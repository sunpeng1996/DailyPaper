---
title: Evaluating LLM Creativity through Long-Tail Performance
title_zh: 基于长尾性能的大语言模型创造力评估
authors:
- Yichen Wang
- Tenghao Huang
- Vishakh Padmakumar
- Mina Lee
affiliations:
- University of Chicago
- Microsoft
- Stanford University
arxiv_id: '2610.12998'
url: https://arxiv.org/abs/2610.12998
pdf_url: https://arxiv.org/pdf/2610.12998
published: '2026-10-08'
collected: '2026-10-14'
category: Eval
direction: LLM 创造力评估指标设计
tags:
- LLM Creativity
- Long Tail
- Evaluation Metric
- Benchmark
- Open-source LLM
one_liner: 提出以参考分布长尾性能量化LLM创造力，设计低成本q@Tail(α)诊断指标
practical_value: '- 做生成式推荐/营销文案生成的模型选型时，可直接复用q@Tail(α)指标评估模型创意输出能力，替代高成本人工标注

  - 电商场景冷启动长尾商品、个性化小众兴趣推荐的创意召回策略，可参考「预训练数据n-gram缺失度」作为新颖性proxy快速筛选候选物料

  - 优化Agent的创意任务（比如营销活动策划、小众用户需求响应）能力时，可定向提升模型在长尾输入输出分布上的性能，无需重构全量训练流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM创造力基准的任务和指标设计差异大，无法统一衡量创造力的核心共性特征，难以对齐人类对创造力的判断标准。
### 方法关键点
1. 将创造力统一形式化为参考输入-输出分布长尾区域的任务特定性能，用预训练数据中n-gram缺失度作为新颖性代理指标，基于新颖性-质量乘积范式落地评估逻辑
2. 设计低成本评估指标q@Tail(α)，仅需在现有基准的α比例长尾子集上计算平均任务质量即可完成创造力诊断，无需设计新的专用基准
### 关键结果
- 覆盖15个基准、26个开源模型的实验显示，创造力基准相比标准基准更多位于分布长尾区域
- 两类基准的长尾子集模型排序与LM-Arena人类创造力判断的对齐度显著高于全量基准
- 用q@Tail(α)评估现有创造力优化方法，证明当前方法的长尾性能提升空间极大
