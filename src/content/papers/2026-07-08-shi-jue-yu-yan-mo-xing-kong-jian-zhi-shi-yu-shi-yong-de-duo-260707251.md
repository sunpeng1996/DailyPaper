---
title: Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language
  Models
title_zh: 视觉语言模型空间指示语使用的多语言能力评估
authors:
- Kaito Watanabe
- Taisei Yamamoto
- Tomoki Doi
- Hitomi Yanaka
affiliations:
- The University of Tokyo
- Riken
- Tohoku University
arxiv_id: '2607.07251'
url: https://arxiv.org/abs/2607.07251
pdf_url: https://arxiv.org/pdf/2607.07251
published: '2026-07-08'
collected: '2026-07-09'
category: Eval
direction: VLM多语言空间推理能力评估
tags:
- VLM
- Multilingual
- Spatial Reasoning
- Benchmark
- Evaluation
one_liner: 构建4种语言的空间指示语评估基准，揭示现有VLM相关表现与人类存在显著差异
practical_value: '- 做跨语种多模态商品导购Agent时，可复用该评估思路验证VLM对多语言空间指代（如“这个/那个”）的理解准确率

  - 跨境电商多模态Query理解场景，可针对不同语言的空间指示语距离判定规则做微调数据增强，降低指代理解误差

  - 多语言VLM迭代优化时，可直接复用该公开基准作为验证集，快速量化空间推理维度的能力提升'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM的多语言空间推理能力缺乏针对性评估，尤其是依赖上下文的空间指示语（如this/that）的跨语种适配能力尚未被系统研究，这类能力是多模态对话、交互类场景的核心基础能力。

### 方法关键点
构建覆盖4种语言的空间指示语评估基准，要求模型同时对齐图像空间结构、理解不同语言专属的空间区分规则，结合物体与观察者的距离等上下文信息选择正确的指示代词，核心考察跨模态对齐、语言规则适配、上下文推理三重能力。

### 关键结果
测试的主流VLM在指示代词选择上与人类表现存在显著差异，尤其在基于物体距离的指示词选择任务上表现明显差于人类，不同语言的能力表现差距较大。
