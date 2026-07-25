---
title: 'ElasticTTT: Prior-Preserving Test-Time Tuning for Video Editing'
title_zh: ElasticTTT：面向视频编辑的先验保留型测试时调优框架
authors:
- Yueyi Liu
- Chi Zhang
- Sen Cui
- Miao Liu
affiliations:
- Tsinghua University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2607.21529'
url: https://arxiv.org/abs/2607.21529
pdf_url: https://arxiv.org/pdf/2607.21529
published: '2026-07-23'
collected: '2026-07-25'
category: Training
direction: 测试时调优 · 扩散模型视频编辑
tags:
- Test-Time-Tuning
- Diffusion-Model
- Video-Editing
- Regularization
- CFG
one_liner: 针对扩散模型视频编辑TTT的先验崩溃问题，提出ElasticTTT实现单样本视频编辑SOTA性能
practical_value: '- 可将Target Distribution Regularization迁移到生成式推荐/电商素材生成的在线微调场景，避免模型遗忘通用生成先验，适配个性化定制需求

  - Contrastive CFG的偏置消除思路可复用到生成式推荐推理阶段，降低用户历史行为的过度拟合，提升推荐结果多样性

  - Asynchronous Noise Schedule思路可借鉴到电商素材局部修改场景，比如商品主图卖点区域保留、短视频局部风格转换'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
预训练扩散模型的Test-Time Tuning（TTT）是当前视频编辑的高效范式，但生成模型的分布映射特性与标准TTT的单点优化存在本质 mismatch，会触发**Prior Collapse**退化问题：模型要么忽略文本条件/空间隐变量，生成结果退化为源视频，要么不同区域特征纠缠，编辑效果严重劣化。
### 方法关键点
提出ElasticTTT框架，包含三个核心设计：1）Target Distribution Regularization：避免模型陷入尖锐的记忆极小值，保留基础模型生成先验；2）Contrastive CFG：引导推理阶段远离源视频偏置，提升编辑内容的符合度；3）Asynchronous Noise Schedule：独立处理编辑/非编辑区域的噪声，保留无需修改的区域特征。
### 关键结果
经理论分析与大量实验验证，ElasticTTT可有效保留基础模型的生成先验，在单样本视频编辑任务上达到SOTA性能。
