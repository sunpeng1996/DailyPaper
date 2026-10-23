---
title: 'Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement
  Learning'
title_zh: 面向智能体强化学习的双世界信用分配方法TWICE
authors:
- Zeropy Surio
- Tobias Engel
- Mei-Lin Chou
- Anika Raman
- Samuel Okafor
affiliations:
- University of Sheffield
- Carnegie Mellon University
- University of Michigan
arxiv_id: '2610.31544'
url: https://arxiv.org/abs/2610.31544
pdf_url: https://arxiv.org/pdf/2610.31544
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent强化学习 · 细粒度信用分配
tags:
- Reinforcement Learning
- Credit Assignment
- Counterfactual
- Gumbel Noise
- Search Agent
one_liner: 通过共享下游采样噪声构造反事实双世界，大幅降低Agent RL信用分配的方差与训练成本
practical_value: '- 电商/搜索Agent做RL微调时，可复用keyed Gumbel噪声方案构造反事实轨迹，在低额外成本下降低信用分配噪声，提升多轮检索、多轮推荐query生成等多步决策的训练效果

  - 对于确定性工具（固定召回池检索、推荐排序链路）的Agent场景，可直接复用TWICE的平方根预算分配规则，优先给结果波动大的决策分支分配计算资源，资源利用率远高于均匀分支

  - 现有GRPO/PPO训练的Agent可直接叠加TWICE的细粒度信用项，无需修改原有损失函数，也无需改动上线Actor模型，迁移成本极低，适合业务快速迭代'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agentic RL仅给完整episode分配最终奖励，传统反事实分支方法的下游采样噪声独立，导致结果差异混合了决策效果与后续运气，信用分配方差高、样本效率差，微小决策效果差异需要极多样本才能检测，训练成本居高不下。

### 方法关键点
1. 利用Agent搜索场景下检索、语料、打分模块的确定性，按(episode, turn, line, position)键值绑定Gumbel噪声，构造反事实双世界：仅修改单步决策，下游采样噪声完全复用真实轨迹的噪声，隔离决策的单独影响
2. 双世界结果差直接作为步级优势，与GRPO的episode级优势加权融合做策略更新，训练完成后仅部署Actor即可，无额外推理开销
3. 采用平方根预算分配规则，优先给预测结果分歧大、生成成本低的决策分配反事实分支配额，用Horvitz-Thompson估计保证无偏

### 关键实验
在7个QA基准（含单跳、多跳）上，基于Qwen2.5-3B/7B backbone对比9种基线：TWICE平均Exact Match比GRPO高5.3/4.5个点，比最优基线AT2PO高1.7个点；错误信用符号占比从CRR的21.7%降到6.9%，比VinePPO少68%的辅助token开销。

最值得记住的一句话：对于工具可重放的Agent场景，共享下游噪声的反事实分支能将信用估计的样本复杂度从O(Δ⁻²)降到O(Δ⁻¹)，极低迁移成本即可大幅提升RL训练效率
