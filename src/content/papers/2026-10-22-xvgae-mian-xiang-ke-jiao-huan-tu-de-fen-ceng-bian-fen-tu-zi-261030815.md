---
title: 'xVGAE: A Hierarchical Variational Graph Autoencoder for Exchangeable Graphs'
title_zh: xVGAE：面向可交换图的分层变分图自编码器
authors:
- Daniele Micheletti
- Federica Zoe Ricci
- Erik B. Sudderth
affiliations:
- University of California, Irvine
- Swarthmore College
arxiv_id: '2610.30815'
url: https://arxiv.org/abs/2610.30815
pdf_url: https://arxiv.org/pdf/2610.30815
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 可交换图生成 · 分层VAE架构
tags:
- Graph Generation
- Variational Autoencoder
- Graph Representation Learning
- Generative Model
- Hierarchical Model
one_liner: 基于Aldous-Hoover定理提出分层变分图自编码器，生成图速度较SOTA快数个量级且效果持平
practical_value: '- 电商用户社交/行为关联图高效生成可借鉴xVGAE分层隐变量建模思路，大幅降低生成时延

  - 可迁移图-节点双层隐变量解耦架构，用于用户-物品交互图表征学习，提升召回排序特征质量

  - 图数据增强场景可复用one-shot生成逻辑，快速生成符合真实分布的交互样本缓解冷启动'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有SOTA图生成模型存在两大痛点：常规计算预算下收敛难度高、生成时延过大，且需满足节点索引排列不变的可交换性约束，无法适配大规模场景需求。
### 方法关键点
基于Aldous-Hoover定理设计分层生成架构：1）引入图级、节点级双层可交换隐变量，天然适配节点排列不变性要求；2）用graphon函数映射双层隐变量到节点对边生成概率；训练阶段同时拟合隐变量分布与graphon近似。
### 关键结果
生成图质量与SOTA持平，生成速度快数个量级；学到的隐表征与图、节点属性高度相关，支持one-shot快速生成符合训练集统计规律的新图
