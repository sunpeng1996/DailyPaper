---
title: Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation
title_zh: Keep-or-Drop：面向紧凑视频表征的自适应分词器
authors:
- Yeonkyeong Lee
- Hyunsung Go
- Jongmin Kim
- Sewoong Lim
- Donghoon Lee
affiliations:
- Kakao Corp., Republic of Korea
arxiv_id: '2608.24293'
url: https://arxiv.org/abs/2608.24293
pdf_url: https://arxiv.org/pdf/2608.24293
published: '2026-08-24'
collected: '2026-09-02'
category: Multimodal
direction: 多模态视频生成 · 自适应分词
tags:
- VAE
- Adaptive Tokenization
- Video Diffusion
- Latent Representation
- Compression
one_liner: 提出融合自适应token选择器的Transformer架构VAE KATok，实现SOTA压缩率下的高质量视频生成与重建
practical_value: '- 电商短视频/直播内容的压缩存储场景，可复用KATok的token重要度评估机制，在不损失画质的前提下降低存储与传输成本

  - 生成式电商短视频的扩散模型推理优化，可借鉴自适应token丢弃策略，减少推理阶段的token计算量，提升生成速度

  - 多模态召回的视频特征表征场景，可复用内容感知的token选择逻辑，过滤冗余特征，提升检索精度与召回效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有Latent Diffusion Model配套的VAE采用固定压缩比，无法适配视频时空内容复杂度差异，难以平衡压缩效率与还原质量；自适应token丢弃易破坏时空结构导致空间失配。
### 方法关键点
1. 提出Transformer-based VAE架构KATok，端到端联合训练自适应token选择器，基于每个token的内容丰富度输出keep-or-drop概率，动态丢弃无信息token，实现数据依赖的自适应压缩
2. 设计级联生成、联合生成两种位置预测策略，缓解token丢弃带来的时空结构扰动，保证空间一致性
### 关键结果
在SOTA级压缩率下实现了更优的视频重建与生成质量，量化、定性实验均证明效果来自对时空冗余的有效削减
