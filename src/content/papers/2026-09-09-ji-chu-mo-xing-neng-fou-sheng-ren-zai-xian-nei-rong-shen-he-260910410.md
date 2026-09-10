---
title: Can Foundation Models Moderate Online Content? Evaluating Instruction- vs.
  Example-Driven Policy Operationalization
title_zh: 基础模型能否胜任在线内容审核？指令与示例驱动策略落地对比
authors:
- Ayan Majumdar
- Shounak Paul
- Pushpdeep Singh
- Ines Abdelaziz
- Sayeh Jarollahi
- Seungeon Lee
- Krishna P. Gummadi
- Ingmar Weber
- Abhisek Dash
affiliations:
- MPI-SWS
- Saarland University
- INRIA
arxiv_id: '2609.10410'
url: https://arxiv.org/abs/2609.10410
pdf_url: https://arxiv.org/pdf/2609.10410
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: 大模型内容审核 · 范式对比评估
tags:
- Content Moderation
- VLM
- Instruction Tuning
- Few-shot Learning
- Benchmark
one_liner: 构建4000条真实帖子的ModerationBench，对比VLM两种内容审核范式，效果远超现有部署系统
practical_value: '- 电商UGC、商品评论、直播间弹幕等内容审核场景，可直接复用指令/示例驱动的VLM范式，两种峰值效果相当可按需选择

  - 业务侧有复杂审核规则落地需求时，可参考论文思路先构建千级规模的场景专属标注测试集，快速验证模型适配效果

  - 现有规则匹配类审核系统效果不佳的长尾场景，替换为VLM方案无需大量标注即可获得数倍F1提升'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前各大平台内容审核政策日趋复杂，传统规则式系统落地一致性差、迭代成本高，大模型能否支撑可靠的规模化内容审核尚无明确验证结论。
### 方法关键点
1. 构建ModerationBench基准数据集，包含4000条Bluesky平台的真实公开帖子，全部经过人工标注；
2. 系统对比两类VLM引导范式：基于政策条文直接推理的指令驱动范式、基于历史标注判例泛化的示例驱动范式。
### 关键结果
两类范式的峰值效果基本持平，大模型方案在随机帖子测试集上F1达到0.60，是Bluesky现有部署审核系统（F1=0.22）的近3倍
