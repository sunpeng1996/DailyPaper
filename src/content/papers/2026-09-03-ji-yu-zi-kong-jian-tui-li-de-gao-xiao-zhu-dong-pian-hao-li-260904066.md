---
title: Subspace Inference Enables Efficient Active Reward Learning from Preferences
title_zh: 基于子空间推理的高效主动偏好奖励学习方法
authors:
- Yutai Zhou
- Erdem Bıyık
affiliations:
- University of Southern California
arxiv_id: '2609.04066'
url: https://arxiv.org/abs/2609.04066
pdf_url: https://arxiv.org/pdf/2609.04066
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 主动偏好奖励学习 · 贝叶斯子空间推理
tags:
- RLHF
- Active Learning
- Bayesian Inference
- Extended Kalman Filter
- Subspace Inference
- Reward Modeling
one_liner: 提出PreferenceEKF方法，通过子空间贝叶斯滤波提升主动奖励学习的样本与计算效率
practical_value: '- 做推荐/广告的用户偏好排序Reward Model主动学习时，可借鉴子空间推理思路规避全参数后验的高开销，相比DeepEnsemble方案可获得5倍以上的训练提速

  - 新品冷启动、小众用户群偏好建模等低标注样本场景，可复用PreferenceEKF的序列增量更新逻辑，新增标注无需全量重训模型，大幅降低迭代成本

  - 对预测置信度要求高的高客单价商品推荐、广告投放风控场景，可尝试子空间投影+EKF的不确定性量化方案，预期校准误差（ECE）低于现有ensemble、dropout方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLHF依赖的人工偏好反馈单条信息量极低，主动学习需要对奖励模型做不确定性量化以筛选高价值标注，但现有贝叶斯深度学习方法要么计算开销过大（如集成模型、MCMC），要么不确定性估计质量差（如dropout），无法适配大规模神经网络奖励模型的高效训练需求。

### 方法关键点
- 提出PreferenceEKF框架，将主动偏好学习建模为序列贝叶斯滤波问题，用扩展卡尔曼滤波（EKF）做后验更新，天然支持增量学习
- 基于SGD迭代结果SVD分解或随机投影构建低维参数子空间，将推理复杂度从O(|θ|²)降至O(|z|²)（|z|远小于全参数量|θ|），大幅降低计算开销
- 支持任意数量的奖励模型后验采样，可直接适配InfoGain等主流不确定性感知的采集函数，无需额外改造

### 关键结果
在D4RL、V-D4RL共12个连续控制任务上对比DeepEnsemble、Dropout等4个主流基线：
- 样本效率、测试集对数似然优于或持平所有基线，预期校准误差（ECE）为所有方法最低
- 运行速度比DeepEnsemble快5倍，比LLMCMC快40倍，模型规模、后验采样数增大时扩展性显著优于所有基线
- 学习到的奖励模型用于离线RL策略优化，性能与地面真值奖励训练的策略持平

### 核心结论
神经网络的有效参数维度远低于全参数量，在低维子空间做贝叶斯推理可同时兼顾不确定性估计质量与计算效率，是降低偏好类任务标注成本的高性价比路径
