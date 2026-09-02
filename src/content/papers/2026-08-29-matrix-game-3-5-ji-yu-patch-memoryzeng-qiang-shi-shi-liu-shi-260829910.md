---
title: 'Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with
  Patch Memory'
title_zh: Matrix-Game 3.5：基于Patch Memory增强实时流式交互世界模型
authors:
- Runjia Qian
- Zile Wang
- Jihai Zhang
- Kai Zou
- Wei Yu
- Jiaxing Li
- Zexiang Liu
- Yaokun Li
- Fei Kang
- Kaichen Huang
affiliations:
- Riemann Dynamics
arxiv_id: '2608.29910'
url: https://arxiv.org/abs/2608.29910
pdf_url: https://arxiv.org/pdf/2608.29910
published: '2026-08-29'
collected: '2026-09-02'
category: Agent
direction: 具身Agent · 交互世界模型构建
tags:
- World Model
- Patch Memory
- Diffusion Distillation
- Embodied Agent
- Real-Time Generation
one_liner: 通过无参数Patch Memory、动静解耦表示和两步蒸馏实现长时序一致的实时交互世界生成
practical_value: '- 搭建3D电商场景、虚拟导购交互系统时，可复用无参数Patch Memory+投影相机条件机制，降低场景几何一致性建模的训练开销

  - 长时序动态内容生成（如直播间虚拟背景实时渲染、互动营销场景）可借鉴动静解耦表示方案，分别优化静态场景、动态主体的一致性

  - 大模型低延迟推理优化可参考两步渐进蒸馏框架，将双向扩散模型转换为少步因果生成器，满足实时交互的延迟要求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互世界模型需同时支撑长时序场景一致性、精准相机控制、低延迟实时生成三类核心需求，现有方案难以兼顾，长时序生成易出现几何崩坏、主体身份漂移、交互延迟过高等问题。
### 方法关键点
1. 提出无额外可训练参数的几何感知内存框架，融合3D Patch检索与投影相机条件，实现几何一致的相机控制和长时序场景召回
2. 引入静态-动态解耦的世界表示，分别建模静态场景几何和动态主体，同时保留两类信息的长时序一致性
3. 开发两阶段渐进实时蒸馏框架，通过感知流匹配和课程式Self-Rollout DMD，将双向扩散模型转换为少步因果生成器
### 关键结果
在Unreal仿真、开放世界游戏、互联网视频混合数据集上训练，实现分钟级实时交互生成，在长时序场景召回、相机控制精度、主体一致性等指标上均显著优于基线。
