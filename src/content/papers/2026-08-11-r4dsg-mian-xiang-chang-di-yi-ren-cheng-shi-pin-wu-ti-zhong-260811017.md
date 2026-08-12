---
title: 'R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering
  in Long Egocentric Video'
title_zh: R4DSG：面向长第一人称视频物体中心问答的相对4D场景图记忆
authors:
- Ke Ma
- Yamin Mao
- Weiming Li
- Shuai Tan
- Yijie Zhong
- Hao Chen
- Haofen Wang
- Meng Wang
affiliations:
- Tongji University
- Samsung R&D Institute China - Beijing
- Shanghai Jiao Tong University
- Samsung Research America
- Shanghai Research Institute for Intelligent Autonomous Systems
arxiv_id: '2608.11017'
url: https://arxiv.org/abs/2608.11017
pdf_url: https://arxiv.org/pdf/2608.11017
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: 具身Agent · 长时序结构化记忆设计
tags:
- Egocentric Video
- Scene Graph
- Memory Module
- Question Answering
- Embodied Agent
one_liner: 提出仅需RGB输入的相对4D场景图记忆，显著提升长第一人称视频物体中心问答性能
practical_value: '- 线下AR导购/智能穿戴购物Agent可复用「静态锚点+动态物体分离」记忆设计，仅需RGB摄像头即可跟踪商品位置、状态变化，无需全局3D建模，降低硬件门槛

  - 长时序用户交互/行为数据的记忆系统可借鉴多维度联合索引方案：按时间、实体、相对变化、上下文联合索引，提升目标检索的召回准确率

  - 从用户第一人称视频挖掘消费需求的内容推荐场景，可复用跨帧持久实体ID生成方法，减少重复识别的计算开销'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
长时序第一人称视频是穿戴AI助手的核心数据载体，但现有基于字幕/转录的记忆方案无法保留持久物体ID与结构化空间变化，传统3D场景图方法又依赖深度输入、全局位姿等高成本条件，无法适配普通穿戴RGB摄像头的自由运动场景。

### 方法关键点
1. 提出R4DSG相对4D场景图记忆，将视频转换为按时间、地点、持久物体、锚点相对变化、本地交互上下文索引的紧凑可查询条目，无需存储原始图序列；
2. 分离静态锚点与动态物体，跨帧维护持久物体ID，用锚点相对变化而非全局对齐世界模型表示物体状态；
3. 仅依赖RGB输入，基于可提示视频分割、时序传播、相对3D升维等成熟技术实现。

### 关键结果
在EgoLifeQA的255道物体相关问题子集上，仅用问题检索时，整体效果较EgoRAG-Text提升6.7个百分点，时间类问题效果提升12.5个百分点。
