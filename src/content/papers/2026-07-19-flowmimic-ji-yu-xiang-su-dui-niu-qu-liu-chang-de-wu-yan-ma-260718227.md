---
title: 'FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped
  Flow Field for Online Video Editing Data Generation and Modality Mimicry'
title_zh: FlowMimic：基于像素对扭曲流场的无掩码视觉编辑与视频数据生成方法
authors:
- Dingyun Zhang
- Lixue Gong
- Wei Liu
affiliations:
- ByteDance
arxiv_id: '2607.18227'
url: https://arxiv.org/abs/2607.18227
pdf_url: https://arxiv.org/pdf/2607.18227
published: '2026-07-19'
collected: '2026-07-22'
category: Multimodal
direction: 多模态生成 · 无掩码视频/图像编辑
tags:
- Video Editing
- Image Editing
- Training Data Generation
- Mask-free Generation
- Modality Alignment
one_liner: 提出基于像素对扭曲流场的无掩码视觉编辑框架，可从图像样本实时生成高质量视频编辑训练数据
practical_value: '- 电商商品短视频编辑场景可复用像素对扭曲流场方案，无需人工标注掩码即可从商品图批量生成同款短视频编辑训练样本，大幅降低数据采集成本

  - 内容推荐场景的短视频批量生产链路可借鉴模态模拟损失设计，对齐图片/视频的生成效果分布，保证跨模态内容风格一致性

  - 虚拟试穿、商品换款等AIGC工具开发可复用无掩码区域感知训练方案，省去推理阶段额外的掩码输入或MLLM辅助模块，简化部署流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频编辑训练数据采集依赖人工掩码标注、I2V模型合成带误差的配对样本、VLM质量过滤，成本高、任务扩展性差，视频编辑任务多样性远低于图像编辑；现有语言驱动视觉编辑依赖额外MLLM微调或推理时显式输入掩码，部署链路复杂。

### 方法关键点
1. 像素对时间扭曲流场可从已有图像编辑样本实时生成对应视频编辑训练样本，无需人工标注；
2. 模态模拟生成损失与编辑损失对齐图像、视频模态的编辑能力与输出分布，单模型同时支持两类模态的生成编辑任务；
3. 引入指代分割等感知任务，搭配编辑区域感知的隐层损失与注意力损失，让模型内生具备编辑区域定位能力，无需推理时额外辅助输入。

### 关键结果
在多层级视频编辑任务上验证，仅用该框架生成的训练数据即可让模型习得稳定的视频编辑能力，无需额外人工标注数据。
