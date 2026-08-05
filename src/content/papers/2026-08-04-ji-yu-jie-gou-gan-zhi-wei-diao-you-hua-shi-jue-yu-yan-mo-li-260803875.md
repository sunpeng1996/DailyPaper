---
title: Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning
title_zh: 基于结构感知微调优化视觉语言模型奖励模型
authors:
- Pyrros Koussios
- Chenhao Li
- Xin Chen
- Andreas Krause
affiliations:
- ETH Zürich
arxiv_id: '2608.03875'
url: https://arxiv.org/abs/2608.03875
pdf_url: https://arxiv.org/pdf/2608.03875
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 多模态模型微调 · RL奖励模型优化
tags:
- VLM
- Reward Model
- LoRA
- Fine-Tuning
- RL
- Inductive Bias
one_liner: 通过无监督结构感知微调+LoRA优化VLM奖励模型，无需标注即可降噪并加速RL策略收敛
practical_value: '- 电商/内容推荐RLHF排序优化场景，可复用SAFT思路，用业务自带结构先验（如用户点击序列、类目层级）替代部分人工标注做奖励模型微调，降低标注成本

  - 多模态推荐（图文商品匹配、直播话术打分）场景，可给VLM加LoRA做轻量结构感知正则，降低奖励信号噪声，提升排序策略收敛速度

  - 电商导购等多轮交互Agent落地时，无需大量人工偏好标注，用任务内在结构约束奖励模型，快速稳定RL训练流程'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
RL落地核心瓶颈是奖励函数设计，现有零样本VLM奖励模型噪声高可靠性差，RLHF等偏好学习方法依赖大量人工标注，成本高难以规模化落地。
### 方法关键点
1. 提出自监督SAFT（Structure-Aware Fine-Tuning）方案，无需真值标注即可在线优化VLM奖励信号
2. 基于LoRA适配器注入任务固有结构先验，正则化VLM隐空间，解决奖励模型的结构脆性问题
### 关键结果
跨不同能力等级的基础VLM测试均稳定实现奖励分布降噪，相比基线策略收敛速度显著提升，对齐度指标EPIC距离大幅优化，可完全替代人工偏好标注实现同等奖励模型效果。
