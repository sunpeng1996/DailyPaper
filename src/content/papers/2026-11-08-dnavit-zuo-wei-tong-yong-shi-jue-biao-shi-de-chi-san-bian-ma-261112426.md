---
title: 'dNaViT: Discrete Codes are General-Purpose Visual Representations'
title_zh: dNaViT：作为通用视觉表示的离散编码方案
authors:
- Xiaotong Li
- Zhengrong Yue
- Xu Huang
- Jialv Zou
- Minhao Jing
- Wenhao Yan
- Haodong Li
- Hai Huang
- Bo Zhao
- Yan Feng
affiliations:
- Meituan LongCat Team
arxiv_id: '2611.12426'
url: https://arxiv.org/abs/2611.12426
pdf_url: https://arxiv.org/pdf/2611.12426
published: '2026-11-08'
collected: '2026-11-11'
category: Multimodal
direction: 多模态 · 离散视觉Tokenizer设计
tags:
- dNaViT
- Discrete Tokenizer
- Vision Transformer
- Multimodal Encoding
- Product Quantization
one_liner: 提出离散原生分辨率视觉Transformer dNaViT，实现统一多模态框架下的高质量视觉表征与编解码
practical_value: '- 电商多模态检索/生成场景可复用dNaViT的离散视觉token化方案，对齐文本token范式，统一多模态召回、排序的特征空间

  - 商品图理解/生成任务可借鉴分组乘积量化技巧，在不增加序列长度的前提下提升离散表征容量，降低多模态大模型推理成本

  - 冻结预训练编码器+轻量残差调制的训练范式可直接复用，低成本适配业务场景的商品图专属tokenizer训练'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态框架图文表征范式不统一，无法复用LLM成熟的next-token预测训练与推理基建，需探索可对齐语言token的通用离散视觉表征方案。
### 方法关键点
基于冻结预训练编码器搭建dNaViT离散原生分辨率视觉Transformer；采用双分支目标的轻量残差调制，向语义特征注入重建感知信号；引入分组乘积量化，在不提升空间序列长度的前提下扩容离散表征能力，搭配平衡训练策略同时保留语义与像素级信息。
### 关键结果数字
在12个视觉理解基准、4个生成基准、1个图像编辑基准上性能持平或超过任务专属基线；图像重建指标PSNR达49.5，优于O-MAGVIT2、LlamaGen等同类方案。
