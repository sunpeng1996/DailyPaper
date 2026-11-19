---
title: 'Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view
  Consensus'
title_zh: 让样本协同发声：基于跨视图共识消除虚假相关性
authors:
- Weiwei Li
- Junzhuo Liu
- Tong Chu
- Hengfu Yu
- Yinjie Lei
- Wen Li
affiliations:
- University of Electronic Science and Technology of China
- Sichuan University
arxiv_id: '2611.22668'
url: https://arxiv.org/abs/2611.22668
pdf_url: https://arxiv.org/pdf/2611.22668
published: '2026-11-16'
collected: '2026-11-19'
category: Training
direction: 模型训练 · 无监督虚假关联消除
tags:
- Debiasing
- Multi-view Learning
- Spurious Correlation
- Unsupervised Learning
- Robustness
one_liner: 提出无监督去偏多视图框架CHORD，跨多表征空间聚合共识消虚假关联，提升少数样本组预测精度
practical_value: '- 推荐场景样本去偏可复用跨视图共识思路：同时用用户行为、内容属性、语义表征3个视图的类别划分结果，交叉识别虚假关联特征，无需人工标注bias属性

  - 冷启少数样本（小众品类、低活用户）的模型鲁棒性优化可参考CHORD范式，不需要额外标注组信息即可提升尾部分类/排序精度

  - 多模态推荐的特征融合阶段可引入跨视图类内聚合逻辑，过滤不同模态的噪声shortcut特征，降低模态bias对推荐结果的影响'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
深度模型通常依赖训练集中的虚假相关性完成预测，在低占比少数样本组上表现大幅退化；现有去偏方法要么需要人工标注偏差属性，标注成本高且与模型实际使用的shortcut特征存在偏差，要么基于单表征空间推理偏差，噪声高、信息不完整。
### 方法关键点
提出无监督去偏框架CHORD，核心假设是单一特征空间中难以识别的偏差在其他特征空间可能更显著；通过聚合多个视图下的类内划分结果作为候选偏差代理，无需偏差标注即可对目标表征和分类器做去偏优化，实现跨视图鲁棒共识。
### 关键结果
在视觉、语言、语音、医学影像共7个基准数据集上测试，最差组精度获得一致提升，代码与预训练权重已开源。
