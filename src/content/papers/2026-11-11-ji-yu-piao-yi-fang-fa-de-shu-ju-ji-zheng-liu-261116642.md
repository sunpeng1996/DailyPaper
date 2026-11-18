---
title: Dataset Distillation via Drifting
title_zh: 基于漂移方法的数据集蒸馏
authors:
- George Cazenavette
- Angelina Quan
- Giannis Daras
- Antonio Torralba
- Vincent Sitzmann
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2611.16642'
url: https://arxiv.org/abs/2611.16642
pdf_url: https://arxiv.org/pdf/2611.16642
published: '2026-11-11'
collected: '2026-11-18'
category: Training
direction: 数据集蒸馏 · 训练数据合成
tags:
- Dataset-Distillation
- Training-Data-Synthesis
- Latent-Space-Optimization
- Representation-Learning
- Multi-Modal
one_liner: 提出无分类目标的特征空间漂移蒸馏法，直接拟合类数据分布，覆盖度与训练效果优于现有方案
practical_value: '- 针对推荐/广告场景大尺寸用户行为/物料数据集蒸馏需求，可复用本方法的特征空间吸引+排斥损失构造思路，无需分类监督即可生成高覆盖度的小尺寸合成数据集，降低小模型微调训练成本

  - 做物料语义分布可视化/模型可解释性分析时，可借鉴本方法的分布拟合蒸馏逻辑，合成对应类别的代表性样本，快速定位语义分布偏移问题

  - 跨模态物料库压缩场景可直接迁移本方法框架，替换特征提取器为文本/多模态预训练模型即可实现文本/图文类数据集的蒸馏'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有数据集蒸馏方案普遍以分类任务目标优化合成样本，对原始数据的分布覆盖度不足，且场景适配性受限，难以直接迁移至多模态、无分类标签的数据集蒸馏场景。

### 方法关键点
1. 不依赖分类损失，在预训练特征提取器的隐空间对合成样本做优化；
2. 设计漂移损失函数，驱动合成样本同时向同类别真实样本的隐向量靠近、与其他合成样本的隐向量远离，直接拟合每类的真实数据分布；
3. 框架无模态绑定，替换对应模态的预训练特征提取器即可实现跨模态适配。

### 关键结果
合成样本的原始数据分布覆盖度显著优于现有蒸馏方法，下游分类任务训练效果与分类目标导向的蒸馏方案持平；ImageNet-1k每类仅蒸馏10张样本即可支撑分类器训练，同时支持多模态数据集蒸馏，还可作为模型可解释性的可视化工具。
