---
title: Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective
title_zh: 从强化学习视角剖析在线策略蒸馏的效果增益与训练崩溃机制
authors:
- Han Cui
- Jianhao Yan
- Yun Luo
- Hongbo Zhang
- Zhizhang Fu
- Yue Zhang
affiliations:
- Zhejiang University
- Westlake University
arxiv_id: '2610.03185'
url: https://arxiv.org/abs/2610.03185
pdf_url: https://arxiv.org/pdf/2610.03185
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 大模型后训练 · 在线策略蒸馏优化
tags:
- On-Policy-Distillation
- Reinforcement-Learning
- Reward-Hacking
- LLM-Post-Training
- Knowledge-Distillation
one_liner: 将在线策略蒸馏解释为隐式奖励优化过程，明确其增益来源与崩溃原因及缓解方案
practical_value: '- 做生成式推荐、Agent端侧小模型蒸馏落地时，不要默认OPD能扩展小模型能力边界，其仅能提升已有正确响应的采样概率，需先确保SFT阶段覆盖业务所需全量能力

  - 若OPD训练出现重复、过长输出等崩溃问题，可直接复用两种低成本干预手段：1. 对触发生成长度上限的异常样本做loss掩码；2. 用高质量SFT checkpoint做初始化预热，无需更换教师模型

  - 做业务场景蒸馏对齐时，需提前审计教师模型对学生初始输出的偏好是否与业务目标对齐，避免隐式奖励偏置被放大导致效果退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy Distillation（OPD）已成为大模型后训练的主流方案，但现有实践中既存在稳定性能增益，也常出现输出过长、重复等训练崩溃问题，背后机制一直不明确，缺乏可落地的崩溃归因与通用缓解框架。

### 方法关键点
- 从RL视角重构OPD目标，将教师模型的反向KL监督等价为隐式令牌级奖励加熵正则的优化过程，证明OPD本质是对学生已有响应做基于教师偏好的重加权，而非扩展学生的能力边界；
- 定位训练崩溃为奖励黑客问题：学生不断拟合教师偏置但输出质量持续退化，提出两种无侵入干预方案：对触发生成长度上限的异常样本做loss掩码、使用高质量SFT checkpoint做初始化预热。

### 关键实验
在DeepMath-103K、OpenThoughts3数学推理数据集上，用JustRL-1.5B、DeepScaleR-1.5B、Qwen3系列模型做师生对测试：1. 正常OPD的pass@1增益最高达16.2pp，但随采样预算k提升增益逐渐消失，没有新增学生初始阶段无法解决的问题；2. 崩溃场景下99.4%输出触发生成长度上限，38%输出存在严重重复；3. 两种干预方案平均提升准确率3.08pp，SFT预热方案最终平均准确率达16.38%，超出基线6.22pp。

### 核心结论
OPD的效果上限由学生初始能力决定，教师的评估偏好可靠性比自身生成质量更影响蒸馏结果。
