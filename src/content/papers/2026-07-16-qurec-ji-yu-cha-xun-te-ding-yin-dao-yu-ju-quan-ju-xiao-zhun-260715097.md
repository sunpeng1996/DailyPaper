---
title: 'QuReC: All-in-One Image Restoration with Query-Specific Guidance and Local-Global
  Response Calibration'
title_zh: QuReC：基于查询特定引导与局全局校准的一体化图像修复
authors:
- Shen Zhou
- Jinghui Zhang
- Wenbo Huang
- Xuwei Qian
- Zhen Wu
- Guangwen Peng
- Zhiyuan Li
- Ding Ding
- Dian Shen
- Fang Dong
affiliations:
- Southeast University
- Hainan University
arxiv_id: '2607.15097'
url: https://arxiv.org/abs/2607.15097
pdf_url: https://arxiv.org/pdf/2607.15097
published: '2026-07-16'
collected: '2026-07-18'
category: Other
direction: 计算机视觉·一体化图像修复
tags:
- Image Restoration
- Prototype Learning
- Weakly Supervised Learning
- Feature Aggregation
- Query Matching
one_liner: 提出融合退化感知查询重构与局全局响应校准的一体化图像修复框架QuReC，性能超越现有基准
practical_value: '- 电商商品图/广告素材瑕疵修复、降噪、去水印场景可直接复用QuReC框架，用统一模型处理多种图像退化问题，减少多模型运维成本

  - 空间查询与原型库匹配生成自适应引导的思路，可迁移至多模态推荐的细粒度用户/物品语义表征对齐场景

  - 局部-全局双分支特征聚合+可学习先验校准的结构，可复用至多模态召回排序的特征融合模块，平衡细粒度特征与全局上下文'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有一体化图像修复方法依赖图像级提示或共享引导，无法应对单张图像内空间异质、混合存在的多种退化；仅靠空间自适应引导也难以平衡局部细节与全局上下文的聚合需求。
### 方法关键点
1. 设计退化引导查询重构模块DQRM：将每个空间查询与退化原型空间匹配，重构查询特定的退化感知表征，提供细粒度空间自适应修复引导；配套弱监督原型匹配学习策略，提升优化稳定性与退化语义一致性
2. 设计局部-全局响应校准模块LGRCM：采用局部-全局双分支聚合结构，用可学习先验校准聚合响应，提升特征聚合可靠性，平衡局部细节建模与全局上下文建模的协同性
### 关键结果
在多个一体化图像修复基准数据集上性能显著优于现有SOTA方法，代码已开源
