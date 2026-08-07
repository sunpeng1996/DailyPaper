---
title: 'KVAE: Family of Tokenizers for Multimodal Generative Models'
title_zh: KVAE：面向多模态生成模型的Tokenizer家族
authors:
- Andrey Shutkin
- Denis Parkhomenko
- Ivan Kirillov
- Kirill Chernyshev
- Kirill Malakhov
- Ilia Vasiliev
- Ilia Trushkin
- Valeriya Kobenko
- David Chikovani
- Alexander Ivanov
affiliations:
- Kandinsky Lab
arxiv_id: '2608.05798'
url: https://arxiv.org/abs/2608.05798
pdf_url: https://arxiv.org/pdf/2608.05798
published: '2026-08-05'
collected: '2026-08-07'
category: Multimodal
direction: 多模态生成 · 音视频图像Tokenizer
tags:
- Tokenizer
- Multimodal
- Latent Diffusion
- VAE
- Content Generation
one_liner: 开源覆盖音视频、图像的KVAE系列Tokenizer，效果优于主流开源方案
practical_value: '- 电商多模态内容生成（商品图/种草短视频/语音解说）可直接复用开源KVAE Tokenizer，平衡压缩效率与生成质量

  - 多模态生成链路优化可参考KVAE的设计思路，针对文本条件生成场景定制Tokenizer，提升跨模态对齐效果

  - 自研Tokenizer可复用其公开的训练流程、模型选型方法与消融结论，大幅降低研发试错成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Latent Diffusion建模的训练速度、生成样本质量高度依赖Tokenizer性能，现有主流开源Tokenizer在多模态覆盖、压缩比与重建质量平衡、文本条件生成适配性上仍有不足，且公开的训练落地细节少。

### 方法关键点
推出全系列面向文本条件生成优化的KVAE Tokenizer：
1. KVAE-Audio：48kHz全频连续音频Tokenizer，输出64通道50Hz latent
2. KVAE-3D：两个因果视频Tokenizer，支持4x16x16、4x8x8压缩比
3. KVAE-2D：图像Tokenizer，8倍压缩比输出32通道特征

### 关键结果
重建指标（PSNR、LPIPS、PESQ等）、生成客观指标（Frechet Distance、CLIP/CLAP score）及主观侧评均匹配或超越Wan-2.2、HunyuanVideo-1.5、FLUX.2、StableAudio等前沿开源Tokenizer，训练代码完全开源。
