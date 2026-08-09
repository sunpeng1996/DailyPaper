---
title: 'DistMedVL: Distributional Vision-Language Alignment for Uncertainty-Aware
  Medical Image Segmentation'
title_zh: DistMedVL：面向不确定性感知医学图像分割的分布式视觉-语言对齐
authors:
- Jiaxuan Li
- Qing Xu
- Xiangjian He
- Yue Li
- Daokun Zhang
- Fiseha B. Tesema
- Rong Qu
arxiv_id: '2608.05683'
url: https://arxiv.org/abs/2608.05683
pdf_url: https://arxiv.org/pdf/2608.05683
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 多模态医疗图像分割 · 跨模态对齐
tags:
- Multimodal
- Cross-Modal Alignment
- Adapter
- Uncertainty Modeling
- Medical Imaging
one_liner: 在冻结编码器上引入轻量概率跨模态适配器，建模表示不确定性提升多模态医学分割性能
practical_value: '- 跨模态对齐场景（如多模态电商检索、多模态推荐）可借鉴PCM-Adapter思路，在冻结大模型基础上仅训练少量参数实现概率级对齐，大幅降低算力成本

  - 特征匹配阶段可引入马氏距离计算特征兼容性，动态降权不可靠特征维度，有效提升跨域鲁棒性

  - 多模态融合时可加入单模态置信度估计模块，用主模态分布修正辅助模态分布，适配不同模态的分布差异'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有医疗多模态分割方法采用确定性跨模态匹配，忽略了边界模糊带来的偶然不确定性、训练数据不足带来的认知不确定性，域迁移下性能脆弱。
### 方法关键点
提出概率视觉-语言框架DistMedVL，在冻结的视觉、文本编码器上插入仅6.3M参数的Probabilistic Cross-Modal Adapter（PCM-Adapter）分两步做渐进式概率对齐：1）Mahalanobis Alignment Module（MAM）将文本token建模为高斯分布，通过马氏距离计算patch-文本兼容性，基于方差降权不可靠特征维度；2）Distribution Flow Module（DFM）估计各模态置信参数，用视觉信息引导优化文本分布，适配不同成像模态的分布差异。
### 关键结果数字
在8个医学分割基准上超过SOTA，数据效率、扰动鲁棒性、跨数据集泛化性均显著优于现有方法。
