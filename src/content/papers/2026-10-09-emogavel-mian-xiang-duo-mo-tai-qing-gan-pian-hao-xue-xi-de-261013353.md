---
title: 'EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for
  Multimodal Emotion Preference Learning'
title_zh: EmoGavel：面向多模态情感偏好学习的可验证奖励感知定位RL框架
authors:
- Zilong Huang
- Kong Aik Lee
- Zezhong Jin
- Man-Wai Mak
- Tatsuya Kawahara
affiliations:
- The Hong Kong Polytechnic University
- Kyoto University
arxiv_id: '2610.13353'
url: https://arxiv.org/abs/2610.13353
pdf_url: https://arxiv.org/pdf/2610.13353
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 多模态偏好学习 · RL训练优化
tags:
- Reinforcement Learning
- Preference Learning
- Multimodal
- GRPO
- Grounding
- Reward Design
one_liner: 提出带可验证奖励的感知定位RL框架，同步实现多模态情感偏好预测、错误定位与修复
practical_value: '- 电商商品评价情感判别、广告素材偏好对齐场景，可复用Grounded SFT思路，联合训练偏好预测+错误定位任务，提升偏好判断可解释性

  - RL优化偏好类任务时，遇到组内样本全错无有效梯度的场景，可引入动态零方差救援机制，回收可用学习信号，降低训练样本浪费

  - 多模态内容质量校验类任务，可借鉴可验证奖励设计思路，将错误定位、修复效果等可落地校验项转化为奖励子项，提升RL训练稳定性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态情感偏好学习仅聚焦最终偏好决策输出，缺少对错误内容定位、修正的显式监督，偏好判断可解释性弱、结果难以校验，无法支撑需要可追溯偏好依据的落地场景。

### 方法关键点
1. 设计Grounded SFT预训练阶段，利用可控错误构造的标注信息，联合学习偏好预测、错误定位、内容修复、缺失证据恢复4个关联任务，为后续RL阶段提供可验证的输出基础
2. 提出GA-GRPO优化算法，融合偏好门控的定位奖励与动态零方差救援机制，优先保障偏好判断正确性，同时从全错误样本组中回收有效学习信号，避免训练梯度浪费

### 关键结果
在EmoPrefer公开数据集与自定义可控错误测试集上，自然偏好预测准确率、可控错误判别能力均优于基线，同时保持SOTA级别的错误定位性能
