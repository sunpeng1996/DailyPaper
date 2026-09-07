---
title: 'MURAL: Multimodal Uncertainty-aware Recommendation via Adaptive edge Learning'
title_zh: MURAL：基于自适应边学习的多模态不确定性感知推荐框架
authors:
- Ahmad Mousavi
- Majid Alikhani
- Yeon-Chang Lee
- Roberto Corizzo
- Yeganeh Abdollahinejad
affiliations:
- American University
- Independent Researcher
- Ulsan National Institute of Science and Technology
- Michigan State University
arxiv_id: '2609.04574'
url: https://arxiv.org/abs/2609.04574
pdf_url: https://arxiv.org/pdf/2609.04574
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 多模态推荐 · 图结构学习
tags:
- MultimodalRec
- GraphNeuralNetwork
- UncertaintyEstimation
- StructureLearning
- ContrastiveLearning
one_liner: 采用可微自适应拓扑发现与不确定性感知融合，解决多模态GNN推荐的结构刚性与语义脆弱问题，性能超越现有SOTA
practical_value: '- 多模态融合可借鉴UAF模块设计：为每个item的每个模态建模aleatoric uncertainty，用1/σ²加权特征，自动降权低质模态（如电商场景下的模糊主图、凑数的商品描述），无需人工调权重

  - 可学习图结构的低成本落地方案：用HNSW做ANN检索剪枝候选邻居，再用轻量MLP动态学习边权重，每10个epoch更新一次索引，复杂度O(NlogN)可支持千万级item规模的生产场景

  - 对比学习优化trick：模态对齐时对用户行为embedding加stopgrad，避免梯度泄露扭曲协同信号，在不引入复杂交叉注意力的前提下保证对齐稳定性

  - 抗噪优化可复用：为学到的邻接矩阵加熵正则，避免边权重塌缩为one-hot，能有效提升GNN消息传递的鲁棒性，适合数据噪声大的电商/短视频场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态GNN推荐存在两大瓶颈：一是结构刚性，依赖静态预计算的相似性图，无法适配动态变化的用户偏好，还易出现「镜像效应」，即模态图和交互图拓扑冗余，无法挖掘纯多模态空间的潜在item关联；二是语义脆弱，采用确定性融合策略，不区分模态噪声水平，低质模态会干扰协同信号，尤其在电商、短视频场景下模态质量差异极大（如短视频的背景音无区分度、商品描述冗余），传统方案效果受限。
### 方法关键点
- 自适应边学习（AEL）：采用「检索+精排」两阶段构建动态item图，第一阶段用HNSW ANN检索每个item的候选邻居，控制复杂度为O(NlogN)，每10个epoch更新一次索引；第二阶段用轻量MLP基于模态特征+行为embedding学习边权重，加熵正则避免邻接矩阵塌缩。
- 不确定性感知融合（UAF）：为每个item的每个模态建模aleatoric uncertainty σ，用α*(1/σ²)加权融合多模态特征，自动降权噪声大的模态信号。
- 稳定对齐策略：模态和行为对齐时对行为embedding加stopgrad避免梯度泄露，结合行为-模态、跨模态两种对比损失保证表征一致性。
### 关键实验
在TikTok、Amazon Baby、Amazon Sports三个公开基准数据集上，对比LightGCN、MMGCN、AlignRec、DiffCL等10个SOTA基线，MURAL在Recall@20上相对最优基线分别提升5.4%（TikTok：0.1221 vs 0.1158）、5.9%（Amazon Baby：0.1068 vs 0.1008）、4.1%（Amazon Sports：0.1173 vs 0.1127），NDCG@20对应提升10.4%、13.8%、8.4%，在20%模态特征被噪声污染的场景下性能仅下降2%以内，鲁棒性显著优于基线。
### 核心结论
多模态推荐的结构和语义瓶颈可以通过动态拓扑学习+不确定性加权的组合方案解决，无需引入扩散、复杂交叉注意力等heavy模块即可实现性能和效率的双重提升
