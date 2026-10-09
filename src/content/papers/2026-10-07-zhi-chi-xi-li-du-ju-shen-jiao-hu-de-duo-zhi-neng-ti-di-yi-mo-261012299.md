---
title: Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction
title_zh: 支持细粒度具身交互的多智能体第一人称世界模型
authors:
- Dahyun Chung
- Siyoon Jin
- Hyunwook Choi
- Honggyu An
- Junyoung Seo
- Hyunsung Kim
- Seung Wook Kim
- Seungryong Kim
affiliations:
- KAIST AI
arxiv_id: '2610.12299'
url: https://arxiv.org/abs/2610.12299
pdf_url: https://arxiv.org/pdf/2610.12299
published: '2026-10-07'
collected: '2026-10-09'
category: MultiAgent
direction: 多智能体具身交互 · 世界模型构建
tags:
- MultiAgent
- WorldModel
- EmbodiedAI
- GenerativeModel
- ConsistencyMetric
one_liner: ME-World多智能体第一人称世界模型，实现共享环境下细粒度具身交互的同步多视角观测生成
practical_value: '- 多Agent电商导购/客服协作场景可借鉴共享环境内存设计，保证不同Agent输出的库存、优惠等信息全局一致，避免应答冲突

  - 多Agent系统线上评测可直接复用本文提出的环境、更新、身份三类一致性度量维度，构建量化效果校验体系

  - AR虚拟逛街、多用户协同试穿等具身电商场景可复用多流联合去噪+姿态条件的生成架构，保障不同用户视角下虚拟场景同步'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有第一人称世界模型大多针对单智能体设计，无法适配多智能体共享环境交互场景；已有的多智能体世界模型仅支持移动、相机控制等粗粒度动作，缺乏细粒度具身交互能力，且存在跨视角动作、环境、状态更新不一致问题。

### 方法关键点
1. 将多智能体第一人称世界建模定义为共享环境下细粒度动作交互的多智能体同步第一视角流生成任务
2. ME-World架构：在共享token序列中联合去噪多视角流，以所有智能体目标视角姿态为生成条件，引入共享环境内存锚定生成内容一致性
3. 设计覆盖环境一致性、更新一致性、身份一致性的共享世界一致性度量体系

### 关键结果
在真实和合成多智能体数据集上，相比现有基线，ME-World在共享世界一致性、动作控制、身份保留、视频生成质量四个维度均实现显著提升。
