---
title: Whisper-Based Speech Transcription from Videos Across Multiple Languages for
  Cross-Cultural Understanding
title_zh: 基于Whisper的多语言视频语音转录方法助力跨文化理解
authors:
- Michael Picheny
affiliations:
- NYU Courant Institute School of Mathematics, Computing, and Data Science
- NYU
arxiv_id: '2609.11772'
url: https://arxiv.org/abs/2609.11772
pdf_url: https://arxiv.org/pdf/2609.11772
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态处理 · 多语言语音转录
tags:
- Whisper
- Speech Recognition
- Multilingual
- Video Transcription
- Multimodal
one_liner: 提出低门槛Whisper多语言视频转录优化方案，7种语言错误率可降至20%
practical_value: '- 跨境电商多语言UGC/直播内容处理场景可直接复用轻量Whisper微调方案，少量标注数据即可降低转写错误率10pct，大幅降低内容文本化成本

  - 跨地域内容推荐/广告投放场景，可基于该方法快速提取多语言视频素材的语音语义标签，补充特征维度提升召回排序效果

  - 跨文化交互Agent开发无需深度语音领域 expertise 即可快速搭建多语言语音转文本pipeline，降低多模态交互模块开发门槛'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
全球化互联互通背景下跨文化理解需求激增，LLM驱动的跨文化工具开发依赖野生多模态数据，但低门槛多语言视频语音转写工具缺失，非语音领域开发者难以快速搭建可用转录pipeline。
### 方法关键点
基于开源Whisper框架搭建多语言视频转录流程，针对无深度语音处理专业能力的开发者优化工具易用性，仅需少量标注微调数据即可实现效果优化。
### 关键结果
在西班牙语、日语、韩语、普通话、土耳其语、俄语、希伯来语共7种语言的公开YouTube视频测试集上，基础方案平均转录错误率为30%；仅加入少量微调数据后，平均错误率可降至20%，满足下游任务使用要求；同时开源配套语音、元数据供社区迭代。
