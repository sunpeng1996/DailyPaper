---
title: Learning to Coach for Experiential Learning
title_zh: 面向体验式学习的LLM教练训练框架L2C
authors:
- Guanheng Chen
- Tianzhu Ye
- Li Dong
- Xun Wu
- Shaohan Huang
- Furu Wei
affiliations:
- Microsoft Research
- Tsinghua University
arxiv_id: '2609.15851'
url: https://arxiv.org/abs/2609.15851
pdf_url: https://arxiv.org/pdf/2609.15851
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: Agent 体验式学习 · LLM-as-a-Coach
tags:
- LLM-as-a-Coach
- Experiential Learning
- GRPO
- Reinforcement Learning
- Test-time Scaling
one_liner: 冻结Actor模型训练专属LLM教练，从历史轨迹提取经验提升Agent性能
practical_value: '- 电商导购/搜索推荐Agent迭代可复用该架构：主Actor模型（如通用大模型、排序模型）保持冻结，仅训练轻量Coach从用户交互/推理错误轨迹中提取经验，大幅降低主模型迭代风险

  - 两种奖励设计可直接迁移：same-instance reward用于优化单query/单商品场景的错误修正，cross-instance reward用于提取跨场景通用推荐规则/运营策略

  - 测试时缩放思路可复用：多轮迭代引导比单纯扩大Actor解码token预算性价比更高，可用于用户咨询回复、复杂需求推荐等场景，兼顾准确率与推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM作为Agent执行推理、交互任务时，历史轨迹包含失败路径、有效中间结果、环境隐规则等高价值经验，但原始轨迹长、噪声冗余高，直接用于自修正易重复错误、分散注意力；直接微调Actor模型成本高，还会破坏原有通用能力，亟需低侵入的经验提取利用方案。

### 方法关键点
- 提出L2C框架：冻结执行任务的Actor模型，单独训练LLM-as-a-Coach从Actor历史轨迹提取可落地的经验，用GRPO做强化学习优化，奖励信号为Actor接收经验后输出结果的正确率
- 设计两类适配不同目标的奖励：same-instance reward用原始问题的引导回复正确率评估，鼓励提取单实例专属错误诊断、有效中间结果；cross-instance reward用经验在无关实例上的平均正确率评估，鼓励提取可迁移的通用任务规则
- 支持多轮迭代体验学习：Coach可基于Actor最新轨迹持续更新经验，迭代优化Actor输出

### 关键实验
在DAPO-Math-17K数学题、FrozenLake/Sokoban文本游戏上测试，对比Base Actor、Self-Refinement、未训练LLM Coach三类基线：同实例场景下FrozenLake准确率从23.4%提升至65.4%，Sokoban准确率从7.6%提升至23.6%；10轮迭代后Actor回复长度缩短24%，准确率持续上涨；计算效率上，L2C 10轮迭代比给Actor加2倍解码预算的准确率高3~5个百分点。

最值得记住的结论：把额外计算量花在迭代式经验提取和引导上，比单纯扩大模型解码预算的测试时缩放效率更高
