---
title: 'From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for
  VLM Rerankers'
title_zh: 面向VLM重排器的保排序视觉Token剪枝：从显著性到判别性
authors:
- Siyi Liu
- Hanjun Yang
- Chenchen Zhang
- Xiaorong Zhu
- Xinyu Zuo
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Junfu Pu
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- ARC Lab, Tencent
arxiv_id: '2609.00667'
url: https://arxiv.org/abs/2609.00667
pdf_url: https://arxiv.org/pdf/2609.00667
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 多模态重排 · VLM Token剪枝优化
tags:
- VLM
- Token Pruning
- Reranking
- Inference Optimization
- Training-Free
one_liner: 提出无需训练的RaDiCal保排序VLM Token剪枝框架，实现1.28-1.45倍近似无损推理提速
practical_value: '- 电商多模态商品重排场景可复用DTI设计逻辑，优先保留与query相关、跨候选集有区分度的视觉特征，替代纯视觉显著性剪枝，解决同类商品重排精度下降问题

  - 无需训练的剪枝流程可直接落地，通过归一化注意力熵动态校准各层saliency信任权重、自动选择剪枝层，无需针对不同品类/场景单独调参，适配性强

  - 线上部署VLM重排器时，RaDiCal在20% Token保留率下几乎无损重排精度，可降低39~45% FLOPs，获得1.28~1.45倍端到端提速，直接优化多模态重排链路延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
VLM作为列表式重排器需同时处理数十路候选的视觉Token，推理成本极高是落地核心瓶颈；现有基于注意力显著性的剪枝方法与排序贡献严重错配——视觉突出的Token往往是候选间共有的共性特征，对区分候选排序无帮助，且saliency可靠性随层变化极大，无法直接复用。

### 方法关键点
- 设计DTI（Discriminative Token Importance）无注意力先验，融合query相关性、跨候选区分度计算Token的排序贡献，仅在ViT编码后计算1次即可全局复用
- 用归一化注意力熵Hnorm判断每层saliency可靠程度，动态校准DTI和层专属AttentionInfo saliency的融合权重：熵越低（注意力越集中）越信任saliency，反之越依赖DTI
- 基于α-Maximin自动选择跨不同信任区间的剪枝层，每层等比例保留Token，全程无需训练、无数据集专属调参

### 关键结果
在Flickr30K、MSCOCO、FashionIQ三个基准，Qwen3-VL、InternVL2.5两类VLM架构上测试：20% Token预算下，Flickr30K MRR@10与无剪枝基线持平，MSCOCO MRR@10反超基线，FashionIQ性能在所有剪枝方法中排第一；10% Token预算下MRR@10较无剪枝基线下降不超过1.2pp；降低FLOPs 39~45%，端到端实测提速1.28~1.45倍，无需针对数据集/模型重调。

### 核心结论
VLM重排剪枝的核心不是保留视觉显著的Token，而是保留能区分候选排序的判别性Token，层动态的信任校准比单纯激进剪枝更能实现精度和效率的最优平衡
