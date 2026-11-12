---
title: 'SpecValley: Aggregation as Spectral Valley in Dense Heterophilic Graphs'
title_zh: SpecValley：稠密异配图中的谱谷聚合方法
authors:
- Christoph Jahn
- Delvin Bacho
- Urs Waldmann
- Bastian Goldluecke
affiliations:
- Mercedes-Benz AG
- University of Konstanz
arxiv_id: '2611.14176'
url: https://arxiv.org/abs/2611.14176
pdf_url: https://arxiv.org/pdf/2611.14176
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 异配图节点分类 · 可学习谱聚合
tags:
- Graph Neural Network
- Heterophilic Graph
- Node Classification
- Spectral Filter
- Learnable Aggregation
one_liner: 提出可学习谱谷聚合算子SpecValley，解决异配图节点分类中固定度归一化的有效信号衰减问题
practical_value: '- 电商用户-物品异配交互图的节点建模可替换固定度归一化，引入可学习谱谷聚合，避免有效标签信号被预设定的归一化衰减

  - 做图召回/排序的GNN优化时，可参考其频谱能量预算分析逻辑，先校验聚合阶段损失的信号是否可被下游滤波器恢复，减少无效调优

  - 异配场景下的图特征传播可复用其二阶段架构：先做适配数据分布的可学习聚合，再接普通谱滤波，无需定制复杂传播算子，降低开发成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
异配图节点分类任务中，固定度归一化的邻域聚合本质是预设在λ=1位置的谱谷，恰好对应稠密图特征值聚集区，会无差别衰减该区间携带标签信息的有效信号，且该损失无法被下游线性谱滤波器恢复。
### 方法关键点
采用二阶段架构：首先为每张图独立学习聚合算子的谱谷位置、锐度、侧翼增益，自适应过滤无效信号，再接普通谱滤波器完成特征传播，无需定制复杂传播算子，从聚合层面解决异配信号衰减问题。
### 关键结果
在全系列异配图节点分类基准上取得SOTA表现，ablation实验验证性能增益完全来自可学习聚合模块，与下游滤波器无关。
