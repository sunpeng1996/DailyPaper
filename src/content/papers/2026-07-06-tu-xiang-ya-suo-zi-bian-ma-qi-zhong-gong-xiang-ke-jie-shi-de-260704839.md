---
title: Discovering shared interpretable operations in image compression autoencoders
title_zh: 图像压缩自编码器中共享可解释操作的挖掘
authors:
- Caroline Mazini Rodrigues
- Nicolas Keriven
- Thomas Maugey
affiliations:
- Univ. Rennes
- Inria
- CNRS
- IRISA
arxiv_id: '2607.04839'
url: https://arxiv.org/abs/2607.04839
pdf_url: https://arxiv.org/pdf/2607.04839
published: '2026-07-06'
collected: '2026-07-10'
category: Other
direction: 深度学习可解释性 · 图像压缩模型优化
tags:
- Interpretability
- Autoencoder
- Image Compression
- Jacobian Analysis
- Model Efficiency
one_liner: 通过雅可比分析挖掘无偏图像压缩自编码器内部通用可解释操作，支撑低复杂度模型设计
practical_value: '- 雅可比分析挖掘黑盒模型内部通用核心操作的思路，可迁移到LLM/推荐大模型的轻量化优化，从高复杂度SOTA模型提取核心逻辑降本

  - 若业务涉及商品图/短视频等多模态内容的压缩存储、端侧传输，可复用无偏自编码器通用操作挖掘范式，降低部署硬件门槛

  - 从高复杂度模型提炼共享可解释模块的思路，可用于指导推荐模型的分块可解释性设计，降低问题排查难度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
深度学习图像压缩自编码器的率失真性能提升高度依赖模型规模与复杂度增长，黑盒特性导致轻量化改造缺乏明确指导，硬件受限场景部署难度高；现有可解释性分析多为局部结论，无法支撑通用轻量化架构设计。
### 方法关键点
针对无偏图像压缩自编码器，引入雅可比分析方法挖掘模型内部运行的通用共享可解释操作，验证这类操作的跨模型可迁移性，基于提炼的核心操作推导低复杂度压缩模型的设计思路。
### 结果
已验证该方法可稳定定位不同架构无偏自编码器中的共享核心操作，后续基于该操作设计的轻量化压缩模型可在性能损失可控的前提下，大幅降低计算开销与存储占用。
