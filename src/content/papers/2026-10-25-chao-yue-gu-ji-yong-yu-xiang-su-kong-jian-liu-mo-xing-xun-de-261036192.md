---
title: 'Beyond the Estimate: Wiener-Informed Decoding for Easier Training of Pixel-Space
  Flow Models'
title_zh: 超越估计：用于像素空间流模型训练优化的维纳感知解码
authors:
- Ziqiao Wang
- Yang You
affiliations:
- NUS HPC-AI Lab
arxiv_id: '2610.36192'
url: https://arxiv.org/abs/2610.36192
pdf_url: https://arxiv.org/pdf/2610.36192
published: '2026-10-25'
collected: '2026-10-29'
category: Multimodal
direction: 多模态生成 · 流模型训练优化
tags:
- Flow Model
- Wiener Filter
- Training Acceleration
- Pixel Generation
- Decoder Optimization
one_liner: 引入维纳统计先验设计WiD解码结构，加速像素空间流模型训练并提升生成质量
practical_value: '- 电商商品图、营销素材生成场景可直接引入WiD结构，大幅降低像素级生成模型的训练成本，缩短迭代周期

  - 可复用「统计先验初始化轻量并行预测支路+主模型残差修正」的架构思路，适配推荐场景高维稠密特征建模任务，加速模型收敛

  - 统计先验可用于组织解码器计算流、平滑梯度的思路，可迁移至各类大模型训练优化场景，不局限于生成任务'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
直接在像素空间训练流模型需处理高维噪声像素，存在优化慢、收敛难的痛点，现有方法未充分挖掘统计先验的价值。
### 方法关键点
1. 提出Wiener-informed Decoding（WiD），无需修改原生解码器结构，新增可训练维纳预测支路，通过系数接口向原生解码器注入特征并接收系数修正量，所有新增参数用数据统计量初始化后联合训练
2. 同时利用统计先验的直接预测价值与计算结构组织价值，优化梯度轨迹稳定性
### 关键结果
在ImageNet 256×256数据集上，搭载WiD的PixelDiT-XL训练500epoch即可达到FID 1.53，同等生成质量下训练轮次减少37.5%，仅引入少量参数开销，兼容不同模型规模、解码器架构及文本生成图像、类别条件生成等任务。
