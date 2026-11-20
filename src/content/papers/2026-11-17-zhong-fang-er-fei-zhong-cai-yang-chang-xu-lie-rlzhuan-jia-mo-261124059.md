---
title: 'Replay, Don''t Resample: Off-Policy Consolidation of Long-Horizon RL Experts'
title_zh: 重放而非重采样：长序列RL专家模型的离线策略整合
authors:
- Zhenrui Yue
- Gongxiaohui Chen
- Huimin Zeng
- Honglei Zhuang
- Jiashuo Sun
- Zhen Han
- Dong Wang
affiliations:
- University of Illinois Urbana-Champaign
- ANL
- Independent Researcher
- Amazon
arxiv_id: '2611.24059'
url: https://arxiv.org/abs/2611.24059
pdf_url: https://arxiv.org/pdf/2611.24059
published: '2026-11-17'
collected: '2026-11-20'
category: Agent
direction: Agent多域专家模型低成本整合
tags:
- RL
- Policy Distillation
- Off-Policy Learning
- Model Consolidation
- Long-Horizon Agent
one_liner: 提出多专家重放策略蒸馏MRPD，复用RL专家训练日志实现低成本高性能多域模型整合
practical_value: '- 多域Agent/生成式推荐模型整合场景下，可复用单域RL专家的全量训练日志作为训练数据，无需重新采样交互、调用奖励模型，蒸馏成本可降至原在线方案的1/7

  - 专家训练日志需按生成的时间顺序回放，而非随机打乱作为混合数据集，可让训练全程保持准同策略状态，避免off-policy偏差，效果可提升2~3个点

  - 蒸馏损失优先选择稠密top-k KL而非单采样token的KL估计，可减少梯度截断，收敛速度更快、最终效果更优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流多域长序列Agent整合方案多教师在线策略蒸馏（MOPD）成本极高：需学生模型重新在各环境采样、每个专家逐token打分，还会继承最终专家的漂移问题；而单域RL专家训练过程中产生的带奖励、采样概率的轨迹数据通常被直接丢弃，未被利用到整合环节。
### 方法关键点
- 提出多专家重放策略蒸馏（MRPD），按专家训练的时间顺序回放各单域RL专家的训练日志，无需重新采样、调用环境或奖励模型
- 训练目标融合两部分：基于回放轨迹重算的策略梯度损失、回放前缀处学生与对应域最终专家的稠密top-k KL蒸馏损失
- 按顺序回放保证学生模型始终与生成轨迹的原始策略接近，虽本质为off-policy，但全程保持准同策略状态，仅不到4%的token被梯度截断
### 关键实验
在推理、搜索、SQL三个长序列Agent域验证，对比在线RL（GRPO/PPO）、MOPD、模型合并（TIES/模型汤）等基线：
- MRPD整体效果得分58.6，优于MOPD的58.2，单步成本仅为MOPD的1/3、训练单域专家总计算量的1/7
- 日志顺序对效果影响远大于数据量和奖励，打乱日志会导致效果下降0.6~3.1个点
### 核心结论
专家训练日志是天然的学习课程，而非可以随机混合的数据集，复用已有轨迹的成本远低于重新采样
