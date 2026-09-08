---
title: An Analysis of Self-supervised Pre-training with Dependent Samples
title_zh: 《带依赖样本的自监督预训练效果分析》
authors:
- Maximilian Fleissner
- Debarghya Ghoshdastidar
- Samory Kpotufe
affiliations:
- Technical University of Munich
- Columbia University
arxiv_id: '2609.05031'
url: https://arxiv.org/abs/2609.05031
pdf_url: https://arxiv.org/pdf/2609.05031
published: '2026-09-04'
collected: '2026-09-08'
category: Training
direction: 自监督预训练 · 数据增强策略理论分析
tags:
- Self-Supervised-Learning
- Data-Augmentation
- Pre-training
- Statistical-Analysis
- Representation-Learning
one_liner: 从理论层面证明自监督预训练中混合同一样本的多组增强数据效果优于拆分独立样本子集的基线方案
practical_value: '- 做用户/商品表征预训练、LLM领域预训练等自监督任务时，可直接pooling同一样本的多组增强数据，无需刻意拆分独立样本子集，即可获得更优的误差收敛效果

  - 针对mask、噪声注入类增强策略，可增加单样本的增强次数，能加快模型表征学习的收敛速度，降低下游任务对标注数据的依赖

  - 推荐系统冷启动场景下，可对少量冷启动样本做多次差异化增强后pooling训练，能在数据量有限的前提下降低表征估计方差'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有自监督预训练理论通常要求规避同一样本多组增强数据之间的依赖，仅能在小规模独立样本子集上训练，与工业界直接混合所有增强数据的实操存在断层，相关做法缺乏理论支撑。
### 方法关键点
针对自监督预训练的不变子空间估计场景，分别推导混合所有增强样本（pooling）、拆分独立样本子集两种方案的统计误差边界，分析同一样本不同增强的相关性对估计效果的影响。
### 关键结果
1. pooling方案的统计估计误差边界始终不劣于拆分基线方案；
2. 针对浅层网络的mask、噪声注入类增强场景，pooling的收敛速度随增强次数提升更快；
3. 当不同增强的相关性对估计影响较弱或可降低方差时，pooling的收益更加突出
