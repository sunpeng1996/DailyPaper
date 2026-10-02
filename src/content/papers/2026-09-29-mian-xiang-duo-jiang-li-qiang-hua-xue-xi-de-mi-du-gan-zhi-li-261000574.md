---
title: 'Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward
  RL'
title_zh: 面向多奖励强化学习的密度感知奖励聚合方法DARA
authors:
- Tong Zheng
- Skylar Zhai
- Zhan Cheng
- TianMing Sha
- Youling Huang
- Shuo Zhou
- Shaotong Qi
- Jingcheng Liang
- Xuwei Ding
- Pengcheng Xu
affiliations:
- University of Chinese Academy of Sciences
- University of Minnesota Twin Cities
- University of Wisconsin–Madison
- Stony Brook University
- Kuaishou Technology
arxiv_id: '2610.00574'
url: https://arxiv.org/abs/2610.00574
pdf_url: https://arxiv.org/pdf/2610.00574
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: 多奖励RL训练 · 稀疏奖励优化
tags:
- Multi-Reward RL
- Sparse Reward
- Reward Aggregation
- GRPO
- LLM Alignment
one_liner: 基于主动组密度动态校准多奖励权重，加速稀疏奖励目标的RL训练收敛
practical_value: '- 电商/广告推荐多目标RLHF训练（同时优化点击率、转化、合规、话术友好等）时，可直接复用DARA的主动组密度加权逻辑，避免稀疏难学目标（比如合规、高客单转化）被易学目标淹没，无需人工调多目标固定权重

  - 工具调用类Agent的RL训练优先用DARA-Asym变体，对稀疏的格式合规、参数正确性奖励加权，可减少26%训练步数达到相同格式达标率，同时不损失主任务效果

  - 多目标RL训练时可适当调大rollout组大小G，相同响应预算下G越大稀疏奖励的主动组密度越高，单位样本的有效信号密度越高，能加快稀疏目标收敛

  - 业务多目标训练中某类奖励接近饱和时（比如推荐点击率已到高位），DARA会自动降低其权重，把梯度空间留给仍在提升的长尾目标（比如复购率），减少人工调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多奖励RL是LLM对齐多目标、Agent训练的核心方案，GDPO等现有方法通过分奖励维度组内归一化解决了奖励坍缩问题，但存在不同目标学习进度不均的缺陷：易学目标快速占满梯度信号，稀疏/难学目标（比如格式合规、约束满足）训练进度极慢，人工调整固定权重又容易导致主任务效果下降，缺乏动态的奖励权重校准机制。
### 方法关键点
- 定义**主动组密度**：单奖励在rollout组内产生非零相对优势的组占总batch的比例，理想GDPO归一化下，单奖励的优势能量（batch内平方优势和）和主动组密度线性正相关，密度低的稀疏奖励贡献的梯度信号天然更弱
- 提出DARA校正规则：按主动组密度的平方根倒数给奖励加权，密度越低的奖励权重越大，同时加权重上限w_max防止极端情况；分为对称（正负优势都加权）的DARA-Sym和非对称（仅正优势加权，避免负信号冲突）的DARA-Asym两个变体
- 权重完全基于每batch的实时统计计算，无需人工预定义，不改动底层策略优化目标，可直接接入所有GRPO/GDPO训练pipeline
### 关键结果
在工具调用（BFCL-v4数据集）和数学推理（MATH-500等5个基准）任务上对比GRPO、GDPO、DVAO等baseline：工具调用任务DARA达到相同格式合规度比GDPO少26%训练步数，3奖励场景下新增长度约束目标时不会挤压原有格式、准确率目标的学习效果；数学推理任务DARA达到99%长度合规度比GDPO少65%训练步数，最终效果和baseline持平甚至更优，固定权重对照组加速收敛的同时会损失1%+的准确率。
### 核心结论
多奖励RL训练中，稀疏奖励的梯度信号弱本质是主动组密度低导致的优势能量不足，基于实时密度动态加权比人工固定调参更能兼顾收敛速度和最终效果。
