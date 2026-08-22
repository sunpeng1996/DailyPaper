---
title: Finetuning Strategies for Querying Sounds by Vocal Imitation
title_zh: 面向语音模仿检索音效的微调策略研究
authors:
- Aditya Bhattacharjee
- Christos Plachouras
- Sungkyun Chang
- Emmanouil Benetos
affiliations:
- Queen Mary University of London
arxiv_id: '2608.19174'
url: https://arxiv.org/abs/2608.19174
pdf_url: https://arxiv.org/pdf/2608.19174
published: '2026-08-19'
collected: '2026-08-22'
category: Training
direction: 音频检索 微调训练策略优化
tags:
- Contrastive Learning
- Fine-tuning
- Triplet Loss
- Audio Retrieval
- Semi-hard Negatives
- MobileNetV3
one_liner: 提出两种互补微调策略，斩获AES AIMLA 2025语音模仿音效检索挑战赛冠军
practical_value: '- 跨模态/跨域相似度匹配任务可复用「冻结预训练大编码器对比微调+轻量编码器联合三元组学习」的互补方案，兼顾效果和部署成本

  - 处理高多样性用户输入（如口语化搜索query、多模态query）的检索场景，可引入semi-hard negatives采样做三元组正则，提升泛化性

  - 端侧检索/推荐场景可优先选用MobileNetV3作为轻量编码器，平衡推理速度与匹配精度'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
语音模仿检索音效（QbVI）任务需弥合人声模仿与目标音效的表征差异，同时适配不同用户人声模仿的高度多样性、不同音效类别的声学特征跨度大等问题，传统基于手工特征或简单对比学习的方案匹配准确率低，难以落地。
### 方法关键点
1. 策略1：冻结预训练CED音频编码器，仅在上层网络做对比学习微调，充分复用预训练模型的通用音频表征能力，算力消耗低
2. 策略2：基于MobileNetV3轻量编码器，采用对比损失+三元组损失联合训练，引入semi-hard negatives采样做正则，降低匹配误差
两种策略可独立输出结果，也可做结果融合，适配不同部署算力要求
### 关键结果
组合方案获得AES AIMLA 2025 QbVI挑战赛冠军，效果优于官方基线及其他参赛方案
