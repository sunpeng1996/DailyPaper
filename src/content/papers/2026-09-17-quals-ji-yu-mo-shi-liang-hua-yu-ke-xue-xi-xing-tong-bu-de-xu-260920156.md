---
title: 'QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization
  and Learnability Synchronization'
title_zh: QUALS：基于模式量化与可学习性同步的通用时序预测语料均衡框架
authors:
- Yujie Li
- Zezhi Shao
- Chengqing Yu
- Yisong Fu
- Weijie Zhu
- Yifan Du
- Jilin Hu
- Bin Yang
- Yongjun Xu
- Fei Wang
arxiv_id: '2609.20156'
url: https://arxiv.org/abs/2609.20156
pdf_url: https://arxiv.org/pdf/2609.20156
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 时序大模型预训练 · 数据效率优化
tags:
- Time Series Forecasting
- Foundation Model Pre-training
- Data Efficiency
- Zero-shot Learning
- Vector Quantization
one_liner: 提出时序预训练语料均衡框架QUALS，大幅提升训练数据效率与零样本时序预测性能
practical_value: '- 时序预测是电商销量预测、库存预警、流量预估等业务的核心模块，可复用QUALS的模式量化+动态采样思路，解决多品类/多场景时序数据分布不均的问题，提升小样本场景下的预测精度

  - 可学习性同步校准采样权重的trick，可直接迁移到推荐系统多任务预训练、多域召回预训练的采样环节，平衡简单/困难样本、热门/长尾域的训练权重，提升整体收敛效率与下游效果

  - 低训练预算下的预训练优化思路，适合资源有限的业务团队搭建轻量通用时序底座，无需使用全量训练数据即可获得不错的零样本泛化效果，降低预训练成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前时序大模型预训练研究侧重架构创新，普遍忽略数据多样性适配问题，依赖简单采样策略无法有效处理复杂数据分布，导致训练数据利用效率低、零样本预测性能不达预期。
### 方法关键点
1. 模式量化模块：通过向量量化与均匀分箱机制，从混合异构语料中系统性解码不同类别的时序模式，对齐不同域的分布差异；
2. 可学习性同步模块：动态校准各类异构模式的采样权重，弥合简单与时序复杂模式间的优化gap，最大化整体训练效率。
### 关键结果
在多个公开时序基准测试上，基于QUALS预训练的模型在训练数据规模大幅缩减的前提下，仍稳定取得更优的零样本预测性能，数据效率提升显著。
