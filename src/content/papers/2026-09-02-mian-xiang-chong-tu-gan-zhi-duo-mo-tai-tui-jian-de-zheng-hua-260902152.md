---
title: 'Beyond Modality Harmony: Orthogonal Purification and Topology-Guided MoE for
  Conflict-Aware Multimodal Recommendation'
title_zh: 面向冲突感知多模态推荐的正交纯化与拓扑引导MoE方法
authors:
- Jialin Liu
- Zhaorui Zhang
- Ray C. C. Cheung
affiliations:
- City University of Hong Kong
- The Hong Kong Polytechnic University
arxiv_id: '2609.02152'
url: https://arxiv.org/abs/2609.02152
pdf_url: https://arxiv.org/pdf/2609.02152
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 多模态推荐 · 噪声过滤与模态融合优化
tags:
- Multimodal Recommendation
- MoE
- Contrastive Learning
- GNN
- Denoising
one_liner: 提出OrthoRec框架解决多模态推荐中模态-拓扑冲突的噪声污染与融合零和瓶颈
practical_value: '- 多模态特征预处理可复用CGOP思路：以纯协同ID embedding为锚点，将模态特征拆分为平行/正交分量，自适应截断正交噪声同时保留L2
  norm，避免直接丢弃噪声导致的信息损失，尤其适配电商场景大量标题党、图货不符的商品特征

  - 模态融合层可替换为sigmoid门控的解耦路由MoE，打破传统softmax注意力的零和约束，支持多模态特征独立加权，避免视觉特征强势时压制文本语义的问题，适配电商商品图文价值不均衡的场景

  - 跨模态对比学习可引入安全加权机制：复用模态-协同冲突分动态调低冲突样本的对齐权重，避免强制对齐矛盾图文导致的表征扭曲，鲁棒性优于固定权重的对比损失

  - 冷启动场景可优先复用该框架：商品交互稀疏时，OrthoRec对多模态噪声的过滤能力能更安全地利用图文信息，冷启动商品Recall@20相对提升可达41%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐默认「模态和谐」假设，认为图文特征天然与用户交互行为一致，但真实场景普遍存在视觉标题党、图文语义 mismatch 等模态-拓扑冲突，盲目融合会污染纯协同表征空间，同时softmax融合的零和约束会压制有价值的弱模态信号，现有方案要么丢弃噪声损失信息要么强制对齐导致表征扭曲。

### 方法关键点
- 先提取纯协同锚点：仅用ID embedding跑LightGCN得到纯净的协同拓扑表征，作为几何参考基准
- 协同引导正交纯化（CGOP）：把原始图文特征投影到协同锚点上拆分为平行（共识语义）和正交（噪声+探索性语义）分量，用模态-协同余弦冲突分自适应缩放正交分量，最后做能量保持归一化，修正语义方向的同时保留特征原始L2 norm
- 拓扑感知路由MoE（TAR-MoE）：用协同锚点作为路由条件，每个模态用独立sigmoid门控计算加权系数，打破softmax零和约束，自主决定各纯化模态的注入尺度
- 安全对比学习（Safe-SSL）：复用CGOP的冲突分动态调整对比损失权重，冲突越高的图文对对齐权重越低，避免强制对齐矛盾样本导致的表征扭曲

### 关键结果
在3个Amazon公开数据集（Baby、Sports、Clothing）上对比16个SOTA基线，整体Recall@20相对最优基线最高提升6.55%，NDCG@20最高提升11.28%；在30%模态噪声注入下性能仅下降10.6%，优于基线的11.6%；冷启动商品（交互≤5）Recall@20相对基线最多提升41%。

### 核心结论
多模态信号不是免费午餐，模态融合前先做基于协同共识的噪声过滤、用解耦门控替代softmax融合，能大幅提升多模态推荐的鲁棒性和冷启动性能
