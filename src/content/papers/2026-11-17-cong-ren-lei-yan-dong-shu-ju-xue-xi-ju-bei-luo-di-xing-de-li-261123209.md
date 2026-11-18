---
title: Learning Grounded Reasoning from Human Gaze
title_zh: 从人类眼动数据学习具备落地性的视觉推理能力
authors:
- Gabriel Sarch
- Declan Campbell
- Nicholas Budny
- Kia Ghods
- Katerina Fragkiadaki
- Jonathan D. Cohen
- Brenden M. Lake
- Taylor W. Webb
affiliations:
- Princeton University
- Perceptron AI
- Carnegie Mellon University
arxiv_id: '2611.23209'
url: https://arxiv.org/abs/2611.23209
pdf_url: https://arxiv.org/pdf/2611.23209
published: '2026-11-17'
collected: '2026-11-18'
category: Reasoning
direction: 多模态推理 · 眼动引导人类对齐
tags:
- VLM
- Visual Reasoning
- Human Gaze
- Alignment
- Reinforcement Learning
one_liner: 提出眼动引导推理模型GGR，在不模仿完整眼动序列的前提下提升VLM视觉推理表现与人类对齐度
practical_value: '- 电商多模态搜索/商品理解场景，可采集用户浏览眼动热点作为弱监督信号，替代完整行为序列训练多模态模型，降低标注成本同时提升推理对齐度

  - Agent视觉探索任务中，无需完全模仿人类行为全序列，仅用人类行为先验做引导，再结合RL微调即可同时提升任务精度与人类对齐度

  - 多模态模型行为对齐任务中，可优先采用先验引导+RL优化的范式，避免原始人类行为数据中的噪声与冗余带来的负迁移'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉-语言模型（VLM）的视觉推理缺乏类人的空间探索逻辑，直接采用人类完整眼动序列做监督会引入噪声与冗余，迁移到VLM的效果较差。
### 方法关键点
1. 收集覆盖图表理解、视觉搜索、计数三类任务的7109条人类眼动试验数据，对比不同眼动引导方式的训练效果
2. 提出GGR模型，仅将人类眼动作为推理先验而非完整监督信号，可结合强化学习（RL）进一步优化
### 关键结果数字
- 三类视觉推理任务上，GGR性能持平或超过现有SOTA grounded reasoning基线，人类眼动对齐度显著提升
- GGR-RL版本的视觉grounding准确率达74.9%，比无眼动引导的RL基线高4.4个百分点
- 仅用眼动先验引导的方案，效果显著优于全眼动序列监督的方案
