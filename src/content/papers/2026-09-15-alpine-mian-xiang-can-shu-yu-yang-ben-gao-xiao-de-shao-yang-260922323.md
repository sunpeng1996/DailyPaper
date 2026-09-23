---
title: 'ALPINE: Adaptive Localization for Parameter- and Sample-Efficient Few-Shot
  Learning'
title_zh: ALPINE：面向参数与样本高效的少样本学习自适应定位方法
authors:
- Neeraj Yadav
affiliations:
- Independent Researcher, Uttar Pradesh, India
arxiv_id: '2609.22323'
url: https://arxiv.org/abs/2609.22323
pdf_url: https://arxiv.org/pdf/2609.22323
published: '2026-09-15'
collected: '2026-09-23'
category: Training
direction: 小样本高效训练 · 轻量化架构设计
tags:
- Few-shot Learning
- Parameter Efficiency
- Sample Efficiency
- Adaptive Localization
- Model Compression
one_liner: 提出参数仅22k~35k的超轻量少样本分类架构，准确率更高、参数更少、收敛更快
practical_value: '- 电商新品类目打标、稀缺样本召回等小样本分类场景，可复用内容自适应patch定位器设计，替换复杂关系模块，大幅降低参数开销

  - 算力受限的边缘端推荐/图像分类任务，可参考22k~35k参数的超轻量架构设计思路，在低参数预算下做性能平衡

  - 跨品类电商数据迁移等跨域泛化场景，可借鉴固定特征引导+自适应定位的框架，实现零重训适配新领域'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有少样本学习研究仅以准确率为核心评估指标，忽略参数规模、训练样本量的落地约束，难以适配无大规模算力的业务场景。
### 方法关键点
1. 提出超轻量空间关系架构ALPINE，仅含22249~34917个可训练参数，结合固定Gabor边缘能量引导与窗口化内容自适应patch定位器；
2. 采用严格等训练episode的公平对比协议，通过消融实验验证核心性能贡献来自自适应patch定位模块，而非成对关系计算。
### 关键结果
5-shot分类任务上，在CIFAR-FS、MiniImageNet数据集准确率全面超越Prototypical Networks、Relation Networks、MAML基线，参数少27%~53%；收敛所需训练episode更少，零重训泛化到CUB-200-2011细分类域效果更优，对50%遮挡、25%空间平移的鲁棒性优于所有基线
