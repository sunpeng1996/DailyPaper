---
title: 'CoCaRS: Correlation Calibration-Based Redundancy Suppression for Heterogeneous
  Knowledge Distillation'
title_zh: CoCaRS：基于相关性校准的冗余抑制异构知识蒸馏方法
authors:
- Fengming Yu
- Haiwei Pan
- Kejia Zhang
- Chunling Chen
- Jian Guan
- Baoying Ma
affiliations:
- College of Computer Science and Technology, Harbin Engineering University
arxiv_id: '2607.27054'
url: https://arxiv.org/abs/2607.27054
pdf_url: https://arxiv.org/pdf/2607.27054
published: '2026-07-29'
collected: '2026-07-30'
category: Training
direction: 异构知识蒸馏 · 模型压缩训练优化
tags:
- Knowledge Distillation
- Model Compression
- Heterogeneous KD
- Redundancy Suppression
- Training Optimization
one_liner: 提出基于相关性校准的冗余抑制异构知识蒸馏框架，降低超参敏感度同时保留特征结构信息
practical_value: '- 推荐/广告场景跨架构蒸馏（如LLM蒸馏小排序/召回模型）时，可替换传统均匀去相关方法，避免破坏排序判别性结构

  - 蒸馏训练无需人工调试冗余抑制损失的固定系数，用ACR自适应按损失相对比例调整权重，降低超参调优成本

  - 迁移至多模态推荐模型蒸馏场景时，可引入CEE模块捕捉跨模态可靠语义关系，提升异构知识转移效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
异构知识蒸馏中师生模型架构归纳偏置差异大，特征表示偏差高，直接知识转移效果差；现有冗余抑制方案采用均匀去相关，易损失有用结构信息，固定系数导致效果对师生对、训练阶段高度敏感。
### 方法关键点
1. 设计Confusion Evidence Estimation（CEE）捕捉可靠语义关系用于相关性估计，搭配Strength Allocation Control（SAC）在去相关过程中保留判别性结构，完成特征去相关校准
2. 新增Adaptive Coefficient Regulation（ACR）模块，根据冗余抑制损失的相对规模自适应调整其贡献权重，降低超参设置敏感度
### 关键结果
在CIFAR-100、ImageNet-1K数据集上验证，CoCaRS显著提升异构蒸馏性能，同时大幅降低对系数设置的敏感度
