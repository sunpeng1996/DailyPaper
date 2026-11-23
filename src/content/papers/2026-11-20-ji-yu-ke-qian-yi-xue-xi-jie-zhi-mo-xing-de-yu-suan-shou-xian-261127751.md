---
title: Budgeted Subset Selection with a Transferable Learned Value Model
title_zh: 基于可迁移学习价值模型的预算受限子集选择方法
authors:
- Jade Lejeune Herman
- Johan A. K. Suykens
- Peter Goos
affiliations:
- KU Leuven
- Mechatronics, Biostatistics and Sensors (MeBioS)
- ESAT-Stadius
arxiv_id: '2611.27751'
url: https://arxiv.org/abs/2611.27751
pdf_url: https://arxiv.org/pdf/2611.27751
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 组合优化 · 可迁移子集选择
tags:
- Subset Selection
- Combinatorial Optimization
- Transfer Learning
- Diversity-aware Selection
- Value Estimation
one_liner: 提出价值预估+多样性搜索两阶段可迁移子集选择框架SALVES，性能优于领域专用基线
practical_value: '- 电商选品、召回池截断、营销候选精选等预算受限子集选择场景，可复用SALVES「价值预估+多样性约束」两阶段架构，替代定制化方案提升跨场景迁移能力

  - 跨品类/新活动选品场景可参考其可迁移价值模型训练思路，用历史已标注选品效果数据训练通用价值模型，降低新场景冷启动成本

  - 子集选择阶段的带多样性惩罚的模拟退火搜索策略，可直接用于候选集重排环节，平衡推荐精准度与内容/品类多样性，减少冗余曝光'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有子集选择方案普遍将价值预估与冗余控制耦合，均为领域定制开发，跨场景迁移能力差，无法适配多业务下的通用预算受限子集选择需求。

### 方法关键点
提出SALVES两阶段子集选择框架：
1. 可迁移价值模型：在隐信息（如标签、业务反馈）已知的历史任务上做监督训练，迁移到新任务时可直接预测单个候选加入当前选择集的边际效用
2. 选择搜索模块：基于价值预测结果，采用带多样性惩罚项的模拟退火算法搜索最优子集，同时控制选择结果的冗余度

### 关键结果
- 在4类不同应用任务上平均性能持平或优于领域专用基线
- 光谱带选择任务中，同等精度下所需带宽远低于基线
- 输入选择任务中传统基线失效时，SALVES仍能保持稳定可靠的表现
