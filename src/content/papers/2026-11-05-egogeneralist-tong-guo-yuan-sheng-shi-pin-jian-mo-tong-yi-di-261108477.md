---
title: 'EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native
  Modeling'
title_zh: EgoGeneralist：通过原生视频建模统一第一人称动作视频任务
authors:
- Yanlin Jin
- Bowen Yang
- Cheng Zhang
- Yifan Yang
- Zhe Li
- Jianfei Cai
- Kai Zhu
affiliations:
- Monash University
- Ant Digital Technologies, Ant Group
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2611.08477'
url: https://arxiv.org/abs/2611.08477
pdf_url: https://arxiv.org/pdf/2611.08477
published: '2026-11-05'
collected: '2026-11-07'
category: Multimodal
direction: 多模态 · 第一人称动作视频统一建模
tags:
- Video Generation
- Egocentric Vision
- Multimodal Modeling
- 3D Pose Estimation
- Lightweight Adaptation
one_liner: 基于预训练视频生成器设计双模块实现5类第一人称动作视频任务统一，跨场景泛化性优异
practical_value: '- 多模态任务统一框架可复用：用轻量适配保留预训练大模型先验的思路，可迁移到电商多模态内容生成（如商品演示视频、带货动作视频生成）场景，降低全量微调成本

  - 跨模态耦合方法可借鉴：动作-视觉双流对齐的设计逻辑，可用于AR/VR试穿、虚拟数字人带货场景下的用户动作与虚拟内容的精准同步

  - 小数据泛化思路可复用：仅在实验室受控数据上适配即可泛化到开放场景的特性，可降低多模态电商内容生成的训练数据采集成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频模型虽具备强视觉先验，但无法在度量3D空间原生表征人类动作，难以同时支撑动作控制、视频生成、姿态估计等多类第一人称动作视频任务。

### 方法关键点
1. 基于预训练视频生成器做轻量适配，设计角色自适应动作渲染器，输出原生视频表征支持多方向动作-视频学习，让度量级动作既可作为空间控制信号也可作为可恢复的生成目标；
2. 设计跨流动作-视频耦合模块，在保留预训练视觉先验的前提下建立度量级动作与视觉动态的紧密对应关系。

### 关键结果
框架可统一覆盖5类第一人称动作视频任务，仅在实验室受控录制数据上完成适配，即可泛化到各类未见过的场景与交互，动作控制有效性、生成视频视觉质量均达标，打通了预训练视觉知识与度量3D人体运动的链路。
