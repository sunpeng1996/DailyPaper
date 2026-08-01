---
title: 'ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine'
title_zh: ACE-Data-0：以人为中心的环境采集具身数据引擎
authors:
- Yukang Cao
- Haozhe Xie
- Beichen Wen
- Runmao Yao
- Yinghao Liu
- Yue Huang
- Zhichao Liao
- Yunxiang Wang
- Haiheng Liu
- Xingshun Tian
affiliations:
- S-Lab, Nanyang Technological University
- ACE Robotics
arxiv_id: '2607.28625'
url: https://arxiv.org/abs/2607.28625
pdf_url: https://arxiv.org/pdf/2607.28625
published: '2026-07-29'
collected: '2026-08-01'
category: Agent
direction: 具身Agent · 多模态数据采集与基准构建
tags:
- Embodied AI
- Data Engine
- Multimodal Dataset
- Imitation Learning
- World Model
one_liner: 推出双尺度多模态同步具身采集引擎ACE、150小时家用场景交互数据集及分层评测基准
practical_value: '- 家居场景具身导购/家务Agent研发可复用ACE双尺度（桌面+全屋）多模态同步采集范式，低成本构建自有场景交互数据集

  - 多模态时空对齐的工程实现方案可迁移到电商直播/短视频的多模态（视频、动作、语音、用户交互信号）同步标注 pipeline，降低标注误差

  - 分层评测基准的设计思路可复用在具身Agent的能力迭代评测中，从感知层到任务层分阶段验证模型效果'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
具身智能面临核心数据瓶颈，现有数据集在视角、模态、空间尺度上碎片化，无法完整观测感知-动作全闭环，缺失多模态同步的自然人类交互行为标注。

### 方法关键点
1. 推出Ambient Capture Engine (ACE)双尺度采集系统：桌面级配置捕捉细粒度手物操作，房间级配置捕捉全身运动、移动及全屋交互，所有模态（egocentric/多视角视频、动作捕捉、触觉、音频等）时空对齐，输出统一多模态流。
2. 构建ACE-Data-0数据集：覆盖200类家用任务、50名参与者、2个真实家居环境，含150小时数据、17M视频帧、7.5万交互片段，仅下发目标级指令而非步骤引导，保留自然行为差异。
3. 配套分层评测基准，从信号感知、场景组件识别到交互任务完成度分阶段评测。

### 关键结果
对SOTA方法的评测显示，其在接触、遮挡、自运动、长时序场景下表现存在显著差距，数据集为模仿学习、World Model、视觉-语言-动作系统提供可扩展数据支撑。
