---
title: How to Train a Critic Stably and Efficiently
title_zh: 如何稳定高效地训练Critic网络
authors:
- Penghui Qi
- Xiangxin Zhou
- Wee Sun Lee
affiliations:
- National University of Singapore
- Tencent Hunyuan
arxiv_id: '2608.23566'
url: https://arxiv.org/abs/2608.23566
pdf_url: https://arxiv.org/pdf/2608.23566
published: '2026-08-24'
collected: '2026-08-25'
category: Training
direction: LLM强化学习 · Critic训练优化
tags:
- RLHF
- Critic Optimization
- PPO
- DPPO
- MoE
one_liner: 提出BPCO训练范式，解决LLM RL中Critic训练不稳定问题，单样本采样即可匹配或超过组方法性能
practical_value: '- 落地LLM驱动的推荐话术生成、Agent决策RL优化场景时，可直接复用BPCO全流程优化trick替代现有PPO方案，避免Critic训练崩溃，同时无需GRPO类多采样，可降低70%+的推理采样成本

  - 做奖励建模时，可给训练阶段的Critic输入特权信息（如电商场景的真实下单转化率、广告真实点击标签、Agent任务的标准解决路径），无需改动推理侧Policy输入，就能大幅提升Critic拟合效率

  - 现有RLHF流程优化可优先做两个零成本改动：移除batch级advantage归一化、给value预测加奖励范围约束（如0/1点击Reward就将value约束在0-1区间），即可显著提升训练稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM RL方案中，GRPO类组方法需要对单个prompt采样多个响应，计算成本高且token级优势分配粗糙；传统Critic-based RL可实现单样本token级优势计算，但训练极不稳定易崩溃，缺乏可落地的成熟范式。

### 方法关键点
- 基础优化：用DPPO替代原生PPO，基于token绝对概率变化做裁剪，避免低概率token被过度更新
- Critic适配：用缩放arctan将value预测约束到已知奖励区间，避免预测值溢出；Critic训练采用无偏蒙特卡洛目标（λV=1），不使用bootstrapped目标减少自引用偏差
- 优势计算：移除batch级advantage归一化，避免训练后期噪声被放大；采用长度自适应GAE，λ随响应长度动态调整，平衡长短序列的优势分配偏差
- 特权输入：训练阶段给Critic输入参考答案、评分规则等Policy不可见的特权信息，降低Critic拟合难度，推理侧完全不改动Policy输入

### 关键实验
实验覆盖1.46K小样本数学题、40.3K DeepScaleR数学数据集、30B-A3B MoE模型、rubric评分任务，对比基线为16采样的Dr.GRPO组方法、传统Critic基线。核心结果：1.5B模型上BPCO比Critic基线AIME 2025准确率提升~5pct，30B MoE模型上超过组基线~8pct，单样本采样即可持平甚至优于16样本的GRPO性能，训练全程无崩溃。

### 核心结论
Critic本身不是LLM RL的短板，只要对齐其输出范围、训练目标、输入和优势信号的设计，就能实现比组方法成本更低、性能更优的RL训练。
