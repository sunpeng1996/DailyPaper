---
title: Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive
  Worlds
title_zh: 面向持久叙事与交互世界的长时序视听生成方法
authors:
- Nan Duan
- Haoyang Huang
- Weiyang Jin
- Haoran Li
- Yaowei Li
- Yuming Li
- Yijun Liu
- Xin Lu
- Xiaoxiao Ma
- Yanwen Ma
affiliations:
- Joy Future Academy, JD
arxiv_id: '2608.23383'
url: https://arxiv.org/abs/2608.23383
pdf_url: https://arxiv.org/pdf/2608.23383
published: '2026-08-24'
collected: '2026-08-25'
category: Multimodal
direction: 多模态生成·长时序音视频与交互世界建模
tags:
- Audio-Visual Generation
- Long-Video Generation
- World Model
- Memory Mechanism
- Geometry Control
one_liner: 推出双变体统一视听生成系统JoyAI-Echo-1.5，在长视频一致性、交互世界建模任务上表现SOTA
practical_value: '- 跨镜头记忆机制可复用在电商生成式商品短视频、直播切片多片段一致性生成场景，保证商品、主播ID连贯

  - 长短时序Self-Gradient Forcing训练策略可迁移到长序列生成类任务（如用户全生命周期行为建模、长文案生成）的训练优化，提升长序列输出稳定性

  - 异构输入转校准6-DoF轨迹的几何感知条件通路设计，可借鉴到AR电商试穿、虚拟导购交互场景的视角控制逻辑'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频生成多聚焦孤立片段，长叙事、交互世界场景下存在身份一致性差、控制精度不足、长序列生成不稳定的痛点。
### 方法关键点
1. 推出JoyAI-Echo-1.5双变体统一系统：长视频变体引入可组合跨镜头记忆，聚合多镜头视觉、语音说话人线索，支持跨模态条件下的人物/声音身份持久一致；世界模型变体将异构导航输入转换为校准6-DoF相机轨迹，通过几何感知条件通路注入，实现灵活视角下的控制器无关交互
2. 训练侧采用渐进式teacher forcing、长短时序Self-Gradient Forcing，将双向视听骨干改造为因果少步生成器，提升长时序生成效率
### 关键结果数字
长视频变体在跨镜头一致性、视觉质量、文本对齐、语音保真度上优于现有基线；世界模型变体在WBench平均得分81.7排名第一，在SANA-WM-Bench上视觉质量、长时序持久性领先
