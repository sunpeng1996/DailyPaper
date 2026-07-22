---
title: Appearance Pointers -- Multimodal Region Control of Diffusion Transformers
title_zh: Appearance Pointers：面向扩散Transformer的多模态区域控制方法
authors:
- Rahul Sajnani
- Yulia Gryaditskaya
- Radomír Měch
- Srinath Sridhar
- Matheus Gadelha
affiliations:
- Brown University
- Adobe Research
arxiv_id: '2607.19344'
url: https://arxiv.org/abs/2607.19344
pdf_url: https://arxiv.org/pdf/2607.19344
published: '2026-07-20'
collected: '2026-07-22'
category: Multimodal
direction: 多模态可控图像生成 · DiT优化
tags:
- DiT
- Diffusion Model
- Controllable Generation
- Multimodal
- Token Design
one_liner: 提出轻量外观指针token，无需重训基础DiT即可实现多模态细粒度区域可控图像生成
practical_value: '- 电商营销物料生成可复用该方案：无需重训基础DiT，即可通过掩码+文本/参考图指定局部区域的材质、风格、物体，快速产出多版本海报、商品图

  - 智能设计Agent可集成该能力：支持用户低门槛指定局部修改需求，替代现有逐区域重生成的低效方案，提升设计效率

  - 个性化种草素材生成：可针对不同用户偏好单独调整商品图的背景、配饰等局部元素，提升素材点击率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
仅靠文本prompt无法满足创意场景对生成图像的材质、物体身份、空间布局的精准区域控制需求，现有Diffusion Transformers（DiT）缺乏指定异质token影响输出的位置和方式的机制。
### 方法关键点
1. 设计外观指针（appearance pointers）轻量token，将文本/图像输入与用户指定的区域掩码对齐，引导DiT在对应空间位置生成符合要求的外观特征
2. 由区域对应网络生成外观指针，经空间聚合机制优化，多区域控制场景下不会显著增加token负载
3. 支持模态无关的控制接口，无需从头重训基础DiT模型
### 关键结果
单模型在多类控制任务的指标上达到或超过模态专属SOTA方法的性能，支持单次降噪pass完成区域可控生成
