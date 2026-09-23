---
title: Virtual Encoders in Multimodal Transformers
title_zh: 多模态Transformer中的虚拟编码器
authors:
- Katsuya Ogata
- Yuta Nakashima
affiliations:
- The University of Osaka
arxiv_id: '2609.26513'
url: https://arxiv.org/abs/2609.26513
pdf_url: https://arxiv.org/pdf/2609.26513
published: '2026-09-22'
collected: '2026-09-23'
category: Multimodal
direction: 多模态大模型 · 感知编码机制研究
tags:
- Multimodal-LLM
- Transformer
- Virtual-Encoder
- Perception-Encoding
- Encoder-free-MLLM
one_liner: 发现无专用感知编码器的多模态大模型可在Transformer早中层自发形成类编码器的虚拟计算结构
practical_value: '- 多模态商品理解、图文搜索场景优化时，可裁剪冗余的专用视觉编码器，利用Transformer早中层的Virtual Encoder能力降本提速

  - 多模态生成式推荐场景下，可针对性微调Transformer早中层提升感知编码精度，无需调整全量backbone，大幅降低训练成本

  - 轻量级多模态Agent端侧部署优化时，可采用轻量投影+共享Transformer的架构，去掉外部感知编码器模块，降低端侧推理时延'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统多模态大模型依赖独立的专用感知编码器生成任务可用表征，近年无编码器、离散token类集成式多模态架构兴起，但感知编码计算的实际发生位置与机制未被明确。
### 方法关键点
针对编码器全量、离散token、无编码器三类主流MLLM架构，通过线性探测、感知编码器表征相似性比对、因果干预三类分析，定位感知计算的功能边界与结构特征。
### 关键结果
验证了无外部专用编码器的MLLM会在Transformer早-中层自发形成具备感知编码能力的Virtual Encoder结构，其生成的表征可直接支撑下游多模态任务；同时证明感知与语言处理的边界无需与架构模块对齐，类编码器计算可作为共享Transformer内的独立功能域存在，为多模态架构简化提供了理论支撑。
