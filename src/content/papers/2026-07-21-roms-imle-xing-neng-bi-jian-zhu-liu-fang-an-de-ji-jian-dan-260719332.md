---
title: 'ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling'
title_zh: ROMS-IMLE：性能比肩主流方案的极简单步生成建模方法
authors:
- Chirag Vashist
- Ke Li
affiliations:
- APEX Lab
- Simon Fraser University
- Amii
- CIFAR
arxiv_id: '2607.19332'
url: https://arxiv.org/abs/2607.19332
pdf_url: https://arxiv.org/pdf/2607.19332
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: 单步生成模型 · 极简训练框架
tags:
- Generative Modeling
- IMLE
- Single-step Generation
- Convolutional Network
- Training Objective
one_liner: 基于IMLE损失和轻量卷积网络，实现无迭代去噪的高性能单步生成模型
practical_value: '- 生成式推荐/广告物料生成场景可替换迭代扩散生成流程为单步IMLE训练方案，大幅降低推理延迟，提升物料生产吞吐

  - 无需盲目堆叠大参数量Transformer架构，可针对业务场景验证中等规模轻量卷积网络效果，降低部署算力成本

  - 训练目标选型可优先验证IMLE这类轻量方案，避免直接引入复杂的变分推断、对抗训练，降低算法迭代试错成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前主流生成模型（扩散、流匹配等）普遍依赖多步迭代噪声变换实现高保真生成，业界默认迭代去噪是高性能生成的必要前提，导致模型训练、推理复杂度持续攀升，亟需验证极简方案的性能上限。
### 方法关键点
1. 训练目标选用轻量的IMLE，摒弃变分推断、对抗训练、数值积分等复杂组件
2. 主干模型采用中等规模卷积网络，无需Transformer架构
3. 完全移除迭代去噪步骤，仅添加必要的核心优化模块，实现单步端到端生成
### 关键结果
在ImageNet 256×256图像生成任务上FID达到2.56，同时保持优秀的精度与召回率，推理速度、参数量效率均显著优于多步扩散模型。
