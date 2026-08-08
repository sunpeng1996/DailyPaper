---
title: 'FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels
  for Crowded and Chaotic Global South Urban Worlds'
title_zh: FactorJEPA：拆分整体未来表征为布局-智能体-交互通道适配高密度混乱城市场景
authors:
- Kapil Wanaskar
- Gaytri Jena
- Aman Chadha
- Vinija Jain
- Vasu Sharma
- Amitava Das
affiliations:
- San Jose State University
- UC Berkeley
- Apple
- Meta
- BITS Pilani Goa
arxiv_id: '2608.01049'
url: https://arxiv.org/abs/2608.01049
pdf_url: https://arxiv.org/pdf/2608.01049
published: '2026-08-01'
collected: '2026-08-08'
category: Other
direction: 世界模型 · JEPA架构优化
tags:
- JEPA
- World Model
- Representation Factorization
- Dataset
- Predictive Architecture
one_liner: 提出拆分表征的FactorJEPA与高密度城市世界模型数据集，提升JEPA在复杂异构场景的预测性能
practical_value: '- 多异构实体交互场景建模可借鉴三因子（静态布局/动态实体/交互关系）拆分表征思路，替代整体隐空间编码减少特征混淆，可迁移至电商用户-物品-场交互建模

  - 可见性门控过滤部分观测噪声的方法可用于处理推荐系统隐式反馈的缺失值、曝光偏差问题

  - 独立子空间训练避免跨因子学习捷径的trick可用于多任务推荐模型的特征解耦，提升多任务泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有JEPA架构针对低密度结构化城市场景设计，在人口密集、空间边界模糊、智能体高度异构、遮挡频繁的全球南方高密度混乱城市场景下，无法保留密集交互动态，且缺乏对应场景的大规模评测数据集。

### 方法关键点
提出FactorJEPA，不再使用整体隐空间编码未来状态，而是将表征拆分为布局、实体、交互三个独立子空间，引入visibility gate保留部分观测的智能体信息，同时避免跨因子的学习捷径；配套发布覆盖22个城市的1000小时多视角视频数据集DENSEWORLD-115k。

### 关键结果
在1B/2B参数量的V-JEPA 2.1 backbone上均稳定提升，Future-frame L1、Causal L1、Mask-ratio slope三类指标均优化，多指标跨backbone的排序相关性ρ达0.895~0.978。
