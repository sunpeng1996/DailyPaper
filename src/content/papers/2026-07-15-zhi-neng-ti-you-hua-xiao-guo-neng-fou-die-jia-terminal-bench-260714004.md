---
title: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench
  2.0
title_zh: 智能体优化效果能否叠加？Terminal-Bench 2.0下的持续学习评估
authors:
- Wenxiao Wang
- Priyatham Kattakinda
- Soheil Feizi
affiliations:
- RELAI.ai
arxiv_id: '2607.14004'
url: https://arxiv.org/abs/2607.14004
pdf_url: https://arxiv.org/pdf/2607.14004
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 持续优化 效果可叠加性评估
tags:
- Agent-Optimization
- Continual-Learning
- Terminal-Bench
- Regression-Control
- Catastrophic-Forgetting
one_liner: 提出两阶段持续学习评估协议，验证环内回归控制是智能体优化收益可叠加的核心条件
practical_value: '- 优化线上导购Agent、推荐话术生成Agent时，不要仅参考单次静态评测结果，必须加入回归校验环节，避免新功能迭代导致旧场景效果下跌

  - 可借鉴RELAI-VCL的环内回归约束设计，在Agent迭代的候选搜索环节就直接丢弃会导致已上线场景效果衰退的方案，远低于事后回滚的业务损失成本

  - 做Agent迭代效果评估时，可复用两阶段评测框架：先在旧任务集优化，再测跨新任务泛化性，最后测新旧任务联合优化的叠加效果，避免静态评测过拟合'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前主流Agent优化方法都仅在固定静态基准下评测单次优化效果，完全无法匹配生产环境的真实场景：线上Agent需要随业务迭代反复优化、新增任务，多次优化的收益是否可叠加、不会出现优化新任务就遗忘旧能力的灾难性遗忘问题，是Agent落地必须解决的核心痛点。

### 方法关键点
- 设计两阶段持续学习评测协议：Phase1在初始任务集T1优化Agent，评测T1上的静态优化效果、以及新增任务集T2后的跨域泛化效果；Phase2在T1+T2联合任务集上继续优化，评测持续优化的收益叠加能力，用终身平均通过率作为综合指标。
- 控制变量对比三类主流Agent Harness优化方法：GEPA（反射式进化提示优化）、Meta Harness（代码级Harness搜索优化）、RELAI-VCL（带环内回归控制的持续学习优化），三类方法共用底层GPT-5.5、每阶段200次rollout预算。
- RELAI-VCL核心设计是在优化搜索环节内置无回归约束：任何候选方案如果提升新任务效果但导致旧已解决任务效果下跌，直接在搜索过程中丢弃，而非事后校验。

### 关键实验
基于Terminal-Bench 2.0的22个硬难度终端任务，T1含12个任务，T2含10个任务。结果显示：静态Phase1下三类方法均超过基线58.7%的通过率，RELAI-VCL的终身平均通过率达76.4%，领先GEPA的66.0%、Meta Harness的64.6%；是唯一同时实现正迁移到新任务、二次优化后收益继续提升的方法，GEPA过拟合旧任务导致迁移效果低于基线，Meta Harness泛化性好但二次优化停滞。

**最值得记住的一句话：** Agent优化收益要实现可叠加，必须将回归控制内置到优化搜索循环内，而不是仅作为事后校验环节。
