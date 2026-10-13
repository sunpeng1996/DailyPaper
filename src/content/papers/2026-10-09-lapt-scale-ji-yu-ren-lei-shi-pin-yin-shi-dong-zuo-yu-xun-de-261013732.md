---
title: 'LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human
  Videos'
title_zh: LAPT-Scale：基于人类视频隐式动作预训练的具身策略规模化方法
authors:
- Zhiyuan Xiang
- Peidong Liu
- Mingyang Li
- Jiawei Li
- Wenhow Li
- Wenbo Ding
- Xiang Deng
affiliations:
- Joy Future Academy, JD
- School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen
- Tsinghua SIGS, Tsinghua University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.13732'
url: https://arxiv.org/abs/2610.13732
pdf_url: https://arxiv.org/pdf/2610.13732
published: '2026-10-09'
collected: '2026-10-13'
category: Agent
direction: 具身Agent · 隐式动作预训练
tags:
- Latent Action Pre-training
- Embodied Agent
- Human Video Pre-training
- VLA Policy
- Robotics
one_liner: 提出基于人类第一视角视频的无标注隐式动作预训练具身策略规模化范式
practical_value: '- 无标注多模态数据预训练范式可迁移到电商用户行为序列建模：无需显式动作标签，通过帧/行为序列的转移信号学习隐式表征，降低标注成本

  - 连续隐空间代替向量量化的思路可用于用户意图建模：保留细粒度行为/交互动态，提升推荐系统对小众/长尾用户需求的捕捉能力

  - 多信号对齐（感知/语义/光流）的监督方式可复用在跨域推荐对齐：替代单一像素/行为损失，提升跨场景迁移效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
具身机器人策略规模化受限于交互数据采集成本高，大规模人类第一视角视频无对应机器人动作标签，现有标注方法噪点多，难以适配复杂真实场景和多元操作动态。
### 方法关键点
1. 双模块范式LAPT-Scale：LAPT-Scale-LAM通过解释人类视频帧间视觉转移学习连续隐式动作作为监督信号，用连续隐空间替代传统向量量化方案保留细粒度运动动态，融合感知、语义、光流多对齐信号优化监督效果；
2. LAPT-Scale-Policy分三步训练VLA策略：人类视频隐式动作预训练、目标机器人具身对齐、任务特定后训练。
### 关键结果
在23.3K小时第一视角视频训练下，标注数据从1K小时提升到5K小时时，真实机器人任务成功率从63.3%提升至85.0%，策略可泛化到未见过的视觉条件。
