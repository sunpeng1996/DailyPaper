---
title: 'PixRestore: Unified Image Restoration via Pixel Diffusion Transformer'
title_zh: PixRestore：基于像素扩散Transformer的统一图像修复
authors:
- Lingchen Sun
- Rongyuan Wu
- Xiangtao Kong
- Jixin Zhao
- Qiaosi Yi
- Yujing Sun
- Shuaizheng Liu
- Zhengqiang Zhang
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
- OPPO Research Institute
arxiv_id: '2608.16793'
url: https://arxiv.org/abs/2608.16793
pdf_url: https://arxiv.org/pdf/2608.16793
published: '2026-08-16'
collected: '2026-08-19'
category: Multimodal
direction: 多模态·统一图像修复
tags:
- Image Restoration
- Diffusion Transformer
- Flow Matching
- DINO
- Efficient Inference
one_liner: 提出无VAE的像素空间扩散Transformer，用50M参数量单步推理实现SOTA级统一图像修复
practical_value: '- 电商商品图劣化修复、主图美化场景可复用无VAE像素扩散架构，规避VAE丢纹理、字体重影等问题，提升修复后商品图的保真度

  - 可借鉴基于DINO特征相似度的层可靠性评估思路，用于多类型退化（模糊、压缩、低分辨率）场景下的特征融合与监督权重动态分配

  - 小参数量+单步推理的蒸馏方案可落地到端侧低延迟需求场景，比如商家端上传商品图的实时自动修复、短视频帧劣化修复'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有统一图像修复方案大多基于预训练文生图隐空间扩散模型，内置VAE会丢失修复敏感的细粒度细节，开放生成先验易引入内容不一致伪影，同时大参数量+多步推理的模式难落地低延迟业务场景。
### 方法关键点
1. 设计无VAE的像素空间Diffusion Transformer，从头训练不依赖文生图预训练，直接对分块像素做流匹配，兼顾细粒度细节保留与token序列可处理性
2. 基于LQ-HQ图像的DINO特征相似度预测层特征可靠性，可靠层特征融合为稠密条件输入，不可靠层施加更强HQ特征监督，适配不同退化类型
3. 采用基于DINO的对抗目标微调为单步生成器，大幅压缩推理耗时
### 关键结果
仅50M参数量、单步推理，在公开基准和真实测试集上的保真度、感知质量、退化鲁棒性均优于同类SOTA模型，推理效率远高于其他扩散类修复方案，更大参数量版本可进一步提升性能。
