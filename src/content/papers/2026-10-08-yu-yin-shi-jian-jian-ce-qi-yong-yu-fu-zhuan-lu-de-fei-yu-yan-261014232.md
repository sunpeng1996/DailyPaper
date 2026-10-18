---
title: 'Speech event detector: Timestamped detection of non-verbal vocalizations and
  background sounds for rich speech transcription'
title_zh: 语音事件检测器：用于富转录的非语言发声与背景音带时间戳检测
authors:
- Ayush Kumar Bar
- Promila Ghosh
arxiv_id: '2610.14232'
url: https://arxiv.org/abs/2610.14232
pdf_url: https://arxiv.org/pdf/2610.14232
published: '2026-10-08'
collected: '2026-10-18'
category: Other
direction: 语音事件检测 · 富语音转录增强
tags:
- Sound Event Detection
- Non-verbal Vocalization
- Speech Transcription
- Convolutional Transformer
- Forced Alignment
one_liner: 提出5.8M参数卷积Transformer模型，可检测54类带时间戳的语音/背景事件并融合到Whisper转录
practical_value: '- 语音交互类Agent（如电商智能语音客服）可复用小参数量级+39倍实时推理速度的架构选型，落地边缘端语音事件检测能力

  - 处理多源异构标注数据时，可复用规则映射+CTC强制对齐补全时间戳的方案，解决标签格式不兼容问题，降低标注成本

  - 直播/短视频内容理解场景可集成该检测能力，识别笑声、背景音等信号生成辅助标签，优化推荐召回特征'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有ASR系统（如Whisper）仅输出文本内容，丢失说话人非语言发声（咳嗽、笑声、叹气）、环境背景音等信息，无法满足富转录场景需求。

### 方法关键点
1. 设计仅5.8M参数的卷积-Transformer混合架构，每40ms输出54类事件（20类说话人发声+34类背景音）的概率；
2. 统一7个异构公共数据集标注：通过规则映射对齐标签，CTC强制对齐补全转录内嵌标签的时间戳，成功定位8620个声音中的6360个；
3. 混合168小时真实标注数据、合成混合样本、真实背景噪声做增强训练，后处理输出带时间戳事件，支持直接融合到Whisper转录结果。

### 关键结果
敏感配置下宏观精度0.30，覆盖67%的共9367个测试事件；平衡配置下宏观F1达0.33；8线程CPU下推理速度为实时的39倍。
