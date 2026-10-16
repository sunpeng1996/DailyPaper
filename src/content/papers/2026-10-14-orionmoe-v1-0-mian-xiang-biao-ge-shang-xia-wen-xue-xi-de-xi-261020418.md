---
title: 'OrionMoE-v1.0: A Mixture-of-Experts Foundation Model for Tabular In-Context
  Learning'
title_zh: OrionMoE-v1.0：面向表格上下文学习的稀疏MoE基础模型
authors:
- Mohamed Bouadi
- Nassim Bouarour
- Aditya Tanna
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2610.20418'
url: https://arxiv.org/abs/2610.20418
pdf_url: https://arxiv.org/pdf/2610.20418
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: 表格基础模型 · 数据集感知MoE路由
tags:
- MoE
- In-Context Learning
- Tabular Foundation Model
- Pretraining
- Classification
one_liner: 37.7M参数量小尺寸表格上下文学习MoE模型，性能追平50-150M中等规模同类模型
practical_value: '- 电商用户/物品特征表格建模可复用双轴Transformer架构，分别对样本维度和特征维度做注意力交互，适配异质特征特性

  - 小样本分类场景（如新用户冷启动预测、小众类目转化预估）可直接复用开源37.7M参数量OrionMoE做零调参上下文预测，降低部署成本

  - 特征维度的MoE路由设计可迁移到推荐系统特征处理层，通过数据集感知路由为不同特征选择适配变换，提升高维稀疏特征表征效率

  - 多视图推理聚合trick可直接复用，对输入做特征顺序、编码方式的多变换后聚合预测，提升模型对特征扰动的鲁棒性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有表格上下文学习基础模型多采用密集Transformer架构，对所有特征和数据集使用相同计算路径，无法适配表格数据异质的分布特性，且大参数量模型部署成本高，小参数量模型性能存在瓶颈，亟需兼顾轻量化和效果的表格基础模型架构。

### 方法关键点
- 双轴Transformer骨干：分别沿样本轴做跨观测诱导注意力（复杂度随样本数线性增长）、沿特征轴做跨属性注意力，分离证据聚合与特征交互过程
- 数据集感知稀疏MoE层：特征轴替换密集FFN为MoE模块，每个特征token经过固定共享专家+Topk路由专家处理，路由分数结合局部特征表征与全局数据集寄存器统计信息生成，适配不同数据集特性
- 预训练范式：基于扩展的O'PRIOR合成数据生成器，覆盖异质特征分布、因果机制、缺失模式的分类任务，下游无需梯度更新即可做上下文预测
- 推理优化：默认生成8种特征变换、排列的输入视图，在logit层聚合结果，支持支持集表征缓存复用，降低批量查询延迟

### 关键结果
在TabArena、BeyondArena、OpenML-CC18、TALENT四大表格分类基准测评，仅37.7M参数量的OrionMoE-Small，在所有基准上均超过同档位的TabICLv2，性能追平53M参数量的TabPFN-3，在OpenML-CC18、TALENT基准上反超TabPFN-3；在小数据集、中等类别不平衡场景下Elo评分分别达1404、1501，超过同档位所有基线。

### 核心结论
小参数量稀疏MoE架构通过数据集感知的条件计算，可在表格任务上实现远超参数规模对应的性能表现，是平衡推理成本和效果的可行路径。
