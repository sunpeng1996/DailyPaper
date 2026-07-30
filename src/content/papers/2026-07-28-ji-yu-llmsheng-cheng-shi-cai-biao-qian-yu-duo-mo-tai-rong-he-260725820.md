---
title: Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion
title_zh: 基于LLM生成食材标签与多模态融合的食物图像分割方法
authors:
- Jui-Feng Chi
- Wei-Ta Chu
- Sheng-Long Lin
affiliations:
- National Cheng Kung University
arxiv_id: '2607.25820'
url: https://arxiv.org/abs/2607.25820
pdf_url: https://arxiv.org/pdf/2607.25820
published: '2026-07-28'
collected: '2026-07-30'
category: Multimodal
direction: 多模态理解 · 图像语义分割优化
tags:
- Multimodal Segmentation
- LLM
- Semantic Injection
- Plug-and-Play Module
- Computer Vision
one_liner: 提出两个即插即用多模态模块，利用LLM生成的食材标签提升食物图像分割效果
practical_value: '- 电商食品/生鲜类SKU细粒度识别场景可复用两个即插即用语义注入模块，无需重训大模型即可提升相似品类区分度，降低迭代成本

  - 多模态任务中若视觉特征区分度不足，可引入LLM生成的细粒度语义标签直接注入视觉pipeline，无需提前做图文预对齐，减少标注开销

  - 健康饮食推荐、膳食管理类App的食物图像理解模块可直接复用该架构，仅需付出可控显存开销即可大幅提升细粒度分割精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有食物图像分割模型对视觉相似食材、稀有品类识别效果差，难以支撑营养跟踪、个性化健康监测等下游应用。
### 方法关键点
1. 先通过LLM从食物图像推理得到细粒度食材语义标签；
2. 提出两个即插即用的语言注入模块：LIM-F适配输出多层特征的任意图像编码器（如Swin Transformer），LIM-Q适配Mask2Former类Transformer解码器；
3. 两个模块无需提前做图文预对齐，直接将语义信息注入视觉分析pipeline。
### 关键结果数字
在FoodSeg103基准上达到SOTA：Swin-L+Mask2Former集成LIM-Q得mIoU 55.0，集成LIM-F得mIoU 54.4；LIM-F适配CNN架构时将mIoU从47.7提升至49.8，训练阶段显存最多仅增加3.8GB，开销可控。
