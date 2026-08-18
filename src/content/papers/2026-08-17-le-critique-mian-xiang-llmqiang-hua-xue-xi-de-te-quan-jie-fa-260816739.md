---
title: 'Le Critique: Privileged Value Functions for LLM Reinforcement Learning'
title_zh: Le Critique：面向LLM强化学习的特权价值函数优化方法
authors:
- Siddarth Venkatraman
- Matthieu Dinot
- Laurence Aitchison
affiliations:
- Mistral AI
- Mila – Quebec AI Institute
- Université de Montréal
arxiv_id: '2608.16739'
url: https://arxiv.org/abs/2608.16739
pdf_url: https://arxiv.org/pdf/2608.16739
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: LLM强化学习 · 价值函数优化
tags:
- RLHF
- Value Function
- GRPO
- Reinforcement Learning
- LLM Training
one_liner: 提出特权价值函数PVF与自适应基线TETHER，优化LLM强化学习的梯度估计与训练效果
practical_value: '- 电商/推荐系统做RL排序、Agent做RL对齐时，可引入PVF思路：给价值函数喂仅训练时可用的特权信息（如推荐场景真实转化标签、Agent任务标准答案），不改变策略目标的前提下降低梯度方差，提升训练效率

  - 现有GRPO pipeline可低成本接入TETHER自适应基线：无需大幅改动架构，自动在组基线和价值基线间插值，初期用稳定的GRPO组基线，后期价值函数拟合好后切换到token级价值信号，降低迁移风险

  - 长序列多轮推荐、多步Agent任务中优先用PVF+TETHER组合，相比纯GRPO可减少straggler问题，降低off-policy程度，提升长序列credit分配效果

  - 工程上可复用论文开源的异步价值函数训练架构，价值训练单独走回放缓冲，不阻塞策略训练主流程，提升RL训练整体吞吐量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM RL主流的GRPO等无批评家方法依赖多采样分组计算优势，仅能提供序列级credit，存在拖尾样本降低吞吐、off-policy程度高的问题；传统价值函数虽能提供token级优势，但拟合效果不稳定、工程成本高，实际落地难度大，亟需兼顾两者优势的优化方案。

### 方法关键点
1. 提出**Privileged Value Functions（PVF）**：允许价值函数引入策略无法访问的训练时特权信息（如标准答案、同组其他样本的轨迹与奖励、评分规则等），满足无偏条件的前提下大幅提升价值预测准确率，降低梯度方差
2. 提出**TETHER**自适应基线：通过线性组合留一法组基线与token级价值基线，自适应拟合混合系数ρ，自动在两种基线的优势间插值，初期优先用稳定的组基线，随价值函数精度提升逐渐切换到价值基线
3. 工程实现异步价值函数训练架构，价值训练走独立回放缓冲，不阻塞策略主训练流程，提升整体吞吐量

### 关键结果
在Reasoning Gym、CodeIO、Sudoku、MiniF2F四类推理任务上对比MEAN（GRPO组基线）、普通VF基线：PVF在所有任务上效果最优，Sudoku任务上相比普通VF奖励提升39%，CodeIO任务上相比GRPO提升5%；TETHER在所有任务上优于普通VF，在Reasoning Gym和MiniF2F上超过GRPO，Sudoku任务上相比普通VF缩小与GRPO的差距60%以上。

最值得记住的一句话：价值函数引入训练时特权信息不会改变策略优化目标，是比自蒸馏更稳定的梯度方差降低手段，TETHER为现有GRPO pipeline提供了低风险接入价值函数的路径。
