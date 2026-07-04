---
title: 'SwiftAudio: Data-Efficient Caption-Only Distillation for One-Step Text-to-Audio
  Diffusion-based Generation'
title_zh: SwiftAudio：仅用字幕蒸馏的高效单步文本转音频扩散生成框架
authors:
- Binh Mai
- Tran Quoc Bao Le
- Hung Dinh
- Cong Tran
arxiv_id: '2606.31259'
url: https://arxiv.org/abs/2606.31259
pdf_url: https://arxiv.org/pdf/2606.31259
published: '2026-06-30'
collected: '2026-07-04'
category: Multimodal
direction: 多模态生成 · 文本转音频单步蒸馏
tags:
- Diffusion Model
- Text-to-Audio
- Knowledge Distillation
- One-step Generation
- Temporal Regularization
one_liner: 提出无需配对文本音频数据、仅用45K字幕蒸馏的单步文本转音频扩散框架，性能达SOTA
practical_value: '- 电商商品语音介绍、直播脚本转旁白、广告语音素材生成等实时场景，可复用该无配对数据蒸馏方案，大幅降低音频标注成本

  - 时序模态单步扩散蒸馏的时序平滑正则化trick，可直接迁移至语音、短视频片段等生成场景的提速优化

  - 仅需数万文本样本的小样本蒸馏范式，可复用在垂直品类（如3C、美妆）专属语音生成的低成本落地'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
扩散类文本转音频（TTA）模型生成质量优异，但多步迭代去噪逻辑导致推理延迟高，难以落地实时场景；现有单步蒸馏提速方案均依赖配对文本-音频标注数据，数据获取成本高、小样本下效果受限。

### 方法关键点
1. 将Variational Score Distillation（VSD）适配到音频领域，仅用文本字幕即可从预训练扩散教师模型完成蒸馏，无需配对音频监督信号；
2. 引入时序平滑正则化目标，约束隐层音频表征的连贯性，避免单步生成出现时序断裂问题；
3. 训练仅需约45K文本字幕样本，数据效率极高。

### 关键结果
在AudioCaps、Clotho公开数据集上，性能达到所有严格单步TTA方法的SOTA，大幅缩小了与多步扩散系统的性能差距。
