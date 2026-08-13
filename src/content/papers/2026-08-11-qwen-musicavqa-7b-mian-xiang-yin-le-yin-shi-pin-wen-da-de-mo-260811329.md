---
title: 'Qwen-MusicAVQA-7B: A Multimodal Model for Music Audio-Visual QA'
title_zh: Qwen-MusicAVQA-7B：面向音乐音视频问答的多模态模型
authors:
- Maryam Dehdashti
affiliations:
- Inference Matter Labs
arxiv_id: '2608.11329'
url: https://arxiv.org/abs/2608.11329
pdf_url: https://arxiv.org/pdf/2608.11329
published: '2026-08-11'
collected: '2026-08-13'
category: Multimodal
direction: 多模态大模型 · 音视频问答轻量适配
tags:
- Multimodal-LLM
- AVQA
- Frozen-Encoder
- Lightweight-Adaptation
- Qwen-Series
- Whisper
one_liner: 基于冻结Whisper与Qwen2-VL的轻量适配，实现低成本SOTA音乐音视频问答
practical_value: '- 做短视频/直播内容理解、音乐类商品推荐场景的多模态建模时，可采用「冻结主干编码器+轻量线性投影」的适配方案，大幅降低训练算力成本，无需全量微调大模型

  - 音频特征建模优先保留细粒度时序信息，固定token预算下，步长池化的序列特征效果远优于全局池化特征，可直接复用在直播/音乐相关推荐的内容特征提取环节

  - 多模态特征融合可直接复用LLM原生自注意力层，无需额外开发任务专属融合网络，减少架构复杂度与上线成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态大模型扩展音频能力通常需要全量训练/适配全域模态系统，算力成本高，针对音乐场景的音视频问答缺乏轻量高效的落地方案。

### 方法关键点
1. 架构采用冻结Whisper编码器分别处理音乐音频与语音问题，通过独立可学习线性投影接入冻结的Qwen2-VL-7B-Instruct，复用LLM原生自注意力完成多模态融合，无任务专属融合网络
2. 训练全程主干编码器全冻结，仅优化线性投影层

### 关键结果
- MUSIC-AVQA测试集准确率达96.0%±3.9%，比同参数级微调后的Qwen2.5-Omni-7B高15pct
- 固定32token预算下，步长池化Whisper特征比全局池化PANNs特征准确率高26pct
- 全流程仅需单A100 80GB训练5小时，改写后长尾测试集准确率仍达95.6%
