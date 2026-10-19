---
title: Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning
title_zh: 面向偏好强化学习的理由引导人类奖励建模方法
authors:
- Anshul Nayak
- Shahil Shaik
- Jonathan Smereka
- Yue Wang
affiliations:
- Clemson University
- U.S. Army DEVCOM Ground Vehicle Systems Center
arxiv_id: '2610.23550'
url: https://arxiv.org/abs/2610.23550
pdf_url: https://arxiv.org/pdf/2610.23550
published: '2026-10-16'
collected: '2026-10-19'
category: Training
direction: RLHF · 理由引导的人类奖励建模
tags:
- RLHF
- Reward Modeling
- Preference-based RL
- Human Alignment
- Policy Optimization
one_liner: 在RLHF偏好标注外加入结构化理由标签联合训练奖励模型，提升策略的人类对齐度与可解释性
practical_value: '- 做RLHF类用户偏好对齐任务（如个性化排序、生成式内容调优）时，可在偏好标注（喜欢/不喜欢）外增加结构化理由标签（如“性价比高”“款式符合需求”），新增BCE损失监督奖励模型训练，无需大幅增加标注成本即可显著提升对齐效果

  - 奖励模型训练时可直接复用双正则trick：同时约束奖励值大小、相邻步奖励的平滑度，能有效避免奖励波动，提升下游策略的稳定性

  - 业务策略优化时可采用业务原生奖励与人类偏好奖励加权求和的方式，通过权重λ动态调节业务目标（如GMV、点击率）与用户体验的平衡，适配不同业务阶段的需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统基于偏好的RLHF仅使用二选一的偏好标签训练奖励模型，仅能捕捉人类的选择结果，无法建模偏好背后的真实原因，导致奖励模型可解释性差，下游策略容易出现符合偏好标签但不符合人类实际预期的问题；同时仅用任务奖励训练的Agent容易出现效率优先但牺牲人类安全、体验的问题，如导航路径太贴近障碍物、推荐为了点击率推低质内容。

### 方法关键点
- 标注阶段在轨迹偏好标签外，新增多热编码的结构化理由标签，支持同时选中多个偏好原因
- 奖励模型采用双分支结构：偏好分支输出单步人类奖励，聚合后基于Bradley-Terry模型计算交叉熵损失；理由分支基于轨迹嵌入聚合结果预测偏好理由，用二元交叉熵损失监督
- 新增双正则项约束奖励值大小、相邻步奖励平滑度，避免奖励波动影响下游策略
- 策略优化阶段使用任务奖励与学习到的人类偏好奖励加权求和的总奖励，通过λ参数动态调节偏好权重

### 关键结果
基于越野导航模拟环境的350条人工标注轨迹对进行实验，对比仅用偏好损失的基线：
- 加入理由监督+正则项后，λ=0.1时任务成功率从66.7%提升至78.3%，人类主观偏好评分从33.1%提升至67.2%
- λ=0.2时，仅加正则项的版本即可达到最高成功率81.7%、最高主观偏好评分81.8%，与全量目标效果相当

少量结构化的偏好理由标注，就能大幅提升RLHF的人类对齐效率，远高于仅用偏好标签的效果
