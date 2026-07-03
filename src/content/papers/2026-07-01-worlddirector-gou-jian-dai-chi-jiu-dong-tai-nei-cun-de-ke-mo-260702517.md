---
title: 'WorldDirector: Building Controllable World Simulators with Persistent Dynamic
  Memory'
title_zh: WorldDirector：构建带持久动态内存的可控世界模拟器
authors:
- Hanlin Wang
- Hao Ouyang
- Qiuyu Wang
- Wen Wang
- Qingyan Bai
- Ka Leong Cheng
- Yue Yu
- Yixuan Li
- Yihao Meng
- Zichen Liu
affiliations:
- HKUST
- Ant Group
- ZJU
- CUHK
arxiv_id: '2607.02517'
url: https://arxiv.org/abs/2607.02517
pdf_url: https://arxiv.org/pdf/2607.02517
published: '2026-07-01'
collected: '2026-07-03'
category: LLM
direction: LLM驱动可控世界模拟器构建
tags:
- World Model
- LLM Orchestration
- Dynamic Memory
- Video Generation
- 3D Control
one_liner: 提出解耦语义编排与视觉生成的可控视频世界模型，实现动态对象持久记忆与自由视角探索
practical_value: '- 动态实体持久记忆的设计思路可迁移到用户长期兴趣建模，召回长期未交互的历史偏好物品时可保留特征一致性，降低兴趣偏移误判

  - 解耦语义逻辑编排与内容生成的架构，可复用到电商商品短视频批量生成、直播虚拟场景编排，解决现有生成方案中物体穿模、属性跳变的问题

  - LLM协调3D轨迹与视角的控制方案，可优化AR试穿、虚拟导购等多视角交互场景的逻辑一致性，提升用户交互体验'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型耦合物理动态与像素渲染，依赖连续视觉观测维持运动逻辑，动态对象移出视野后复现时易出现身份、属性失真，无法支撑长时序可控环境模拟。
### 方法关键点
1. 解耦语义运动编排与视觉生成流程，引入LLM统一协调动态对象3D运动轨迹与相机视角变换，输出标准化控制信号驱动视频生成；
2. 内置持久动态内存，持续追踪移出视野对象的状态、视觉特征，采用因果分块自回归模式生成长时序视频。
### 关键结果
可支撑最长240帧的复杂长时序事件合成，动态对象离镜复现的视觉身份一致性、物理运动逻辑合规性均显著优于现有SOTA方法，支持无限制视角探索
