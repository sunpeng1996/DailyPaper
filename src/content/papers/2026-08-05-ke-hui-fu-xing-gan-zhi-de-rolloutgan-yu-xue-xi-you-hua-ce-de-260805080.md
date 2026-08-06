---
title: 'Optimizing What Policies Learn From: Recoverability-aware Rollout Intervention
  Learning'
title_zh: 可恢复性感知的Rollout干预学习：优化策略的训练采样来源
authors:
- Zheyuan Zhang
- Manqing Mao
- Hong Wang
- Zhuoer Wang
- Samson Koelle
- Jie Yuan
- Yanjun Lin
- James Feng
- Nikki Lijing Kuang
- Yanfang Ye
affiliations:
- University of Notre Dame
- Amazon, Inc.
arxiv_id: '2608.05080'
url: https://arxiv.org/abs/2608.05080
pdf_url: https://arxiv.org/pdf/2608.05080
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: LLM后训练 · 自适应Rollout分配
tags:
- GRPO
- Reinforcement Learning
- Rollout Allocation
- Contextual Bandit
- LLM Post-training
one_liner: 提出RAIL框架，在线学习结构化rollout干预决策，低预算下提升无critic RL训练效果
practical_value: '- 做LLM Agent/生成式推荐的GRPO类RL微调时，可复用RAIL的可恢复性评估逻辑替代固定rollout采样，把预算倾斜给高收益轨迹分支，降本提效

  - 动态采样场景可参考shadow-to-live部署流程：先在暖身阶段用启发式规则收集干预收益样本，再上线学习到的控制器，规避冷启动问题

  - 多步交互推荐Agent（如导购、多轮搜索）的探索策略优化，可参考结构化干预空间设计，同时调整分支数量和采样温度，适配不同阶段的探索需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前无critic的分组RL（如GRPO）是LLM后训练的主流范式，但默认均匀分配rollout预算的方式忽略了不同任务、不同轨迹状态的学习价值差异，导致算力浪费、优化信号被稀释；现有自适应rollout方法要么依赖静态启发式规则（无法适配训练过程中策略演化带来的非平稳性），要么仅调整rollout数量这一单维度，无法协调在哪干预、怎么干预的结构化决策问题。

### 方法关键点
- 定义可恢复性（recoverability）指标，量化干预对rollout组奖励方差的提升幅度，作为干预收益的直接度量
- 将干预选择建模为在线上下文老虎机问题，训练可恢复性控制器，基于最近W窗口的干预迹（状态、干预动作、实际收益）用带近因权重的Huber损失更新，适配策略演化的非平稳性
- 设计shadow-to-live部署流程：影子阶段用启发式规则（高熵节点分支）收集监督数据，上线后用效用门控选择性触发干预，仅当预测收益高于阈值时才执行，同时持续在线更新控制器

### 关键实验
在AgentBench（OS/DB）、WebShop、ToolQA四个Agent推理基准上测试，对比GRPO、ARPO、VIP、Tree-GRPO等SOTA基线，RAIL在平均rollout仅为GRPO-32的一半的情况下，所有任务成功率均领先：AgentBench-OS成功率达33.30%（超SOTA基线2.05个百分点），ToolQA Hard分组成功率78.50%（超SOTA基线3.5个百分点），同时预测收益的MAE比固定控制器低40%以上。

### 核心结论
Rollout生成过程本身也应该作为优化对象，而非固定的采样流程，通过在线学习干预决策能以更低算力成本获得更强的优化信号。
