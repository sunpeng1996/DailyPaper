---
title: 'WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for
  LLM-Based TTS'
title_zh: WordVoice：面向LLM驱动TTS的显式解耦多维度词级控制框架
authors:
- Sihang Nie
- Jinxin Ji
- Xiaofen Xing
- Deyi Tuo
- Chengbin Jin
- Jialong Mai
- Xiangmin Xu
affiliations:
- South China University of Technology
- Huya Inc.
- Tongji University
- The Hong Kong Polytechnic University
- Foshan University
arxiv_id: '2607.06461'
url: https://arxiv.org/abs/2607.06461
pdf_url: https://arxiv.org/pdf/2607.06461
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 大语言模型可控语音合成
tags:
- LLM
- TTS
- Controllable Generation
- Fine-grained Annotation
- Speech Synthesis
one_liner: 提出五维词级标注的4.7k小时数据集与显式可控LLM-TTS框架，实现多维度声学属性解耦控制
practical_value: '- 可复用语言学引导的细粒度标注流水线，构建电商场景（直播配音、商品口播）专属语音标注数据集

  - 借鉴bound-token+显式声学规划机制，实现优惠信息、品牌名等核心关键词的重读、停顿精准控制，提升广告触达效果

  - 词级声学对齐方案可用于短视频带货配音与画面的严格时序匹配，大幅降低内容制作人力成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于LLM的TTS多采用隐式端到端生成范式，控制粒度粗糙，无法满足有声书、视频配音等需要精准风格干预、严格时序对齐的场景；同时存在细粒度标注数据集稀缺、多维度控制信号与离散自回归生成融合的架构难点。
### 方法关键点
1. 构建WordVoice-5A数据集，包含4.7k小时双语数据，通过语言学引导流水线标注时长、边界、能量、音高、声调五维词级声学属性；
2. 提出WordVoice框架，在LLM中引入bound-token机制实现显式「声学规划」，支持多任务韵律规划与灵活人工干预；在token转波形阶段新增细粒度声学调制模块，弥合高压缩离散token与连续波形的分辨率差，实现词级属性严格对齐。
### 关键结果数字
在多维度声学属性解耦控制效果上显著优于现有方案，同时保持业界竞争力的零样本合成稳定性。
