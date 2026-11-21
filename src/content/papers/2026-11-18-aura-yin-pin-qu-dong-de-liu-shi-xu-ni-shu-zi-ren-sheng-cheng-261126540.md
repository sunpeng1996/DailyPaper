---
title: 'AURA: AUdio-dRiven streaming Avatar'
title_zh: AURA：音频驱动的流式虚拟数字人生成模型
authors:
- Nathaniel Cohen
- Nicolas Dufour
- Amélie Royer
- Alasdair Newson
- Patrick Pérez
affiliations:
- Kyutai
- ISIR, Sorbonne Université
- Google DeepMind
arxiv_id: '2611.26540'
url: https://arxiv.org/abs/2611.26540
pdf_url: https://arxiv.org/pdf/2611.26540
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 流式数字人 · 音频驱动生成
tags:
- Audio-Driven-Avatar
- Streaming-Generation
- KV-Cache
- Diffusion-Model
- Model-Distillation
one_liner: 提出基于滚动KV缓存和两阶段蒸馏的音频驱动流式数字人，单GPU即可实时推理
practical_value: '- 电商直播虚拟主播、智能客服Agent等低延迟交互场景，可复用滚动KV缓存+分块因果注意力方案，取消多秒音频前瞻依赖，大幅降低端到端延迟

  - 大模型落地的速度-效果平衡可参考两阶段蒸馏流程：先对齐教师模型轨迹压缩推理步数，再用分布匹配蒸馏补全质量缺口

  - 面向不同落地硬件（端侧/云端）、业务需求（标清/高清数字人）可复用多尺寸模型选型思路，覆盖不同成本层级场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音频驱动 talking head 扩散模型需要多秒音频前瞻、数十步去噪，延迟过高，无法满足语音助手、虚拟主播等流式交互场景的低延迟因果生成要求。
### 方法关键点
1. 采用滚动KV缓存实现逐chunk生成，仅依赖当前chunk音频即可启动推理，无前瞻依赖
2. 两阶段蒸馏 pipeline：第一阶段用分块滑动窗口因果注意力掩码训练学生模型对齐教师轨迹，压缩扩散步数；第二阶段用带反向模拟的Distribution Matching Distillation（DMD）缩小质量差距
### 关键结果数字
- AURA 1.3B 单GPU可实时生成576p视频（20.7fps，适配16Hz播放），比双向教师模型快23倍，质量比肩TalkVerse
- AURA 5B 生成720p视频达9.7fps，比教师模型快17倍，质量匹配TalkVerse
