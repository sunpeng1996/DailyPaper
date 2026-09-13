---
title: 'Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based
  Neuroevolution'
title_zh: 打破中心偏差：面向坐标基神经进化的空间划分专家方法
authors:
- Romain Claret
- Arthur Gygax
- Michael O'Neill
- Paul Cotofrei
- Michael Palma Mendes
- Pascal Felber
affiliations:
- University of Neuchâtel, Switzerland
- University College Dublin, Ireland
arxiv_id: '2609.11518'
url: https://arxiv.org/abs/2609.11518
pdf_url: https://arxiv.org/pdf/2609.11518
published: '2026-09-10'
collected: '2026-09-13'
category: Other
direction: 空间划分MoE · 神经进化训练优化
tags:
- MoE
- Neuroevolution
- Spatial Partitioning
- Receptive Field
- ES-HyperNEAT
one_liner: 受MoE启发提出空间划分专家方案，解决ES-HyperNEAT中心偏差，准确率相对提升106%
practical_value: '- 遇到模型特征集中在头部/中心区域的偏差问题时，可参考空间/维度划分MoE思路，强制每个专家仅处理固定分段输入，避免特征覆盖坍缩

  - 多专家融合时若标注数据不足，可优先采用等权平均策略，无需额外验证数据即可获得大部分增益，降低落地成本

  - 可复用receptive field诊断方法，快速排查推荐/多模态模型是否存在输入特征覆盖不足问题，定位性能瓶颈'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于坐标的生物启发间接编码方法ES-HyperNEAT存在空间集中偏差，输入像素映射到原点为中心的坐标空间时，进化网络仅收敛到中心小范围像素簇，MNIST基准上平均准确率仅21%，偏差根源是优化缺陷还是架构上限尚不明确。
### 方法关键点
受MoE原理启发，将输入划分为非重叠空间分段，每个分段分配独立进化的专属专家网络；架构增益不依赖数据驱动的聚合策略，无验证数据的等权平均即可实现大部分收益。
### 关键结果
13个专家时MNIST平均准确率达43%，相对基线提升106%；等权平均融合即可实现70%相对提升；输入有效像素覆盖率从4%提升至79%；同时输出可泛化的输入覆盖坍缩receptive field诊断工具、空间划分修复方案。
