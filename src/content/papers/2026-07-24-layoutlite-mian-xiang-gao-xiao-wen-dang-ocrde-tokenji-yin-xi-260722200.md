---
title: 'LayoutLite: Token-Level Implicit Layout Analysis for Efficient Document OCR'
title_zh: LayoutLite：面向高效文档OCR的Token级隐式版面分析
authors:
- Xudong Liu
- Bicheng Wan
- Yulin Jin
affiliations:
- Yuanli Technology (Beijing) Co., Ltd.
- Beijing Normal University
arxiv_id: '2607.22200'
url: https://arxiv.org/abs/2607.22200
pdf_url: https://arxiv.org/pdf/2607.22200
published: '2026-07-24'
collected: '2026-07-27'
category: Multimodal
direction: 多模态VLM优化 · 视觉token剪枝
tags:
- VLM
- OCR
- Token Pruning
- KV Cache
- Reinforcement Learning
one_liner: 提出轻量即插即用的token级隐式版面分析模块，大幅降低VLM-OCR推理成本且精度损失可忽略
practical_value: '- 电商多模态内容理解场景可复用token重要性打分+低信息token剪枝思路，降低VLM推理时的KV cache占用与prefill延迟，适配高并发的商品素材/用户上传凭证OCR需求

  - 无标注训练策略可迁移：用下游任务输出一致性作为RL优化目标+弱辅助信号稳定训练，大幅降低标注成本

  - 即插即用模块设计无需改动原有VLM的视觉编码器、语言解码器架构，可快速集成到现有多模态OCR管线中'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于VLM的端到端OCR在复杂文档场景性能优异，但高分辨率图像生成的大量视觉token包含大量空白/冗余区域，通用视觉token压缩方法易丢失OCR所需的细粒度关键信息，推理效率瓶颈突出。
### 方法关键点
1. 轻量即插即用模块，在视觉编码器与语言解码器之间做token级隐式版面分析，无需显式版面检测
2. 聚合视觉编码器多层表征，用轻量打分网络预测每个视觉token的重要性，移除低信息token同时保留留存token的原始空间位置信息
3. 无标注训练：将token选择建模为RL问题，基于OCR输出一致性驱动的组相对策略优化目标训练，辅以版面辅助监督信号稳定训练
### 关键结果
OmniDocBench测试中，50% token压缩率下，两个OCR专用VLM精度几乎无损失，prefill延迟、FLOPs、KV cache显存占用均降低40%以上，额外推理开销极小
