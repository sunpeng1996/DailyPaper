---
title: 'The Geometry of Simulated Perspectives: Dissociating Representation and Behaviour
  in a Multimodal Language Model'
title_zh: 模拟视角的几何学：多模态大语言模型中表征与行为的解耦
authors:
- Mathis Immertreu
- Fitim Abdullahu
- Thomas Kinfe
- Claus Metzner
- Helmut Grabner
- Patrick Krauss
- Achim Schilling
affiliations:
- University Erlangen-Nürnberg
- ZHAW School of Engineering
- Heidelberg University
- BGU Ludwigshafen
arxiv_id: '2611.08262'
url: https://arxiv.org/abs/2611.08262
pdf_url: https://arxiv.org/pdf/2611.08262
published: '2026-11-05'
collected: '2026-11-07'
category: LLM
direction: 多模态LLM 表征与行为解耦研究
tags:
- Multimodal LLM
- Representational Geometry
- Persona Prompt
- Prompt Engineering
- Internal Representation
one_liner: 揭示多模态大模型中prompt框架、人设对内部表征与输出行为的影响存在解耦效应
practical_value: '- 做人设驱动的Agent/个性化推荐时，不要仅通过内部表征相似度判断人设生效性，应以实际输出行为为核心判断标准

  - Prompt工程优化时，若想改变多模态模型输出优先调整人设内容，若想对齐模型内部表征空间优先调整prompt表述框架

  - 做个性化生成任务时，可通过轻量的身份声明prompt调整模型内部表征，无需修改输出即可实现后续任务的表征预对齐'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态大模型可模拟不同观察者视角，但人设等视角信息如何重塑内部表征、表征变化是否决定输出判断的机制尚不明确。
### 方法关键点
以Qwen3-VL-8B-Instruct为研究对象，基于100张图像、53种prompt条件，系统控制人设内容与prompt引入框架，同时采集行为评分与逐层隐状态，分析表征几何结构变化规律。
### 关键结果
- 表征几何随网络深度系统重组：浅层主要编码图像身份，人设专属结构在深层涌现
- Prompt框架对内部表征的重塑强度显著高于人设身份，但人设内容对行为判断的影响更大
- 存在明确的表征-行为解耦现象：仅修改身份声明不改变输出时，内部表征仍会发生变化，表征距离与行为相关性无必然对应关系
