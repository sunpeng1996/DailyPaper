---
title: 'CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems'
title_zh: CEAA：面向交互式计算系统的认知具身智能体架构
authors:
- Aimilios Hadjiliasi
- Louis Nisiotis
affiliations:
- University of Central Lancashire, Cyprus
- InSPIRE Research Center
arxiv_id: '2608.09848'
url: https://arxiv.org/abs/2608.09848
pdf_url: https://arxiv.org/pdf/2608.09848
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: 具身Agent 认知架构设计与落地
tags:
- Embodied Agent
- Agent Architecture
- BDI
- Sense-Think-Act
- Interactive System
one_liner: 提出模块化可落地的认知具身Agent架构，打通高层推理与实时具身执行的链路
practical_value: '- 开发电商元宇宙/虚拟导购具身Agent时，可直接复用CEAA模块化架构模板，快速对接现有感知交互层与LLM推理层，降低落地成本

  - 可参考Sense-Think-Act范式+BDI模型的结合思路，优化虚拟导购Agent行为逻辑，解决行为不一致、不可解释的问题，提升交互体验

  - 落地具身Agent时可借鉴其实现优先的设计思路，平衡推理复杂度与实时交互要求，避免过度追求复杂模型导致无法适配业务场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有具身智能体（IVA）架构存在明显断层：要么偏底层反应控制，受商业游戏引擎约束扩展性差；要么偏高层推理模型，难以落地到实时虚拟交互环境，无法同时满足认知能力与执行效率要求。

### 方法关键点
1. 基于成熟的Sense-Think-Act范式、BDI认知模型等预研框架搭建完全解耦的模块化架构，各模块可独立迭代适配不同场景；
2. 以落地实现为核心设计导向，作为通用模板可直接对接交互式3D系统的IVA「大脑」部署，无需从零搭建架构；
3. 原生打通高层认知推理与底层实时具身执行的链路，内置支持可扩展、自适应、可解释的智能体开发能力。

### 关键结果
填补了高层推理与实时执行的技术gap，可支撑元宇宙、VR、虚拟导购、严肃游戏等复杂交互场景下认知型具身Agent的快速部署，大幅降低定制开发成本。
