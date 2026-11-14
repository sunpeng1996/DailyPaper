---
title: 'HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality
  Assessment'
title_zh: HiVE-VQA：基于体嵌入分层交互的无参考视频质量评估方法
authors:
- Robbie Hamilton
- Fan Zhang
- David Bull
affiliations:
- University of Bristol, UK
arxiv_id: '2611.17146'
url: https://arxiv.org/abs/2611.17146
pdf_url: https://arxiv.org/pdf/2611.17146
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: 无参考视频质量评估 · 基础模型特征融合
tags:
- VQA
- Video Foundation Model
- Feature Fusion
- JEPA
- Frozen Backbone
one_liner: 基于冻结V-JEPA模型，通过分层体特征融合实现SOTA无参考视频质量评估
practical_value: '- 电商UGC短视频、直播内容的质量自动质检场景可复用该方案，仅训练轻量3D卷积头，冻结视频基础模型，大幅降低训练成本

  - 特征构建可参考多深度分层融合思路，结合浅层失真特征与深层语义时序特征，提升质量评分准确性

  - 推理成本与视频分辨率无关的特性适配高并发内容质检场景，可直接接入现有内容审核链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
UGC视频内容爆发，现有无参考视频质量评估（NR-VQA）方案存在多分支架构复杂、单分支微调算力成本高的问题，亟需高效低成本的落地方案。
### 方法关键点
采用冻结的V-JEPA 2.1预训练视频模型作为backbone，抽取不同深度的token网格构建分层时空体特征，使用仅5.2M参数（占总参数量5.7%）的轻量3D卷积头跨层、空间、时序维度融合特征，兼顾浅层失真信息与深层语义时序上下文，训练仅更新头部参数，无需辅助多模态模型，推理成本不受视频分辨率影响。
### 关键结果
仅在LSVQ数据集训练且无额外微调，在4个基准测试集上SROCC、PLCC指标超过17个SOTA方法，效果优于任务专属多网络融合方案。
