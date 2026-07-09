---
title: 'Rank-Then-Act: Reward-Free Control from Frame-Order Progress'
title_zh: Rank-Then-Act：基于帧序进度的无奖励控制框架
authors:
- Yuriy Maksyuta
- George Bredis
- Ruslan Rakhimov
- Daniil Gavrilov
affiliations:
- T-Tech
arxiv_id: '2607.01897'
url: https://arxiv.org/abs/2607.01897
pdf_url: https://arxiv.org/pdf/2607.01897
published: '2026-07-01'
collected: '2026-07-09'
category: Agent
direction: 无奖励Agent · 专家视频策略学习
tags:
- Agent
- Reward-Free RL
- VLM
- GRPO
- Ordinal Ranking
one_liner: 提出无奖励控制框架RTA，基于VLM帧序排序与相关度奖励实现跨任务专家视频策略学习
practical_value: '- 推荐系统序列排序类任务（如用户行为序列排序、内容流转优先级排序）可借鉴GRPO组相对优化思路，规避绝对分校准误差问题

  - 电商落地Agent（如直播运营Agent、售后处理Agent）时，若手工奖励设计成本高易投机，可改用斯皮尔曼秩相关作为替代奖励信号，降低奖励工程工作量

  - 跨场景复用排序/打分模型时，可借鉴相关度作为学习信号的设计，减少跨域分数校准的额外开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
通用Agent无奖励控制是落地核心痛点，现有基于VLM的奖励模型存在依赖时间捷径、绝对得分跨任务难校准、计算成本高问题，手工奖励设计又易被投机利用。
### 方法关键点
1. 离线用GRPO目标在打乱的帧序列上训练VLM作为序数进度打分器，强制模型从视觉语义而非trivial时间线索还原帧序；
2. 不直接用打分器输出作为标量奖励，改用预测进度排名与真实时序索引的斯皮尔曼秩相关作为RL奖励，信号有界、尺度无关，无需绝对校准即可跨任务迁移。
### 关键结果
在离散控制（Catrap、Kirby游戏）、连续控制（PointMaze、MetaWorld）基准上，性能追平或优于所有此前的视频奖励学习、基于排序的基线方法，单个预训练进度打分器具备强跨任务复用能力。
