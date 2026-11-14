---
title: Experience-Handoff Reinforcement Learning for Recursive Self-Improvement
title_zh: 面向递归自提升的经验交接强化学习方法
authors:
- Doyoung Kim
- Byeongguk Jeon
- Kailin Zhang
- Sherry Yang
affiliations:
- New York University
- KAIST AI
arxiv_id: '2611.16409'
url: https://arxiv.org/abs/2611.16409
pdf_url: https://arxiv.org/pdf/2611.16409
published: '2026-11-11'
collected: '2026-11-14'
category: Agent
direction: Agent递归自提升 · 强化学习训练
tags:
- ReinforcementLearning
- RecursiveSelfImprovement
- AgentTraining
- GRPO
- PlaybookMemory
one_liner: 提出ACE-RL联合优化Agent执行/反思/经验沉淀三角色，同等算力下多基准性能超基线
practical_value: '- 可复用「分角色分组credit分配」思路优化搜索推荐Agent的RL训练：将query理解、排序、结果反思的中间产出按角色分组计算优势，降低credit分配方差

  - 电商导购/客服Agent可落地「playbook动态迭代」机制：将每次对话的错误、用户反馈沉淀为可编辑的经验手册，后续对话直接复用，无需等待权重更新

  - 训练部署分离场景可参考适配：若业务已用GRPO训好基础执行模型，套入经验交接harness前可补训反思和沉淀角色，避免生成无效经验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的RL训练仅用标量奖励，丢弃了交互过程的细粒度环境信息（如错误日志、工具返回结果）；而基于harness的推理时自提升方法仅用冻模生成经验，不会优化经验生成质量，两者各有缺陷，亟需同时兼顾权重更新和富经验交接的训练方法。

### 方法关键点
- 基于ACE harness定义三个共享权重的角色：actor执行任务、reflector从轨迹提取洞察、curator编辑任务级playbook
- 设计可验证奖励机制：每个候选playbook的奖励由新执行rollout的实际效果直接打分，无需额外奖励模型
- 按角色分对比组计算优势：actor、reflector、curator的产出分别在同输入组内归一化优势，降低credit分配方差
- 用GRPO风格更新同时优化三个角色的行为，训练算力与纯actor RL持平

### 关键实验
在Mastermind、MBPP、AppWorld、MiniSWEBench四个基准测试，对比GRPO、ERL、Delayed-joint PPO等基线，同等训练算力下：ACE-RL的RSI@3分别达到0.775、0.987、0.667、0.340，全部最优；比纯actor GRPO的RSI@3最高提升16.7%，且性能优势在K=8次尝试时依然保持，playbook的贡献可独立验证。

Agent训练不仅要优化当前rollout的动作，还要优化写给未来rollout的经验内容，才能实现真正的递归自提升。
