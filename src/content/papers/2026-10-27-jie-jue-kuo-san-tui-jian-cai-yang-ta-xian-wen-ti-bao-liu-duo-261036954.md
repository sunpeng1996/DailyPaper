---
title: 'When Diffusion Recommenders Stop Sampling: Preserving Generative Diversity'
title_zh: 解决扩散推荐采样塌陷问题：保留生成多样性的DARTS框架
authors:
- Louis Castres Saint Martin
- Alain Rakotomamonjy
- Patrick Gallinari
affiliations:
- Criteo AI Lab
- Sorbonne Université
- CNRS
- ISIR
arxiv_id: '2610.36954'
url: https://arxiv.org/abs/2610.36954
pdf_url: https://arxiv.org/pdf/2610.36954
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 扩散模型多样性优化
tags:
- Diffusion Model
- Sequential Recommendation
- Generative Diversity
- Latent Diffusion
- Diversity-Accuracy Tradeoff
one_liner: 提出三阶段解耦的扩散推荐框架DARTS，同时提升排序精度与生成多样性
practical_value: '- 扩散推荐设计避坑：扩散训练阶段不要加离散分类损失、不要联合训练item embedding与去噪器，否则会引发采样塌陷，同时损失多样性与精度

  - 三阶段训练架构可复用：先预训练冻结序列自编码器的隐空间，再单独训练隐空间扩散模型，最后仅微调解码器适配分布偏移，兼顾精度与多样性

  - 多采样聚合提效：对扩散生成的多个样本做后验预测平均，固定slate大小下可额外提升NDCG@10约3.2%，适合对 latency 不敏感的推荐场景

  - 多样性评估指标可直接复用：Jaccard dissimilarity、generative variance ratio、participation ratio三个指标，可量化生成式推荐的采样多样性，补充传统排序指标的不足'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有扩散推荐系统普遍存在采样塌陷问题，多次独立采样得到的推荐结果几乎一致，无法发挥生成式模型天然的多样性优势；核心原因是两个常见设计缺陷：隐空间与去噪器联合训练、扩散过程中加入离散分类损失，同时还存在多样性-精度的权衡难题，提升多样性往往会牺牲排序效果。

### 方法关键点
- 三阶段解耦训练架构：1）预训练序列自编码器得到item隐空间，冻结编码器和item表示；2）在固定隐空间中仅用回归损失训练条件去噪器，不引入任何离散分类损失；3）仅微调解码器适配扩散生成样本的分布偏移，用BPR损失优化排序效果
- 混合item表示：融合预训练T5生成的语义embedding和协同过滤ID embedding，进一步提升基础效果
- 后验预测聚合：推理时对多个扩散采样结果的预测分布做平均，无需重训即可进一步提升固定slate大小下的排序精度

### 关键结果
在亚马逊2023评论数据集的3个品类（乐器、工业科学、游戏）上，对比SASRec、DiffuRec、DreamRec等10+基线，DARTS的Recall@K、NDCG@K整体领先最优基线6.8%~12%；采样多样性显著优于基线，Jaccard dissimilarity达0.3（基线仅0.02左右）；聚合4个采样结果可额外提升NDCG@10约3.2%，而基线采样聚合几乎无收益。

### 核心结论
扩散推荐中，在扩散训练阶段引入离散分类损失、联合训练item表示与去噪器，会同时损失采样多样性和排序精度，完全避免这两个设计即可实现多样性与精度的双提升
