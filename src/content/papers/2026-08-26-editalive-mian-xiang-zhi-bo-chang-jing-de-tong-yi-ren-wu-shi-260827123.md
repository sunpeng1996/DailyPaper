---
title: EditaLive! Unified Character Video Editing for Live Streaming
title_zh: EditaLive：面向直播场景的统一人物视频编辑框架
authors:
- Zhiyuan Li
- Chi-Man Pun
- Peng-Tao Jiang
- Bo Li
- Xiaodong Cun
affiliations:
- University of Macau
- vivo BlueImage Lab
- GVC Lab, Great Bay University
arxiv_id: '2608.27123'
url: https://arxiv.org/abs/2608.27123
pdf_url: https://arxiv.org/pdf/2608.27123
published: '2026-08-26'
collected: '2026-08-28'
category: Other
direction: 直播生成 · 实时人物视频编辑
tags:
- Real-time Video Editing
- Live Streaming
- Motion Disentanglement
- Knowledge Distillation
- Generative Video
one_liner: 提出面向直播的实时人物视频编辑框架，兼顾编辑效果、表情一致性与低延迟推理
practical_value: '- 电商直播场景可直接复用框架逻辑，给主播实时添加特效、调整服饰/虚拟装扮，提升直播间趣味性与用户停留时长、转化率

  - 离线生成模型转实时流式部署的优化思路可迁移：自蒸馏压缩采样步数、固定RoPE降低训练推理偏差、首帧保留稀疏注意力缓解内容漂移，适配所有低延迟生成类业务需求

  - 预训练模型能力复用的思路可降低多模态生成任务训练成本：基于已有外观-运动解耦的预训练模型微调，无需从零训练大模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频编辑多聚焦场景级内容，直接落地以人为核心的直播场景时，存在面部表情不一致、依赖多步离线推理无法适配实时交互的痛点。
### 方法关键点
1. 以预训练Wan-Animate图像动画模型为底座，利用其原生外观-运动解耦能力，基于自研CharEdit-50K数据集微调，支持指令驱动的人物视频编辑；
2. 将离线双向生成改造为因果流式生成，通过对齐自滚动蒸馏策略压缩为两步采样器，搭配固定RoPE、对齐强制机制缩小训练-推理偏差，首帧保留稀疏注意力过滤冗余历史信息缓解外观漂移。
### 关键结果
编辑效果达SOTA，面部表情保真度高，推理速度达14.47FPS，满足直播低延迟实时交互要求。
