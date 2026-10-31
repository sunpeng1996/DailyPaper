---
title: 'FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet
  Loss'
title_zh: FDSML：带参数感知三元组损失的公式驱动监督度量学习
authors:
- Hina Otake
- Shinei Arakawa
- Keitaro Tanaka
- Yoshihiro Fukuhara
- Hirokatsu Kataoka
- Shigeo Morishima
affiliations:
- Waseda University
- Waseda Research Institute for Science and Engineering
- National Institute of Advanced Industrial Science and Technology
- University of Oxford
arxiv_id: '2610.39423'
url: https://arxiv.org/abs/2610.39423
pdf_url: https://arxiv.org/pdf/2610.39423
published: '2026-10-28'
collected: '2026-10-31'
category: Training
direction: 合成数据预训练 · 度量学习优化
tags:
- Metric Learning
- Synthetic Pre-training
- Triplet Loss
- Transfer Learning
- Representation Learning
one_liner: 基于生成参数构造关系监督信号，优化合成数据预训练的跨任务迁移性与鲁棒性
practical_value: '- 电商商品图像召回预训练场景，可基于合成图像生成参数构造三元组正负例，省去大量人工标注成本

  - 优化表征学习监督信号时，可引入生成过程的连续参数构建关系约束，替代纯离散分类标签，大幅提升召回类任务的Recall指标

  - 构造合成训练数据集时，可通过提升类内方差+稳定结构的设计思路，优化下游任务对图像破损、模糊等低质量输入的鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有公式驱动监督学习（FDSL）基于离散分类标签开展合成数据预训练，丢弃生成过程的连续性信息，跨任务迁移能力有限；传统真实数据预训练还存在标注成本高、隐私风险、数据偏见等问题。
### 方法关键点
1. FDSML框架从图像生成参数而非离散标签中提取关系监督信号
2. 构造FineFractalDB分形数据集，提升类内方差同时维持结构稳定性
3. 设计Parameter-Aware Triplet（PA-Triplet）损失，基于迭代函数系统参数空间的距离分配正负样本，训练得到的embedding可对齐参数衍生的相对相似度排序
### 关键结果
ResNet-50架构下，相比基线FDSL预训练：
- Stanford Online Products 数据集Recall@1从65.6%提升至74.0%
- Stanford Cars 数据集Recall@1从56.2%提升至78.4%
- 下游分类任务表现持平，多种图像扰动场景下鲁棒性显著提升
