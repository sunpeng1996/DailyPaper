---
title: 'Persistent Identity Preservation in Generative Image Models: A Benchmark and
  Evaluation System'
title_zh: 生成式图像模型持久身份保留：基准与评估系统
authors:
- Mengwei Ren
- Xuaner Zhang
- Zhihao Xia
affiliations:
- Phota Labs Research
arxiv_id: '2609.04151'
url: https://arxiv.org/abs/2609.04151
pdf_url: https://arxiv.org/pdf/2609.04151
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 多模态生成 · 身份保留基准测评
tags:
- Identity Preservation
- Generative Image Model
- Benchmark
- LoRA
- Persistent Identity
one_liner: 系统测评三类主体驱动生成的身份表示范式，验证持久身份层可显著提升多场景身份保真度
practical_value: '- 电商商品图生成/编辑场景可引入持久身份层方案，避免迭代修图、多主体合成时商品外观/品牌标识的身份漂移，降低素材返工率

  - 主体驱动生成类应用技术选型时，优先测试持久身份范式，而非仅依赖输入上下文注入或LoRA微调，平衡身份保真度与生成效率

  - 搭建业务侧生成内容评估体系时，可复用论文的压力测试设计（小主体、迭代编辑、多主体组合等场景），更全面度量生成质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**
当前生成式图像模型生成/编辑特定主体时，易随姿态、场景、迭代操作出现身份漂移，不同身份表示范式的效果缺乏系统横向测评。
**方法关键点**
横向对比三类主流身份表示方案：输入上下文注入、主体专属LoRA微调、可跨生成/编辑任务复用的持久身份层，覆盖主体生成、编辑、修复、多主体组合四大场景，设计逐层加压的身份保留测试任务。
**关键结果**
1. 图像质量、指令遵循能力强不代表身份保真度高，迭代编辑、小主体尺寸、图像严重退化、多主体组合场景下身份退化更显著
2. 持久身份层可全场景大幅降低身份退化幅度，跨不同基础模型应用时身份保留效果稳定提升，同时指令遵循度、感知图像质量无明显下降
