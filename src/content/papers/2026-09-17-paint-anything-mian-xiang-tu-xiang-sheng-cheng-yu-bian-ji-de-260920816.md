---
title: 'Paint-Anything: Unified Any-Color Control for Image Generation and Editing'
title_zh: Paint-Anything：面向图像生成与编辑的统一任意颜色控制框架
authors:
- Ji Xie
- Dewei Zhou
- Xinyu Huang
- Zhennan Chen
- Xun Wang
affiliations:
- ByteDance Seed
- Zhejiang University
- Nanjing University
arxiv_id: '2609.20816'
url: https://arxiv.org/abs/2609.20816
pdf_url: https://arxiv.org/pdf/2609.20816
published: '2026-09-17'
collected: '2026-09-18'
category: Multimodal
direction: 多模态图像生成 · 精确色值控制
tags:
- Image Generation
- Image Editing
- Color Control
- Hex Prompt
- Dataset
- Evaluation Benchmark
one_liner: 提出支持任意24位hex色值控制的图像生成编辑框架，配套训练数据集与色值精度评估基准
practical_value: '- 电商商品图生成/修图场景可直接复用hex色值控制逻辑，无需自定义颜色表征，直接对接品牌标准色库实现批量商品图统一调色生成

  - 训练数据构建可参考「真实标注+纯色锚点分噪声阶段训练」方案，解决真实场景标签受光影干扰的问题，降低标注成本同时提升控制精度

  - 可直接复用ACBench评估逻辑，量化评估电商商品图生成的色值准确率，替代人工抽检'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有图像生成编辑的颜色控制依赖专用表征或特殊推理流程，无法支持专业设计、电商场景要求的24位hex精确色值控制，无法满足品牌标准色、商品系列色的精准生成需求。

### 方法关键点
1. 构建Paint-500K数据集，通过目标grounding、感知颜色标注、编辑对合成流程从真实图像生成训练数据；
2. 引入纯色锚点辅助训练，仅在高噪声步使用精确色值锚点监督，低噪声步用真实图训练，解决真实图标注受光影干扰的问题；
3. 提出统一hex-prompt接口，同时支持文生图和图像编辑两种任务的色值控制；
4. 构建ACBench基准，包含T2I和编辑两个子任务，量化评估目标级hex色值保真度。

### 关键结果
基于FLUX.2-4B底座，ACBench-T2I得分较基线提升85.3%，ACBench-Edit得分提升28.3%，CompColor平均得分在所有对比方法中排名第一。
