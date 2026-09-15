---
title: 'ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation'
title_zh: ReMoMask-2：基于隐空间检索增强的掩码动作生成
authors:
- Yiran Wang
- Zeyu Zhang
- Ling Shao
- Hao Tang
arxiv_id: '2609.08365'
url: https://arxiv.org/abs/2609.08365
pdf_url: https://arxiv.org/pdf/2609.08365
published: '2026-09-07'
collected: '2026-09-15'
category: Other
direction: 文本生成动作 · 检索增强生成优化
tags:
- RAG
- Text-to-Motion
- Contrastive Learning
- Latent Space
- Masked Generation
one_liner: 推出结构感知RAG框架及隐空间优化版ReMoMask-2，刷新文本生成动作领域SOTA
practical_value: '- RAG检索库直接构建在生成器预量化隐空间的设计思路，可迁移至生成式推荐RAG架构，降低检索与生成模块的表征对齐成本

  - 层级双向动量对比学习对齐全局+细粒度特征的方法，可复用在多模态商品/内容检索召回场景，提升检索精度

  - 基于语义相关性的自适应掩码训练策略，可用于优化生成式推荐模型，提升生成结果与用户需求的细粒度对齐能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有检索增强文本生成动作（RAG-T2M）存在两个核心痛点：① 粗粒度检索与融合机制忽略人体动作的层级时空拓扑结构，细粒度对齐能力差；② 检索结果所处的语义空间与生成器隐空间存在表征Gap，限制生成质量。
### 方法关键点
1. 结构感知RAG框架ReMoMask搭配层级双向动量（HBM）对比学习对齐全局/部件级特征与文本，语义时空注意力（SSTA）实现拓扑感知融合，拓扑结构掩码（TSM）自适应掩码训练强化细粒度接地能力。
2. 优化版本ReMoMask-2直接在生成器预量化隐空间构建检索库，通过从检索器蒸馏的轻量投影器对齐文本查询，消除检索-生成表征Gap。
### 关键结果
文本到动作检索精度达SOTA，ReMoMask-2在KIT-ML、SnapMoGen数据集上取得最低FID，单阶段推理速度超过原版两阶段ReMoMask。
