---
title: 'The Geometry of Metaphor: Probing and Steering Metaphor Representations in
  Large Language Models'
title_zh: 隐喻的几何结构：大语言模型中隐喻表征的探测与调控
authors:
- Shihui Li
- Mette Andersen
- Martha Lewis
affiliations:
- University of Amsterdam
- Institute for Logic, Language, and Computation
arxiv_id: '2610.31520'
url: https://arxiv.org/abs/2610.31520
pdf_url: https://arxiv.org/pdf/2610.31520
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 大语言模型机制可解释性 · 输出属性调控
tags:
- Mechanistic Interpretability
- LLM Control
- Representation Probing
- Causal Subspace
- Metaphor Generation
one_liner: 利用机制可解释性技术识别LLM中隐喻表征的因果子空间，可调控输出内容的隐喻程度
practical_value: '- 广告/营销文案生成场景可复用因果子空间探测方法，定向调控文案的隐喻/文艺程度，适配不同用户群体的内容偏好

  - 商品卖点、活动话术生成时，可通过干预LLM特定层表征的方式快速调整表达风格，无需额外微调或复杂prompt工程

  - 可迁移因果子空间识别思路，用于探测LLM中幽默、正式度、亲和力等其他风格属性的表征方向，实现多维度输出管控'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
隐喻是人类认知和语言表达的核心组成部分，当前LLM虽具备一定隐喻理解生成能力，但缺乏机制层面的表征解释，也缺少低成本调控输出隐喻程度的可行方案。
### 方法关键点
采用机制可解释性技术，在不同架构、不同参数量的LLM中识别隐喻表征对应的因果子空间，通过对模型特定层的表征做因果干预实现输出属性调控，无需额外训练数据或微调。
### 关键结果
跨词性的隐喻分类任务中输出调控准确率稳定达标，生成任务中可精准控制输出文本的隐喻性/字面性程度，方案适配多种主流LLM架构。
