---
title: 'BARS: Beat-Adaptive Rap Synthesis via Flow Matching'
title_zh: 基于流匹配的节拍自适应说唱合成模型BARS
authors:
- Taemin Cho
- Hector Martel
- Enyan Koh
affiliations:
- BandLab Technologies, Singapore
arxiv_id: '2611.12061'
url: https://arxiv.org/abs/2611.12061
pdf_url: https://arxiv.org/pdf/2611.12061
published: '2026-11-09'
collected: '2026-11-15'
category: Other
direction: 多模态生成 · 说唱语音合成
tags:
- Flow Matching
- Non-autoregressive Generation
- Text-to-Speech
- RoPE
- Multimodal
one_liner: 基于流匹配的非自回归说唱生成模型，支持零样本音色控制、节拍对齐与歌词局部编辑
practical_value: '- 非标文本（俚语、缩写、数字）编码可复用ByT5+轻量Transformer adapter方案，无需依赖领域预训练编码器，适合电商场景下商品标题、用户评论等非标文本的特征提取，降本提效

  - 跨模态对齐不稳定问题可借鉴Asymmetric Scaled RoPE方案，给交叉注意力引入位置结构，可迁移到图文/音文跨模态检索、推荐的对齐模块优化，提升匹配准确率

  - span masking局部重生成思路可复用在生成式推荐的文案修改场景，无需全量重生成即可调整商品种草文案、广告文案片段，保留整体风格一致性，提升生成效率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有自回归说唱合成方案节奏严格受节拍约束，无法灵活调速，且难以适配说唱歌词中大量俚语、缩写等非标准文本，还存在歌词-音频对齐不稳定（token丢失、重复）、不支持局部编辑的缺陷。
### 方法关键点
1. 基于Flow Matching构建非自回归生成框架，输入为节拍轨道、歌词、短参考音频，支持零-shot音色控制，无需显式时长预测或音素级对齐即可独立调节说唱tempo；
2. 采用预训练ByT5编码器+轻量Transformer adapter联合训练编码歌词，无需依赖语音预训练文本编码器即可处理非标准文本；
3. 提出Asymmetric Scaled RoPE优化交叉注意力，引入位置结构缓解强节拍约束下的对齐不稳定问题；
4. 支持span masking局部重生成，可在保留周边音色风格的前提下编辑歌词片段。
### 关键结果
模型实现高歌词保真度，说唱flow自然且与节拍节奏一致性高，在各类说唱风格、速度下均具备稳定的节奏控制能力。
