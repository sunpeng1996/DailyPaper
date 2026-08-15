---
title: Statistical Properties of Robust Learning under Distributional Shifts
title_zh: 分布偏移下鲁棒学习的统计特性
authors:
- Zhiyi Li
- Xiaojie Mao
- Yunbei Xu
- Ruohan Zhan
affiliations:
- National University of Singapore
- Tsinghua University
- University College London
arxiv_id: '2608.13133'
url: https://arxiv.org/abs/2608.13133
pdf_url: https://arxiv.org/pdf/2608.13133
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: 鲁棒训练 · 分布偏移泛化分析
tags:
- Distributional Shift
- DRO
- Robust Learning
- Generalization Bound
- Hyperparameter Tuning
one_liner: 推导DRO与RS在分布偏移目标域的有限样本泛化界，提出信息导向超参校准方法，明确二者互补特性
practical_value: '- 可复用推导的泛化界评估推荐系统跨域/冷启动等天然分布偏移场景下的DRO鲁棒训练效果

  - 当能拿到目标域偏移量级/方向等部分信息时，可直接套用信息导向超参校准方法优化DRO正则系数，平衡鲁棒性与精度

  - 电商需求预测、用户行为建模等场景可参考DRO与RS的特性对比，选择适配的鲁棒框架应对分布波动'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分布偏移鲁棒学习框架（DRO、RS）的分析多聚焦源域性能或模糊集上的对抗最坏情况，缺乏目标部署域下的有限样本泛化保证，也无标准化系统性对比逻辑。
### 方法关键点
1. 推导DRO、RS在偏移目标域下的有限样本泛化误差界，明确鲁棒超参在「降低偏移敏感度」和「引入正则惩罚」间的量化权衡，规避Wasserstein经验浓度关联的维度灾难；
2. 设计利用偏移量级/方向等部分信息的超参校准方案，在对齐信息条件下对比DRO与RS的特性差异；
3. 落地到网络批量规划场景，解释鲁棒策略对需求分布正偏移的响应逻辑。
### 关键结果
校准后的DRO与RS在不同部分信息场景下表现出理论与实验层面的互补性，填补了分布偏移下鲁棒学习统计特性的研究空白。
