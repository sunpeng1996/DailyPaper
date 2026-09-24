---
title: 'MicroQonv: Reshaping Convolution Tensors for Efficient Microscaling in Training
  and Inference'
title_zh: MicroQonv：重塑卷积张量实现训练推理的高效微缩放量化
authors:
- Romain Facq
- Sami Ben Ali
- Olivier Sentieys
affiliations:
- Univ Rennes
- Inria
- CNRS
- IRISA
arxiv_id: '2609.28358'
url: https://arxiv.org/abs/2609.28358
pdf_url: https://arxiv.org/pdf/2609.28358
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 卷积网络微缩放量化效率优化
tags:
- Quantization
- CNN
- Microscaling
- Hardware Acceleration
- Model Efficiency
one_liner: 提出单次量化+通道批次优先im2col的MicroQonv，大幅降低卷积层微缩放量化开销
practical_value: '- 电商/广告场景的CNN类召回、排序、多模态特征提取模型部署时，可复用MicroQonv的单次量化+修改版im2col逻辑，降低显存占用与推理延迟，提升部署密度

  - 端侧Agent的视觉感知模块本地微调时，可采用MicroQonv+4bit微缩放量化方案，在几乎无损精度下降低内存开销，落地边缘轻量训练能力

  - 大模型中的卷积算子（如ViT的patch embedding、多模态模型的视觉卷积层）量化优化可参考该思路，减少量化带来的额外内存搬运开销'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
微缩放量化可将神经网络参数量化到8bit及以下且精度损失极小，但直接应用于卷积层时存在两大痛点：张量重复量化带来额外内存搬运，im2col变换在量化前执行导致激活张量尺寸暴涨，整体量化开销远超预期。
### 方法关键点
1. 每个张量仅执行1次量化，取消重复量化步骤，直接降低量化计算与内存搬运成本
2. 调整im2col执行顺序：先对激活张量完成量化，再执行自研的通道批次优先版im2col变换，适配卷积层前向/反向传播全流程
### 关键结果
权重、梯度的量化开销降低2倍，激活量化开销最高降低9倍，精度损失可忽略；相比全精度方案，内存搬运与存储开销最高降低7.53倍；YOLOV8nano的微缩放量化激活内存搬运降低3.5倍，YOLOV26nano降低2.2倍；边缘持续学习场景下，支持4位微缩放量化，精度提升5.7%~11%
