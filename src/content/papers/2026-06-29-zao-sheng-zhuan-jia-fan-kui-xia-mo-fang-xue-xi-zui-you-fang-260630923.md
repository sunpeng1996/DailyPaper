---
title: 'Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation
  for Noisy Expert Feedback'
title_zh: 噪声专家反馈下模仿学习最优方案：On-Policy蒸馏优于行为克隆
authors:
- Ved Sriraman
- Peihan Liu
- Daniel Hsu
- Adam Block
affiliations:
- Columbia University
arxiv_id: '2606.30923'
url: https://arxiv.org/abs/2606.30923
pdf_url: https://arxiv.org/pdf/2606.30923
published: '2026-06-29'
collected: '2026-07-01'
category: Training
direction: 模型训练 · 噪声鲁棒模仿学习
tags:
- Imitation Learning
- On-Policy Distillation
- Behavior Cloning
- Noisy Expert
- LLM Distillation
one_liner: 证明噪声专家反馈场景下on-policy蒸馏样本复杂度远优于离线行为克隆，提出鲁棒算法NAIL
practical_value: '- 训练电商导购Agent、多轮推荐决策模型时，若标注/专家反馈存在噪声（如用户历史行为有偶然错误、人工标注有偏差），优先选用on-policy蒸馏而非离线SFT，可避免样本复杂度随决策长度指数上升

  - 做LLM蒸馏（如把大模型的推荐文案生成、query理解能力蒸馏到小模型上线）时，若教师模型输出有噪声，可复用NAIL的优化trick：学生侧用greedy生成轨迹，再用教师在对应状态的反馈做augmented
  KL loss优化，效果优于普通OPD

  - 长链任务（如用户多轮购物引导、多步搜索推荐决策）的模型训练，离线BC对数据噪声容忍度极低，所需样本量随决策步长指数增长，不建议在噪声大的场景使用'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有模仿学习理论证明干净专家场景下离线行为克隆（BC/SFT）是最优的，但实际LLM训练、Agent蒸馏场景中，on-policy蒸馏（OPD）效果往往远好于离线BC，核心原因是真实场景的专家反馈普遍存在噪声（如大模型蒸馏的教师输出有错误、人工标注有偏差、用户行为有偶然误操作），现有理论无法解释这一gap，也没有给出噪声场景下的最优训练范式。
### 方法关键点
- 提出噪声专家模型：观测到的专家策略是干净最优策略加固定比例的随机噪声，覆盖LLM蒸馏、标注噪声等常见业务场景
- 理论证明：噪声场景下离线BC的样本复杂度随决策horizon指数增长，而OPD可将其降到多项式甚至horizon无关（满足噪声支配条件时）
- 提出噪声鲁棒OPD变体NAIL：每次用当前学生策略greedy生成轨迹，查询噪声专家在轨迹对应状态的输出，通过最小化augmented轨迹分布的KL散度更新策略，针对确定性专家场景扩展了支持未知噪声的NAILGUN算法
### 关键实验结果
- 数据集：合成模块化加法任务、GSM-8K数学推理数据集
- 对比基线：离线BC（SFT）、标准OPD-F（正向KL）、OPD-R（反向KL）
- 核心数字：高噪声场景下模块化加法任务基线用1M样本仍无法学习，NAIL仅用少量样本达到100%准确率；GSM-8K高噪声场景下基线准确率为0，NAIL仍能学到有效策略
### 核心结论
只要专家反馈存在噪声，长决策/推理链任务的训练一定要优先用on-policy范式，离线BC的样本效率会低到不可接受
