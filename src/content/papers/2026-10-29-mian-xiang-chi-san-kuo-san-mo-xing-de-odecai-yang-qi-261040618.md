---
title: An ODE-based Sampler for Discrete Diffusion Models
title_zh: 面向离散扩散模型的ODE采样器
authors:
- Samson Gourevitch
- Yazid Janati
- Eric Moulines
- Eric P. Xing
- Alain Durmus
- Giacomo Zanella
affiliations:
- Ecole polytechnique
- Institute of Foundation Models
- MBZUAI
- EPITA
- Bocconi University
arxiv_id: '2610.40618'
url: https://arxiv.org/abs/2610.40618
pdf_url: https://arxiv.org/pdf/2610.40618
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: 离散扩散 · 加速采样与一致性蒸馏
tags:
- Discrete Diffusion
- ODE Sampler
- Consistency Distillation
- ERF
- Text Generation
one_liner: 提出指数残差流ERF作为离散扩散的概率流ODE等效方案，支持加速采样与一致性蒸馏
practical_value: '- 离散扩散用于生成推荐文案、搜索Query时，可复用ERF采样器替代传统随机采样，减少采样步数的同时保持生成质量，降低推理延迟

  - ERF的确定性轨迹特性可直接对接一致性蒸馏流程，适合落地时将离散扩散生成模型蒸馏为少步/单步模型，适配高吞吐的线上推荐、广告文案生成场景

  - 针对掩码扩散等常用离散扩散范式，ERF有现成的特化实现方案，可直接集成进现有文本生成管线，无需大幅重构'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
连续扩散的概率流ODE可实现确定性加速采样、支持一致性蒸馏，但离散扩散长期缺乏等效ODE框架，传统采样方法随机性高、难以适配蒸馏优化，推理速度瓶颈明显。
### 方法关键点
提出指数残差流（ERFs）框架：为每个token/位置的离散状态新增连续残差变量，残差按依赖当前离散状态、扩散正反速率矩阵的分段ODE确定性演化，残差归零时更新离散状态，可严格保留原扩散的边际分布；同时给出实用的离散化采样实现，可特化适配掩码扩散、均匀扩散等常用离散扩散范式。
### 关键结果
ERF的确定性轨迹天然支持一致性蒸馏，在代码生成、文本生成等多个基准上性能优于此前的离散扩散采样方案。
