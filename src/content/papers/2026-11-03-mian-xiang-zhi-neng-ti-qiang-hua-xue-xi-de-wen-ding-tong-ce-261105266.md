---
title: Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的稳定同策略定向引导方法
authors:
- Kevin Frans
- Alexander M Rush
- Sergey Levine
- Pieter Abbeel
- Ashvin Nair
affiliations:
- Cursor Research
- UC Berkeley
arxiv_id: '2611.05266'
url: https://arxiv.org/abs/2611.05266
pdf_url: https://arxiv.org/pdf/2611.05266
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 强化学习 定向引导训练优化
tags:
- Reinforcement Learning
- On-policy Distillation
- Agent Training
- Text Feedback
- RL Stability
one_liner: 结合文本反馈自蒸馏与同策略RL，无需降低基准性能即可优化难收敛的奖励指标
practical_value: '- 电商导购/服务Agent优化可复用该框架，对工具调用格式、合规话术、风格规范等纯RL难优化的规则类指标，搭配定向文本反馈做自蒸馏，避免转化、满意度等主任务性能掉点

  - 多约束Agent训练（如同时满足转化、合规、平台规范要求）时，可将蒸馏损失仅作用于失败的交互轮次，同时保留原RL主任务损失，大幅降低多目标优化的冲突

  - 调优时若出现策略震荡、熵值突增的情况，可先降低蒸馏损失权重，同时将蒸馏作用范围扩展到Agent的思维链（thinking tokens），提升多约束下的训练稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
纯同策略RL受基础模型行为覆盖范围限制，对不在基础分布内的奖励指标（比如新工具调用格式、特定输出风格）难以收敛，甚至完全无法优化；现有自蒸馏方法容易导致主任务性能下降、策略震荡、多样性坍缩等问题，无法直接落地到多轮交互的Agent场景。

### 方法关键点
- 定向引导框架将每个奖励指标关联对应文本反馈字符串，仅在Agent某轮交互未达标时，将反馈插入该轮上下文，以当前模型加反馈的输出作为自蒸馏教师模型，仅对失败轮次计算KL蒸馏损失
- 训练总损失为GRPO RL损失加蒸馏损失，蒸馏损失使用全词表反向KL，停止教师模型梯度，按token归一化KL值避免长序列干扰
- 文本反馈需提前验证：仅保留能让加反馈的模型平均性能优于原模型的反馈字符串，避免引入无效信号

### 关键实验
基于多轮软件工程编码Agent任务，基准模型为Qwen3-Coder-30B，对比Baseline、GRPO、OPSD、Online SFT等6种方法，在7项风格类指标上平均提升50%以上，比如Markdown格式达标率从0提升至85%，同时主任务编码通过率保持33%与基线持平，无性能损失。

### 核心结论
自蒸馏和RL奖励结合、仅对失败轮次施加定向信号，是在不影响主任务的前提下补全Agent能力短板的核心思路。
