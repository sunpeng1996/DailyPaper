---
title: Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的轨迹相对事后蒸馏框架TRIAL
authors:
- Haoyu Zheng
- Yun Zhu
- Qing Wang
- Wenqiao Zhang
affiliations:
- Zhejiang University
- Shanghai AI Laboratory
- Tencent
arxiv_id: '2608.07371'
url: https://arxiv.org/abs/2608.07371
pdf_url: https://arxiv.org/pdf/2608.07371
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 强化学习 · 事后蒸馏优化
tags:
- Agentic RL
- Hindsight Distillation
- GRPO
- Multi-turn Agent
- Reinforcement Learning
one_liner: 提出轨迹归一化事后蒸馏框架TRIAL，全场景超越GRPO，提升多轮交互Agent训练效果
practical_value: '- 电商多轮导购Agent、交互式搜索Agent训练可直接复用TRIAL的监督分配机制：无需额外标注，仅通过轨迹内事后信息动态调整各轮次训练权重，任务成功率提升显著且不增加推理成本

  - 与GRPO的融合架构可迁移：保留GRPO跨轨迹相对优势计算逻辑，新增的轨迹内事后蒸馏损失用GRPO损失幅度做钳位，避免破坏原有训练收敛性

  - 权重归一化trick适配多轮生成任务：多轮序列训练时将轮次权重的合格token加权均值设为1，既差异化分配梯度权重，又能稳定训练总步长，可复用在SFT/RL等各类多轮训练流程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有多轮Agent强化学习依赖稀疏终局奖励，GRPO等方法仅能生成整轨迹级别的监督信号，无法明确多轮决策中各轮次的贡献权重；事后蒸馏虽能补充稠密监督，但不同轮次的监督幅度缺乏校准，易出现权重分配失衡、训练不稳定问题。
### 方法关键点
- 轮次对齐评分协议：每轮决策完成后，将该轮行动的实际后果作为事后信息注入训练时的评分上下文，对比普通上下文和事后上下文下同一段生成token的log概率差，得到token级别的监督方向和局部强度
- 轨迹相对权重归一化：按轮次聚合绝对概率差，计算轮次权重时保证全轨迹合格token加权平均权重为1，将高权重分配给事后评估差异最大的轮次，不改变平均更新幅度
- 联合优化：保留GRPO的整轨迹稀疏损失，事后蒸馏损失的幅度用GRPO损失值钳位，训练阶段的事后模块完全不影响推理部署
### 关键实验
在WebShop电商交互环境、ALFWorld具身交互环境，对比GRPO、SERL、SDAR等5个基线，使用Qwen2.5-3B、Qwen3-1.7B两个backbone，8组实验全场景超越GRPO；WebShop上Qwen3-1.7B的成功率从56.4%提升到75.2%，任务得分从78.7%提升到85.7%，ALFWorld unseen场景平均成功率相对GRPO最高提升22.4个百分点。
> 多轮Agent训练中，事后监督的合理分配比单纯增加稠密监督信号对效果提升的贡献更大
