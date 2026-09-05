---
title: Decoupled Latent Flow Matching for Few-Step Joint Vocal-Accompaniment Separation
title_zh: 解耦隐空间流匹配实现少步数人声-伴奏联合分离
authors:
- Lishi Zuo
- Youzhi Tu
- Lu Yi
- Zezhong Jin
- Chongxin Gan
- Man-Wai Mak
- KongAik Lee
affiliations:
- Dept. of Electrical and Electronic Engineering, Hong Kong Polytechnic University
arxiv_id: '2608.30913'
url: https://arxiv.org/abs/2608.30913
pdf_url: https://arxiv.org/pdf/2608.30913
published: '2026-08-31'
collected: '2026-09-05'
category: Other
direction: 音频生成 · 流匹配少步推理优化
tags:
- Flow Matching
- VAE
- Generative Audio
- Adversarial Training
- Latent Space
one_liner: 提出解耦隐空间流匹配框架结合对抗后训练，实现低采样成本的人声伴奏联合分离
practical_value: '- 流匹配+隐空间压缩+对抗后训练的少步加速范式，可迁移到GenRec、多模态广告素材生成的推理优化，大幅降低线上延迟

  - 语义层与信号/数值预测层解耦的架构设计，可复用在多目标推荐、多模态生成式推荐的特征解耦场景，降低不同目标冲突

  - 预训练降维模型先压缩高维输入再做生成任务的思路，可降低长序列用户行为建模、大候选集生成推荐的计算开销'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于扩散、流匹配的生成式音频分离方案迭代步数多，长音乐信号推理成本高，单独建模人声和伴奏易忽略跨源依赖，导致输出质量下降。

### 方法关键点
1. 用预训练VAE将混合音频和源信号映射到紧致隐空间，流匹配模型联合生成人声、伴奏隐向量，保留跨源依赖关系
2. 架构解耦为Separation Encoder负责语义分离、Velocity Decoder负责声学速度预测，降低建模难度
3. 借鉴Flow2GAN思路增加隐空间对抗后训练，减少生成所需的采样步数

### 关键结果
低采样步数下，隐空间对抗优化可同时提升感知类指标和分离效果类指标，在推理效率和效果间取得更优平衡
