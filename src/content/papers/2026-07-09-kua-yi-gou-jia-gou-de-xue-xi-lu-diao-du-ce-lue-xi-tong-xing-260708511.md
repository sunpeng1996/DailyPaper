---
title: Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous
  Architectures
title_zh: 跨异构架构的学习率调度策略系统性评估
authors:
- Hafsa Mateen
- Radu Timofte
- Dmitry Ignatov
affiliations:
- Computer Vision Lab, CAIDAS & IFI, University of Würzburg, Germany
arxiv_id: '2607.08511'
url: https://arxiv.org/abs/2607.08511
pdf_url: https://arxiv.org/pdf/2607.08511
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 深度学习训练 · 学习率调度优化
tags:
- Learning Rate Scheduler
- Hyperparameter Optimization
- CNN
- Transformer
- Model Training
one_liner: 系统性评测25种学习率调度在30类CNN/Transformer架构的效果，给出选型参考
practical_value: '- 训练推荐/广告领域的CNN、Transformer类模型（如召回排序模型、多模态理解模型）时，优先尝试CosineAnnealingWarmRestarts、CyclicLR两种调度器，收益普遍高于基础衰减策略

  - 做模型训练调优时，不要将学习率调度作为次要超参，最优调度策略与架构强相关，可参考论文公开的LEMUR数据集精度景观缩小调参范围

  - 批量评测超参效果时，可复用论文的自动化代码注入方案，降低多模型多配置评测的开发成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
学习率调度直接影响模型收敛速度、最终精度与泛化性，手动选型成本高且覆盖不全，过往AutoML普遍将其作为次要超参，缺乏跨异构架构的系统性验证。
### 方法关键点
覆盖卷积、Transformer两大系列共30种代表性架构，基于PyTorch实现9个调度器家族的25种配置，通过自动化代码注入批量生成3938种模型变体，在CIFAR-10数据集上完成分类任务评测，结果同步贡献到LEMUR公开数据集。
### 关键结果数字
最优配置Top-1精度达86.45%，共237个变体精度超过80%；CosineAnnealingWarmRestarts、CyclicLR两类调度器在不同架构上均稳定优于基础衰减策略，调度器最优选型与架构强相关。
