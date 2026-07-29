---
title: 'Wonder: Video World Model Done Better'
title_zh: 《Wonder：性能更优的视频世界模型》
authors:
- Jiacong Xu
- Hanwen Jiang
- Zhixin Shu
- Kalyan Sunkavalli
- Vishal M. Patel
- Yiqun Mei
affiliations:
- Adobe Research
- Johns Hopkins University
arxiv_id: '2607.26037'
url: https://arxiv.org/abs/2607.26037
pdf_url: https://arxiv.org/pdf/2607.26037
published: '2026-07-27'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 视频世界模型
tags:
- Video Generation
- World Model
- Sparse Attention
- Knowledge Distillation
- Camera Control
one_liner: 通过控制、内存、训练的系统级协同设计，实现支持实时相机可控交互的通用视频世界模型
practical_value: '- 稀疏注意力内存机制可迁移到长序列推荐/对话Agent的上下文记忆模块，大幅降低长上下文推理延迟

  - 自强迫式蒸馏修正方法可复用在LLM4Rec、生成式推荐的小模型蒸馏流程，提升小模型对用户意图的遵从度

  - 密集坐标场条件化思路可借鉴到3D商品展示、AR试穿等电商多模态生成场景，提升视角切换的视觉一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成多聚焦固定时长片段合成，无法满足游戏、虚拟制作、机器人等场景下交互式可控探索、长时上下文一致性、低延迟响应的核心需求。

### 方法关键点
1. 设计带密集坐标场的相机条件模块，输出空间对齐的运动朝向提示，让模型直接将相机动作用作视觉证据；
2. 提出基于Sparse Attention的内存机制，推理时仅需关注少量相关上下文token，不受上下文长度影响，实现快速精准的内存检索；
3. 修正自强迫式蒸馏pipeline，提升学生模型对控制信号的遵从度，保留教师模型的生成多样性与长时记忆能力。

### 关键结果数字
可生成分钟级多样化视频，推理速度达16FPS，长序列生成下几何、外观、动态特性保持一致，同时支持图生视频、条件视频生成两类任务
