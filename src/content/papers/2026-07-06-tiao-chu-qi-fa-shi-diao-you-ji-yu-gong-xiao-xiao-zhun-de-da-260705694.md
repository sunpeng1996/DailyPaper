---
title: 'Beyond Heuristic Tuning: Power-Calibrated LLM Watermarking'
title_zh: 跳出启发式调优：基于功效校准的大语言模型水印方法
authors:
- Xiaopu Wang
- Zelin He
- Chengyuan Liu
- Runze Li
affiliations:
- Department of Statistics, Pennsylvania State University
arxiv_id: '2607.05694'
url: https://arxiv.org/abs/2607.05694
pdf_url: https://arxiv.org/pdf/2607.05694
published: '2026-07-06'
collected: '2026-07-09'
category: LLM
direction: LLM生成内容水印超参优化
tags:
- LLM Watermarking
- Hyperparameter Tuning
- Statistical Framework
- Pareto Optimization
- Content Provenance
one_liner: 构建功效校准统计框架，量化LLM水印超参、检测能力与语义失真关联，自动生成帕累托最优参数配置
practical_value: '- 做LLM生成商品文案、推荐话术的内容溯源时，可复用该框架校准水印超参，在不影响文案语义效果的前提下最大化检测成功率

  - 若业务对生成内容的失真容忍度、水印检测率有明确约束，可直接套用其参数选择流程快速得到最优配置，替代人工启发式调参

  - 该统计建模思路可迁移到生成式推荐中Semantic ID的隐式水印嵌入场景，平衡ID可识别性与推荐效果损耗'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
基于logit的LLM水印是生成内容溯源的主流方案，但核心存在可检测性与语义失真的权衡，现有方案超参选择缺乏理论指导，完全依赖人工启发式调优，落地成本高、效果不稳定。
### 方法关键点
1. 提出功效校准统计框架，量化建立水印超参、检测功效、语义失真三者的显式映射关系，将水印设计转化为可求解的约束优化问题；
2. 推导可直接落地的参数选择流程，可基于业务给定的失真容忍度、检测率要求，自动输出最优超参组合。
### 关键结果
跨多个LLM、多数据集的实验验证，该框架可稳定输出帕累托最优水印配置，无需人工调参即可实现检测能力与语义保留的最优平衡。
