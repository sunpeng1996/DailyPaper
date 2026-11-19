---
title: 'Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers'
title_zh: 无解码器解码：基于扩散Transformer的直接像素预测
authors:
- Hansheng Chen
- Shengqu Cai
- Jan Ackermann
- Rayhan Zirvi
- Gordon Wetzstein
- Xinchen Yan
- Leonidas Guibas
affiliations:
- Stanford University
- Luma AI
- California Institute of Technology
arxiv_id: '2611.22287'
url: https://arxiv.org/abs/2611.22287
pdf_url: https://arxiv.org/pdf/2611.22287
published: '2026-11-16'
collected: '2026-11-19'
category: Multimodal
direction: 多模态生成 · 扩散模型推理优化
tags:
- Diffusion Transformer
- Latent Diffusion
- Inference Optimization
- Image Generation
- Video Generation
one_liner: 提出拆分去噪与像素预测的DWD方法，省去扩散模型解码器，降推理成本同时提升生成质量
practical_value: '- 现有已训练的电商商品图/营销短视频扩散模型，可仅微调最后几层Transformer块加DWD头省去VAE解码步骤，降低推理时延，压缩部署成本

  - 像素级高清商品图生成场景可复用DWD任务拆分思路，保留原有去噪采样轨迹的同时新增最终步像素预测头，提升纹理、材质细节表现

  - 电商商品短视频生成场景可直接复用DWD优化方案，降低画面闪烁和形变误差，提升用户观感，减少内容审核返工成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有潜空间扩散模型依赖VAE解码器将去噪后潜变量映射到像素，额外增加推理开销与架构复杂度，同时解码器易引入细节失真、视频闪烁等问题，像素级扩散模型也存在纹理过平滑的缺陷。

### 方法关键点
1. 拆分去噪采样与像素输出两个任务，原有去噪头保留预训练参数驱动采样流程，仅新增DWD线性头在采样最终步直接输出像素；
2. 适配预训练潜空间模型时仅微调最后数层Transformer块，固定原有去噪头参数锚定采样轨迹，用像素质量损失训练DWD头；
3. 方案同时兼容无解码器的像素级扩散模型。

### 关键结果
Wan视频生成场景形变误差降低23%，明显减少细节失真与画面闪烁；ImageNet文本生成图像任务FID从1.55降至1.43，达到像素流模型当前SOTA，同时省去解码器降低整体推理成本。
