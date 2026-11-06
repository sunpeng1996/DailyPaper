---
title: Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition
title_zh: 面向鲁棒人脸识别的难样本条件去相关注意力方法
authors:
- Tahar Chettaoui
- Guray Ozgur
- Eduarda Caldeira
- Naser Damer
- Fadi Boutros
affiliations:
- Fraunhofer Institute for Computer Graphics Research IGD, Germany
- TU Darmstadt, Germany
arxiv_id: '2610.41789'
url: https://arxiv.org/abs/2610.41789
pdf_url: https://arxiv.org/pdf/2610.41789
published: '2026-10-30'
collected: '2026-11-06'
category: Other
direction: ViT注意力正则 · 难样本优化
tags:
- Vision Transformer
- Multi-head Attention
- Hard Sample Mining
- Regularization
- Face Recognition
one_liner: 提出难样本感知的多头注意力去相关正则策略，无额外推理成本提升ViT人脸识别性能
practical_value: '- 难样本差异化正则思路可迁移到推荐排序/召回模型优化：对与负样本/低 relevance 样本相似度高的难分样本，施加更强的特征去相关约束，提升模型对边缘样本的区分度

  - 多头注意力冗余优化仅作用于Transformer顶层的结论可复用：无需对全层加正则，仅优化最后几层即可平衡效果与训练开销，适配大模型训练场景

  - 无推理成本的训练侧正则思路适合落地：无需改动模型架构、不增加推理耗时，可直接嵌入现有Transformer-based推荐/多模态模型训练流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
ViT多头注意力无显式正则时易学习冗余模式，现有去相关正则对所有样本统一施加，未重视难样本（特征接近负类中心的样本）对模型优化和泛化的核心价值。
### 方法关键点
提出ViT-HarDis，将注意力头去相关强度与样本难度动态绑定：样本与负类中心余弦相似度越高，施加的去相关正则越强；仅在Transformer最后几层施加正则即可取得最优效果，无需修改模型架构，无额外推理开销。
### 关键结果
在WebFace4M数据集训练时，IJB-B、IJB-C、TinyFace的Rank-1指标达到ViT类方法SOTA；在MS1MV3训练时，IJB-B、TinyFace指标最优，相对基线与统一去相关正则方法在多数benchmark上实现效果提升。
