---
title: Do Vision-Language Models Agree on the Affective Qualities of Shape? A Cross-Model
  Audit for Generative Design Interfaces
title_zh: 视觉语言模型对形状情感属性的认知一致性：生成设计界面跨模型审计
authors:
- Luca Bux
- Thiago Rios
- Ingo Scholtes
- Stefan Menzel
affiliations:
- Honda Research Institute Europe GmbH
- Julius-Maximilians-Universität Würzburg
arxiv_id: '2608.25876'
url: https://arxiv.org/abs/2608.25876
pdf_url: https://arxiv.org/pdf/2608.25876
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: 多模态VLM评估 · 生成设计语义控制
tags:
- VLM
- Affective Semantics
- Generative Design
- Cross-Model Evaluation
- Kansei Engineering
one_liner: 审计6款VLM对3D物体情感属性排序的一致性，为生成设计界面语义控件选型提供依据
practical_value: '- 电商3D商品生成场景，可复用本文的形容词轴对齐评估方法，筛选不同品类下VLM认知一致的风格控制词（如「极简」「优雅」）作为交互控件，降低生成结果不符合用户预期的概率

  - 多模态生成系统的语义控件选型，可参考本文的正负对照评估框架：用几何属性作为正控、无关形容词对作为空对照，量化不同语义方向的模型一致性

  - 注意跨VLM一致性不代表和人类判断一致，业务上线语义控制功能前需补充人工标注校验，避免模型共识偏离用户真实感知'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成设计界面广泛采用VLM编码「优雅」「极简」等情感语义作为用户调控控件，但不同SOTA VLM对同一物体情感属性的表示一致性缺乏验证，易出现控件调控效果不符合预期的问题。
### 方法关键点
选取6款SOTA VLM，基于Kansei工程的情感形容词对构建语义轴（两极文本表征的差值），对ShapeNet 10个类别的无纹理3D物体做情感属性排序；设置几何属性对为正对照、无关形容词对为经验空对照，量化跨模型排序相关性。
### 关键结果
情感轴跨模型平均两两秩相关为0.36，高于空对照的0.14，低于几何属性上限的0.44；不同品类一致性差异显著，书架类仅0.21，罐子类达0.51；一致性核心取决于品类表征变异与语义方向的匹配度，而非整体形状变异程度，且跨模型共识不代表符合人类判断，基于结果可指导不同品类的语义控件筛选。
