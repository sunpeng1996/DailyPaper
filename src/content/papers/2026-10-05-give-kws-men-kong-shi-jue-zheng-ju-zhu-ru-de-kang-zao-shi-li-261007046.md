---
title: 'GIVE-KWS: Gated Injection of Visual Evidence for Noise-Robust Query-by-Example
  Keyword Spotting'
title_zh: GIVE-KWS：门控视觉证据注入的抗噪示例查询关键词识别
authors:
- Ming-Hsiang Hu
- Kuan-Tang Huang
- Hung-Shin Lee
- Berlin Chen
affiliations:
- Department of Computer Science and Information Engineering, National Taiwan Normal
  University
- Graduate Institute of AI Interdisciplinary Applied Technology, National Taiwan Normal
  University
arxiv_id: '2610.07046'
url: https://arxiv.org/abs/2610.07046
pdf_url: https://arxiv.org/pdf/2610.07046
published: '2026-10-05'
collected: '2026-10-10'
category: Multimodal
direction: 多模态音视融合 · 抗噪关键词识别
tags:
- Cross-Modal Fusion
- Keyword Spotting
- Noise Robustness
- Gated Attention
- Audio-Visual Learning
one_liner: 提出门控视觉证据注入的音视融合框架GIVE-KWS，大幅提升低信噪比下示例查询关键词识别精度
practical_value: '- 电商语音导购、语音搜索类Agent可复用门控跨注意力的多模态融合方案，低噪场景注入唇动特征提升语音指令/query识别准确率

  - 多模态特征融合时需保证辅助模态（如视觉、文本侧特征）携带核心语义/音素信息，否则融合增益几乎可忽略

  - 低信噪比场景的query识别任务，可参考GIVE-KWS思路，引入互补模态做门控注入而非简单特征加权'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
纯音频关键词识别在高噪场景性能骤降，现有音视融合方案因视觉编码器缺乏音素信息、仅做特征加权，抗噪增益不足

### 方法关键点
1. 设计GIVE门控融合模块，通过门控交叉注意力将唇动视觉特征条件注入音频查询特征，替代传统音频特征缩放方案
2. 明确视觉编码器需具备音素信息表征能力，才能最大化多模态融合增益

### 关键结果
-10dB低信噪比场景下，相对基准系统未见过关键词的EER降低72.9%，平均EER降低62.8%；带音素信息的视觉编码器下，注入方案比掩码融合方案SNR增益高4.0~9.3dB
