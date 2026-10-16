---
title: 'ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding
  Agents from Verified Beliefs'
title_zh: ANTE：先预判再执行，基于验证信念的编码Agent内部世界模型学习框架
authors:
- Yi Ge
- Kangrui Ruan
- Jifan Chen
- Manish Prajapat
- Christian Bock
- Xiaoyang Wang
- Rein Houthooft
- Aritra Sengupta
- Varun Kumar
affiliations:
- University of Maryland, College Park
- AWS AI Labs
arxiv_id: '2610.15368'
url: https://arxiv.org/abs/2610.15368
pdf_url: https://arxiv.org/pdf/2610.15368
published: '2026-10-10'
collected: '2026-10-16'
category: Agent
direction: Agent 内部世界模型与RL优化
tags:
- Coding Agent
- World Model
- Reinforcement Learning
- Belief State
- Test-Time Optimization
one_liner: 提出带信念锚定RL优化和测试时自排序的编码Agent框架，大幅提升任务成功率
practical_value: '- 可借鉴「行动前输出结构化信念（状态摘要+结果预判+信任决策）」的设计，给电商运营/推荐Agent加入操作前预判环节，比如修改商品规则前预判流量波动，降低试错成本

  - BAPO按预测结果分组分配步级信用的思路，可迁移到多轮交互推荐场景的RL credit assignment，解决长周期任务终态奖励难归因的问题

  - ANTE-TTO用自身预判结果排序候选动作的方案，无需额外外挂打分模型，可直接复用在推荐/广告策略的推理时重排环节，降低部署成本

  - 可落地SFT先学结构化输出范式、RL再优化预判准确性的两阶段训练流程，降低自定义Agent的训练门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent多为反应式，不会预判动作后果，终态RL奖励无法有效归因到早期错误步骤，导致操作易引发不可逆的环境状态损坏；已有的代码世界模型要么在RL前就冻结，仅作为辅助损失参与训练，无法将验证后的预判转化为步级信用指导策略优化。

### 方法关键点
- 两阶段训练：第一阶段SFT基于标注的BeliefTraj语料，让模型学会输出包含状态摘要、结果预判、信任/弃权决策的结构化信念状态
- RL阶段采用Belief-Anchored Policy Optimization（BAPO）：按跨rollout的相同预测结果分组，结合真实执行验证的预判结果，给每步动作分配独立信用，同时加入预测损失和决策奖励共同优化
- 推理时ANTE-TTO策略：当模型弃权或预判动作失败时，采样多个候选动作，用自身输出的信念分数排序，仅执行排名最高的动作，无需外部打分器

### 关键结果
在SWE-bench Verified数据集上，ANTE将Qwen3-32B的pass@1从25.0%提升到57.2%，比无信念的GRPO baseline高6.2个百分点；世界模型预测准确率在RL过程中从44%提升到69%；在11个分布外推理基准上平均性能比基线高6.2个百分点；ANTE-TTO仅增加31%的推理token即可提升效果，远低于best-of-n策略的成本。

**最值得记住的一句话**：让Agent在行动前预判后果、用真实执行反馈校准信念，是提升长周期任务鲁棒性与泛化性的低成本有效路径。
