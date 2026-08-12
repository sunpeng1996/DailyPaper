---
title: 'Watching Synthetic Videos: Aligning Cross-modal Representations with Visual
  Synthesis for Zero-shot Video Captioning'
title_zh: 基于视觉合成对齐跨模态表征的零样本视频字幕生成方法
authors:
- Liangyu Fu
- Junbo Wang
- Yuke Li
- Ya Jing
- Xuecheng Wu
- Zhiyong Wang
arxiv_id: '2608.11013'
url: https://arxiv.org/abs/2608.11013
pdf_url: https://arxiv.org/pdf/2608.11013
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 跨模态表征对齐 · 零样本视频字幕生成
tags:
- Cross-modal Alignment
- Zero-shot Learning
- Video Captioning
- Vision-language
- Generative Model
one_liner: 通过文生视频模型生成合成隐表征对齐跨模态空间，提升零样本视频字幕生成效果
practical_value: '- 电商短视频商品文案/标签零样本生成场景，缺视频-文本对训练数据时，可复用该思路：用预训练文生视频模型生成文本对应的视频隐表征做跨模态对齐，无需标注真实视频数据

  - 合成模态隐分布与真实分布存在gap的场景，可新增轻量polisher模块做分布校正，无需重新训练大尺寸预训练生成模型，大幅降低算力成本

  - 预训练多模态编码器输出的隐表征可直接作为条件prompt输入LLM完成下游生成任务，该范式可复用在短视频内容理解、广告素材自动配文等场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
零样本视频字幕生成普遍采用纯文本训练范式，训练阶段无视频数据，导致训练（纯文本）与推理（纯视频）间存在跨模态gap，仅靠简单线性变换无法完成充分的表征空间对齐，生成字幕准确率低。

### 方法关键点
两阶段WSV框架解决该问题：第一阶段用预训练文生视频模型生成对应文本的合成视频隐表征，新增polisher模块弥合真实与合成视频的分布差，提升隐表征保真度；第二阶段设计prompter模块，将校准后的隐表征作为条件输入GPT-2训练字幕生成能力；推理时输入视频经预训练3D Causal VAE编码后直接喂入prompter引导GPT-2生成字幕。

### 关键结果
在MSVD、MSR-VTT、VATEX三个公开数据集上验证，B@4指标达52，CIDEr指标达95.7，性能优于此前纯文本训练的零样本方案。
