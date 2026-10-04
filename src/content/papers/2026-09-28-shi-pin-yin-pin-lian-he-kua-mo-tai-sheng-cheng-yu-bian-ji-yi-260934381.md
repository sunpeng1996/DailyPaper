---
title: 'Joint and Cross-Modal Video-Audio Generation and Editing: A Unified Formulation
  and Design Taxonomy'
title_zh: 视频-音频联合跨模态生成与编辑：统一表述与设计分类体系
authors:
- Abhinav Sharma
- Sai Karthik Navuluru
- Wang Wei
- Daksh Dangi
- Xiangbo Gao
- Li Li
- Bo Ni
- Vardhan Dongre
- Junda Wu
- Xiyang Hu
affiliations:
- Adobe Research
- University of Massachusetts Amherst
- Virginia Tech
- Stanford University
- Texas A&M University
arxiv_id: '2609.34381'
url: https://arxiv.org/abs/2609.34381
pdf_url: https://arxiv.org/pdf/2609.34381
published: '2026-09-28'
collected: '2026-10-04'
category: Multimodal
direction: 多模态生成 · 音视频联合编辑
tags:
- Multimodal Generation
- Audio-Visual Learning
- Cross-Modal Generation
- Generative Editing
- Taxonomy
one_liner: 首次提出音视频联合/跨模态生成与编辑的统一表述及五维度设计分类体系
practical_value: '- 电商短视频广告生成场景可参考其音视频语义/时序一致性对齐的设计维度，避免音画不同步问题，提升内容转化率

  - 跨模态生成场景（如给商品短视频自动配BGM/旁白）可复用其跨模态生成的任务框架与评估指标，降低效果验证成本

  - 多模态内容批量编辑场景（如批量修改广告的画面/音效/口播）可参考其9大类28种编辑类型划分，对齐业务需求覆盖度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频生成模型多单独建模两个模态，朴素拼接易出现时序、语义不一致问题，缺乏对联合生成、跨模态生成、联合编辑三类任务的统一梳理。

### 方法关键点
- 构建统一表述框架，将三类任务均建模为音视频对联合分布上的求解问题
- 沿五个设计维度构建方法分类体系，首次系统梳理音视频联合编辑任务
- 整理每类任务对应的现有方法、数据集、评估指标，总结核心开放问题

### 关键结果
共梳理出9大联合编辑类别，覆盖28种具体编辑类型
