---
title: When Does On-Policy Interaction Help? Representational Tradeoffs in Value-Based
  Imitation Learning
title_zh: 基于价值的模仿学习中同策略交互的作用与表征权衡
authors:
- Luca Viano
- Antoine Moulin
- Audrey Huang
- Volkan Cevher
- Philip Amortila
- Dylan J. Foster
affiliations:
- EPFL
- UPF
- University of Illinois Urbana-Champaign
- UC Berkeley
- Microsoft
arxiv_id: '2607.29617'
url: https://arxiv.org/abs/2607.29617
pdf_url: https://arxiv.org/pdf/2607.29617
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 模仿学习 · 同策略交互优化
tags:
- Imitation Learning
- On-Policy
- Value-Based RL
- Agent Training
- Representation Learning
one_liner: 提出交互式价值模仿学习算法OVI，证明同策略交互可降低模仿学习表征要求，仅需拟合专家价值函数即可高效学习
practical_value: '- 小模型蒸馏大模型场景（如推荐系统小排序模型蒸馏大模型）可放弃直接拟合大模型输出分布，改为拟合专家价值函数，结合少量同策略交互的专家标注，大幅降低小模型容量要求

  - 多步决策任务（如电商导购Agent多轮对话、搜索多步query改写）可通过价值函数将全局最优拆解为每步局部决策，避免全局搜索的指数级复杂度

  - 离线模仿学习效果差时，优先补充同策略交互的标注数据而非盲目增加离线专家数据量，小模型拟合能力不足的场景下收益更显著'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统模仿学习（如Behavior Cloning）存在误差累积、性能平台问题，尤其是当学习者容量不足以拟合专家完整策略时（如小模型蒸馏大模型）表现退化明显；现有两种优化思路——同策略交互查询专家、基于价值的模仿学习，二者的协同机制和适用边界尚未被清晰解释，亟需明确交互在降低表征要求上的具体作用。

### 方法关键点
- 提出OVI（On-policy Value-based Imitation Learning）算法，采用分层min-max框架，每层先采样同策略状态查询专家动作，再交替更新价值函数和策略：价值函数层最大化专家动作与当前策略动作的价值差，策略层用softmax更新朝向高价值动作
- 理论证明仅需满足专家价值函数可被拟合（QπE-realizability）即可保证算法收敛，无需拟合专家完整策略，大幅降低表征要求
- 证明离线场景下仅靠价值函数可实现假设无法高效学习，同策略交互是必要条件

### 关键实验
在Gymnasium的4个经典控制环境测试，专家是宽度64的2层MLP，学习者宽度从2到64变化，对比BC、DAgger、SPOIL三个baseline；当学习者宽度仅为专家的1/32时，OVI的归一化return比DAgger高30%以上，比离线价值方法SPOIL高45%以上，小容量模型下优势极显著。

**最值得记住的一句话**：同策略交互的核心价值不止是降低误差累积，更本质的是降低了模仿学习对学习者的表征要求，只需拟合价值函数就能达到接近专家的性能，无需完全复刻专家的决策分布。
