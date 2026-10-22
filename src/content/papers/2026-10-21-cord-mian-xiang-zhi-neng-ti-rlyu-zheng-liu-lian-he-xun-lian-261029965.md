---
title: 'CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents'
title_zh: CORD：面向智能体RL与蒸馏联合训练的冲突感知优化框架
authors:
- Wenhao Yu
- Zhengcheng Wang
- Jiahong Liu
- Zexuan Qiu
- Minda Hu
- Shaohang Wei
- Jiafei Lyu
- Junyan Lyu
- Haobo Fu
- Irwin King
affiliations:
- The Chinese University of Hong Kong
- Tencent
- Peking University
arxiv_id: '2610.29965'
url: https://arxiv.org/abs/2610.29965
pdf_url: https://arxiv.org/pdf/2610.29965
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent训练 · 多目标梯度优化
tags:
- Reinforcement Learning
- Knowledge Distillation
- Gradient Projection
- Agent Training
- GRPO
one_liner: 通过梯度投影消解RL与自蒸馏的梯度冲突，通用提升多类Agent联合训练效果
practical_value: '- 电商导购Agent、推荐系统RL微调场景下，同时使用业务reward（点击/转化）和蒸馏信号（专家策略/优质交互）时，可直接接入CORD梯度投影逻辑，优先保护RL梯度消解冲突，无需修改原有损失定义，接入成本低

  - 多目标训练梯度冲突可复用CORD设计：选定核心保护梯度，冲突时将辅助目标梯度投影到保护梯度的正交空间，仅保留非冲突分量，效果优于单纯调整损失权重

  - 配置技巧：保护方向、投影门控、损失权重需联合调优，追求任务完成率优先保护RL，追求动作符合专家习惯可优先保护蒸馏，蒸馏损失与λ系数需配对调整，不可跨损失复用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent联合RL和自蒸馏训练时，稀疏任务reward与稠密token级蒸馏 guidance 可互补，但两者梯度常存在冲突，直接加权求和会抵消部分优化收益，传统固定混合系数无法选择性移除冲突分量，导致训练效率和最终效果下降。

### 方法关键点
- 梯度拆分：每个mini-batch分别累计RL（如GRPO）和蒸馏（如OPD）的加权梯度，选定其中一个为核心保护梯度，另一个为候选梯度
- 冲突触发：通过两梯度内积判断冲突，内积为负时触发投影操作
- 投影逻辑：冲突时将候选梯度投影到保护梯度的正交补空间，仅保留非冲突分量；非冲突时直接保留候选梯度，合并后输入优化器
- 兼容设计：支持切换保护方向（RL/蒸馏）、两种门控（仅冲突投影/始终投影），可兼容任意现有联合训练范式，无需修改原损失定义

### 关键实验
在ALFWorld（家务任务）、WebShop（电商导购任务）上测试，对比三类主流联合训练方案：ALFWorld上Skill-SD、GRPO+OPSD、SDAR成功率分别提升1.5、15.9、3.9个百分点，最高达80.9%；WebShop上Skill-SD成功率提升3.6个百分点，SDAR成功率从60.7%提升至64.6%。

### 核心结论
联合RL与蒸馏训练时，优先保留核心目标梯度、仅保留辅助目标的非冲突梯度，比单纯调整两类损失的混合权重能获得更稳定的收益
