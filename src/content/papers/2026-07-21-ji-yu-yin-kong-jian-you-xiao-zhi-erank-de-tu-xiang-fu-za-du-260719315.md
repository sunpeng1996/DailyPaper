---
title: ERank in Latent Space as an Image-Complexity and Richness Measure
title_zh: 基于隐空间有效秩（ERank）的图像复杂度与丰富度度量方法
authors:
- Maksim Smirnov
- Grigory Kononov
- Anastasiia Linich
- Egor Surkov
- Egor Shvetsov
arxiv_id: '2607.19315'
url: https://arxiv.org/abs/2607.19315
pdf_url: https://arxiv.org/pdf/2607.19315
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 无标注图像复杂度度量 · 数据筛选
tags:
- ERank
- Image Complexity
- Data Selection
- Unsupervised Metric
- Computer Vision
one_liner: 提出基于预训练编码器单前向传播的无标注图像视觉丰富度度量ERank，可适配CV任务做定向数据筛选
practical_value: '- 电商商品素材质量自动筛选：可通过ERank快速识别低丰富度的极简白底图、高丰富度的杂乱图，匹配不同场景素材要求，例如搜索缩略图过滤过高ERank的杂乱图提升点击转化，商详页保留高ERank的细节图提升转化

  - 多模态推荐/生成训练数据清洗：训练多模态召回、文生商品图模型时，可根据任务目标定向过滤低/高ERank样本，例如OCR类商品信息提取任务删高ERank样本，超分辨率类素材生成任务删低ERank样本，提升训练效率与效果

  - AI生成广告素材质量校验：AI生成商品广告图后，可通过ERank快速度量丰富度是否符合投放要求，避免过于单调或杂乱的低质素材上线'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像复杂度度量多依赖人工标注，计算成本高，缺乏轻量无标注的单样本度量方法支撑下游任务的定向数据筛选需求。

### 方法关键点
基于frozen预训练编码器的单次前向传播输出，计算图像特征图通道协方差的ERank，本质为统计图像激活的去相关通道数量，数值越高对应图像视觉丰富度越高，无需标注、计算成本极低。

### 关键结果数字
- 与IC9600数据集人工复杂度标注相关系数达r=0.72，同时与编码码率、清晰度、边缘密度强相关
- 作为数据筛选准则：移除低ERank样本可提升超分辨率任务效果，移除高ERank样本可提升OCR任务效果，预训练、微调阶段均生效，对分类、分割、去噪任务无增益
