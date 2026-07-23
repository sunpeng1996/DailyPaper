---
title: 'Transcription Policy as a Latent Variable: Activating Controllable Verbatim
  ASR with Word-Level Timing'
title_zh: 将转录策略作为隐变量：基于词级时序的可控逐字ASR激活方法
authors:
- Laurin Wagner
- Mario Zusag
- Bernhard Thallinger
affiliations:
- nyra labs, Austria
arxiv_id: '2607.18934'
url: https://arxiv.org/abs/2607.18934
pdf_url: https://arxiv.org/pdf/2607.18934
published: '2026-07-20'
collected: '2026-07-23'
category: Other
direction: 语音识别 · 可控转录风格优化
tags:
- ASR
- Controllable Generation
- Cross-lingual Transfer
- Disfluency Detection
- Word-level Timing
one_liner: 通过任务令牌与交叉注意力微调实现ASR转录风格可控切换，同时提升词级时序精度与跨语言迁移能力
practical_value: '- 语音交互类Agent（如电商语音客服、导购）可参考任务令牌控制输出风格的思路，根据场景（质检需逐字、语义理解需意图转录）动态切换ASR输出模式，无需部署多套模型

  - 跨境电商多语言ASR场景可复用零样本迁移思路，仅用英文语料微调即可覆盖小语种逐字转录需求，大幅降低多语言语料标注成本

  - 涉及直播语音、短视频口播内容分析的业务，可借鉴词级时序优化方法，精准定位口误、违规内容等片段，提升内容标签标注与审核效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有ASR模型在混合标注数据上训练时未显式控制逐字/意图转录风格，导致解码不稳定，最高60%的WER来自风格不匹配，词级时序精度不可靠，无法同时满足语音质检、语义理解等差异化场景需求。

### 方法关键点
1. 基于并行逐字/意图转录对，训练带覆盖感知的解码器任务令牌，实现两种转录风格的可控激活；2. 引入监督交叉注意力微调，优化不流畅语音的词级时间戳精度；3. 提出verbatimize新任务，支持规模化生成高质量逐字转录语料。

### 关键结果
仅用英文语料训练，零样本下德语不流畅检测F1从10%提升至79%；全量英文微调后，英德双语的逐字准确率、不流畅检测效果、意图模式质量均超越基线；词级时序效果优于强制对齐基线。
