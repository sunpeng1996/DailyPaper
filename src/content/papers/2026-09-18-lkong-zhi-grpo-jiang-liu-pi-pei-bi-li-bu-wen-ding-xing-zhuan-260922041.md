---
title: '$λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted
  Resource'
title_zh: λ控制GRPO：将流匹配比例不稳定性转化为可预算资源
authors:
- Yufeng Wang
- Parivesh Priye
- Meeshawn Marathe
- Ramit Pahwa
affiliations:
- Stony Brook University
- Rivian
- Volkswagen Group Technologies
arxiv_id: '2609.22041'
url: https://arxiv.org/abs/2609.22041
pdf_url: https://arxiv.org/pdf/2609.22041
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 流匹配GRPO训练稳定性优化
tags:
- GRPO
- Flow Matching
- Policy Optimization
- Training Stability
- Reinforcement Learning
one_liner: 通过路径方差单变量校准流匹配GRPO训练，无额外超参，提升RL对齐的稳定性与效果
practical_value: '- 生成式推荐/Agent生成内容的GRPO类RL对齐任务中，可复用路径方差估计方法替代经验式归一化，减少超参调优成本

  - 多步决策类PPO训练场景，可借鉴将训练不稳定性抽象为可量化可预算资源的思路，按步分配梯度权重提升稳定性

  - 电商商品图/营销配图等流匹配/扩散生成模型的RL对齐场景，可直接复用LambdaNorm-T校准逻辑，降低裁剪率提升生成效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Flow-GRPO是流匹配生成模型RL对齐的主流方法，但多步去噪过程中重要性比例会出现漂移、分散、裁剪失衡、有效样本减少等问题，过往方法均针对单个症状添加手工稳定器，缺乏统一底层解释与可调控的核心变量，训练稳定性差且超参调优成本高。

### 方法关键点
- 推导得出单步路径方差λ_k，完全决定重要性比例的对数均值、方差、漂移、裁剪行为等所有不稳定特征，可通过采样过程已有的输出值低成本在线估计，无需额外计算
- 提出LambdaNorm-T：基于λ_k的预测值对重要性比例做解析校准，替代经验式归一化，校准所需尺度直接复用PPO的裁剪半径ϵ，无新增超参
- 采用仅阻尼的梯度加权策略：按各去噪步的λ_k预算占用情况分配梯度权重，超过预算的步做梯度衰减，预算阈值由目标有效样本保留率q决定，无额外超参

### 关键实验
在SD3.5、FLUX两个主流文生图模型上测试，对比经验式RatioNorm基线：1）硬OCR任务上，OCR奖励提升0.0199，文本精确匹配率提升39%，子串匹配率提升61%；2）PickScore人类偏好对齐任务上，偏好得分提升0.0075，61.3%的prompt效果优于基线；3）所有任务的训练裁剪率降低约一个数量级，训练稳定性大幅提升。

### 核心结论
多步序列决策的RL训练不稳定性往往可归因到单个可量化的核心变量，与其针对症状加补丁，不如找到底层决定因子作为可预算资源调控，既减少超参又提升效果。
