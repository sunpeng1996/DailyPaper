---
title: Multimodal Decoupling for Diversified Recommendation through Semantic and Structural
  Shaping
title_zh: 基于语义与结构塑形的多模态解耦多样化推荐框架
authors:
- Changran He
- Jiaming Wei
- Jianghong Ma
- Tianjun Wei
- Haijun Zhang
- Xiaofeng Zhang
affiliations:
- 哈尔滨工业大学（深圳）
- 南洋理工大学
- 深圳互联网信息协同重点实验室
- 香港城市大学深圳研究院
arxiv_id: '2610.26024'
url: https://arxiv.org/abs/2610.26024
pdf_url: https://arxiv.org/pdf/2610.26024
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 多模态推荐 · 准确率-多样性权衡优化
tags:
- Multimodal Recommendation
- Diversity
- Graph Neural Network
- Entropy Regularization
- Dimensional Collapse
one_liner: 提出MOSS多模态解耦推荐框架，从语义结构双维度优化推荐准确率与多样性权衡
practical_value: '- 多模态特征处理可复用Category-aware Embedding Selection思路，通过「全局方差+类别响应熵」打分筛选有效维度，避免直接使用预训练多模态特征导致的效果下降，同时降低后续运算量

  - Graph-based推荐缓解维度坍缩可引入Alternating Dual-Graph Propagation机制，交替在用户-物品交互图、多模态物品-物品图上传播，既能保留协同信号，又能丰富item语义表示，提升多样性

  - 优化准确率-多样性权衡可直接复用Entropy-based Diversity Regularization，对top-N推荐结果的类别分布加熵正则，无需修改排序主目标，即可低成本提升品类覆盖率，适合电商品类打散、内容平台多样性优化场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前推荐系统优化准确率时普遍存在结果过度集中问题，多模态信号常被作为ID embedding的辅助特征未有效利用，同时GNN类推荐模型存在表征维度坍缩、优化目标偏向热门品类的结构缺陷，导致准确率-多样性权衡难以兼顾，而多样性直接影响用户长期留存、长尾商品曝光，是电商/内容平台的核心优化目标。

### 方法关键点
- 用MLLM（Qwen2.5-VL-72B）将item多模态内容解耦为共享语义、视觉专属、文本专属三类表征，分别用于传播初始化与模态专属物品图构建
- 提出Category-aware Embedding Selection模块，结合维度全局方差（信息量）与类别响应熵（跨类平衡性）筛选高价值维度，作为图传播的item初始化表征
- 设计Alternating Dual-Graph Propagation机制，偶层在用户-物品交互图做协同传播，奇层在多模态物品-物品图做语义传播，缓解维度坍陷
- 新增Entropy-based Diversity Regularization，对每个用户top-20推荐结果的品类分布加负熵损失，优化品类曝光均衡性

### 关键实验
在Anime、Game两个公开数据集上对比LightGCN、SimGCL、Freedom、DGCN等8个基线，MOSS在多样性指标上领先最优基线：Anime数据集Coverage@10提升13.2%、Entropy@10提升12.8%；Game数据集Coverage@10提升30.3%、Entropy@10提升19.2%；同时准确率-多样性综合指标GM@10分别提升5.7%、21.1%，调优为准确率优先模式时精度也优于所有基线。

### 核心结论
推荐的准确率-多样性权衡本质是语义利用效率与表征结构坍缩的共同结果，通过多模态语义解耦+结构塑形可实现二者的同步提升，不需要牺牲一方换取另一方。
