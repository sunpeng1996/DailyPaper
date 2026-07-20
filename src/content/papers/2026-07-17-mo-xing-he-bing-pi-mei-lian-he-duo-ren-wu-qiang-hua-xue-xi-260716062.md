---
title: 'When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector
  Geometry Analysis'
title_zh: 模型合并媲美联合多任务强化学习的任务向量几何分析
authors:
- S. Aaron McClendon
affiliations:
- Aimpoint Digital Labs
arxiv_id: '2607.16062'
url: https://arxiv.org/abs/2607.16062
pdf_url: https://arxiv.org/pdf/2607.16062
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent多任务优化 · 模型合并
tags:
- Model Merging
- Reinforcement Learning
- Task Vector
- LoRA
- Multi-task Learning
one_liner: 验证RL智能体模型合并效果与联合多任务训练无统计差异，从任务向量几何角度解释其底层机制
practical_value: '- 多场景Agent/LLM落地时，若数据无法池化做联合训练，可优先尝试LoRA微调+模型合并方案，效果接近联合训练且成本更低

  - 合并同基座LoRA微调的多任务模型时，若任务向量余弦相似度<0.1（近正交），无需用复杂的TIES/RAM+算法，直接平均即可达到相同效果

  - 做模型合并前可先计算不同任务向量的余弦相似度（对比随机初始化floor、同任务不同checkpoint ceiling校准），提前预判合并收益，避免无效调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：当前模型合并被广泛宣传为联合多任务训练的低成本替代方案，但在RL训练的智能体场景下，从未在同训练数据、同基座、同训练策略的受控条件下与联合训练基线做公平对比，不同合并算法的效果差异底层机制也不明确。
**方法关键点**：
- 以Qwen3-8B为基座，用LoRA（rank=16）+LOOP（无critic的RL策略梯度方法）分别训练AppWorld难度1、难度2任务的专家模型，同时训练同数据的联合多任务模型作为基线
- 采用TIES、RAM+两种主流合并算法合并两个专家模型，对比合并模型、单专家模型、联合模型的效果
- 设计校准方案：以随机初始化LoRA的任务向量余弦值为floor，同任务不同训练阶段checkpoint的余弦值为ceiling，排除低秩参数化对几何测量的干扰
**关键结果**：在AppWorld test_normal拆分的168个任务上，核心指标任务目标完成率（TGC）显示：所有RL模型TGC均显著高于基座的6.6%；合并模型（TIES 14.3%、RAM+15.5%）与联合训练模型（16.1%）、单专家模型的TGC无统计显著差异（McNemar p≥0.56）；两个专家的任务向量近正交，余弦相似度仅0.06~0.10，符号一致率仅51.9%（接近随机），支持重叠率却达65%，方向与支持完全解耦，导致复杂合并算法退化为简单平均。
**最值得记住的结论**：当多任务的LoRA微调任务向量近正交时，模型合并效果可媲美联合多任务训练，且无需复杂合并策略
