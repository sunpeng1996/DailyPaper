---
title: 'Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite
  Avatars'
title_zh: Avatar-Forever：面向高质量实时无限数字人的解耦并行训练框架
authors:
- Ruibin Li
- Tao Yang
- Zhiyuan Ma
- Fangzhou Ai
- Shilei Wen
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
- ByteDance
- AMD
arxiv_id: '2608.12107'
url: https://arxiv.org/abs/2608.12107
pdf_url: https://arxiv.org/pdf/2608.12107
published: '2026-08-12'
collected: '2026-08-13'
category: Multimodal
direction: 多模态生成 · 实时数字人训练推理优化
tags:
- Digital Avatar
- Parallel Training
- Feature Caching
- Video Foundation Model
- Real-Time Generation
one_liner: 提出解耦并行训练框架与分块缓存机制，实现单H100上27.2FPS高保真无限音频驱动数字人生成
practical_value: '- 解耦并行训练思路可迁移到LLM4Rec长序列建模任务，将短期推荐精度与长序列鲁棒性拆分为独立分支并行训练，避免目标冲突

  - Recovery-oriented Rollout Training（RRT）轻量Adapter训练方法可复用在生成式推荐长序列推理误差累积优化场景，无需全量微调即可提升长Horizon生成稳定性

  - 分块式特征缓存机制可迁移到流式推荐/实时对话Agent推理阶段，大幅降低历史序列重复计算开销，提升推理吞吐量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有流式视频生成依赖串行蒸馏训练流水线，存在两大痛点：一是前序阶段的错误或分布偏移会传导至后序优化，训练收敛难度大；二是蒸馏目标偏向短期生成，长序列自回归误差累积会导致生成质量大幅下降。

### 方法关键点
1. 提出解耦并行训练框架，将生成效率与长序列鲁棒性拆分为两个独立分支并行训练：一支全参数蒸馏训练高视觉质量的高效生成器，另一支通过RRT训练轻量长序列适配Adapter，避免两类目标冲突
2. 设计ForeverCache分块特征缓存机制，减少流式推理时的历史重复计算

### 关键结果
基于22B视频基座模型，单H100 GPU可实现768×512分辨率无限音频驱动数字人生成，端到端吞吐量达27.2FPS，全程保持身份一致性、动作连贯性与视觉保真度
