---
title: Similarity search generalisation in contrastive learning with InfoNCE loss
title_zh: InfoNCE损失下对比学习的相似性搜索泛化能力研究
authors:
- Nick Whiteley
affiliations:
- School of Mathematics, University of Bristol
arxiv_id: '2607.09405'
url: https://arxiv.org/abs/2607.09405
pdf_url: https://arxiv.org/pdf/2607.09405
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 对比学习训练 · InfoNCE泛化理论
tags:
- InfoNCE
- ContrastiveLearning
- SimilaritySearch
- GeneralizationBound
- EmbeddingModel
one_liner: 推导InfoNCE泛化界，证明负样本数量k增大可稳定相似性搜索泛化误差
practical_value: '- 训练向量召回用的对比学习embedding时，可适当增大负采样数量k，降低相似性搜索泛化误差，提升召回准确率

  - 调优InfoNCE温度参数时可参考论文提出的逆温度调参逻辑，平衡embedding对齐效果与泛化性

  - 对带Lipschitz约束的embedding模型，负样本k的增益更稳定，向量召回选型可优先考虑这类结构'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有InfoNCE理论分析多聚焦k→∞极限场景、下游分类任务泛化，缺少相似性搜索场景下有限负样本的泛化能力量化研究，无法指导向量召回等业务场景的模型训练调优。
### 方法关键点
通过Gâteaux微分推导InfoNCE损失的全新连续性界，保留损失中负样本平均的原生结构，引入可与算法温度对齐的逆温度参数；结合参数满足Lipschitz约束的embedding函数特性，分析泛化规律。
### 关键结果
1. 带k个负样本的InfoNCE群体风险与理想软最大化搜索的期望交叉误差为O(1/k)；
2. 负样本数量k增大时，负样本平均效应可直接稳定泛化误差，k越大泛化表现越稳定。
