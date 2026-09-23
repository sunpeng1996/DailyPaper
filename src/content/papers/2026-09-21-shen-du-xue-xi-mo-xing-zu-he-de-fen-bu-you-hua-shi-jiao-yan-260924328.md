---
title: A Distributional Optimisation Perspective on Combining Models in Deep Learning
title_zh: 深度学习模型组合的分布优化视角研究
authors:
- Congye Wang
- Yan Lin
- Zheyang Shen
- Matthew A. Fisher
- Chris. J. Oates
affiliations:
- Newcastle University, UK
arxiv_id: '2609.24328'
url: https://arxiv.org/abs/2609.24328
pdf_url: https://arxiv.org/pdf/2609.24328
published: '2026-09-21'
collected: '2026-09-23'
category: Training
direction: 深度学习模型组合 · 分布优化训练
tags:
- Distributional Optimization
- Ensemble Learning
- LoRA Averaging
- Model Fusion
- Training Optimization
one_liner: 将集成、低秩适配器平均等模型组合策略统一为熵正则分布优化问题，给出收敛性分析与算法效果验证
practical_value: '- 做多模型集成、多LoRA权重融合时，可复用该框架做端到端联合训练，替代后处理式加权融合提升效果

  - 线上Ensemble服务可参考凸性结论优先选择MFLD类算法保证收敛性，降低调参不稳定风险

  - 大模型微调多LoRA权重平均场景，可测试本文提出的函数式变分梯度下降(VGD)算法提升融合效果'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前模型组合（集成、适配器平均等）通常独立训练单模型再通过ad hoc规则融合，缺乏统一的端到端训练理论框架，分布优化的最新进展提供了联合训练的理论可能性但落地价值不明确。

### 方法关键点
1. 将集成学习、低秩适配器平均两种主流模型组合策略统一建模为熵正则分布优化问题，证明集成场景下目标为凸，可直接复用平均场朗之万动力学(MFLD)的收敛保证，适配器平均场景下目标非凸，原有收敛性不成立；2. 对比评估现有与新型优化算法，包括提出的函数式变分梯度下降(VGD)变体。

### 关键结果
在合成分类任务、大语言模型常识推理微调任务上验证了框架有效性，函数式VGD算法在低秩适配器平均场景下表现优于现有基线。
