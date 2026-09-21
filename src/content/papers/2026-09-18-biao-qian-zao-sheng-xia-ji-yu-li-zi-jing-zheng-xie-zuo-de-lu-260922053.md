---
title: Particle Competition and Cooperation for Robust Graph Convolutional Network
  Learning Under Label Noise
title_zh: 标签噪声下基于粒子竞争协作的鲁棒图卷积网络学习框架
authors:
- Fabricio Breve
affiliations:
- São Paulo State University - UNESP
arxiv_id: '2609.22053'
url: https://arxiv.org/abs/2609.22053
pdf_url: https://arxiv.org/pdf/2609.22053
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 图模型训练 · 标签噪声鲁棒优化
tags:
- GCN
- Label Noise
- Label Refinement
- Robust Learning
- Graph Learning
one_liner: 提出PCC标签预提纯模块，在不修改GCN结构的前提下提升其标签噪声下的鲁棒性与运算效率
practical_value: '- 电商推荐场景中用户/物品标签存在噪声时（如用户行为标签误打、物品类目错标），可在GCN召回/排序模块前加PCC标签预提纯预处理，无需修改原有GCN结构即可提升效果

  - PCC模块支持用特征KNN补全图边再做标签修正，可迁移到电商稀疏用户行为图场景，补全边后做标签降噪的效果更稳定

  - 对算力敏感的线上推荐场景，优先选用PCC这类轻量预处理器，比同类抗噪方法训练/推理速度快很多，几乎无额外线上开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
GCN对标签噪声极度敏感，错误监督信号会沿图传播恶化节点表示学习效果，现有鲁棒GCN方法要么修改模型结构适配成本高、要么运算效率低难以落地。
### 方法关键点
1. PCC+GCN混合框架先通过PCC粒子竞争协作动力学识别可疑带标节点，提前对标签做保留/删除/重赋值的提纯处理，再喂入GCN训练，全程不修改GCN本身结构；
2. PCC阶段可基于特征KNN补全图边增强修正效果，GCN仍在原始图结构上训练避免引入偏差。
### 关键结果
在NoisyGL基准10个数据集上测试，常规噪声场景下比基线GCN平均精度高1.67个百分点，整体平均排名最优；实例依赖噪声场景下，在8/10数据集上是速度最快的鲁棒方法，精度与SOTA抗噪方法持平。
