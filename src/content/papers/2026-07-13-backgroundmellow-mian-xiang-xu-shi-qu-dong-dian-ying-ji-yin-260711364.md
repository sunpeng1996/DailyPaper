---
title: 'BackgroundMellow: A Multi-Modal Cohesive Framework for Narrative-Driven Rich
  Cinematic Soundscape Generation'
title_zh: BackgroundMellow：面向叙事驱动电影级音景生成的多模态框架
authors:
- Ajitesh Jamulkar
- Aritra Hazra
affiliations:
- Department of Computer Science & Engineering, Indian Institute of Technology Kharagpur,
  India
arxiv_id: '2607.11364'
url: https://arxiv.org/abs/2607.11364
pdf_url: https://arxiv.org/pdf/2607.11364
published: '2026-07-13'
collected: '2026-07-21'
category: Multimodal
direction: 多模态生成 · 主从Agent协同
tags:
- Text-to-Audio
- Agent Architecture
- Latent Diffusion
- Multimodal Generation
- RAG
one_liner: 基于主从Agent架构实现无监督长文本叙事到同步高沉浸感电影音景的生成
practical_value: '- 主从Agent拆分复杂多模态生成任务的架构可直接复用：针对电商短视频/直播背景音自动生成、商品文案转配音等场景，将任务拆分为cue提取、素材生成/检索、参数调优三个子模块，用多Agent协同降低单模型复杂度，提升生成效果

  - 生成+检索融合的pipeline思路适配业务落地：专业版权素材库检索+通用生成模型合成结合，既规避生成内容的版权风险，又满足定制化需求，可直接迁移到电商内容生产链路

  - 无标注下的跨模态时序对齐方法可借鉴：通过NLP模块预测时序参数（起始时间、响度、时长）实现多素材自动混剪，可复用在商品文案转短视频的音视频同步、直播实时配乐等场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有Text-to-Audio（TTA）框架仅支持孤立音效合成，面向长文本叙事的电影级音景生成存在三大痛点：叙事连贯性不足、时序对齐偏差、缺乏情感适配的电影质感。

### 方法关键点
1. 采用master-specialist Agent架构，无需标注数据即可将长文本拆解为多层精准音频cue，调度对应specialist模块处理不同类型音频：环境音基于Tango2 latent diffusion模型生成，BGM从自建的专业电影配乐库中RAG召回；
2. 自研NLP驱动的混音模块，基于叙事时间线自动预测各音轨的起始时间、时长、相对响度等参数，完成多轨音轨的自动叠加对齐。

### 关键结果
在自制YouTube电影预告片数据集上评测，相较现有端到端TTA方案，时序同步性、音轨覆盖率、频谱丰富度均实现显著提升。
