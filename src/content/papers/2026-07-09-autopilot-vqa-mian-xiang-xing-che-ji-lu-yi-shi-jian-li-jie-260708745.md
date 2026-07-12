---
title: 'AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam
  Understanding'
title_zh: AUTOPILOT VQA：面向行车记录仪事件理解的多模态视觉问答基准
authors:
- Siddharth Damodharan
- Radhika Gupta
- Ali Alshami
- Ryan Rabinowitz
- Jugal Kalita
affiliations:
- University of Colorado Colorado Springs
- University of Michigan
- University of Notre Dame
arxiv_id: '2607.08745'
url: https://arxiv.org/abs/2607.08745
pdf_url: https://arxiv.org/pdf/2607.08745
published: '2026-07-09'
collected: '2026-07-12'
category: Multimodal
direction: 多模态视觉问答 · 自动驾驶场景评测基准
tags:
- Multimodal VQA
- Autonomous Driving
- Benchmark Dataset
- Dashcam Understanding
- Safety Reasoning
one_liner: 构建面向自动驾驶安全关键事件的行车记录仪事件中心VQA评测基准
practical_value: '- 分层分类的多模态场景标注体系可直接迁移到电商广告/短视频内容合规性评测基准的搭建

  - 事件中心的结构化问答评测范式，可用于内容理解Agent的推理能力对齐、效果验证

  - 兼顾上下文属性和事件级细节的评测设计思路，可复用在直播/短视频风控多模态模型迭代中'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态大模型在自动驾驶场景落地缺乏针对安全关键事件的可靠推理能力评测方案，传统VQA基准多停留在物体识别维度，无法覆盖时序关联的安全场景推理需求，难以验证模型对高风险事件的决策合理性。
### 方法关键点
1. 构建AUTOPILOT-VQA基准，基于真实驾驶事故、险肇事故的行车记录仪数据，设计结构化问答评测集
2. 覆盖10+安全相关评测维度，包含环境、交通、事故属性、可避免性推理等多类任务
3. 要求模型同时回答场景上下文属性和事件级时序关联细节，倒逼模型实现时序落地的安全感知推理
### 关键结果
作为CVPR2026 AUTOPILOT竞赛数据集开放，提供标准化的自动驾驶系统可靠性评测基准，支撑可解释、鲁棒的自动驾驶多模态系统研发。
