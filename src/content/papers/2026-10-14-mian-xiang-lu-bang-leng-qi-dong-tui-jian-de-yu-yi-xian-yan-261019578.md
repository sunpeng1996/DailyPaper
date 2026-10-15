---
title: 'Bridging the Topological Divide: Dual-Branch Graph Distillation with Semantic
  Priors for Robust Cold-Start Recommendation'
title_zh: 面向鲁棒冷启动推荐的语义先验双分支图蒸馏框架
authors:
- Yuanfeng Qiu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.19578'
url: https://arxiv.org/abs/2610.19578
pdf_url: https://arxiv.org/pdf/2610.19578
published: '2026-10-14'
collected: '2026-10-15'
category: RecSys
direction: 冷启动推荐 · 图知识蒸馏
tags:
- Cold-Start Recommendation
- Graph Collaborative Filtering
- Knowledge Distillation
- Semantic Prior
- LightGCN
one_liner: 提出双分支图蒸馏框架DualGCN，在不损失暖启性能的前提下显著提升严格冷启推荐效果
practical_value: '- 电商新物品召回可直接复用双分支解耦训练范式：基于现有LightGCN链路改造teacher分支，新增语义student分支做蒸馏，无需改动现有线上暖启推理逻辑，冷启新物品仅需过student分支生成embedding即可入召回库

  - 跨模态对齐蒸馏放弃MSE/InfoNCE损失，改用无量级约束的余弦损失，避免冷启物品拟合暖启物品的流行度偏置，实测冷启Recall@20可提升5%以上

  - 推理阶段复用动态范数校准trick：定时计算全量暖启物品embedding的平均L2范数，冷启物品的student输出归一化后乘以该范数，可消除量级差异导致的检索排序偏差

  - 现有GCF训练可直接加入冻结的语义先验作为初始化锚，无需改动模型结构即可提升稀疏暖启场景的推荐精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
图协同过滤（GCF）是电商/内容平台召回阶段的主流技术，但严格冷启物品无历史交互、无预训练ID embedding，拓扑完全孤立，传统GCF的Recall@20暴跌97%以上；现有融合语义特征的方案通常依赖复杂融合模块，破坏协同信号纯度导致暖启性能下降，亟需兼顾冷启效果、暖启精度和工程轻量化的解决方案。
### 方法关键点
- 双分支架构：teacher分支在GCF初始化阶段加入冻结的物品语义先验（预训练文本特征降维后做锚），训练得到稳定的协同空间，既保留拓扑交互信号又锚定语义分布
- 解耦两阶段训练：第一阶段仅优化teacher分支的ID embedding和语义先验权重，用BPR loss收敛；第二阶段冻结teacher所有参数，用余弦蒸馏loss训练语义student分支的残差映射网络，将静态语义特征对齐到协同空间
- 动态范数重构推理：冷启物品用student分支输出的单位向量，乘以暖启物品embedding的平均L2范数，统一全局检索空间的量级分布，消除几何偏差
### 关键结果
在Amazon-Books、Electronics、Sports三个公开数据集上对比LightGCN、DropoutNet、MetaEmbedding等SOTA基线：
1. 暖启场景下Recall@20最高比LightGCN提升39.7%，暖启整体精度损失小于0.5%
2. 严格冷启场景下Recall@20最高比DropoutNet提升20.8%，比纯ID GCF提升35倍以上

> 最值得记住的结论：冷启语义对齐的核心是匹配协同空间的方向而非绝对值，轻量余弦蒸馏方案可在完全不改造现有GCF召回链路的前提下解决新物品冷启问题
