---
title: The Role of Causality in Algorithmic Recourse
title_zh: 因果性在算法追索机制中的作用研究
authors:
- Srikanth Avasarala
- Varun Gupta
- Shahin Jabbari
- Saber Salehkaleybar
- Juba Ziani
affiliations:
- Georgia Institute of Technology
- Vector Institute
- Drexel University
- Leiden University
arxiv_id: '2607.28497'
url: https://arxiv.org/abs/2607.28497
pdf_url: https://arxiv.org/pdf/2607.28497
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 算法决策 · 因果反博弈机制设计
tags:
- Causality
- Algorithmic Recourse
- Performative Prediction
- Strategic Behavior
- Causal Inference
one_liner: 基于因果执行框架构建反博弈算法追索方案，避免用户刷分导致规则快速失效
practical_value: '- 电商平台给用户/商家发成长任务、权益获取规则时，可引入因果结构建模，区分任务是真的促进正向行为（如真实复购、提升服务质量）还是仅引导刷量博弈，降低规则失效速度

  - 面对用户/商家策略性行为导致的特征分布漂移问题，可参考本文迭代求解稳定均衡点的思路，减少模型反复重训的人力和算力成本

  - 高风险决策场景（如商家准入、信贷额度推荐、大促资源分配）的策略设计，可优先对齐因果结构，平衡短期体验和系统长期稳定性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有算法追索方案仅关注翻转模型预测结果，未区分建议是真正提升用户资质还是仅引导用户博弈刷分，易导致模型预测精度下降、规则随重训快速失效。
### 方法关键点
1. 提出因果执行框架建模追索行为的传播路径，通过结构因果模型捕捉特征间交互、特征修改对真实标签的影响；
2. 证明即使是标准凸损失下该问题仍为非凸优化，推导了执行稳定解的存在条件，可通过简单迭代动力学高效求解。
### 关键结果
在半合成及真实信贷数据集上，方案相比经验风险最小化基线效果更优，可大幅降低应对用户策略性行为导致分布漂移的模型重训频率，同时显著减少用户博弈动机。
