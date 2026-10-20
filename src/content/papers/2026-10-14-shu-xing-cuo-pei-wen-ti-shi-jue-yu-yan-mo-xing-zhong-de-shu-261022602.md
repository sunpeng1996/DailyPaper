---
title: 'Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models'
title_zh: 属性错配问题：视觉语言模型中的属性-对象绑定能力研究
authors:
- Netanel Y. Tamir
- Michael Green
- Issar Tzachor
- Or Shimshi
- Dvir Samuel
- Or Patashnik
- Rami Ben-Ari
affiliations:
- OriginAI
- NVIDIA
- Tel Aviv University
arxiv_id: '2610.22602'
url: https://arxiv.org/abs/2610.22602
pdf_url: https://arxiv.org/pdf/2610.22602
published: '2026-10-14'
collected: '2026-10-20'
category: Multimodal
direction: 多模态检索 · 属性-对象绑定能力优化
tags:
- Multimodal Retrieval
- Vision-Language Model
- Attribute-Object Binding
- Benchmark
- LoRA
one_liner: 提出SABER基准评测多模态模型属性-对象绑定能力，纯文本微调实现跨模态检索性能提升
practical_value: '- 多模态商品检索场景可复用SABER的测试构造逻辑，引入属性-对象错配的hard negative优化检索模型，减少「红色裙子」搜出「红色鞋子」类错误

  - 无需收集昂贵的多模态标注，仅用合成的属性绑定文本数据+LoRA微调MLLM embedder，即可提升跨模态检索效果，适配电商SKU多、标注成本高的场景

  - 微调时冻住预训练主干仅训练LoRA，保留通用多模态嵌入能力的同时优化绑定能力，可直接复用现有MLLM embedding底座，改造落地代价低'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态检索模型的嵌入无法准确捕捉属性-对象绑定关系，现有评测基准仅覆盖简单双对象交换、少量属性、部分模态配对场景，无法全面评测复杂场景下的绑定能力，且依赖多模态标注的优化方案成本极高。
### 方法关键点
1. 提出SABER可控基准，覆盖全4种图文模态配对、多样属性类型、最多10个对象的复杂场景，可全面量化属性绑定能力缺陷
2. 仅使用合成的属性绑定文本数据，对MLLM-based embedder做LoRA微调，无需图像监督即可优化跨模态绑定能力。
### 关键结果
微调后模型在SABER上达到SOTA，同时在否定语义、实例检索基准上实现性能提升，跨模态、图-图检索效果均有增益，且不损失通用多模态嵌入性能。
