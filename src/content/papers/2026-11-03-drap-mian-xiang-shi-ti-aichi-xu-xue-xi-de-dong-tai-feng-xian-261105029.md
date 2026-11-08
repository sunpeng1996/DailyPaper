---
title: 'DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical
  AI'
title_zh: DRAP：面向实体AI持续学习的动态风险自适应可塑性方法
authors:
- Oswaldo Ludwig
arxiv_id: '2611.05029'
url: https://arxiv.org/abs/2611.05029
pdf_url: https://arxiv.org/pdf/2611.05029
published: '2026-11-03'
collected: '2026-11-08'
category: Agent
direction: 具身Agent 无回放持续学习优化
tags:
- Continual Learning
- Embodied Agent
- VLA
- Catastrophic Forgetting
- Adaptive Learning Rate
one_liner: 提出无回放持续学习方法DRAP，适配实体AI轨迹误差累积问题，缓解灾难性遗忘
practical_value: '- 风险加权梯度累积思路可迁移至推荐系统增量更新场景，对历史高价值特征对应的模型张量降低学习率，缓解用户旧兴趣/旧行为的遗忘

  - 自适应缩放AdamW各张量学习率的trick可直接复用到LLM/生成式推荐多任务增量微调，无需历史样本回放，降低存储计算开销

  - 基于状态转移矩阵最大奇异值估计扰动放大风险的方法，可借鉴到电商序列推荐场景，量化单步推荐偏差对后续转化的累积影响'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
实体AI持续学习存在轨迹误差累积问题，单步策略偏差会导致智能体偏移训练分布，最终触发闭环任务失败；传统持续学习方法多依赖样本回放，成本高且未考虑动态风险的影响。

### 方法关键点
1. 无回放设计，基于Lyapunov理论，用岭正则化局部线性模型的状态转移矩阵最大奇异值，独立于策略估计单步扰动放大风险
2. 每个任务结束后，累积风险加权的平方梯度到张量级重要性内存
3. 后续任务中用归一化的累积重要性缩放AdamW各张量的有效学习率，动态降低历史高敏感点对应模型组件的可塑性

### 关键结果
在OpenVLA固定子网络上验证，跨LIBERO Spatial/Object/Goal三个任务套件的无回放顺序适配中，相比标准AdamW微调、EWC方法，旧任务行为保留率大幅提升，同时新任务学习能力无显著下降
