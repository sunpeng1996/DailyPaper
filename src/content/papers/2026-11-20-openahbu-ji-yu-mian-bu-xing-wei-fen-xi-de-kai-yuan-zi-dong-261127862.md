---
title: 'OpenAHBU: Open-sourced Automatic Human Behaviour Understanding Toolkit Through
  Facial Behaviour Analysis'
title_zh: OpenAHBU：基于面部行为分析的开源自动人类行为理解工具包
authors:
- Zijian Wu
- Yupeng Huo
- Cheng Luo
- Yichen Huang
- Junan Long
- Haijun Lin
- Lu Liu
- Hatice Gunes
- Bernard Ghanem
- Siyang Song
arxiv_id: '2611.27862'
url: https://arxiv.org/abs/2611.27862
pdf_url: https://arxiv.org/pdf/2611.27862
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 面部行为理解 · 开源工具包开发
tags:
- Facial-Analysis
- Open-Source-Toolkit
- Multi-task-Learning
- Cross-domain-Generalization
- Human-Behaviour-Understanding
one_liner: 开源覆盖3个语义层级11项功能的面部行为理解工具包，支持多场景灵活部署
practical_value: '- 做直播/短视频内容推荐、广告效果评估时，可调用该工具包提取用户观看时的面部表情、情绪唤醒度等特征，优化内容/广告的个性化排序策略

  - SMTE多任务增强模块可复用在推荐系统多目标优化场景，利用关联任务的预测结果互补增强主任务精度，无需额外引入特征

  - 同一功能提供多档计算复杂度模型的设计思路，可借鉴到推荐系统在线/离线部署场景，适配不同算力资源的推理需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有学术公开的自动面部行为理解（AFBU）工具包存在功能覆盖有限、训练流程不透明、跨域泛化性弱的问题，难以支撑多样的以人为中心的落地需求。
### 方法关键点
1. 开源全链路OpenAHBU工具包，覆盖3个语义层级共11项AFBU功能，包含面部基础属性、短期心理状态、长期心理特质三类任务；
2. 8项自研功能均提供至少4种不同计算复杂度的深度学习模型，适配资源受限端和高吞吐服务端两类部署场景；
3. 引入协同多任务增强（SMTE）模块，利用关联任务的预测互补线索自适应提升各功能效果，多数模型基于多数据集聚合语料训练，保障跨域泛化性。
### 关键结果
综合评测显示，OpenAHBU在功能覆盖度、预测精度上均优于现有开源工具包，同时提供全开源训练推理脚本、预训练权重、GUI及Python库，支持跨平台部署。
