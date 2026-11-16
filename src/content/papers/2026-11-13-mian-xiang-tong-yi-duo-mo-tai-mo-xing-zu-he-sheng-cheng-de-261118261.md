---
title: Structural Self-Teaching for Compositional Generation in Unified Multimodal
  Models
title_zh: 面向统一多模态模型组合生成的结构自训练方法
authors:
- Jaeyoo Park
- Bohyung Han
affiliations:
- Seoul National University
- Samsung Electronics
arxiv_id: '2611.18261'
url: https://arxiv.org/abs/2611.18261
pdf_url: https://arxiv.org/pdf/2611.18261
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态生成 · 结构自训练
tags:
- Multimodal
- Diffusion Model
- Compositional Generation
- Self-Training
- Attention Mechanism
one_liner: 提出无标注结构自训练框架SST，提升扩散型统一多模态模型的组合图像生成保真度
practical_value: '- 电商商品海报/主图生成场景可复用SST思路，利用多模态模型自身理解路径的注意力图做训练监督，无需额外标注即可解决多商品组合场景下的属性绑定错误、物体遗漏问题

  - 训练阶段引入的结构脚手架可在推理时完全移除，无额外推理开销，适合高并发的生成式推荐、商品素材生成业务落地

  - 短语级局部对比对齐的trick可迁移到多模态召回场景，提升细粒度语义匹配准确率，适配图文检索、多模态Query理解需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散架构的统一多模态模型（UMMs）处理密集组合prompt时生成效果差，常出现物体遗漏、属性绑定错误、空间位置偏差问题，现有优化方案依赖外部结构标注成本高。
### 方法关键点
1. 提出SST框架，复用UMMs自身理解路径的内部注意力图，提取短语条件支撑掩码作为训练监督信号，无需外部标注；
2. 设计两种训练机制：短语局部对比对齐用掩码做池化区域，对齐生成区域与目标图对应区域；结构脚手架基于掩码生成短语级布局，训练时调制生成路径的中间空间状态，训练结束后完全移除，推理无额外输入。
### 关键结果
在多个UMMs上验证，相同训练数据下，组合生成保真度优于LoRA微调，且无推理耗时增加。
