---
title: Enabling Immersive Audio-Visual Experience from Any Video
title_zh: 面向任意视频的沉浸式音视频体验生成框架
authors:
- Zitong Lan
- Mutian Tong
- Jiatao Gu
- Mingmin Zhao
affiliations:
- University of Pennsylvania
arxiv_id: '2609.36295'
url: https://arxiv.org/abs/2609.36295
pdf_url: https://arxiv.org/pdf/2609.36295
published: '2026-09-28'
collected: '2026-10-04'
category: Multimodal
direction: 多模态 · 沉浸式音视频生成
tags:
- Multimodal Generation
- Spatial Audio
- 360 Video
- Training-free Framework
- Audio-Visual Alignment
one_liner: 提出免训练OmniDream框架，将单目无音视频转换为音画空间对齐的沉浸式360°视听内容
practical_value: '- 电商VR逛店/全景商品展示场景可复用对象中心音画对齐思路，自动生成同步空间音频，大幅提升用户沉浸式逛购体验

  - 免训练框架的设计范式可迁移至多模态内容增强业务，无需重新训练大模型即可快速落地功能，显著降低部署成本

  - 音源内容与场景声学效应解耦的表示方法可复用在广告内容生成场景，为不同投放场景的商品广告自动适配匹配音效'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有普通视频仅提供窄视野、无空间音频的被动观看体验，沉浸感弱；现有全景视频扩展方案缺失对应空间音景，音画空间不一致导致扩展后的视觉世界仍不完整。
### 方法关键点
免训练框架OmniDream可将无音单目视频转换为沉浸式视听内容，核心为对象中心的音频表示，将每个音源的固有音频内容与场景依赖的声学效应解耦，支持独立音频生成、基于物理的传播效应模拟、灵活的空间音频渲染，实现用户自由切换视角时音频与视觉场景的空间对齐。
### 关键结果
相比基线方案，音画对齐效果、空间正确性、感知沉浸度均实现显著提升，相关demo已在Hugging Face上线
