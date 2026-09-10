---
title: Learning 3D Editing without Paired Supervision via Generative Prior Distillation
title_zh: 基于生成先验蒸馏的无配对监督3D编辑学习方法
authors:
- Hao Wen
- Weibin Yun
- Hongxing Fan
- Haotian Lu
- Rui Chen
- Zehuan Huang
- Lu Sheng
affiliations:
- Beihang University, China
- Central University of Finance and Economics, China
- VAST, China
- Beijing Key Laboratory of Intelligent Creative Content Generation and Immersive
  Experience, China
arxiv_id: '2609.04942'
url: https://arxiv.org/abs/2609.04942
pdf_url: https://arxiv.org/pdf/2609.04942
published: '2026-09-03'
collected: '2026-09-10'
category: Other
direction: 3D内容生成 · 无监督先验蒸馏
tags:
- 3D Editing
- Generative Prior
- Knowledge Distillation
- Foundation Model
- Unsupervised Learning
one_liner: 无需配对3D监督数据，通过蒸馏基础模型先验实现高精度指令引导前馈3D编辑
practical_value: '- 可借鉴多模态先验蒸馏思路解决电商3D商品素材生成场景标注数据稀缺痛点，降低训练数据门槛

  - 多源互补监督信号的设计可复用在多视图商品内容生成任务，有效规避不同视角输出不一致问题

  - 3D感知分布匹配正则化方法可迁移到3D数字人、虚拟商品建模任务，约束生成结果符合真实资产分布'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
指令引导3D编辑是交互式内容生成的核心支撑能力，但当前面临高质量配对3D训练数据严重稀缺的瓶颈，现有方案要么依赖速度极慢的测试时优化，要么用复杂pipeline构造伪配对训练，易出现结构漂移、几何伪影问题。
### 方法关键点
1. 设计无配对3D监督的前馈3D编辑框架，直接从基础模型蒸馏视觉、语义、几何知识到3D编辑模型；
2. 基于可微渲染管线，用图像编辑模型的主视图2D视觉先验、多模态大模型的新视图语义先验双信号监督3D表征，兼顾指令遵循度和源身份保留；
3. 引入3D感知分布匹配正则化作为几何先验，在3D隐空间约束编辑输出落在预训练图像转3D教师模型定义的真实3D资产流形内，解决2D投影监督固有的几何崩溃、多视角不一致问题。
### 关键结果
实验表明，方法在指令保真度、跨视角一致性指标上显著优于当前SOTA基线。
