---
title: 'RHOPE: LLM-Augmented Adaptive Experimental Design with Complex Contextual
  Information'
title_zh: RHOPE：融合LLM的复杂上下文自适应实验设计框架
authors:
- Bowen Shi
- Bo Li
affiliations:
- Tsinghua University
arxiv_id: '2611.33767'
url: https://arxiv.org/abs/2611.33767
pdf_url: https://arxiv.org/pdf/2611.33767
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM增强自适应实验设计
tags:
- LLM
- Adaptive Experimentation
- Bayesian Framework
- Proxy Outcome
- MDP
one_liner: 提出融合LLM代理输出的贝叶斯自适应实验框架RHOPE，提升有限预算下最优策略识别效率
practical_value: '- 推荐/广告策略AB实验优化场景，可先用LLM对非结构化上下文（用户评论、商品文案）生成代理指标，提前预判策略效果，减少真实实验流量消耗

  - 有限流量预算下的多策略择优（新召回/排序策略选型），可参考RHOPE的MDP动态分配逻辑，给表现更优的策略倾斜更多流量，提升实验效率

  - 小流量实验效果评估可引入LLM生成的proxy outcome做样本增强，提升指标估计精度，降低假阳/假阴概率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有自适应实验设计难以有效利用非结构化/高维上下文信息，有限预算下最优策略（臂）识别的精度和效率不足，无法满足多策略快速迭代的需求。
### 方法关键点
1. 用LLM将复杂上下文转换为proxy outcome，从两个维度利用代理信息：作为样本增强数据提升效果估计精度，在每次实验资源分配前先获取代理结果作为先验信息
2. 提出RHOPE贝叶斯自适应实验框架，将有限批次实验设计建模为后验MDP，融合真实实验结果与LLM代理结果优化资源分配
### 关键结果
合成实验与GDSC半合成实验验证：样本增强带来的精度提升贡献了绝大多数收益，提前获取先验信息的增益相对较小；代理信息的有效性、矩估计精度是影响最终效果的核心因素
