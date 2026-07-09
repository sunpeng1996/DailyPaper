---
title: '`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object
  Segmentation'
title_zh: 面向自监督视频对象分割的注意力引导跨时域聚类方法
authors:
- Waqas Arshid
- Mohammad Awrangjeb
- Alan Wee-Chung Liew
- Yongsheng Gao
affiliations:
- School of Information and Communication Technology, Griffith University
- School of Engineering and Built Environment, Griffith University
arxiv_id: '2607.07230'
url: https://arxiv.org/abs/2607.07230
pdf_url: https://arxiv.org/pdf/2607.07230
published: '2026-07-08'
collected: '2026-07-09'
category: Other
direction: 自监督视频理解 · 时序表征学习
tags:
- Self-supervised Learning
- Video Object Segmentation
- Transformer
- Temporal Clustering
- Attention Mechanism
one_liner: 融合注意力引导token选择与轻量时域聚类的自监督VOS框架，兼顾空间精度与时序一致性且无需密集标注
practical_value: '- 跨时域一致性对齐思路可复用在短视频商品理解、用户行为序列的时序特征对齐场景，降低时序特征漂移

  - 冻结Transformer backbone + 轻量下游模块的架构选择，可复用在大模型业务微调场景，降本提效

  - 注意力引导的自适应token选择策略，可迁移至高分辨率长序列任务的特征降维，提升推理效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
自监督视频对象分割（VOS）可避免密集标注的高成本问题，但现有方法难以同时保障空间精度与时序一致性，普遍依赖光流、合成运动先验或特定任务预训练，可扩展性与泛化性受限。
### 方法关键点
CTC2自监督框架采用冻结Transformer backbone加轻量模块的架构，融合注意力引导的自适应token选择与多偏移时域对齐策略，通过显著性加权对称一致性目标对齐跨帧软部件分配，替代传统像素/整对象级操作。
### 关键结果
性能在同期自监督VOS方法中达到竞争力水平，保持实时推理吞吐量，无需依赖运动先验或域自适应，跨数据集评估表现稳定，可仅用首帧掩码扩展至半监督场景。
