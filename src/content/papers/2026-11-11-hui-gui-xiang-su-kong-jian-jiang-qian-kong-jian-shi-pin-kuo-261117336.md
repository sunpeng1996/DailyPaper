---
title: 'Back to Pixels: Lifting Latent Video Diffusion into Pixel Space'
title_zh: 回归像素空间：将潜空间视频扩散模型迁移至像素域生成
authors:
- Yanke Song
- Shuo Chen
- Chris Rockwell
- Guande He
- Nan Liu
- Desai Xie
- Tianpei Gu
- Yong-Hyun Park
- Aryan V S
- Dennis Yuren Menn
affiliations:
- Roblox
- University of California, Merced
- University of Pennsylvania
- University of Texas at Austin
arxiv_id: '2611.17336'
url: https://arxiv.org/abs/2611.17336
pdf_url: https://arxiv.org/pdf/2611.17336
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 多模态视频生成 · 扩散模型优化
tags:
- Video Diffusion
- Latent Diffusion
- Pixel Generation
- Fine-tuning
- Multimodal Generation
one_liner: 提出PixVid方法，将预训练潜空间视频扩散模型迁移到像素空间，实现更高清低延迟可控视频生成
practical_value: '- 可复用「保留预训练大模型主体、仅替换输出头做领域适配」的思路，大幅降低电商商品短视频、广告素材等生成式内容的训练成本

  - 预测干净信号而非残差+更大噪声偏移的微调trick，可迁移到生成式推荐的扩散类模型调优中，提升生成内容质量

  - 逐帧生成的低延迟架构，可适配实时互动Agent的动态内容生成场景，有效降低用户交互响应延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前前沿视频生成模型依赖VAE潜空间压缩降低训练成本，但压缩导致高分辨率生成成本陡增、可控性差、交互延迟高，无法逐帧响应输入。
### 方法关键点
1. 架构复用预训练潜空间扩散Transformer主体，仅替换VAE解码器为卷积头，直接输出像素域帧；
2. 微调时优化预测目标为干净视频而非运动速度，搭配更大噪声偏移保障生成质量；
3. 基于Wan2.1-14B预训练模型微调，仅需~1.3M训练 clips 即可收敛。
### 关键结果
相同每帧token数下分辨率提升2倍；快速运动场景下深度条件视频编辑对齐效果更优；交互响应延迟降低到单帧级别，无需等待多帧块处理。
