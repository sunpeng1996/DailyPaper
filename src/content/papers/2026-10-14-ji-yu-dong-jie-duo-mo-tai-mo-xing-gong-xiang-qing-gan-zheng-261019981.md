---
title: Shared Sentiment Evidence from Frozen Multimodal Models for Continuous Sentiment
  Prediction
title_zh: 基于冻结多模态模型共享情感证据的连续情感预测
authors:
- Shuobo Wang
- Ruiqi Chen
- Shaobo Qiao
- Shixu Yang
- Feng Xu
affiliations:
- UNSW Sydney
- University of Washington
- EULER AI
- SAIC Motor
arxiv_id: '2610.19981'
url: https://arxiv.org/abs/2610.19981
pdf_url: https://arxiv.org/pdf/2610.19981
published: '2026-10-14'
collected: '2026-10-17'
category: Multimodal
direction: 多模态情感分析 · 冻结大模型适配
tags:
- Multimodal Sentiment Analysis
- Frozen Backbone
- Output-space Interface
- Multimodal LLM
- CatBoost
one_liner: 提出跨冻结多模态骨干复用的输出空间共享情感证据接口，提升连续情感预测性能
practical_value: '- 电商场景下用户评论、直播片段等多模态UGC的情感分析可复用该输出空间接口思路，无需微调大模型仅适配轻量回归头即可落地，大幅降低训练与适配成本

  - 多模态特征融合可借鉴「分类分布+统计量+跨模态关系」的特征构造方法，用轻量树模型替代复杂fusion层，推理速度快可直接部署在线实时场景

  - 多模态任务适配可保留冻结大模型原生能力，避免微调带来的灾难性遗忘，适合同接口多业务场景复用的需求'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
连续多模态情感分析需融合文本、音频、视觉多模态异质信号，传统硬判断方法会损失情感备选信息，可学习fusion层则和backbone深度绑定，任务适配成本高、可复用性差。
### 方法关键点
1. 提出Shared Sentiment Evidence (SSE) 输出空间接口，固定视图、情感选项语义，跨所有冻结多模态backbone复用，无需微调backbone
2. 设计4类固定查询，输出5选项情感分布，提取分布概率、熵、跨视图关联特征共28维，输入CatBoost做连续情感回归
### 关键结果
- 基于Qwen的SSE接口在CH-SIMS-v2、CMU-MOSI数据集上性能优于监督联合读出基线
- 相同接口配置、固定读出设置下，额外3种冻结backbone单独拟合头均优于联合预测基线，验证了输出坐标的可复用性
