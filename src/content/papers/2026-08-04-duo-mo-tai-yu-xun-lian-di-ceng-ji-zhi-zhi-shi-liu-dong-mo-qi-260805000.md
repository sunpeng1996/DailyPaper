---
title: 'Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy,
  Early Unification, and Recipes'
title_zh: 多模态预训练底层机制：知识流动、模态协同、早期融合与训练配方
authors:
- Junlin Han
- Shengbang Tong
- David Fan
- Minghao Chen
- Philip Torr
- Filippos Kokkinos
- Mike Lewis
affiliations:
- FAIR, Meta
- Reality Labs, Meta
- University of Oxford
arxiv_id: '2608.05000'
url: https://arxiv.org/abs/2608.05000
pdf_url: https://arxiv.org/pdf/2608.05000
published: '2026-08-04'
collected: '2026-08-06'
category: Multimodal
direction: 多模态预训练 · 机制与训练优化
tags:
- Multimodal Pretraining
- MoE
- Modality Synergy
- Knowledge Transfer
- Efficient Training
one_liner: 系统性拆解多模态预训练模态交互机制，给出4项核心结论与低成本高效训练方案
practical_value: '- 做电商多模态商品理解、多模态生成式推荐预训练时，优先采用早期联合训练方案，避免延迟融合导致模型过度依赖商品标题等文本先验，漏学商品图视觉特征

  - 多模态模型架构可复用「共享注意力+共享归一化+模态专属FFN」组合，既能促进跨模态协同，又能降低模态竞争，且兼容不同视觉tokenizer，适配多模态召回/排序模型迭代

  - 参考论文高效预训练配方，可将多模态预训练算力成本压缩至原有5%，大幅降低中小团队落地多模态生成式推荐、商品文案生成的门槛'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态预训练的模态交互底层机制、架构与训练策略设计空间缺乏系统性实证支撑，业界暂无可复用的高效训练指导原则。
### 方法关键点
通过合成数据集、大规模真实数据集的对照实验，从四个维度拆解多模态预训练核心逻辑：
1. 知识流动：量化跨模态知识迁移的不对称性，语言、视觉理解是视觉生成的强先验；
2. 模态协同：数据复杂度决定模态是协同还是竞争，「共享注意力+共享归一化+模态专属FFN」架构可最大化协同效应，且适配不同视觉tokenizer；
3. 早期融合：极早期模态联合训练效果远优于后对齐、顺序训练，延迟融合会触发「视觉惰性」，导致模型过度依赖语言先验；
4. 训练配方：提炼低算力开销的预训练范式。
### 关键结果
在2T token上训练多组13.5B MoE模型验证所有结论，高效预训练配方仅用5%算力即可达到优秀的多模态生成性能
