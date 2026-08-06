---
title: 'CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning'
title_zh: CURV：基于课程式视觉锚定推理的图表理解能力增强
authors:
- Xuehang Guo
- Pingyue Zhang
- Ruiyi Zhang
- Zhenhailong Wang
- Hanrui Lyu
- Heng Ji
- Tong Sun
- Qingyun Wang
- Manling Li
affiliations:
- William & Mary
- Northwestern University
- Adobe
- UIUC
arxiv_id: '2608.02833'
url: https://arxiv.org/abs/2608.02833
pdf_url: https://arxiv.org/pdf/2608.02833
published: '2026-08-02'
collected: '2026-08-06'
category: Reasoning
direction: 多模态推理 · 课程式视觉锚定
tags:
- Multimodal LLM
- Chart QA
- Curriculum Learning
- Visual Grounding
- Reasoning Chain
one_liner: 提出课程式视觉锚定推理框架CURV与配套数据集，大幅提升图表问答及跨域多模态推理性能
practical_value: '- 电商/广告场景的运营报表、用户趋势图自动问答Agent开发，可复用多步推理+动态视觉锚定联动逻辑，解决MLLM感知不准、推理脱离视觉证据的问题

  - 多模态任务模型训练可参考三级课程式数据集构建思路，从单步简单任务到多步复杂任务递进训练，降低训练难度同时提升最终效果

  - 跨域多模态推理需求落地时，可借鉴空间注意力集中的动态grounding设计，提升模型在未知场景下的泛化性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态大模型（MLLM）在图表问答（CQA）任务中缺乏内生视觉锚定推理能力，仅靠外部CoT提示、视觉cue优化无法解决感知不准确、推理与视觉证据脱节的问题。

### 方法关键点
1. CURV课程学习框架将CQA重定义为多步视觉锚定推理任务，每步通过空间注意力集中机制联动逻辑推理与动态视觉锚定
2. 配套CCQA三级课程数据集支持规模化生成覆盖多样图表类型、推理模式的样本，训练流程从单操作基础推理到多图表组合复杂任务递进

### 关键结果
相比基线模型性能最高提升20.50%，在真实世界基准数据集上最高提升12.30%，跨域多模态推理任务上最高提升10.20%
