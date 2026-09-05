---
title: Statistical Feature Augmentation for Anomaly Detection in Dynamic Graphs
title_zh: 动态图异常检测的统计特征增强方法
authors:
- Philipp Schlinge
- Jean-Luc Schnipper
- Martin Atzmueller
affiliations:
- Osnabrück University
- German Research Centre for Artificial Intelligence (DFKI)
arxiv_id: '2609.02965'
url: https://arxiv.org/abs/2609.02965
pdf_url: https://arxiv.org/pdf/2609.02965
published: '2026-09-02'
collected: '2026-09-05'
category: Other
direction: 动态图异常检测 · 统计特征增强
tags:
- Dynamic Graph
- Anomaly Detection
- Feature Augmentation
- Behavioral Signal
- Temporal Interaction
one_liner: 为动态图异常检测显式编码交互统计特征，跨7类模型3个数据集稳定提升检测性能
practical_value: '- 电商刷单、虚假评论等用户行为动态图异常检测场景，可直接复用该方案，将交互频次、时间间隔惯性等统计特征拼接入模型输入，无需改动架构即可涨点

  - 做推荐系统黑盒模型可解释性分析时，可参考该方法将业务统计特征作为独立输入维度，便于事后归因不同行为特征对预测结果的贡献权重

  - 处理连续时间用户行为流数据时，不要完全依赖端到端模型隐式学习短周期信号，显式加入统计特征的投入产出比远高于调优模型结构'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有动态图深度学习模型很难从原始事件流中直接学习到发送强度、交互惯性等短期行为交互信号，无法同时高效捕捉时序结构与特征信息，限制了异常检测等下游任务的表现。
### 方法关键点
提出统计特征增强方案，无需改动原有模型结构，直接将用户/节点的行为交互统计量显式编码到输入特征空间，同时适配连续时间、离散时间两类动态图架构；每个统计特征独占一个输入维度，支持后续细粒度的行为重要性归因分析。
### 关键结果
在Reddit、Wikipedia、MOOC三个真实世界数据集上验证，覆盖7种主流动态图模型，相比仅用原始embedding训练的基线，该增强方案可稳定提升异常检测性能，无额外模型适配成本。
