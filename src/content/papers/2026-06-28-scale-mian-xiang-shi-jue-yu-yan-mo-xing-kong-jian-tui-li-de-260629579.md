---
title: 'ScAle: Attention Head Scaling as a Minimal Adapter for Spatial Reasoning in
  Vision Language Models'
title_zh: 'ScAle: 面向视觉语言模型空间推理的超轻量注意力头缩放适配器'
authors:
- Rahul Chowdhury
- Timothy A Rupprecht
- Xuan Shen
- Pu Zhao
- Yanzhi Wang
affiliations:
- Northeastern University
- EmbodyX Inc.
- Zhejiang University
arxiv_id: '2606.29579'
url: https://arxiv.org/abs/2606.29579
pdf_url: https://arxiv.org/pdf/2606.29579
published: '2026-06-28'
collected: '2026-07-01'
category: Training
direction: 参数高效微调 · VLM空间推理优化
tags:
- PEFT
- VLM
- Spatial Reasoning
- Attention Head
- Parameter Efficiency
- LoRA
one_liner: 仅用1K可训练参数的激活缩放PEFT方案，大幅提升VLM空间推理性能，参数效率远超LoRA
practical_value: '- 多模态搜广推场景中可复用激活重加权思路替代LoRA做轻量微调，大幅降低多模态大模型适配的参数开销

  - 面向商品空间位置理解、多模态Query理解等需空间推理的任务，可参考仅调整last-token注意力+MLP激活的微调范式，不破坏基座原有能力

  - 低资源多模态Agent部署时，可采用该超轻量适配方案快速对齐特定下游任务，边缘端也可落地'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视觉语言模型（VLM）空间推理能力普遍偏弱，常规参数高效微调（PEFT）方案如LoRA需百万级可训练参数，适配成本高；前期实验发现无需修改预训练权重，仅重缩放Transformer选中层的激活值，就能显著影响下游空间推理性能。
### 方法关键点
ScAle为架构无关的超轻量适配方案，完全冻结基座权重，仅学习一组标量系数，调制最后token的注意力头输出与MLP层激活值，无需修改原有模型结构。
### 关键结果
在SpatialEval、COCOQA、VGQA等多类数据集跨模型家族评测，仅用1K可训练参数，相对精度增益最高达134.1%，参数效率远高于LoRA等常规PEFT方法；同时能保留非空间VQA任务的原有精度，可恢复常规PEFT方案的大部分性能。
