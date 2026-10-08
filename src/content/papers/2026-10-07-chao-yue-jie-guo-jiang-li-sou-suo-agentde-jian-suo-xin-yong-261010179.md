---
title: 'Beyond Outcome Rewards: Constructing and Assigning Retrieval Credit for Search
  Agents'
title_zh: 《超越结果奖励：搜索Agent的检索信用构建与分配方法》
authors:
- Wenyu Huang
- Xinyu Hou
- Pavlos Vougiouklis
- Ruofei Lai
- Jeff Z. Pan
affiliations:
- University of Edinburgh, UK
- Huawei Technologies R&D (UK) Limited
arxiv_id: '2610.10179'
url: https://arxiv.org/abs/2610.10179
pdf_url: https://arxiv.org/pdf/2610.10179
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 搜索Agent 检索信用分配 RL训练优化
tags:
- Search Agent
- Credit Assignment
- GRPO
- Retrieval Reward
- Reinforcement Learning
one_liner: 提出结合中间检索信号与结果奖励的训练框架，大幅提升搜索Agent多跳问答性能
practical_value: '- 电商/广告搜索场景的检索增强Agent做RL训练时，不要仅用最终转化/点击奖励，可叠加中间检索相关性的局部信用，多步检索场景收益更明显

  - 中间检索信号优先选用无前置依赖的证据覆盖率，将信用直接分配给对应检索动作的效果远优于将检索奖励加到全局轨迹奖励，平均效果可提升2个百分点以上

  - 必须保证检索信用和产生它的搜索动作严格对齐，错位分配会导致效果下降2-3个点，多跳检索场景的下降幅度更大

  - 中间检索信用不要局限于最终奖励相同的轨迹组，全组覆盖的效果最好，比仅给平分组分配的收益高2个点以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前基于RLVR的搜索Agent训练仅依赖稀疏的最终结果奖励，信用分配难度大、学习效率低：两条最终结果相同的轨迹，可能一条已经检索到部分核心证据，另一条完全未命中，但最终奖励无法区分这种差异，中间检索进度的监督信号未被有效利用，不同信号设计和信用分配方式的效果差异缺乏系统性研究。
### 方法关键点
- 构建14000条带子问题、证据依赖关系、支撑段落标注的多跳QA训练数据集，支持三种中间检索信号计算：无依赖证据覆盖率（Cov）、带前置依赖的证据覆盖率（Cov-Dep）、答案匹配（AM）
- 对比两种信用分配逻辑：scalar方式将检索奖励累加后和最终结果奖励合并做全局标准化，给整条轨迹所有token共享；local方式将检索奖励按步骤标准化后，仅分配给产生该检索结果的搜索动作对应的token
- 基于GRPO框架训练，所有实验条件的训练预算、超参数完全一致，仅修改奖励或token advantage的计算逻辑，控制变量验证不同设计的效果
### 关键结果
在7个公开QA基准（含HotpotQA、MuSiQue等多跳数据集）上对比仅用最终结果奖励的baseline：
- Cov信号+local信用分配的方案平均F1提升3.09，多跳QA场景下提升达4.81
- 同一种检索信号下，local信用分配比scalar全局分配的效果平均高1.5-2个百分点
- 检索信用和对应搜索动作严格对齐，比随机错位分配的F1高2.12以上，多跳场景差距达3.73
### 核心结论
中间检索监督信号的效果与信用分配方式强耦合，证据打分和动作级信用分配必须作为耦合的设计维度共同优化
