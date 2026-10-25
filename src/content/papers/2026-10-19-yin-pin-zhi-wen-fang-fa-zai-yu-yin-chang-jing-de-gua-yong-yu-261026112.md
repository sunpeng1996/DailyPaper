---
title: Applicability and Generalization of Audio Fingerprinting Methods to Speech
title_zh: 音频指纹方法在语音场景的适用性与泛化能力研究
authors:
- Kemal Altwlkany
- Elmedin Selmanovic
- Sead Delalić
- Emanuel Lacic
affiliations:
- Infobip
- Faculty of Science, University of Sarajevo
arxiv_id: '2610.26112'
url: https://arxiv.org/abs/2610.26112
pdf_url: https://arxiv.org/pdf/2610.26112
published: '2026-10-19'
collected: '2026-10-25'
category: Other
direction: 音频指纹 · 语音场景性能基准测试
tags:
- AudioFingerprinting
- SelfSupervisedLearning
- SpeechProcessing
- Benchmark
- NoiseRobustness
one_liner: 对主流音频指纹模型做语音场景基准测试，揭示自监督方案优势及误匹配规律
practical_value: '- 仅适用于有语音相关业务的场景（如直播音频查重、语音客服质检、语音交互Agent），无相关业务的团队可直接忽略

  - 语音场景下做音频指纹匹配优先选用自监督训练的方案，抗噪声、混响、压缩畸变的表现显著优于传统方法

  - 语音指纹误匹配更易命中同说话人而非同文本，做语音内容合规校验、话术匹配时需叠加ASR文本校验降低误判'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
传统音频指纹技术的研发与评估长期聚焦音乐场景，但其在语音交互、内容质检、语音查重等语音场景的落地缺乏系统性验证，不同方案的抗畸变能力、泛化表现无公开基准参考。

### 方法关键点
选取当前性能最优的多款音频指纹模型，在语音数据集上开展全场景基准测试，覆盖业务中常见的噪声、混响、时序拉伸/压缩、音调修改、有损压缩五类畸变场景，同时统计分析误匹配样本的分布规律。

### 关键结果
1. 自监督学习训练的音频指纹方案在语音场景的表现显著优于传统特征工程类方法
2. 所有测试方案在语音场景的识别精度均低于其在音乐场景的基准精度
3. 误匹配样本中，模型更倾向将同说话人不同内容的语音判定为匹配，而非同内容不同说话人的样本
