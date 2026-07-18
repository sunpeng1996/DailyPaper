---
title: 'From Pixels to States: Rethinking Interactive World Models as Game Engines'
title_zh: 从像素到状态：重思作为游戏引擎的交互式世界模型
authors:
- Zhen Li
- Zian Meng
- Shuwei Shi
- Mingliang Zhai
- Jiaming Tan
- Chuanhao Li
- Kaipeng Zhang
affiliations:
- Alaya Lab
arxiv_id: '2607.14076'
url: https://arxiv.org/abs/2607.14076
pdf_url: https://arxiv.org/pdf/2607.14076
published: '2026-07-14'
collected: '2026-07-18'
category: Agent
direction: Agent世界模型 · 交互式场景构建
tags:
- World Model
- Interactive Generation
- Game Engine
- Video Generation
- Dataset
one_liner: 梳理交互式世界模型四大维度技术路线与权衡，发布黑神话悟空90小时带标注游戏数据集
practical_value: '- 做交互式Agent（如电商导购Agent、互动广告Agent）时，可参考四大维度（动作控制、状态动态、状态-观测一致性、实时生成）的技术选型权衡，避免盲目堆叠生成模型

  - 构建交互场景训练数据集时，可复用帧级对齐用户动作、真实状态、观测结果+语义标注的方案，大幅提升世界模型的规则一致性

  - 长周期交互生成场景（如电商虚拟逛街、互动内容）可借鉴传统游戏引擎的action-state-observation循环架构，替代纯端到端生成，降低逻辑崩坏概率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有数据驱动的视频生成式交互式世界模型存在规则一致性差、长程交互结果无法持久、生成延迟高等问题，难以满足真实交互场景的核心需求，传统游戏引擎的显式动作-状态-观测循环架构可作为研究参照。
### 方法关键点
以传统游戏引擎的action-state-observation循环为核心分析框架，从玩家动作控制、游戏状态动态、状态-观测持久性、实时交互生成四大维度，对现有技术路线归类，逐一分析各技术路线的能力边界与取舍。
### 关键结果
构建了面向《黑神话：悟空》的可扩展数据引擎，累计采集90+小时帧级对齐的游戏数据，包含玩家动作、真实游戏状态、视觉观测及结构化语义标注，可直接用于状态感知型世界模型训练。
