---
title: 'An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM
  Reasoning'
title_zh: RL视角下的OPD：面向样本高效LLM推理的最小二乘策略蒸馏
authors:
- Shangzhe Li
- Yuxiao Yang
- Tianrun Yu
- Kaixiang Zhao
- Xiaoyun Wang
- Taylor W. Killian
- Weitong Zhang
affiliations:
- University of North Carolina at Chapel Hill
- Brigham Young University
- NVIDIA
arxiv_id: '2609.35505'
url: https://arxiv.org/abs/2609.35505
pdf_url: https://arxiv.org/pdf/2609.35505
published: '2026-09-27'
collected: '2026-09-29'
category: Training
direction: LLM策略蒸馏 · 样本高效训练
tags:
- Policy Distillation
- Off-policy Learning
- Sample Efficiency
- RL for LLM
- Reasoning
one_liner: 将价值RL的离线复用与探索引入策略蒸馏，提出LSPD，同等性能下仅需原OPD 25%的rollout批次
practical_value: '- 做垂直场景小模型蒸馏（比如电商导购Agent、Query生成模型）时，可将原有KD/OPD损失替换为LSPD的二次匹配损失+Huber鲁棒项，加0.1系数的熵正则，既能提升训练稳定性，还能保留生成多样性

  - 对rollout采样成本高的场景，接入LSPD-RB的FIFO replay buffer复用历史生成轨迹，仅需原有OPD 25%的rollout批次即可达到同等性能，大幅降低训练时的推理采样成本

  - 业务需要多候选生成召回（比如搜索suggestion、多候选广告文案生成）时，LSPD的熵正则可稳定提升Pass@k表现，Pass@32/64平均比现有EOPD基线高1.5+点，覆盖更多用户需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-policy Distillation（OPD）多基于PPO等策略RL框架实现，仅能使用当前策略生成的新鲜rollout数据，无法复用历史轨迹，采样效率极低；同时缺乏显式探索机制，蒸馏后模型生成多样性差，多候选召回的Pass@k表现不佳，亟需更高效的策略蒸馏范式。
### 方法关键点
- 将OPD的reverse-KL目标重新形式化为KL正则化RL问题，把教师模型的相对对数似然作为奖励信号，打通价值类RL与策略蒸馏的理论关联
- 提出LSPD框架，核心损失为学生与教师对数概率的二次匹配损失+显式熵正则，训练时采用Huber损失截断过大的概率差异常值，提升优化稳定性
- 支持两种部署模式：基础版LSPD支持单rollout批次多轮更新，全离线版LSPD-RB加入FIFO replay buffer复用所有历史轨迹，完全适配off-policy训练
### 关键结果
在6个数学推理基准、3组不同规模的Qwen3师生模型对下对比KD、OPD、EOPD基线：LSPD平均Avg@16比最强基线EOPD高+0.91点，Pass@16高+0.85点；LSPD-RB仅用10步训练（基线需40步）即可达到同等性能，rollout批次仅需原OPD的25%；Pass@k随采样量增大优势更明显，Pass@32/64平均比EOPD高+1.51/+1.52点；消融实验显示熵正则对Avg@16影响极小，但可提升Pass@16约2个点。
### 核心结论
策略蒸馏不需要完全依赖on-policy的PPO类框架，引入价值RL的离线复用和乐观探索机制，既能降低采样成本，还能同时提升精度和生成多样性
