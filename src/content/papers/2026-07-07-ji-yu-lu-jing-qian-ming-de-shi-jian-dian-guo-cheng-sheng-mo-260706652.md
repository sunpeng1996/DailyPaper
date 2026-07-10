---
title: 'From Jumps to Signatures: a Generative Method for Temporal Point Processes'
title_zh: 基于路径签名的时间点过程生成建模方法
authors:
- Niels Cariou-Kotlarek
- Vasileios Lampos
affiliations:
- University College London
- Centre for Artificial Intelligence
- Department of Computer Science
arxiv_id: '2607.06652'
url: https://arxiv.org/abs/2607.06652
pdf_url: https://arxiv.org/pdf/2607.06652
published: '2026-07-07'
collected: '2026-07-10'
category: Other
direction: 时间点过程 · 序列生成建模
tags:
- Temporal Point Process
- Generative Model
- Rough Path Signature
- Sequence Modeling
- Evaluation Metric
one_liner: 提出interarrival embedding映射离散事件序列为连续路径，实现首个基于路径签名的TPP生成模型sigTPP
practical_value: '- 电商用户点击/加购/下单等行为序列本质是TPP，可复用interarrival embedding将离散行为序列转换为连续路径，用路径签名做全局特征提取，替代传统RNN/Transformer的序列embedding方案

  - 现有序列推荐、用户行为预测模型多采用逐点损失优化，可迁移sigTPP的全局轨迹级损失训练思路，提升长序列建模的整体一致性

  - 变长行为序列生成/预测的效果评估可复用论文推导的3种分布差异指标，解决传统metrics无法衡量序列整体分布匹配度的问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：粗糙路径签名的连续路径特征提取能力无法直接适配Temporal Point Processes (TPP)的离散跳变路径，限制了签名方法在事件序列中的应用；现有神经TPP模型多优化逐事件目标，缺乏全局序列级损失，且变长事件序列评估缺少合理的分布差异度量。
**方法关键点**：设计interarrival embedding，将离散跳变路径稳定单射映射为有界变差连续路径，把签名方法拓展到离散事件序列；构建sigTPP，为首个基于签名的TPP生成模型，采用完整轨迹的路径级损失训练；推导3种计数路径空间的分布差异指标，为生成式TPP提供理论完备的评估工具。
**关键结果**：在合成和真实数据集上，sigTPP在8种互补指标下平均排名最优，64%的数据集-指标对表现优于或与最强基线误差相当，相对所有基线平均提升至少19%。
