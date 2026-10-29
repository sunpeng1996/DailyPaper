---
title: 'Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding'
title_zh: 几何学习与推理：生成能力如何提升空间理解效果
authors:
- Rui Yang
- Yanwei Li
- Sili Chen
- Jingjia Huang
- Yi Lin
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- Shanghai Jiao Tong University
- ByteDance Seed
arxiv_id: '2610.36022'
url: https://arxiv.org/abs/2610.36022
pdf_url: https://arxiv.org/pdf/2610.36022
published: '2026-10-25'
collected: '2026-10-29'
category: Reasoning
direction: 多模态推理 · 几何理解
tags:
- Multimodal Reasoning
- Geometric Understanding
- Visual Generation
- Reinforcement Learning
- Benchmark
one_liner: 提出整合生成与空间理解的GeoUG模型，自适应推理降本同时在多几何基准上取得高精度
practical_value: '- 电商3D商品展示、AR试穿类多模态应用可复用多尺度深度Codec设计，基于预训练视觉自编码器生成度量级深度信息，提升3D空间感知精度

  - 多模态Agent执行复杂空间推理任务时，可借鉴自适应交错推理逻辑：先输出草稿答案，再通过RL判断是否生成额外几何证据修正，平衡精度与计算成本

  - 构建多模态能力测评基准时，可参考3DCueBench设计思路，可控调整任务难度同时平衡多维度输入信号，保障测评结果公平性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像/视频生成器已具备空间一致内容生成能力，但如何将该能力迁移到空间理解任务的研究不足，同时缺乏可控几何难度的测评基准，也没有兼顾推理精度与生成成本的优化方案。
### 方法关键点
1. 提出统一几何理解生成模型GeoUG，整合深度、多视图生成与空间理解能力，设计多尺度深度Codec基于预训练视觉自编码器实现度量深度生成，通过联合训练提升空间理解效果
2. 构建3DCueBench基准，可控调整几何难度的同时平衡2D输入信号，可公平评估模型几何推理能力
3. 提出自适应交错推理机制，先输出答案草稿，通过RL训练决策模块判断是否需要生成几何证据修正结果，平衡精度收益与生成开销
### 关键结果
在CV-Bench-3D、3DCueBench、DA-2K上分别取得97.9%、90.8%、94.2%的循环精度，生成调用次数远低于全量生成方案
