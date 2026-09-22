---
title: 'G-NAC: Graph Neural Automata Clustering via Emergent Domain Formation'
title_zh: G-NAC：基于涌现域形成的图神经元胞自动机聚类方法
authors:
- Keith Miller
- Tristan Crawford
arxiv_id: '2609.24823'
url: https://arxiv.org/abs/2609.24823
pdf_url: https://arxiv.org/pdf/2609.24823
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 无监督图聚类 · 跨规模低资源适配
tags:
- Graph Clustering
- Unsupervised Learning
- GNN
- Cellular Automata
- Transfer Learning
one_liner: 提出无监督图神经元胞自动机聚类方法G-NAC，性能比肩SOTA且支持跨规模低损失迁移
practical_value: '- 可复用G-NAC近线性复杂度的大规模图聚类能力，适配电商千万级用户/商品无标注分群需求，降低训练与显存开销

  - 小图训练规则迁移大图的特性，可基于小样本用户分群任务训练模型直接迁移到全量数据集，大幅节省训练成本

  - 抗边删除噪声的鲁棒性设计，可直接用于含噪声交互的用户行为图分群，降低行为数据预处理的过滤成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有聚类方法普遍存在大规模数据下复杂度高、跨场景迁移性弱、对噪声图鲁棒性不足的问题，难以适配工业界大规模无标注样本分群需求。
### 方法关键点
无监督聚类框架G-NAC将每个观测映射为固定邻接图上的元胞，通过共享循环图神经元胞规则经局部交互演化隐域状态，结合图平滑度、方差、协方差等正则项，将演化后的关系状态转换为基于秩的稀疏谱亲和度完成分群。
### 关键结果
在57个基准数据集的73个聚类任务上平均ARI达0.7951，比肩SOTA方法Genie（0.7941），优于其余基线；5千至10万节点规模下，训练时间、GPU显存近似线性增长（缩放指数分别为1.02、0.99）；小图训练的迁移规则在10万节点目标图上ARI损失不到0.009。
