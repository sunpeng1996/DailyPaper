---
title: 'GRACE: Generation-aware latent compression for efficient video generation'
title_zh: GRACE：面向高效视频生成的生成感知潜空间压缩方法
authors:
- Jiyoung Kim
- Paul Hyunbin Cho
- Jisu Nam
- Donghoon Lee
- Hyunsung Go
- Yeonkyeong Lee
- Hansaem Kim
- Seungryong Kim
affiliations:
- KAIST AI
- Kakao Corp.
arxiv_id: '2610.10524'
url: https://arxiv.org/abs/2610.10524
pdf_url: https://arxiv.org/pdf/2610.10524
published: '2026-10-06'
collected: '2026-10-08'
category: Multimodal
direction: 多模态视频生成 · 模型推理加速优化
tags:
- Latent Compression
- Diffusion Transformer
- Video Generation
- Model Acceleration
- Autoencoder
one_liner: 提出双阶段生成感知潜空间压缩框架，不损失生成质量下实现视频DiT最高15.5倍推理加速
practical_value: '- 大模型推理压缩场景可复用「保留预训练基潜变量+残差补信息」的思路，避免全量重训的高额成本

  - 预训练模型适配压缩后隐空间时，可借鉴「特征空间对齐+轻量微调+非对称去噪」方案，平衡加速比与效果损失

  - 电商商品短视频批量生成场景可直接套用该框架，大幅降低高分辨率营销短视频的生成推理成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
高压缩比视频自编码器可通过减少DiT处理token数加速视频生成，但常规压缩方案要么降低重建质量，要么改变预训练DiT适配的潜空间分布，需全量重训DiT，成本极高。
### 方法关键点
1. 双阶段压缩框架：冻结预训练编码器的基潜变量，学习残差潜变量补充强压缩丢失的信息
2. 在冻结DiT的特征空间对齐压缩前后潜变量分布，优化目标偏向生成效果而非仅重建精度
3. 采用轻量微调+非对称去噪适配DiT，基潜变量优先完成去噪
### 关键结果
对Wan2.1-I2V-14B实现8倍token数压缩：480x832x81分辨率下latency降低11.1倍，VBench生成质量与原预训练pipeline持平；736p分辨率下latency降低15.5倍，效果优于现有高压缩自编码器方案。
