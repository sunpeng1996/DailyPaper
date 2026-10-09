---
title: Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in
  a Long-Running Game Agent Competition
title_zh: AI Agent能否登顶？长期游戏竞赛场景下的启发式学习效果评估
authors:
- Kaisen Yang
- Qingle Liu
- Kejin Wang
- Yicheng Zhao
- Jieming Li
- Shenghan Zheng
- Ruize Yang
- Bojun Yang
- Heng Gong
- Xiang Gao
affiliations:
- Tsinghua University Department of Computer Science and Technology
- Tsinghua University College of AI
arxiv_id: '2610.12341'
url: https://arxiv.org/abs/2610.12341
pdf_url: https://arxiv.org/pdf/2610.12341
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 对抗启发式学习性能评测
tags:
- Heuristic Learning
- Adversarial Agent
- Code as Policy
- Benchmark
- Policy Optimization
one_liner: 提出对抗启发式学习AHL范式与AAArena基准，验证固定权重下Agent迭代代码优化策略的能力
practical_value: '- 可复用「Code as Policy」思路，将推荐/广告的排序/出价策略抽象为可编辑代码，由Agent基于业务反馈自动迭代，无需微调大模型权重，降低策略迭代成本

  - 借鉴“小流量验证+全量评估”的两级迭代流程：先用小流量AB test（对应小匹配）获取稠密反馈验证策略假设，再全量跑通评测（对应全池评估）确认效果，平衡迭代效率和评估准确性

  - 对抗类业务（如竞价广告、电商流量抢占、反作弊）可引入off-policy replay学习对手的历史行为数据，无需获取对手策略代码即可突破自身策略瓶颈

  - 复杂规则场景下优先做规则拆解降维，实验显示规则复杂度越高Agent优化效果越差，降低规则理解成本可显著提升Agent迭代成功率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
对抗游戏一直是AI能力验证的核心场景，但传统强化学习依赖海量样本与梯度更新，在动态对抗、少交互的场景下策略适配难度大；现有基于大模型的Agent迭代多依赖微调，可解释性差、可控性弱，亟需探索固定权重下的可解释策略迭代范式。
### 方法关键点
- 形式化**Adversarial Heuristic Learning (AHL)** 范式：固定大模型权重，Agent通过解读规则、分析对战回放、迭代优化可执行代码形式的策略，全程无需梯度更新，策略天然可解释可编辑
- 搭建**AAArena** 评测基准：包含12款真实对抗游戏、1920份归档人类策略代码，模拟真实竞赛流程，设置两类反馈通道：小匹配（可选对手，返回稠密回放）用于验证策略假设，全池评估（返回全榜Elo、排名）用于确认效果，严格限制匹配/评估预算
### 关键结果
对比7种模型+工具链配置，在默认128次小匹配、16次全量评估的预算下：
- Opus5.5 + Claude Code 组合在12款游戏中拿到6个金牌（排名第一），其余6款高复杂度游戏无任何配置能登顶
- 规则复杂度与性能强负相关：6款低规则复杂度游戏中5款被AI登顶，6款高复杂度游戏仅1款被AI登顶
- 对手选择、稠密反馈、自身/他人的off-policy回放均能显著提升策略迭代效率
### 核心结论
固定大模型权重下，Agent通过迭代可解释的代码策略完全可以在特定任务上超越人类最优水平，复杂规则理解是当前的主要瓶颈
