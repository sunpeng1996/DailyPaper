---
title: 'XARA: A Multimodal Agentic System for eXtended Reality Experiment Generation'
title_zh: 《XARA：面向扩展现实实验生成的多模态智能体系统》
authors:
- Tareq Alsaleh
- Thomas Zhao
- Luke Guardino
- Keagan Valentine
- Isabel Kim
- Bilal Farooq
affiliations:
- Laboratory of Innovations in Transportation (LiTrans), Toronto Metropolitan University,
  Toronto, Canada
arxiv_id: '2610.21067'
url: https://arxiv.org/abs/2610.21067
pdf_url: https://arxiv.org/pdf/2610.21067
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: 多模态Agent · XR场景自动生成
tags:
- Multimodal Agent
- LLM
- XR
- Natural Language Interface
- Voice Interaction
one_liner: 提出双LLM架构多模态Agent系统XARA，支持语音驱动实时生成交通研究XR实验场景
practical_value: '- 双LLM自然语言转结构化指令pipeline可直接迁移到电商XR场景（虚拟试穿、3D卖场）的语音交互功能开发

  - 模块化实时3D场景操控架构可复用在XR电商导购、虚拟店铺的快速搭建工具开发中

  - 自然语言驱动的无代码交互设计思路，可用于优化商家后台内容生成工具，降低非技术运营的操作门槛'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
交通领域XR行为实验设计要求研究者掌握Unity/Unreal等游戏引擎开发能力，技术门槛高，严重限制了实验场景的快速原型迭代与落地效率。
### 方法关键点
1. 构建双LLM架构的多模态Agent系统XARA，设计语音转结构化指令pipeline：先完成语音输入转写，再将自然语言指令解析为可直接操控Unity XR场景的结构化命令
2. 采用模块化架构，支持对象创建、空间位置调整、动画控制、场景持久化存储等核心能力，同时兼容手势交互输入
### 关键结果
可支持无游戏引擎开发经验的交通研究者，通过语音/手势快速生成驾驶、行人、城市设计类XR实验场景，覆盖行为出行实验、交通安全研究、人因研究、政策测试等多个应用场景
