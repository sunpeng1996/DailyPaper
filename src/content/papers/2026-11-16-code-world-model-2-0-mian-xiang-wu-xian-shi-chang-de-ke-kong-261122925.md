---
title: 'Code World Model 2.0: Towards Infinite Controllable Video Generation'
title_zh: Code World Model 2.0：面向无限时长的可控视频生成
authors:
- Ruoyu Wang
- Hao Zhong
- Yanming Yang
- Jiahao Tian
- Lin Liu
- Biao Gong
- Guoshan Lu
- Yiding Tian
- Chunhua Shen
- Zhenzhong Lan
affiliations:
- Inclusion AI, Ant Group
- Westlake University
- Zhejiang University
arxiv_id: '2611.22925'
url: https://arxiv.org/abs/2611.22925
pdf_url: https://arxiv.org/pdf/2611.22925
published: '2026-11-16'
collected: '2026-11-19'
category: Other
direction: 可控视频生成 · 世界模型优化
tags:
- Video Generation
- World Model
- Streaming Inference
- Controllable Generation
- Knowledge Distillation
one_liner: 提出适配多粒度视觉代理的Invoker-Render框架，结合渐进强迫训练实现无漂移长时可控视频流生成
practical_value: '- Progressive Forcing（ProForcing）训练范式可迁移至生成式广告/商品展示视频的长序列生成任务，解决自回归生成的漂移问题

  - 多粒度条件统一接口设计，可适配电商场景下从粗布局到精细3D模型的商品视频生成需求，支持灵活选择输入粒度

  - 4步因果流式推理+流水线部署方案，可复用在互动直播、实时虚拟导购场景的低延迟视频流生成工程落地'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于视觉代理的可控视频生成存在两大痛点：一是上游代理粒度差异大（从粗布局到精细几何结构），统一适配性差；二是流式自回归生成易积累漂移，无法支撑长时稳定输出。

### 方法关键点
1. 提出Invoker-Render框架，统一双向离线生成模型与4步因果流式生成模型，共享结构代理、外观参考、文本三类条件输入接口
2. 提出ProForcing训练策略：先基于训练视频历史蒸馏得到4步渲染器，再切换到自生成序列训练，从根源避免漂移
3. 基于200小时多粒度对齐语料训练，配套流水线服务栈支撑高效流式推理

### 关键结果
在多粒度代理、相机路径控制任务上效果优于现有流式基线，可实现30分钟稳定赛车视频生成，场景与主体外观无明显退化
