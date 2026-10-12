---
title: 'Beyond Temporal Proximity: Explanatory World Models for Credit Assignment
  in Reinforcement Learning'
title_zh: 超越时间邻近：强化学习信用分配的解释性世界模型
authors:
- Oriol Corcoll
- Qiyao Wei
- Ciarán Mark Gilligan-Lee
affiliations:
- Spotify
- University of Cambridge
arxiv_id: '2610.13504'
url: https://arxiv.org/abs/2610.13504
pdf_url: https://arxiv.org/pdf/2610.13504
published: '2026-10-09'
collected: '2026-10-12'
category: GenRec
direction: 生成式推荐 · RL长延迟奖励信用分配
tags:
- Credit Assignment
- Reinforcement Learning
- Explanatory World Model
- Generative Recommendation
- LLM4Rec
one_liner: 提出解释性世界模型框架，基于因果解释而非时间邻近分配RL信用，解决长延迟奖励学习低效问题
practical_value: '- 长周期业务指标（用户留存、复购、LTV）优化可直接复用EWM框架：用LLM分析用户行为序列，把延迟几百/数千步的奖励分配到之前的关键推荐/营销动作，替代纯时间折扣的RL信用分配，大幅提升样本效率

  - 可直接复用保守分层重分配算子（CHO）：递归分配奖励时全程保留episode总回报不变，不会引入额外偏置，无缝适配离线/在线RL流程，不需要修改原有策略架构和优化器

  - 电商/内容推荐场景可直接复用6种解释Prompt模板：根据业务目标（AUC提升/TopN排序优化）选择对应解释规则（反事实、解释广度、简洁性等），不需要重新设计归因逻辑

  - 可直接复用EWM的行为规则挖掘能力：比如从KuaiRand数据中挖掘出的近5步内容标签不重复的规则，直接作为推荐兜底规则，可使会话长度提升50%以上'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐、长周期Agent决策等场景中，奖励往往延迟几百到数千步才出现，传统RL基于时间邻近的折扣信用分配会稀释远距离关键动作的奖励信号，导致样本效率极低，无法有效优化用户长期留存、复购等核心业务指标。

### 方法关键点
- 提出Explanatory World Models（EWM）归因框架：输入用户全轨迹和目标事件（留存、付费等），用前沿LLM输出各历史动作对目标事件的贡献权重，构建解释因果图
- 设计保守分层重分配算子（CHO）：递归地把目标事件的奖励按贡献权重分配到对应的历史动作，全程保留整个episode的总回报不变，避免引入额外奖励偏置，适配所有标准RL算法
- 设计6种适配不同场景的解释Prompt规则：覆盖反事实归因、解释广度、解释简洁性等多种归因逻辑，可根据业务目标灵活选择

### 关键结果
- 控制环境Crafter：奖励延迟1000步时，EWM性能是LaRe的2倍，远优于PPO基线；WordCraft 3-mix长依赖任务中，EWM接近Oracle性能，PPO几乎无法学习
- 公开推荐数据集KuaiRand：离线场景下LB解释变体AUC比SFT高1.99pp，在线场景下EWM挖掘的标签去重规则使A2C的累积回报提升3.51倍，会话长度从8.1提升到30
- Spotify工业级生成式推荐：EWM优化的RLFT相比SFT基线，Recall提升3.75倍，下游多步engagement指标提升4倍

长horizon决策的信用分配核心不是时间远近，而是动作与结果的因果关联，LLM的先验知识可以大幅降低长延迟奖励的学习成本。
