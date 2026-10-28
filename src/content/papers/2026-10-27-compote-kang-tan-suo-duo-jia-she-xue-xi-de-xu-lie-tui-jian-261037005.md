---
title: 'Compote: Collapse-Resistant Multiple Hypothesis Learning For Sequential Recommendation'
title_zh: COMPOTE：抗坍缩多假设学习的序列推荐方法
authors:
- Louis Castres Saint Martin
- Clement Calauzenes
- Alain Rakotomamonjy
- Patrick Gallinari
affiliations:
- Criteo AI Lab
- Sorbonne Université
- CNRS
- ISIR
arxiv_id: '2610.37005'
url: https://arxiv.org/abs/2610.37005
pdf_url: https://arxiv.org/pdf/2610.37005
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 序列推荐 · 多兴趣建模 抗坍缩训练
tags:
- Sequential Recommendation
- Multi-Interest Learning
- Winner-Takes-All
- Head Collapse
- Transformer
one_liner: 提出带退火赢者通吃训练的多假设序列推荐框架，解决多头坍缩问题，性能优于全品类主流基线
practical_value: '- 存量多兴趣模型可直接复用退火WTA训练策略，从全头均匀监督逐步过渡到赢者通吃，无需额外加多样性正则项，减少调参成本

  - 推理阶段可直接用max cosine similarity替代带softmax的max pooling，无需计算全局归一化因子，完全兼容现有向量数据库检索链路，无性能损失

  - 理论证明多兴趣头数M的泛化误差仅随lnM增长，可根据业务场景适度增加头数（实测3-5最优），不会出现线性过拟合风险

  - 等参对比下多假设拆分比单头加深收益更高，序列推荐模型迭代时可优先尝试拆分多头加退火训练，而非盲目增大单头容量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
序列推荐的下一个物品预测本质是多模态分布，单个用户表征会平均多个潜在意图导致结果偏差；现有多兴趣模型普遍存在头坍缩问题，所有头学到的表征高度重合，多样性增益无法落地，性能甚至弱于同参单头模型。

### 方法关键点
- 架构：共享因果Transformer编码用户交互序列，最后一位表征拆分M个独立假设头，每个头输出对应兴趣的物品打分
- 训练：采用退火多选择学习损失，高温阶段所有头均匀更新，温度逐步降至0后过渡为纯赢者通吃（WTA），仅更新当前样本打分最高的头，强制头分工无额外多样性正则
- 推理：直接对M个头的cosine相似度取max排序，无需计算全局softmax归一化因子，完全兼容现有向量数据库检索链路

### 关键结果
在3个Amazon Reviews 2023数据集（乐器、工业科学、游戏）上对比14个主流基线（单兴趣、多兴趣、生成式推荐），COMPOTE在12个评测指标（H@5/H@10/N@5/N@10）中11项最优；对比最强生成式基线TIGER，N@5在工业科学数据集提升9.7%，游戏数据集提升9.6%，仅用item ID无需额外内容特征，推理为单前向pass无额外开销。

> 最值得记住的结论：多兴趣模型的核心瓶颈不是架构设计，而是训练阶段的头坍缩问题，退火WTA训练比任何人工设计的路由机制、多样性正则都更高效。
