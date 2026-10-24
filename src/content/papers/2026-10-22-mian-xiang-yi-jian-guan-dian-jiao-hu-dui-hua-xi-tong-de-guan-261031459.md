---
title: How Different, or Different How? Stance Granularity in Viewpoint Selection
  for Dialog Systems that Engage Users with Alternative Views
title_zh: 面向异见观点交互对话系统的观点选择立场粒度研究
authors:
- Morita Tarvirdians
- Reeve Lorena
- Catharine Oertel
affiliations:
- TU Delft
arxiv_id: '2610.31459'
url: https://arxiv.org/abs/2610.31459
pdf_url: https://arxiv.org/pdf/2610.31459
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: 对话Agent · 异见观点选择策略优化
tags:
- Stance Encoding
- Viewpoint Selection
- Dialog Agent
- User Modeling
- Controlled Experiment
one_liner: 提出概念级立场向量的观点选择策略，相较传统标量评分实现更广的异见观点覆盖
practical_value: '- 推荐系统做破茧房的异质内容推送时，可替换单一兴趣距离分为概念级立场向量表示，有效提升内容覆盖广度

  - 电商客服/导购Agent处理用户争议性诉求时，可按概念维度拆解用户立场，精准匹配差异点做引导提升转化效率

  - 用户研究可参考其被试间实验设计，量化用户对异质内容的接受度、记忆准确率，辅助策略迭代'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有异见观点推荐仅用标量评分衡量观点差异，粒度过粗无法区分不同维度的立场分歧，易造成内容覆盖窄、无法有效打破信息茧房。
### 方法关键点
1. 基于多臂老虎机设计观点选择策略，动态设定观点与用户立场的差异阈值，在阈值内选取最具新颖性的候选观点；
2. 对比两类立场编码器：传统标量立场评分、Perspectivized Stance Vectors（将整体立场拆解为不同概念维度的独立立场表示）；
3. 落地到对话系统开展63名用户的被试间对照实验。
### 关键结果
概念级立场编码可提升观点曝光序列多样性与话题立场覆盖广度，但未显著改变用户观点论证深度与重构准确率；用户对某概念无明确立场时的观点重构准确率，远低于双方观点存在分歧的场景。
