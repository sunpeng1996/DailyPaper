---
title: 'PixSDS: Why Latent SDS Makes Noisy Pixels'
title_zh: PixSDS：解析隐空间SDS像素噪点成因及优化方案
authors:
- Vsevolod Skorokhodov
affiliations:
- EPFL, Lausanne, Switzerland
arxiv_id: '2608.12997'
url: https://arxiv.org/abs/2608.12997
pdf_url: https://arxiv.org/pdf/2608.12997
published: '2026-08-12'
collected: '2026-08-14'
category: Other
direction: 扩散模型优化 · Score Distillation Sampling
tags:
- Diffusion Model
- Score Distillation Sampling
- VAE
- Text-to-3D
- Artifact Reduction
one_liner: 定位隐空间SDS噪点源于VAE像素漂移，提出轻量梯度修复方法PixSDS有效降低生成伪影
practical_value: '- 电商3D商品生成业务可直接复用PixSDS轻量梯度修复逻辑，无需重训扩散模型即可降低生成伪影，提升3D商品展示效果

  - 基于VAE+隐空间扩散的多模态生成场景（如商品图、营销海报生成）可借鉴噪点成因分析，补充VAE一致性约束减少生成瑕疵

  - 生成式内容生产管线可参考「隐空间预优化+解码回像素空间校准」思路，以极低算力开销提升生成内容画质'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
隐空间SDS是文本生成3D的核心技术，无需训练专属3D生成模型即可基于文本prompt优化3D表征，但生成结果常出现结构化色彩伪影、高频纹理噪点，现有优化方案需重训模型或修改渲染器，落地成本高。
### 方法关键点
1. 定位噪点根源为VAE诱导的像素漂移：优化过程中图像会沿VAE编码器弱约束的像素空间方向移动，隐空间表征仍保持语义正常，但像素层持续积累可见伪影
2. 提出轻量VAE一致梯度修复方案PixSDS：先执行隐空间SDS前向步，将得到的隐向量解码为图像作为像素空间优化的干净方向，抑制VAE不一致方向的偏移，无需重训扩散模型、更换渲染器或修改SDS目标
### 关键结果
2D优化、文本转3D实验中，PixSDS在完整保留语义内容的前提下，大幅降低结构化伪影，代码已开源
