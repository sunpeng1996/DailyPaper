---
title: 'Temporal Self-Distillation: Learning Visual State Tracking in Videos Without
  Supervision'
title_zh: 时间自蒸馏：无监督学习视频中的视觉状态跟踪
authors:
- Shravan Venkatraman
- Wenshuai Zhao
- Mohammad Hassan Vali
- Arno Solin
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Aalto University
arxiv_id: '2609.04203'
url: https://arxiv.org/abs/2609.04203
pdf_url: https://arxiv.org/pdf/2609.04203
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 多模态大模型 · 无监督视频理解
tags:
- Self-Supervised-Learning
- Knowledge-Distillation
- Video-Understanding
- Multimodal-LLM
- State-Tracking
one_liner: 提出S³T无监督时间自蒸馏框架，无需标注/独立教师即可提升多模态大模型视频状态跟踪能力
practical_value: '- 多模态电商内容理解场景可复用时间自蒸馏思路，对直播/短视频的商品状态、动作计数等任务做无监督微调，无需标注即可提升模型时序感知能力

  - 特权信息自蒸馏范式可迁移到搜索推荐的用户行为序列建模，用高密度行为序列做教师蒸馏低密度序列的用户兴趣预测模型，无额外标注成本

  - 自蒸馏训练不增加推理成本的特性适配大模型线上部署需求，可在不改变推理链路的前提下提升多模态模型时序任务性能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频状态跟踪方法依赖标注、外部裁判或独立教师模型，训练成本高，且大多仅挖掘空间信息，无法有效建模时序演进的场景状态，时序泛化性差。

### 方法关键点
提出S³T自监督时间自蒸馏框架，将时间采样密度作为特权信息：同一段视频的高密度采样视图作为教师，共享权重的低密度采样视图作为学生，让学生匹配教师的next-token分布，全程无需标注、独立教师或奖励信号，推理无额外开销。

### 关键结果数字
基于LLaVA-OneVision-2-8B测试，单模型VSTAT精度提升1.74，模型融合后提升2.38，配合视觉编码器适配后提升2.70；合成视频训练的能力可迁移到真实场景，VSTAT-YouTube任务精度提升7.95，MVBench动作计数任务提升4.50，性能远超现有自进化方法。
