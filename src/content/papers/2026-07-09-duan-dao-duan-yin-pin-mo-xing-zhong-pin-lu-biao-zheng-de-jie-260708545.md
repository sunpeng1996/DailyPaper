---
title: Structural Bottlenecks on Frequency Representation in End-to-End Audio Models
title_zh: 端到端音频模型中频率表征的结构瓶颈
authors:
- Nicole Cosme-Clifford
affiliations:
- Yale University
arxiv_id: '2607.08545'
url: https://arxiv.org/abs/2607.08545
pdf_url: https://arxiv.org/pdf/2607.08545
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 音频表征优化 · 可解释性提升
tags:
- Audio Encoder
- Interpretability
- Frequency Representation
- Post-hoc Refactoring
- Convolutional Model
one_liner: 发现端到端音频卷积编码器两类频率表征瓶颈，提出无重训GLRF后处理提升可解释性与可控性
practical_value: '- 做电商直播/短视频音频内容理解时，可复用GLRF无重训后处理方案，在不损失重建精度的前提下提升音调、音色等可解释特征的提取效率，用于内容标签生成、优质内容召回

  - 设计音频类特征编码器时，需提前规避步长卷积带来的频率混叠、分辨率不足两类结构瓶颈，降低特征坍缩概率，提升下游推荐任务的特征有效性

  - 做多模态推荐的音频-文本/图像特征对齐时，可借鉴频率局部基重表达的思路，减少音频特征纠缠度，提升跨模态匹配准确率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
端到端神经音频模型在压缩、生成任务上性能优异，但无法证明其直接编码了音调、音色等可解释特征，SOTA步长卷积编码器是否保留时频局部基原语的可访问性尚不明确，限制了特征可控性与可解释性。
### 方法关键点
1. 通过理论分析与控制实验，验证步长卷积编码器存在两类可预测的结构瓶颈：① 原语坍缩为混叠等价类，限制表征容量；② 学习到的滤波器频率分辨率不足，限制特征可分性。
2. 提出轻量、无需重训的Gabor隐变量重因子化（GLRF）后处理方法，将编码器隐变量重新表达为频率局部基。
### 关键结果数字
真实信号场景下特征坍缩率达31%-35%，原有滤波器带宽是理论分辨率上限的10-35x；GLRF可将带宽压缩至理论上限的1.5-3x，同时保留重建保真度，显著提升音调等属性的控制能力。
