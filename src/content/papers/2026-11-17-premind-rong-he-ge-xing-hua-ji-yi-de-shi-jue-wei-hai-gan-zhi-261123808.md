---
title: 'PReMind: When Personal Memory Meets Visual Hazards'
title_zh: PReMind：融合个性化记忆的视觉危害感知多模态助手
authors:
- Yeongtak Oh
- Donghyeok Lee
- Joonhee Oh
- Jaewon Jeong
- Sungroh Yoon
affiliations:
- Department of Electrical and Computer Engineering, Seoul National University
- Interdisciplinary Program in AI, Seoul National University
arxiv_id: '2611.23808'
url: https://arxiv.org/abs/2611.23808
pdf_url: https://arxiv.org/pdf/2611.23808
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: 多模态个性化Agent · 风险感知与记忆调用
tags:
- Multimodal Agent
- Personalized Assistant
- Reinforcement Learning
- Memory Retrieval
- Risk Perception
one_liner: 提出视觉危害个性化响应评测基准与双阶段RL框架，提升记忆调用与风险响应联合成功率
practical_value: '- 可复用双阶段RL训练范式：结合按需调用+强制召回记忆的训练逻辑，优化个性化推荐/Agent的用户上下文检索准确率

  - 针对强依赖用户个体特征的场景（如过敏/慢病用户的食品/药品推荐），可借鉴「风险识别+用户记忆匹配」的联合评测指标设计思路，避免单一优化个性化或安全性的偏差

  - 多模态Agent面向风险场景的评测基准设计逻辑可迁移，用于搭建电商场景下不良内容/不适配商品的个性化识别评测集'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有个性化视觉语言助手无法同时兼顾视觉危害识别与用户个性化记忆（过敏、慢病、行动障碍等）匹配，单独优化安全性或个性化存在联合效果缺口，缺乏对应专项评测基准。
### 方法关键点
1. 推出PReMind-Bench诊断基准，可分别评测记忆访问、场景grounding、弃权判断、危害响应4个维度，同时评估两者联动场景的联合成功率；
2. 提出双阶段RL框架PReMind，结合按需记忆调用+强制全量记忆召回两种交互模式，联合训练grounded记忆使用与危害响应能力。
### 关键结果
4B参数规模下，联动场景联合成功率从基线12.9%提升至28.6%，主测试集危害响应适配度、正确弃权率均有提升，未见过的危害类型组上仍保持联合成功率增益。
