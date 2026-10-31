---
title: Discovering Interpretable Acoustic Features in Autoregressive Voice-Cloning
  TTS Models
title_zh: 自回归语音克隆TTS模型的可解释声学特征挖掘
authors:
- Anuj Diwan
- David Harwath
- Eunsol Choi
affiliations:
- University of Texas at Austin
- New York University
arxiv_id: '2610.40505'
url: https://arxiv.org/abs/2610.40505
pdf_url: https://arxiv.org/pdf/2610.40505
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: TTS可解释性 · 声学特征挖掘
tags:
- TTS
- Interpretability
- SAE
- PCA
- Acoustic Feature
one_liner: 提出自回归语音克隆TTS特征级可解释性框架，对比多方法适用场景并挖掘684个未预设有效特征
practical_value: '- 做LLM/多模态模型特征可解释性时，可复用SAE+PCA对比的实验框架，明确场景选型：SAE适合稀疏概念探测与新特征发现，PCA适合稠密场景的探测与steering

  - Agent语音交互/电商语音广告场景下，可复用本文的声学特征探测方法，快速定位TTS模型中控制音色、语调、口音的特征维度，实现定制化语音生成

  - 特征有效性验证可参考「强探测效果不代表强steering效果」的结论，必须同时做离线探测和在线生成控制实验避免选型偏差'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
零样本语音克隆TTS可解释性缺失，无法明确模型编码的声学属性与生成控制逻辑，缺少统一的特征级分析框架支撑特征优化与可控生成。
### 方法关键点
针对自回归语音克隆TTS搭建特征可解释性分析框架，对SAE、PCA、随机方向三类特征，通过稀疏探测、生成时steering、自动可解释性三类方法做全维度评估；以Qwen3-TTS为核心测试对象，扩展验证5个不同架构TTS模型的结论泛化性。
### 关键结果
1. 模型明确编码pitch、能量、噪声、口音等概念，但仅部分概念支持稀疏预测与steering，探测效果与steering效果无正相关；
2. 自动可解释性方法在Qwen3-TTS中挖掘到684个经验证的SAE特征，覆盖预设标签外的说话人聚类、说话风格、录音条件等维度
