---
title: 'Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space
  View'
title_zh: 基于统一路径空间视角的扩散模型强化学习算法设计
authors:
- Yixian Xu
- Yuanrui Zhang
- Shengjie Luo
- Liwei Wang
- Di He
affiliations:
- Peking University
- ByteDance Seed
arxiv_id: '2608.14430'
url: https://arxiv.org/abs/2608.14430
pdf_url: https://arxiv.org/pdf/2608.14430
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 扩散模型强化学习训练优化
tags:
- Diffusion Model
- Reinforcement Learning
- Variance Reduction
- Training Framework
- Path Space
one_liner: 提出统一路径空间框架整合扩散RL算法，给出方差降低的优化训练方案
practical_value: '- 生成式推荐/广告素材生成场景下，用扩散模型RL对齐用户偏好时，可直接复用多样本KDE价值梯度估计器，无需额外采样即可降低梯度方差，提升训练稳定性

  - 扩散RL训练可直接套用scale-bounded权重原则，避免不同时间步梯度爆炸/消失，无需盲目试参即可获得稳定的训练效果

  - 业务落地扩散RL优先选确定性价值梯度+有界权重的方案，相比GRPO类方法收敛速度提升2-4倍，大幅降低对齐成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有扩散模型RL后对齐人类/任务偏好的算法呈碎片化状态：反向轨迹类方法依赖离散似然比，前向匹配类方法基于带噪样本训练，两类方法损失结构差异大、缺乏统一理论指导，训练不稳定、收敛慢的问题制约其在生成式业务中的落地。
### 方法关键点
- 基于路径空间重要性采样推导统一的扩散RL目标模板，现有Flow-GRPO、AWM、DiffusionNFT等主流算法均为该模板下不同参数的实例，算法间效果差异本质是方差降低程度不同而非底层RL原理差异
- 多样本KDE价值梯度估计器复用已收集的rollout组样本计算梯度，无额外采样开销，比单样本确定性估计器方差降低67.5%
- scale-bounded权重设计原则保证每步更新量和正则项在所有时间步保持有界，避免梯度爆炸/消失，简化权重调参流程
### 关键实验
在SD3.5-M、Qwen-Image模型上，基于PickScore、OCR、GenEval等奖励验证：OCR任务下对齐效率比AWM快2倍、比DiffusionNFT快3倍；Qwen-Image模型HPSv3奖励下比DiffusionNFT快4倍收敛。
### 核心记忆点
扩散RL算法的效果差异核心是梯度方差控制，复用现有样本做方差降低+有界权重设计可大幅提升训练效率。
