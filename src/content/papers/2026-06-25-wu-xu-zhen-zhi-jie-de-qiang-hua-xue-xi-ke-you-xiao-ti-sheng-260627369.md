---
title: Reinforcement Learning without Ground-Truth Solutions can Improve LLMs
title_zh: 无需真值解的强化学习可有效提升大语言模型能力
authors:
- Yingyu Lin
- Qiyue Gao
- Nikki Lijing Kuang
- Xunpeng Huang
- Kun Zhou
- Tongtong Liang
- Zhewei Yao
- Yi-An Ma
- Yuxiong He
affiliations:
- University of California, San Diego
- Snowflake AI Research
arxiv_id: '2606.27369'
url: https://arxiv.org/abs/2606.27369
pdf_url: https://arxiv.org/pdf/2606.27369
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 大语言模型 · 无真值强化学习训练
tags:
- Reinforcement-Learning
- RLVR
- GRPO
- Reward-Shaping
- Ground-Truth-Free
- LLM-Training
one_liner: 提出RiVER排序诱导可验证RL框架，用无真值优化任务训练LLM并实现跨任务迁移
practical_value: '- 奖励塑形trick可直接复用：针对无真值、分数尺度不一的业务场景（如不同query下的推荐收益、不同类目下的转化评分、Agent任务的连续质量评分），用「实例内排序+赢家加权」替代原始分数归一化做GRPO/PPO的奖励，可解决尺度主导和高频次优解主导问题，训练更稳定

  - 无真值RL数据构造范式：只要有可执行的评估器（如推荐离线仿真器、营销文案的转化率预估器、Agent任务的校验逻辑），就能通过同组采样候选的相对排序构造自监督RL训练信号，无需人工标注最优解，大幅降低训练数据成本

  - 跨任务迁移启示：用开放优化类任务（如多目标推荐策略优化、营销资源分配）做RL训练，只要奖励校准得当，不仅能提升任务本身表现，还可能迁移提升Agent在其他明确规则任务（如订单跟进、优惠券核销）上的推理能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
传统RLVR依赖真值答案生成二元奖励，仅适用于有明确标准答案的任务，但大量真实优化场景（如算法设计、路径规划）没有唯一最优解，仅能通过可执行评估器得到连续质量评分。直接用原始分数做RL存在两个核心问题：一是不同实例的分数尺度差异大，大尺度实例会主导策略更新（scale dominance）；二是高频次优解的梯度总和易超过稀有最优解，导致模型无法学到最优策略（frequency dominance）。

**方法关键点**
- 基于GRPO构建RiVER框架，无需任何真值解，仅依靠「可行性校验+目标分数计算」的可执行评估器提供监督信号
- 实例-wise排名：每个测试实例内单独对候选解排序，采用平均并列排名规则，彻底消除跨实例的分数尺度差异
- 赢家加权奖励塑形：无效解奖励-1，同组最优解奖励1，其余有效解映射到[-0.5, 0.5]区间，既拉开最优解梯度权重，又保留中间解的细粒度监督
- 多实例奖励取平均后直接作为GRPO优势值，无需额外归一化

**关键实验**
训练集为12个无真值的AHC启发式编程竞赛任务，基线包含5种不同奖励设计方案，backbone覆盖Qwen3-8B、GLM-Z1-9B-0414。核心结果：ALE-Bench评分上，两个backbone分别提升142、157分，排名百分位下降8.9%、9.4%；在完全不相关的精确解编程基准（LiveCodeBench、USACO）上，平均准确率分别提升2.4%、3.5%，是唯一能同时提升两类任务的方法，其余基线均存在精确解任务性能下降的问题。增益集中在中高难度题目，说明提升的是深层推理能力。

**最值得记住的一句话**
没有真值的开放优化任务，只要奖励校准得当，不仅可用于LLM训练，还能迁移提升通用推理能力，是低成本扩展RL训练数据的重要方向。
