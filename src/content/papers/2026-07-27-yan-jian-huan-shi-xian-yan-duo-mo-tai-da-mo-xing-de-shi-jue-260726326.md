---
title: Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language
  Models
title_zh: 眼见还是先验？多模态大模型的视觉上下文敏感度研究
authors:
- Jiaang Li
- Chengzu Li
- Zhaochong An
- Yifei Yuan
- Xi Liu
- Serge Belongie
- Vésteinn Snæbjarnarson
affiliations:
- University of Copenhagen
- University of Cambridge
- ETH Zürich
- Clemson University
arxiv_id: '2607.26326'
url: https://arxiv.org/abs/2607.26326
pdf_url: https://arxiv.org/pdf/2607.26326
published: '2026-07-27'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 视觉-知识先验权衡
tags:
- MLLM
- Visual Context
- Knowledge Prior
- Benchmark
- Controllability
one_liner: 提出WhatIfVis诊断基准，定位多模态大模型视觉任务失败根因并给出视觉-先验权衡调控方法
practical_value: '- 搭建多模态商品理解模块时，若粗粒度属性识别出错，优先优化后感知阶段的视觉信息利用逻辑，无需盲目重训视觉编码器

  - 开发多模态导购/推荐Agent时，可通过小样本SFT或注入预训练steering vector，快速调控模型优先遵循商品图视觉信息还是通用知识先验，适配不同业务场景

  - 可复用WhatIfVis的基准设计思路，构造商品属性维度的对抗测试集，评估自有MLLM在商品理解场景的鲁棒性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
MLLM在视觉中心任务中常出现视觉证据与预训练知识冲突时的回答错误，过往无法定位错误根因是来自视觉编码阶段还是后续信息利用阶段。
### 方法关键点
1. 设计两种诊断范式：通过图像重建探测视觉信息是否完整编码，构造覆盖时空/颜色/计数/大小/重量5维度的WhatIfVis基准，测量模型视觉上下文敏感度
2. 采用激活补丁定位视觉-先验权衡的对应网络层，训练steering vector实现无需指令的权衡调控
### 关键结果
- 粗粒度视觉属性可从冻结MLLM末层图像token完整重建，证明错误根因为后感知利用阶段而非视觉编码损失
- 原生MLLM即使给定显式指令也无法稳定控制视觉依赖，SFT后可控性显著提升且可跨域泛化，6款测试模型的视觉-先验权衡点均定位到特定深度网络层
- 注入学习到的steering vector无需额外指令，即可较原生模型大幅提升视觉依赖可控性
