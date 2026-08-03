---
title: 'LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from
  Preference Feedback'
title_zh: LEMUR：基于偏好反馈的多目标强化学习对齐框架
authors:
- Manith Adikari
- Bei Peng
- Samuele Vinanzi
- Angelo Cangelosi
affiliations:
- University of Manchester
- University of Sheffield
- Sheffield Hallam University
- Centre for Robotics & AI, University of Manchester
arxiv_id: '2607.29559'
url: https://arxiv.org/abs/2607.29559
pdf_url: https://arxiv.org/pdf/2607.29559
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: 多目标强化学习 · 偏好对齐
tags:
- Multi-Objective RL
- Preference-based RL
- Reward Learning
- Pareto Optimization
- Human Feedback
one_liner: 提出联合学习多目标专属奖励模型与策略的框架，无需预定义奖励即可平衡多冲突目标
practical_value: '- 多目标优化场景（如推荐兼顾点击率、时长、合规）可直接借鉴分目标单独训练奖励模型的思路，避免将多维度反馈聚合为单标量导致的信号损失，平衡不同业务目标的trade-off

  - 可复用向量奖励重标记（vector reward relabeling）技巧，解决奖励模型迭代后历史样本奖励过期的问题，提升离线/半离线RL训练的稳定性，尤其适合频繁调整业务目标的场景

  - 低标注预算场景可参考无监督预训练+轨迹对均匀采样的方案，用低成本的探索数据先丰富样本池，再用少量偏好标注即可获得较好的奖励模型拟合效果，降低人工标注成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有的多目标强化学习（MORL）依赖预定义的各目标奖励函数，而偏好式RL（PbRL）大多仅支持单目标，无法满足现实场景中多冲突目标（如自动驾驶兼顾速度与安全、推荐兼顾转化与用户体验）的对齐需求，人工设计多目标 reward 易出现偏差、信号稀释等问题，亟需无需预定义奖励的多目标偏好对齐方案。

### 方法关键点
- 分三阶段训练：第一阶段无监督预训练，用基于状态熵的内在奖励驱动探索，收集多样化样本填充回放池；第二阶段为每个目标/标注者单独训练专属奖励模型，基于Bradley-Terry模型拟合轨迹对偏好，所有奖励模型耦合到统一的向量奖励空间；第三阶段多目标RL训练，采用MO-SAC算法优化策略，支持动态调整目标权重以覆盖Pareto最优前沿
- 核心优化点：所有策略共享回放池提升样本效率；每次采样训练批次时用最新的奖励模型实时计算向量奖励（重标记），解决奖励模型迭代带来的非平稳问题；采用帕累托模拟退火自适应调整目标权重，保障策略多样性

### 关键实验
在MO-Lunarlander、MO-Hopper、MO-Cheetah、MO-MetaWorld四个基准环境测试，对比Utilitarian、Naive pooling、MORAL、PbMORL、FPbRL五个基线，LEMUR的Hypervolume最高，相比次优的PbMORL在MO-Hopper任务上提升63.8%，Sparsity仅为PbMORL的17%；可支持4个以上目标扩展，15%标注噪声下性能下降不明显，仅需260条标注即可产出可用策略。

最值得记住的结论：多目标对齐的核心是保留每个目标的独立反馈信号而非提前聚合为单标量，才能在复杂trade-off场景下获得更优的均衡效果。
