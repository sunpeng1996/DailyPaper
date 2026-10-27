---
title: 'FOCUS: Active Critic Learning for Long-Horizon Language Model Agents'
title_zh: FOCUS：面向长序列LLM Agent的主动评判器学习方法
authors:
- Zhengping Jiang
- William Jurayj
- Liaoyaqi Wang
- Chunsheng Zuo
- Anqi Liu
- Benjamin Van Durme
affiliations:
- Johns Hopkins University
arxiv_id: '2610.35801'
url: https://arxiv.org/abs/2610.35801
pdf_url: https://arxiv.org/pdf/2610.35801
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: 长序列LLM Agent 强化学习优化
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- Critic Learning
- Long Horizon
one_liner: 提出主动分配rollout预算的RL框架FOCUS，解决长序列LLM Agent信用分配低效、采样成本高问题
practical_value: '- 电商导购/搜索Agent的RL训练可复用其rollout主动分配策略，优先给评判器误差大的状态加采样，在有限算力预算下提升训练效率

  - 多轮交互类推荐Agent的信用分配可借鉴其基于上下文compaction边界的分段优势估计方法，缓解长轨迹奖励稀疏问题

  - 工具调用类Agent（如商品检索、客服Agent）可直接适配其模块化上下文管理接口，无需修改核心rollout调度逻辑快速落地'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长horizon LLM Agent的RL训练面临两大核心痛点：一是稀疏的终态奖励难以精准分配到轨迹早期的动作，信用分配效率极低；二是现有学习式critic的中间状态价值估计误差大，均匀采样中间状态续跑的rollout成本极高，有限算力预算下训练效果难以提升。
### 方法关键点
- 将critic价值估计优化建模为主动学习问题，rollout调度器通过计算边际MSE reduction指标，优先选择能最大程度降低critic估计误差的中间状态采样续跑
- 基于上下文compaction边界划分轨迹段，结合critic预测值与采样续跑的实际奖励做递归值备份，生成更准确的段级TD优势用于策略更新，同时用采样结果监督critic训练
- 模块化设计解耦上下文管理、rollout分配、信用分配三大模块，支持任意compaction实现接入，适配不同长horizon Agent场景
### 关键实验
在DeonticBench法律推理、BrowseComp-Plus深度搜索、LocBench代码定位三个长horizon基准上对比GRPO、VinePPO基线，相同每步生成预算下，Qwen3.5-9B规模上FOCUS在BrowseComp-Plus准确率领先最强基线7.2个点（55.4 vs 48.2），DeonticBench领先4.1个点（56.5 vs 52.4），LocBench File@1领先2.3个点。
### 核心结论
有限rollout预算下，优先给critic估计不确定性高的状态分配采样资源，比均匀采样能更高效降低价值估计误差，显著提升长horizon Agent训练效果。
