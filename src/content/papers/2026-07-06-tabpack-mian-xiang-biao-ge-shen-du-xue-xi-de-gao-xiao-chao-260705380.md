---
title: 'TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning'
title_zh: TabPack：面向表格深度学习的高效超参数集成方法
authors:
- Yury Gorishniy
- Akim Kotelnikov
- Ivan Rubachev
- Artem Babenko
affiliations:
- Yandex
- HSE University
arxiv_id: '2607.05380'
url: https://arxiv.org/abs/2607.05380
pdf_url: https://arxiv.org/pdf/2607.05380
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: 表格深度学习 · 超参数集成优化
tags:
- TabularDL
- EnsembleLearning
- HyperparameterTuning
- MLP
- Efficiency
one_liner: 提出无需精细调参的超参数采样并行MLP集成框架，性能对标经充分调优的基线
practical_value: '- 电商CTR/CVR预估等场景多为表格特征输入，可复用TabPack超参数采样并行集成思路，大幅降低模型调参成本

  - 业务小流量实验阶段可直接用默认配置的TabPack快速迭代，无需占用大量GPU做超参数搜索，缩短上线周期

  - 可参考训练中动态筛选集成成员的机制，优化现有多模型融合的在线更新流程，降低推理时延'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格深度学习的MLP集成方案要求所有子模型使用相同超参数，需投入大量资源做超参数调优才能达到最优性能，人力和算力成本高。

### 方法关键点
1. 仅需指定超参数采样范围，无需提前固定精确取值，单次运行即可随机生成多组不同超参数的MLP并行训练
2. 训练过程中动态筛选表现优异的子模型组成最终集成，无需额外后处理
3. 整体架构轻量化，资源占用极低。

### 关键结果数字
在17个覆盖分类/回归任务的中大型公开表格数据集上，默认配置的TabPack性能与经过充分调优的现有基线持平；现代MacBook上运行默认TabPack的耗时，短于部分基线在工业级GPU上的调参耗时，大幅降低了表格任务获得SOTA级别结果的成本。
