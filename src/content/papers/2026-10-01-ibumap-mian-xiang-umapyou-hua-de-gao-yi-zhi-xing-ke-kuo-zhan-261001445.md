---
title: 'ibUMAP: Coherent and Scalable Field Evaluation for UMAP Optimization'
title_zh: ibUMAP：面向UMAP优化的高一致性可扩展场评估方法
authors:
- Bin Chen
- Yumeng Xue
- Patrick Paetzold
- Yunhai Wang
- Oliver Deussen
affiliations:
- University of Konstanz
- Renmin University of China
arxiv_id: '2610.01445'
url: https://arxiv.org/abs/2610.01445
pdf_url: https://arxiv.org/pdf/2610.01445
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 降维嵌入优化 · 效率与稳定性提升
tags:
- UMAP
- Dimensionality Reduction
- Embedding
- FFT
- Training Optimization
one_liner: 提出基于场评估的ibUMAP，优化UMAP嵌入稳定性的同时实现多场景运算加速
practical_value: '- 电商/推荐系统做大规模用户/物品Embedding降维可视化分析时，可替换原生UMAP为ibUMAP，既提升运行速度，又保证多次运行的嵌入稳定性，降低分析结果波动

  - 其基于FFT插值替代全对计算的思路，可迁移到大规模Embedding召回的相似度计算、图神经网络的邻域聚合等场景，降低计算复杂度

  - 用负采样条件期望推导度加权斥力场的设计思路，可优化推荐系统负采样模块的梯度估计稳定性，减少训练过程的结果波动'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
原生UMAP依赖随机负采样优化布局，采样顺序会导致斥力估计偏差，多次运行的嵌入结果不稳定，无法满足大规模场景下重复计算、作为下游pipeline中间表示的要求。
### 方法关键点
1. 提出ibUMAP，基于共享嵌入快照同步计算吸引力与斥力，消除采样顺序带来的不稳定问题；
2. 基于固定嵌入下负采样的条件期望构造度加权斥力场，用三个标量矩表示，通过基于插值的FFT方案在CPU/GPU上高效计算，避免显式全对运算带来的开销。
### 关键结果
CPU上相对umap-learn无随机种子时中位数加速3.29倍、有种子时加速5.79倍；GPU无种子百万级数据集上相对cuML加速1.44倍，同时嵌入运行间稳定性显著提升，最终质量波动极小。
