---
title: Unified Video Dense Prediction from Disjoint Data
title_zh: 基于非重叠数据集的统一视频密集预测模型
authors:
- Yihong Sun
- Seoung Wug Oh
- Jiahui Huang
- Bharath Hariharan
- Joon-Young Lee
affiliations:
- Adobe Research
- Cornell University
arxiv_id: '2607.21592'
url: https://arxiv.org/abs/2607.21592
pdf_url: https://arxiv.org/pdf/2607.21592
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 多模态视觉 · 统一多任务密集预测
tags:
- Multimodal
- Unified Model
- Dense Prediction
- Knowledge Distillation
- Diffusion Model
one_liner: 利用预训练扩散模型先验与蒸馏方案，从非重叠标注数据训练多任务统一视频密集预测模型
practical_value: '- 「单任务专家蒸馏+轻量任务投影头」的训练范式可复用至多模态推荐的多任务预训练，解决不同召回/排序任务标注分散无重叠的问题，降低统一特征的标注成本

  - 利用大模型预训练先验桥接跨域非重叠数据的思路，可迁移至多品类/跨场景电商推荐的域适应任务，提升冷启动泛化效果

  - 统一多任务推理架构可降低视觉内容理解模块的部署开销，适合电商短视频/直播场景的多维度内容标签批量生产'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多任务视频密集预测方法要么依赖全量共标注数据（与实际标注分散的现状矛盾），要么采用计算成本极高的伪标签方案，无法高效利用各独立任务的分散标注数据。
### 方法关键点
1. 推出的UniD统一视频模型，可联合预测深度、表面法向量、语义分割、材质等8类密集场景属性；
2. 采用单任务专家通过轻量任务投影头监督统一backbone的蒸馏方案，无需标注重叠或伪标签；
3. 依托预训练扩散模型的强视觉先验桥接非重叠训练数据的域gap，支持训练时未见过的场景-任务组合泛化。
### 关键结果
性能与单任务专家、多任务基线相当，分布外场景泛化性更优，时序、跨任务一致性显著提升。
