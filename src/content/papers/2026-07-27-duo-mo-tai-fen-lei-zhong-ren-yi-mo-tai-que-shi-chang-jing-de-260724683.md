---
title: Co-Learning for Missing Arbitrary Modalities in Multi-modal Classification
title_zh: 多模态分类中任意模态缺失场景下的协同学习方法
authors:
- Francisco Mena
- Dino Ienco
- Roberto Interdonato
- Cassio F. Dantas
- Simon Besnard
affiliations:
- GFZ Helmholtz Center for Geosciences
- INRAE UMR TETIS University of Montpellier
- INRIA EVERGREEN University of Montpellier
- CIRAD UMR TETIS University of Montpellier
arxiv_id: '2607.24683'
url: https://arxiv.org/abs/2607.24683
pdf_url: https://arxiv.org/pdf/2607.24683
published: '2026-07-27'
collected: '2026-07-29'
category: Multimodal
direction: 多模态分类 · 缺失模态鲁棒性优化
tags:
- Multi-modal Classification
- Co-learning
- Missing Modality
- Robustness
- Decision Fusion
one_liner: 提出特征/决策层级两类跨模态协同学习方法，提升任意模态缺失时多模态分类鲁棒性
practical_value: '- 多模态商品分类、广告创意审核、多模态召回排序等场景，遇到商品无视频/用户行为数据缺失等模态不全问题时，可复用特征+决策双层协同学习框架替代传统融合策略，提升模型鲁棒性

  - 针对业务不同模态缺失程度分策略选型：轻度缺失（仅缺1种模态）优先用特征级协同方法，极端缺失（仅存1种有效模态）优先用决策级协同方法，适配不同故障场景

  - 无需预定义模态缺失模式的训练范式，可直接迁移至多模态相关任务，降低缺失样本预处理的规则开发成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态分类依赖多源互补信息提升预测效果，但实际场景受传感器故障、隐私限制等约束，训练与推理阶段模态可用性不一致；现有方案多仅覆盖双模态场景、聚焦优化融合流程，无法应对无预定义模式的任意模态缺失问题。

### 方法关键点
放弃传统多模态融合思路，采用模态间协同学习框架，提出两类方案分别从特征层、决策层复用跨模态信息，支持任意子集模态缺失的推理场景，无需预定义缺失模式。

### 关键结果
在两个多模态分类基准测试集上，各类缺失场景下鲁棒性均显著优于基线；单模态缺失的轻度缺失场景下特征级方法表现更优，仅存单模态的极端缺失场景下决策级方法效果提升更明显。
