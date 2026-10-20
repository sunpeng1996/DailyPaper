---
title: 'OneChord: Distill What You Rank, Recommend in One Pass'
title_zh: OneChord：蒸馏排序目标实现单步生成式推荐
authors:
- Zesheng Li
- Chengchang Pan
- Honggang Qi
affiliations:
- University of Chinese Academy of Sciences
arxiv_id: '2610.25805'
url: https://arxiv.org/abs/2610.25805
pdf_url: https://arxiv.org/pdf/2610.25805
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式推荐 · Semantic ID 蒸馏优化
tags:
- Semantic ID
- Generative Recommendation
- Distillation
- Parallel Decoding
- Sequential Recommendation
one_liner: 统一监督、蒸馏、推理的融合分布，实现精度更高、速度更快的单步生成式推荐
practical_value: '- 多源打分融合可借鉴其可学习门控+全Catalog归一化方案，避免人工调权重，同时保证候选排序一致性，适合生成式推荐的SID+匹配分融合场景

  - 蒸馏目标设计可复用其「蒸馏部署时实际用的排序分布」思路，不用蒸馏中间分支输出，直接对齐最终推理用的融合分布，减少分布漂移

  - 硬候选构造方案可直接迁移：采样负例+直接预测TopK+精炼预测TopK的并集作为蒸馏候选集，覆盖竞争候选，降低蒸馏计算量同时保证TopK效果对齐'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐通常需融合SID生成概率与Item匹配分，部署时的融合权重、归一化规则与训练目标脱节，导致推理时排序分布和训练目标不一致；同时多步精炼类方法精度高但推理延迟高，难以满足线上低延迟要求，亟需兼顾精度和效率的单步生成式推荐方案。

### 方法关键点
- 遵循「distill what you rank」原则，训练、蒸馏、推理全程使用同一个可学习的融合分布：门控α自动加权归一化后的SID生成概率与Item匹配分，无需人工调参
- 训练时用冻结的去噪器生成合法的部分掩码SID，学生模型基于这些状态构造精炼的融合排序目标，在共享硬候选集上对齐直接预测分布与精炼目标分布，将多步精炼效果蒸馏进单步预测
- 给出候选条件下的融合权重漂移理论保证：只要硬候选集覆盖全量TopK且精炼目标的排序边际大于蒸馏对齐误差，就能保证蒸馏后全量TopK排序一致性

### 关键实验
在6个亚马逊公开数据集（Sports、Beauty、Toys等）上对比14个基线（包括SPRINT、DiffGRM等最新SID生成式推荐模型），平均Recall@5相对最优基线提升6.30%，NDCG@5平均提升7.12%，最高在Beauty数据集NDCG@5提升9.96%；推理速度比最快基线还快1.04~1.18倍，同时在长尾物品、长历史用户场景下均有稳定增益。

最值得记住的一句话：生成式推荐的蒸馏目标不需要对齐中间分支输出，直接对齐部署时实际用的最终排序分布，能同时获得更高精度和更低推理延迟。
