---
title: 'VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation
  Autoencoders'
title_zh: VideoRAE：基于表征自编码器的视频基础模型生成建模适配
authors:
- Zhihao Xie
- Junfeng Wu
- Xinting Hu
- Junchao Huang
- Li Jiang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Huazhong University of Science and Technology
- Shenzhen Loop Area Institute
- University of Science and Technology of China
arxiv_id: '2607.14088'
url: https://arxiv.org/abs/2607.14088
pdf_url: https://arxiv.org/pdf/2607.14088
published: '2026-07-14'
collected: '2026-07-20'
category: Multimodal
direction: 多模态视频生成 · 表征自编码器优化
tags:
- Video Foundation Model
- Representation Autoencoder
- Latent Compression
- Video Generation
- Quantization
one_liner: 基于冻结视频基础模型多尺度特征构建表征自编码器，适配两类生成隐空间，训练收敛提速5倍
practical_value: '- 可复用「冻结大模型多尺度特征+轻量自注意力投影压缩」思路，落地到短视频推荐/广告的多模态表征压缩场景，降低大模型推理 overhead

  - 多码本量化同时适配连续/离散隐空间的设计，可迁移到生成式推荐系统，支持DiT/AR两类不同范式的物品/内容生成需求

  - 训练阶段采用大模型teacher表征对齐代替KL正则的trick，可用于小模型蒸馏任务，在加快收敛速度的同时提升语义表征保留度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统3D-VAE基于像素级重建优化，隐空间捕获的语义与时空结构能力受限；冻结视频基础模型（VFM）的强理解能力尚未被转化为适合生成的紧凑隐空间。
### 方法关键点
1. 提取冻结VFM的多尺度分层特征，通过轻量1D自注意力投影器压缩得到高压缩率隐空间
2. 采用多码本高维量化，同时支持Diffusion Transformers所需的连续隐表示、自回归模型所需的离散token
3. 训练时增加与冻结VFM teacher的局部+全局表征对齐目标，无需KL正则即可保障语义信息不丢失
### 关键结果
- UCF-101数据集上，搭配AR/DiT生成器的类生成视频gFVD分别达40/93，达到SOTA水平
- 收敛速度较同类自编码器基线快约5倍
- 2B参数量文生视频任务中替换LTX-VAE，同等设置下收敛更快、VBench表现更优
