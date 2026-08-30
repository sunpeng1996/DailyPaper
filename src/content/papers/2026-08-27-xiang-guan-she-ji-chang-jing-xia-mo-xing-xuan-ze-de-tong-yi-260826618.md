---
title: A Unified Descriptive-Complexity Framework for Model Selection under Correlated
  Designs
title_zh: 相关设计场景下模型选择的统一描述复杂度框架
authors:
- Yanhang Zhang
- Wei Liu
- Yuhong Yang
affiliations:
- Tsinghua University Yau Mathematical Sciences Center
- Citigroup
- Beijing Institute of Mathematical Sciences and Applications
arxiv_id: '2608.26618'
url: https://arxiv.org/abs/2608.26618
pdf_url: https://arxiv.org/pdf/2608.26618
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 通用模型选择 · 高维强相关特征场景
tags:
- Model Selection
- High Dimensional Data
- Correlated Features
- Information Criterion
- Statistical Learning
one_liner: 提出DCIC描述复杂度信息准则，解决强特征依赖、模型类不确定场景下的高维模型选择问题
practical_value: '- 推荐系统特征工程面对高度相关的用户/物品特征时，可引入DCIC准则替代传统L1正则做特征选择，降低特征冗余

  - 召回/排序层多模型类选型可复用框架的跨模型类复杂度统一度量逻辑，降低异构模型选型成本

  - 高维候选模型集搜索可借鉴复杂度引导的搜索路径，平衡线上计算开销与模型效果，适配算力约束'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维场景下特征强依赖、模型类不确定、候选模型规模指数级增长，现有模型选择方法依赖RIP类近正交假设，泛用性差，无法保障模型误设下的效果。

### 方法关键点
1. 提出DCIC描述复杂度信息准则，基于Kraft可容许码长正则化大规模候选模型集，无需RIP类限制条件
2. 用统一编码规则对异构模型类做复杂度度量，仅增加极小的类识别开销，支持跨类模型选择
3. 设计复杂度引导的搜索路径，可显式权衡计算开销与统计效果。

### 关键结果
亚Weibull噪声下理论证明选择一致性，给出模型误设下仍有效的非渐近oracle风险界；大惩罚项设置下可高概率保留多项式规模的搜索区域，大幅降低计算量；数值实验显示强特征依赖下支持恢复稳定性优于基线，估计性能表现突出。
