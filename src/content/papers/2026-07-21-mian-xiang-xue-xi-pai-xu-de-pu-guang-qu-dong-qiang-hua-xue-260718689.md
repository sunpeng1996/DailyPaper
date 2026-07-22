---
title: Exposure-Based Reinforcement Learning to Rank
title_zh: 面向学习排序的曝光驱动强化学习方法
authors:
- Harrie Oosterhuis
- Rolf Jagerman
- Zhen Qin
- Xuanhui Wang
affiliations:
- University of Amsterdam
- Google DeepMind
arxiv_id: '2607.18689'
url: https://arxiv.org/abs/2607.18689
pdf_url: https://arxiv.org/pdf/2607.18689
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 强化学习排序 · 曝光建模
tags:
- Reinforcement Learning
- Learning to Rank
- Exposure Modeling
- Auto-differentiation
- GPU Optimization
one_liner: 提出兼容自动微分的曝光驱动RL4LTR方法，解决传统自定义梯度RL排序不稳定、难落地的问题
practical_value: '- 业务需要优化曝光公平性、排序蒸馏、自定义业务排序目标时，可直接复用本文曝光层抽象，无需开发复杂自定义梯度，大幅降低工程实现成本

  - 现有RL4LTR落地遇到收敛不稳定问题时，可尝试本文的基线校正+局部边缘化策略，配合GPU矩阵运算优化，几乎无额外耗时即可提升收敛速度

  - 用32位浮点GPU训练RL排序模型时，避免使用PL-Rank这类需要中间存储未归一化值的自定义梯度方法，优先选择全log空间计算的曝光类方案

  - 本文代码已集成到Google RAX开源框架，可直接调用快速验证RL排序在个性化推荐、搜索排序场景的效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RL for LTR可灵活优化DCG、曝光公平性、排序蒸馏等任意排序目标，但传统方案依赖复杂的自定义梯度实现，不仅难以适配PyTorch/JAX等主流自动微分框架，在32位浮点GPU训练时还存在严重的数值不稳定问题，长周期训练容易出现性能暴跌，落地门槛极高。

### 方法关键点
- 引入基线校正、局部边缘化两种无侵入策略降低RL梯度估计方差，完全规避自定义梯度开发
- 提出曝光分布抽象层：将RL策略梯度估计隐藏在文档曝光分布计算之后，任意可微的曝光相关损失（公平性、蒸馏、业务自定义目标）都能直接通过自动微分优化
- 全流程在log空间计算概率，大幅提升数值稳定性，所有运算均为标准矩阵操作，天然适配GPU并行加速

### 关键结果
在MSLR-Web30k、Istella-S两个公开LTR数据集上对比PL-Rank、标准策略梯度等5种基线：
- 本文方法在MSLR数据集上NDCG@10最高达0.4815，比最优基线提升0.5%以上，收敛速度快3倍，仅需1/3训练轮次即可达到同等效果
- 训练稳定性远优于SOTA PL-Rank：PL-Rank训练250轮后就出现性能暴跌，本文方法无收敛异常
- GPU上单轮训练耗时和标准RL方法持平，采样数N≥100时计算效率超过PL-Rank

最值得记住的一句话：RL4LTR落地的核心瓶颈不是性能，而是实现复杂度和训练稳定性，基于曝光层抽象兼容自动微分是降低落地门槛的核心路径。
