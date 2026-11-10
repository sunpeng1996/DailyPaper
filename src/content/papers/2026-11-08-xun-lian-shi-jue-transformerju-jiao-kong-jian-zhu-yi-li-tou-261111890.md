---
title: 'Training Vision Transformers to Focus: Emergence of Spatial Attention Head
  Specialization'
title_zh: 训练视觉Transformer聚焦：空间注意力头的专属分工涌现
authors:
- Yuji Nozawa
- Yu-Chieh Lin
- Youyang Ng
affiliations:
- Kioxia Corporation
arxiv_id: '2611.11890'
url: https://arxiv.org/abs/2611.11890
pdf_url: https://arxiv.org/pdf/2611.11890
published: '2026-11-08'
collected: '2026-11-10'
category: Training
direction: ViT训练 · 注意力头特化优化
tags:
- ViT
- Self-supervised Learning
- Attention Head
- Spatial Perception
- Dense Prediction
one_liner: 提出两种无标注视觉聚焦损失，引导ViT注意力头空间特化，提升密集预测性能与可解释性
practical_value: '- 多模态电商推荐的物品图片特征提取环节，可复用无标注聚焦损失优化ViT注意力，提升细粒度视觉特征区分度，减少相似商品表征模糊问题

  - 涉视觉理解的Agent（如商品导购Agent、内容审核Agent）可引入该方法优化视觉感知模块的可解释性，方便定位注意力偏差问题

  - 零样本图像分割场景（如电商商品自动抠图、类目识别）可直接复用该训练策略，无需额外标注即可提升DINO等预训练ViT的下游任务性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自监督训练的ViT（如DINO系列）缺乏训练阶段的聚焦机制，生成的感知表征常存在模糊、相似度高的问题，限制下游密集预测任务性能与模型可解释性。
### 方法关键点
设计两种无需额外标注的视觉聚焦损失，引导ViT的多头注意力与图像特定区域建立对应关系，驱动空间注意力头的专属分工涌现，让不同注意力头具备差异化的空间聚焦感知能力，全程无需标注数据即可实现。
### 关键结果
对比原生DINOv2预训练模型，该方法大幅提升注意力头的空间选择性与多样性，零样本图像分割等密集预测任务性能显著提升，同时模型可解释性得到大幅优化。
