---
title: 'ID-V2V: Identity-Preserving Video Restylization'
title_zh: ID-V2V：保留人物身份的视频重风格化生成框架
authors:
- Yuancheng Xu
- Mingming He
- Pablo Salamanca
- Li Ma
- Yash Kant
- Emmett Steven
- Paul Debevec
- Ning Yu
affiliations:
- Netflix
- Adobe
- Eyeline Labs
arxiv_id: '2607.22830'
url: https://arxiv.org/abs/2607.22830
pdf_url: https://arxiv.org/pdf/2607.22830
published: '2026-07-23'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 视频风格迁移
tags:
- Video Generation
- Identity Preservation
- Style Transfer
- Video-to-Video
- Generative AI
one_liner: 通过解耦身份保留与编辑生成模块，实现无配对数据训练的高保真人脸视频重风格化
practical_value: '- 电商短视频二次创作可复用该框架：对直播/商品展示片段改风格（如转卡通/复古风）时保留主播/模特身份与表情口型，降低内容生产成本

  - 可借鉴「解耦核心要素保留与风格生成」的设计思路：多模态内容生成场景中拆分核心保真要素（如人脸/商品特征）与可变编辑要素，解决无配对训练数据的问题

  - 短平快内容生产场景可复用其单帧编辑+全视频传播的工作流：仅修改首帧风格即可自动生成全片风格化内容，降低运营/内容团队操作门槛'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有生成式视频模型对视频做风格化编辑时，难以同时保留人物身份、微表情、眼动与口型同步，且业界缺少身份保留的配对视频训练数据，落地门槛高。

### 方法关键点
将任务解耦为源视频身份保留、编辑驱动视频合成两个独立模块：
1. 把身份保留转化为视频重光照问题，仅允许光照变化，用人脸重光照区域、人脸法向图严格约束人脸相似度与表情动作
2. 用编辑后的关键帧、深度序列控制风格传播与时间一致性，仅用单条视频即可构造训练对，无需稀缺的配对标注数据

### 关键结果
实验显示ID-V2V在人脸相似度、细粒度表情保留指标上显著优于现有SOTA方法，支持单/多人物场景，生成视频视觉质量满足商用内容生产要求
