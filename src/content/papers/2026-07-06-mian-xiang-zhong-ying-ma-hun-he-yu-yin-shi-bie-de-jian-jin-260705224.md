---
title: 'Progressive Refinement: An Iterative Pseudo-Labeling Approach for Mandarin-English
  Code-Switching ASR'
title_zh: 面向中英码混合语音识别的渐进式迭代伪标注方法
authors:
- Qu Yang
- Cakra Wardhana
- Tim Ng
affiliations:
- Apple, Singapore
- National University of Singapore, Singapore
arxiv_id: '2607.05224'
url: https://arxiv.org/abs/2607.05224
pdf_url: https://arxiv.org/pdf/2607.05224
published: '2026-07-06'
collected: '2026-07-08'
category: Other
direction: 中英混语音识别 · 半监督伪标注训练
tags:
- Semi-supervised Learning
- Pseudo Labeling
- Code-switching ASR
- Speech Recognition
- Iterative Training
one_liner: 首次将迭代伪标注应用于中英混语音识别，利用无标注数据有效降低识别混错率
practical_value: '- 做语音导购、语音搜索类电商Agent时，面对用户中英混输入（如“帮我找Adidas的跑步鞋”），可复用迭代伪标注框架，利用海量无标注用户语音数据优化ASR效果，大幅降低标注成本

  - 小样本标注场景下，「伪标签生成→两阶段预训练微调→迭代优化」的训练范式可直接迁移至多模态Query理解、跨语言内容识别等推荐搜索上游任务

  - 面向东南亚等多语言电商市场，无需大规模标注混语语料，通过迭代伪标注就能快速提升语音搜索的识别准确率，缩短新市场落地周期'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
中英码混合（CS）语音在东南亚等多语言区域的用户语音交互中普遍存在，但标注CS训练数据稀缺，现有ASR模型对混语场景识别准确率低，无法满足语音助手、语音搜索等场景的体验要求。
### 方法关键点
首次将迭代伪标注框架引入CS-ASR任务，分为三个核心阶段：1. 基于基线模型对大规模无标注语料生成伪标签，构建半监督训练数据集；2. 两阶段双语模型训练：先在半监督数据集上预训练，再在少量有标注CS数据上微调；3. 多轮迭代更新伪标签与模型参数，逐步优化复杂码混合场景的识别能力。
### 关键结果
在SEAME公开数据集的devman子集上Mix Error Rate（MER）降低6.35%，devsge子集上MER降低8.29%，效果显著优于基线方案。
