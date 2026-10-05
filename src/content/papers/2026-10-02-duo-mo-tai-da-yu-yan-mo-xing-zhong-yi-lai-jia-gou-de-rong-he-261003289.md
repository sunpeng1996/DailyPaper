---
title: Architecture-Dependent Fusion Pathways in MLLMs
title_zh: 多模态大语言模型中依赖架构的融合路径研究
authors:
- Hebao Zhu
- Dongxia Wu
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.03289'
url: https://arxiv.org/abs/2610.03289
pdf_url: https://arxiv.org/pdf/2610.03289
published: '2026-10-02'
collected: '2026-10-05'
category: Multimodal
direction: 多模态大模型 · 跨模态融合机制分析
tags:
- MLLM
- Multimodal Fusion
- Attention Routing
- CKA
- Feature Alignment
one_liner: 揭示两类MLLM架构的跨模态融合路径差异，提供多模态融合机制解释与架构感知诊断方法
practical_value: '- 选型搜广推场景MLLM时优先选择原生多模态架构，可实现更早的图文特征共适配，提升跨模态召回/排序效率

  - 可复用对齐解耦、注意力路由熵、固有维度三类分析方法，诊断自研MLLM的跨模态融合效果

  - 做MLLM多模态特征适配时，可参考visual CKA指标验证跨模态表征对齐程度，降低下游任务调优成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前MLLM跨层图文融合内部机制尚不明确，不同架构范式的融合路径差异缺乏系统性量化分析，制约MLLM的架构选型与业务场景优化。
### 方法关键点
针对拼接式、原生多模态两类主流MLLM架构，开展三层递进分析：对齐解耦识别模态变化规律，注意力路由与熵量化跨模态信息分布，固有维度分析特征空间重构规律，补充因果干预实验、visual CKA指标验证结论可靠性。
### 关键结果
明确两类架构的差异化融合路径：拼接式MLLM遵循先文本、后视觉的融合顺序，原生多模态MLLM可实现更早的图文共适配与特征空间重组，证明架构设计直接决定跨模态融合效率。
