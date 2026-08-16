---
title: 'Deliberate Practice: Learning Robot Skills under a Budget'
title_zh: 《刻意练习：有限练习预算下的机器人技能学习方法》
authors:
- Shivam Vats
- Sudarshan Harithas
- Mete Tuluhan Akbulut
- Arvind Raghunathan
- George Konidaris
affiliations:
- Brown University
- Mitsubishi Electric Research Laboratories
arxiv_id: '2608.13415'
url: https://arxiv.org/abs/2608.13415
pdf_url: https://arxiv.org/pdf/2608.13415
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 有限预算下的主动技能优化方法
tags:
- Active Learning
- Budget Optimization
- Bilinear Programming
- Skill Learning
- Sequential Decision Making
one_liner: 提出预算最优的主动技能学习算法Deliberate Practice，通过双线性规划实现有限练习资源下收益最大化的技能分配
practical_value: '- 多任务/多场景训练的优先级分配场景可复用预算最优分配思路，例如推荐系统有限训练算力下的多业务迭代优先级规划

  - 双线性规划求解组合技能收益的方法可迁移到Agent复杂任务拆解后的子任务训练资源分配场景

  - 可借鉴「技能掌握成本+解锁后续收益」双维度评估逻辑，优化大模型Agent工具调用能力的迭代优先级'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前机器人预训练策略无法覆盖全部真实场景，而部署阶段可用于练习的时间/算力预算极其有限，现有RL算法样本效率低，无法适配预算约束下的技能自主学习需求。

### 方法关键点
1. 提出Deliberate Practice (DP)主动学习算法，同时估算技能掌握所需时间、技能解锁的任务计划累计收益两个核心指标，输出可证明预算最优的练习资源分配方案；
2. 设计双线性规划求解逻辑，解决大预算下组合技能计划推理复杂度爆炸的问题，可直接调用现有商用求解器完成精确计算。

### 关键结果
在长序列操控任务的仿真和真实世界实验中，DP可最优利用有限练习时间获取有效策略，显著提升长horizon规划效果。
