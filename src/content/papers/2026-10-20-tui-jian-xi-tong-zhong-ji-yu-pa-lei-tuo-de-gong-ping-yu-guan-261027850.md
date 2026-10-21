---
title: Robustness Analysis of Pareto-based Joint Evaluation of Fairness and Relevance
  in Recommender Systems
title_zh: 推荐系统中基于帕累托的公平与相关性联合评估鲁棒性分析
authors:
- Theresia Veronika Rampisela
- Maria Maistro
- Tuukka Ruotsalo
- Christina Lioma
affiliations:
- University of Copenhagen, Denmark
- LUT University, Finland
arxiv_id: '2610.27850'
url: https://arxiv.org/abs/2610.27850
pdf_url: https://arxiv.org/pdf/2610.27850
published: '2026-10-20'
collected: '2026-10-21'
category: Eval
direction: 推荐系统评估 · 公平性与相关性权衡
tags:
- recommender_system
- fairness
- pareto_optimality
- evaluation_metric
- robustness
one_liner: 基于帕累托前沿距离的DPFR指标，实现推荐系统公平性与相关性的鲁棒联合评估
practical_value: '- 做推荐系统公平性与相关性多目标评估时，可直接复用DPFR框架，替代原有加权平均/单联合指标方案，避免评估失衡问题

  - 业务场景中可通过调整α参数灵活适配不同阶段的评估侧重：冷启动阶段调大α优先保障长尾商品公平曝光，大促阶段调小α优先保障推荐相关性

  - 多目标优化的模型选型阶段，可基于DPFR的距离值快速筛选符合业务权衡要求的最优模型，解决不同维度指标排名冲突的痛点

  - 帕累托前沿生成的Oracle2Fair算法可迁移至多目标重排模块，快速生成兼顾相关性与公平性的帕累托最优推荐候选集'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统评估存在两类缺陷：单独计算相关性、公平性指标会出现两个维度下模型排名冲突，无法直接选出综合最优方案；采用单一关联感知公平指标则往往对两个维度的评估失衡，无法反映模型在公平-相关性权衡上与理论最优解的真实差距。
### 方法关键点
- DPFR框架基于用户交互数据生成公平性与相关性的Pareto Frontier，覆盖两者的所有帕累托最优权衡点
- 支持通过α参数灵活调整公平与相关性的权重，计算待评估模型的（相关性、公平性）得分到前沿参考点的距离作为联合评估值，可兼容现有所有相关性、公平性指标
- 提供高效近似实现，通过采样Pareto Frontier上均匀分布的少量点降低计算开销，适配大规模工业数据集
### 关键实验
在6个公开数据集（电商、音乐、电影、视频等场景）上，基于4种主流推荐模型+3种公平感知重排器验证：现有联合评估指标与DPFR的相关性仅为0.2~0.4，无法作为帕累托最优视角下的可靠代理指标；DPFR的鲁棒性优于现有联合评估方法30%以上；高效近似版本仅需采样10个帕累托点即可达到与全量计算95%以上的一致性。
### 核心结论
简单平均相关性与公平性得分的评估方式会严重高估单一维度表现优秀的模型，基于帕累托最优前沿的距离计算是多目标联合评估的可靠方案。
