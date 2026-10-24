---
title: 'GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression
  and Super-Resolution'
title_zh: GigaBench：十亿像素图像压缩与超分的可学习表示基准
authors:
- Matteo Fusconi
- Alex Costanzino
- Pierluigi Zama Ramirez
- Luigi Di Stefano
affiliations:
- CVLab, University of Bologna
- Ca’ Foscari University of Venice
arxiv_id: '2610.31644'
url: https://arxiv.org/abs/2610.31644
pdf_url: https://arxiv.org/pdf/2610.31644
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: 十亿像素图像处理 · 基准评测
tags:
- Learnable Representations
- Gigapixel Image
- Image Compression
- Super-Resolution
- Benchmark
one_liner: 首个面向十亿像素图像的可学习表示评测基准，适配消费级硬件并给出选型指导
practical_value: '- 电商高清商品图、长详情页存储可参考评测筛选的高压缩比LR方法，降低存储与CDN带宽成本

  - 移动端商品高清展示场景可借鉴LR方法适配消费级硬件的工程优化方案，实现端侧实时超分

  - 多模态推荐的图像特征存储可复用LR紧凑表示特性，减少特征库占用同时支持直接下游推理'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
可学习表示（LR）作为新型神经原生数据格式，具备高紧凑性、分辨率无关、支持直接神经处理的优势，但当前缺乏十亿像素图像场景下的适配方案与系统性评测体系，而十亿像素图像在工业、文化等领域的应用正在快速普及。
### 方法关键点
1. 构建GigaBench基准，覆盖多领域真实采集与合成的十亿像素图像，面向图像压缩、超分两类核心任务
2. 适配隐式、混合、显式三类代表性LR方法，优化后可在消费级硬件上稳定运行十亿像素级任务
3. 从重建质量、模型大小、压缩耗时、推理耗时四个维度开展全链路系统性评测
### 关键结果
明确了不同类别LR方法在各指标上的优劣势趋势，输出了十亿像素场景下LR技术选型的可落地指导。
