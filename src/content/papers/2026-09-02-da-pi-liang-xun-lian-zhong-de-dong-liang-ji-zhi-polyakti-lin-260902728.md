---
title: 'Momentum in large-batch training: Polyak enlarges the critical batch size,
  Nesterov improves data efficiency'
title_zh: 大批量训练中的动量机制：Polyak提升临界批次，Nesterov优化数据效率
authors:
- Jia-Nan Wang
- Zixun Huang
- Kairui Li
- Lei Wu
affiliations:
- Peking University
- AI for Science Institute, Beijing
- University of Pennsylvania
arxiv_id: '2609.02728'
url: https://arxiv.org/abs/2609.02728
pdf_url: https://arxiv.org/pdf/2609.02728
published: '2026-09-02'
collected: '2026-09-04'
category: Training
direction: 大模型训练优化 · 动量机制调优
tags:
- LargeBatchTraining
- PolyakMomentum
- NesterovMomentum
- TrainingOptimization
- ScalingLaws
one_liner: 理论结合实验揭示Polyak、Nesterov动量在大批量训练中的作用机制与增益边界
practical_value: '- 训练大参数量推荐/多模态召回模型时，优先使用Polyak动量可放大临界批次大小，无需牺牲数据效率即可提升多卡并行训练速度

  - 超大批次训练场景（如万级别批次的LLM/Embedding预训练）下换用Nesterov动量，可抑制噪声积累，在固定数据预算下降低最终训练损失

  - 优化器调参时可参考论文给出的临界学习率公式，结合批次大小B和动量因子ρ快速确定学习率的合理区间，减少网格调参的算力成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
大批量训练是提升大模型训练效率的核心手段，但普遍存在稳定性差、数据效率随批次增大快速下降的问题，两类主流动量（Polyak、Nesterov）的适用场景缺乏量化理论指导。

### 方法关键点
以幂律核回归为可解分析框架，定义临界学习率作为训练稳定性的衡量指标，推导SGD、Polyak、Nesterov三类优化器的临界学习率与批次大小B、动量因子ρ的量化关系；在固定数据预算下优化最终训练风险，得到三阶段批次大小相图，明确不同动量的适用区间。

### 关键结果
- Polyak动量可放大临界批次大小，保持小批次的最优数据缩放指数，并行度提升无效果损失
- 超大批次场景下Nesterov动量的最终 excess risk 比SGD低约40%，数据效率显著更优
- 所有理论结论均在数值实验中得到完全验证
