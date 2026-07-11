---
title: 'Whareformer: Learning to Track What is Where in Long Egocentric Videos'
title_zh: Whareformer：长第一人称视频的对象位置跟踪学习
authors:
- Jacob Chalk
- Saptarshi Sinha
- Dima Damen
- Yannis Kalantidis
- Diane Larlus
affiliations:
- University of Bristol, UK
- NAVER LABS Europe, France
arxiv_id: '2607.08537'
url: https://arxiv.org/abs/2607.08537
pdf_url: https://arxiv.org/pdf/2607.08537
published: '2026-07-09'
collected: '2026-07-11'
category: Agent
direction: Agent空间感知 · 第一人称视频对象跟踪
tags:
- Egocentric Video
- Object Tracking
- Transformer
- Spatial Memory
- Agent Perception
one_liner: 首个Transformer架构的OSNOM任务学习方案，仅56条训练视频即可在多数据集达到SOTA
practical_value: '- 线下实体零售/导购Agent场景可复用「可更新轨迹记忆库+前馈轨迹分配模块」设计，实现遮挡/移出视野商品的位置追踪，优化动线引导、找货等交互体验

  - 小样本训练场景可借鉴相对距离编码+动态轨迹表征更新的设计，大幅降低训练数据采集成本，提升跨场景泛化性

  - 多模态交互Agent的空间记忆模块可引入专用New Track token机制，快速识别未录入的新实体，无需全量重训即可扩展能力边界'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
第一人称视频OSNOM（视线外对象跟踪）任务此前无成熟学习方案，自主Agent要实现类人空间感知，需能持续跟踪移出视野/重度遮挡的对象位置，支撑复杂环境交互任务。
### 方法关键点
提出Transformer架构Whareformer，核心包含两个模块：1）可更新的已生成轨迹记忆库；2）前馈式轨迹分配模块，将当前观测与已有轨迹做关联；同时联合建模动态对象外观（what）与3D位置（where），引入专用New Track token识别新增对象，采用相对距离编码+动态轨迹表征设计适配小样本训练。
### 关键结果
仅用56条视频训练，在EPIC-KITCHENS-100、IT3DEgo、HD-EPIC三个数据集共260条长测试视频上取得SOTA，较此前方案有显著绝对性能提升。
